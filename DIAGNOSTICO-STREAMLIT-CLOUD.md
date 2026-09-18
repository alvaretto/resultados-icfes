# Hibernación en Streamlit Community Cloud — diagnóstico y defensa

**URL:** https://resultados-icfes-pcielo-2025.streamlit.app/
**Última revisión:** 2026-09-18
**Estado:** despertador automático activo y verificado en producción

---

## El problema

Streamlit Community Cloud duerme **toda app que pase 12 horas sin tráfico**
(«All apps without traffic for 12 hours go to sleep», documentación oficial).
Quien entra entonces no ve el panel: ve una pantalla con «Zzzz — This app has gone
to sleep due to inactivity» y un botón **«Yes, get this app back up!»**.

El despertar es **manual**: alguien tiene que hacer ese clic. Para un docente o un
directivo que abre el enlace, eso se lee como «el panel está roto».

## Por qué el primer intento de solución no sirvió (2026-03-28 → 2026-05-28)

Se añadió un workflow que hacía `curl` cada 6 h y aceptaba cualquier código HTTP
como éxito. Falló por dos motivos independientes, ambos verificados:

**1. El chequeo era ciego.** Medido el 2026-09-18 con la app dormida:

| Sonda | App dormida | App viva |
|---|---|---|
| `GET /` | `303` | `303` *(idéntico)* |
| `GET /healthz` | `200 {"status":"ok"}` | `200 {"status":"ok"}` *(idéntico)* |
| `GET /_stcore/health` | `303` a auth | `303` a auth |

Ningún endpoint HTTP distingue los dos estados. El workflow reportó **«success»
243 veces mientras la app dormía**. Cualquier monitor tipo curl, UptimeRobot o
cron-job.org tiene exactamente el mismo punto ciego.

**2. El cron llevaba 113 días apagado.** GitHub documenta: *«In a public repository,
scheduled workflows are automatically disabled when no repository activity has
occurred in 60 days»*. Último push `2026-03-29` + 60 días = **`2026-05-28`**, que es
la fecha de la última corrida registrada. El API lo confirmaba sin ambigüedad:

```
gh api repos/alvaretto/resultados-icfes/actions/workflows --jq '.workflows[].state'
→ "disabled_inactivity"
```

Y un workflow deshabilitado **no falla**: deja de correr en silencio, sin avisar a nadie.

## Cómo se distingue viva de dormida

Solo con un navegador real, y leyendo **dentro de los frames**: la app se sirve
dentro de un `<iframe>`, así que el `innerText` del frame superior está **vacío**
cuando la app funciona correctamente.

| Señal | DORMIDA | VIVA |
|---|---|---|
| `<title>` | `Streamlit` | `Análisis ICFES - Pedacito de Cielo · Streamlit` |
| Texto en frames | `Zzzz… gone to sleep…` | ~2.600 caracteres del panel |
| `<iframe>` de la app | ausente | presente |

## La defensa montada

| Pieza | Qué hace | Cadencia |
|---|---|---|
| `.github/scripts/keep-alive.mjs` | Abre un navegador real, detecta la hibernación, **hace el clic**, espera el arranque en frío y verifica por frames que quedó viva. Reintenta una vez. Sale con error si no lo logra. | — |
| `.github/workflows/keep-alive.yml` | Ejecuta el despertador. 3 h da 4 oportunidades por cada ventana de 12 h, margen para las corridas que GitHub retrasa o descarta bajo carga. | cada 3 h (minuto 17) |
| `.github/workflows/heartbeat.yml` | Commit vacío en la rama `ci-heartbeat` para reiniciar el contador de 60 días, más una red de seguridad que re-habilita el despertador si GitHub lo apagó. | lunes 06:23 UTC |
| `.github/scripts/verificar.sh` | Verificación manual desde tu máquina. | a demanda |
| Alerta a Telegram en ambos workflows | Si el despertador no logra dejar viva la app, o si falla el latido, avisa al canal de Hermes. Credenciales en secretos del repo, nunca en el YAML. | al fallar |
| `~/.local/bin/icfes-streamlit-watchdog.sh` + timer systemd | Vigía **fuera de GitHub**: avisa por Telegram si los crons aparecen apagados o si el despertador lleva más de 8 h sin correr. Silencio = todo normal. | cada 6 h |

La rama `ci-heartbeat` existe solo para registrar actividad: no toca `main` ni
dispara redespliegues en Streamlit Cloud.

## Cómo comprobarlo tú mismo

```bash
# ¿Está viva ahora? (la despierta si hace falta)
.github/scripts/verificar.sh

# ¿El despertador sigue corriendo?
gh run list --workflow=keep-alive.yml --limit 5

# ¿GitHub volvió a apagar los crons?  Debe decir "active" en ambos.
gh api repos/alvaretto/resultados-icfes/actions/workflows --jq '.workflows[] | "\(.path) -> \(.state)"'

# Forzar una corrida ahora
gh workflow run keep-alive.yml --repo alvaretto/resultados-icfes
```

## Qué puede volver a romperlo

1. **Que GitHub pierda 4 corridas seguidas** (12 h completas). Poco probable; entonces
   la app duerme hasta la siguiente corrida, que la despierta sola.
2. **Que el commit del bot no cuente como actividad del repo.** Es el único supuesto
   no demostrado todavía: se confirma revisando el estado de los workflows después
   del 2026-11-17 (60 días desde hoy).
3. **Que Streamlit cambie el texto del botón o la estructura del DOM.** El despertador
   fallaría de forma ruidosa, no silenciosa: llega alerta a Telegram (bot de Hermes) y
   correo de GitHub al dueño del repo.
4. **Que se acabe el plan gratuito o cambie la política de hibernación.** La solución
   de fondo, si el panel llega a ser el enlace institucional permanente, es moverlo a
   una plataforma que despierte sola con la primera petición (Cloud Run, Fly.io,
   Render): ahí esta pantalla no existe.

---

*Documento actualizado tras verificar cada afirmación contra el sistema real.
Las versiones anteriores daban el despliegue por «✅ Funcional» mientras la app
llevaba meses durmiendo.*
