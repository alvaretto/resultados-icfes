#!/usr/bin/env node
/**
 * Despertador + verificador de la app en Streamlit Community Cloud.
 *
 * POR QUE UN NAVEGADOR Y NO UN curl (medido el 2026-09-18 contra la app dormida):
 *   GET /          -> 303 identico este viva o dormida
 *   GET /healthz   -> 200 {"status":"ok"} INCLUSO CON LA APP DORMIDA
 *   => ningun endpoint HTTP distingue los dos estados. El estado solo se ve en el DOM
 *      renderizado, y despertarla exige un clic real en un boton.
 *
 * OJO: la app real se sirve dentro de un <iframe>; el innerText del frame superior
 * esta VACIO cuando la app funciona. Por eso se lee el texto de TODOS los frames.
 *
 * Uso local:  APP_URL=https://... CHROME_PATH=/usr/bin/google-chrome-stable node keep-alive.mjs
 * Salida: una linea "VIVA|DORMIDA|INDETERMINADO | <ISO> | <detalle>". Exit 0 solo si VIVA.
 */

let chromium;
try { ({ chromium } = await import('playwright')); }
catch { ({ chromium } = await import('playwright-core')); }

const URL_APP   = process.env.APP_URL || 'https://resultados-icfes-pcielo-2025.streamlit.app/';
const MARCA_APP = new RegExp(process.env.APP_MARKER || 'Pedacito de Cielo|An[aá]lisis (Comparativo )?ICFES', 'i');
const DORMIDA   = /Zzzz|gone to sleep|due to inactivity|get this app back up/i;

const MS_CARGA      = 90_000;   // hasta ver un estado reconocible
const MS_ARRANQUE   = 300_000;  // arranque en frio del contenedor tras el clic
const MS_PERMANENCIA = 10_000;  // sesion abierta tras despertar: esto es el "trafico" real
const INTENTOS = 2;

const t0 = Date.now();
const log = (m) => console.log(`[${((Date.now() - t0) / 1000).toFixed(1)}s] ${m}`);

async function textoDeFrames(page) {
  let out = '';
  for (const f of page.frames()) {
    if (/statuspage\.io/.test(f.url())) continue;  // widget de estado de Streamlit Cloud
    try { out += '\n' + (await f.evaluate(() => document.body?.innerText || '')); } catch { /* frame en transicion */ }
  }
  return out;
}

async function esperarEstado(page, limiteMs) {
  const limite = Date.now() + limiteMs;
  while (Date.now() < limite) {
    const texto = await textoDeFrames(page);
    if (DORMIDA.test(texto))   return { estado: 'DORMIDA', texto };
    if (MARCA_APP.test(texto)) return { estado: 'VIVA', texto };
    await page.waitForTimeout(2000);
  }
  return { estado: 'INDETERMINADO', texto: await textoDeFrames(page) };
}

async function intento(browser, n) {
  const page = await browser.newPage({ viewport: { width: 1366, height: 900 } });
  try {
    log(`intento ${n}: abriendo ${URL_APP}`);
    await page.goto(URL_APP, { waitUntil: 'domcontentloaded', timeout: MS_CARGA });

    let { estado } = await esperarEstado(page, MS_CARGA);
    log(`estado detectado: ${estado}`);

    if (estado === 'DORMIDA') {
      await page.getByRole('button', { name: /get this app back up/i }).click({ timeout: 20_000 });
      log('clic en "Yes, get this app back up!" — esperando arranque del contenedor');
      ({ estado } = await esperarEstado(page, MS_ARRANQUE));
      log(`tras el clic: ${estado}`);
    }

    if (estado === 'VIVA') {
      // Permanecer conectado un momento: el websocket abierto es lo que cuenta como trafico.
      await page.waitForTimeout(MS_PERMANENCIA);
      const texto = await textoDeFrames(page);
      return { estado: 'VIVA', detalle: `${texto.trim().length} chars en ${page.frames().length} frames` };
    }
    return { estado, detalle: `titulo="${await page.title()}"` };
  } catch (e) {
    return { estado: 'INDETERMINADO', detalle: 'error: ' + String(e.message).split('\n')[0] };
  } finally {
    await page.close().catch(() => {});
  }
}

const browser = await chromium.launch({
  ...(process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } : {}),
  args: ['--no-sandbox', '--disable-dev-shm-usage'],
});

let r = { estado: 'INDETERMINADO', detalle: 'sin intentos' };
for (let i = 1; i <= INTENTOS; i++) {
  r = await intento(browser, i);
  if (r.estado === 'VIVA') break;
  if (i < INTENTOS) { log('reintentando en 15s...'); await new Promise((s) => setTimeout(s, 15_000)); }
}
await browser.close();

console.log(`${r.estado} | ${new Date().toISOString()} | ${r.detalle}`);
if (r.estado !== 'VIVA') {
  console.error('::error::La app NO quedo viva. Revisa https://share.streamlit.io/ (logs y estado del despliegue).');
  process.exit(1);
}
