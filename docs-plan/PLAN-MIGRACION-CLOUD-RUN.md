# Plan de migración del panel ICFES a Cloud Run

**Escrito:** 2026-09-18 · **Estado:** propuesta, no ejecutada
**Aplica a:** https://resultados-icfes-pcielo-2025.streamlit.app/ (repo `alvaretto/resultados-icfes`)
**Antecedente obligatorio:** `DIAGNOSTICO-STREAMLIT-CLOUD.md`

---

## 1. Qué decide este documento

Si el panel se queda en Streamlit Community Cloud —donde hace falta un despertador,
un latido, un vigía y dos alertas para compensar la hibernación— o se muda a una
plataforma donde ese problema no existe.

**No ejecutes este plan todavía.** La defensa montada el 2026-09-18 funciona y avisa
por Telegram. Ejecútalo cuando se cumpla **al menos una** de estas condiciones:

1. El panel pasa a ser el **enlace institucional permanente** que se reparte a docentes,
   familias o la Secretaría, y quieres que viva bajo `iepedacitodecielo.edu.co`.
2. El despertador falla dos veces y administrar la limitación deja de compensar.
3. Streamlit cambia su política de hibernación o del plan gratuito.

Si ninguna se cumple, el costo de migrar (2–4 horas más el cambio de URL) es mayor
que el de mantener lo que ya está andando.

## 2. Por qué migrar elimina el problema, en vez de administrarlo

No es una diferencia de configuración, es de **quién despierta el contenedor**.

| | Streamlit Community Cloud | Cloud Run |
|---|---|---|
| App sin tráfico | Contenedor apagado tras **12 h** | **0 instancias** (idéntico efecto, otro nombre) |
| Quién lo enciende | **Un humano**, haciendo clic en «Yes, get this app back up!» | **La propia petición HTTP entrante** |
| Qué ve el visitante | Una pantalla que parece un error | Una espera de segundos |
| Qué hay que mantener | Despertador + latido + vigía + 2 alertas | Un Dockerfile |

En Cloud Run «dormida» no es un estado del que haya que rescatar nada: el proxy retiene
la petición, levanta el contenedor y la sirve. Por eso allá **sobran las cuatro piezas**
que hoy existen solo para compensar la decisión de producto de Streamlit.

## 3. Elección de plataforma

| Plataforma | Arranque en frío | Veredicto |
|---|---|---|
| **Cloud Run** | ~3–10 s | **Recomendada.** Escala a cero real, capa gratuita amplia, dominio propio, soporta WebSockets |
| Fly.io | ~1–3 s | Más simple de operar que GCP, pero su esquema gratuito cambió: **verificar condiciones vigentes** antes de elegirlo |
| Render (free) | ~50 s+ | Descartada: el arranque en frío es peor que el problema que resuelve |
| Hugging Face Spaces | variable | Descartada: también pausa por inactividad en el plan gratuito |

## 4. Hallazgos verificados del port (2026-09-18)

Esto ya se comprobó contra el código real, no son supuestos:

1. **Los datos ya están versionados.** `data/*.xlsx` están rastreados en git, así que
   entran en la imagen con un `COPY`. No hace falta volumen ni bucket.
2. **`data_loader.py` usa rutas relativas** (`pd.read_excel('data/…')`). El `WORKDIR`
   del contenedor tiene que ser la raíz del proyecto o la carga de datos falla.
3. **Los secretos NO exigen tocar el código… pero hay una trampa.** `chat_ia_icfes.py`
   y `brave_search.py` ya caen a `os.getenv()` si la clave no está en `st.secrets`, que
   es justo lo que Cloud Run necesita. **Pero** el patrón es:

   ```python
   if hasattr(st, 'secrets') and "ANTHROPIC_API_KEY" in st.secrets:   # ← sin try/except
   ```

   y sin ningún `secrets.toml` presente, ese `in` **lanza `StreamlitSecretNotFoundError`**
   en vez de devolver `False`. Verificado con Streamlit 1.55:

   | Escenario | Resultado |
   |---|---|
   | Sin `secrets.toml` | **`StreamlitSecretNotFoundError`** → la app rompe |
   | Con `.streamlit/secrets.toml` **vacío** + clave en variable de entorno | `in` → `False`, cae a `os.getenv` → **funciona** |

   **Mitigación elegida:** incluir un `secrets.toml` vacío en la imagen. Cero cambios en
   el código de la app, cero riesgo de regresión. (La alternativa —envolver los tres
   accesos en `try/except`— es más limpia a futuro pero toca código que hoy funciona.)
4. **`.streamlit/config.toml` fija `port = 8501`**, pero Cloud Run inyecta `$PORT` (8080).
   El flag de línea de comandos manda sobre el `config.toml`, así que basta pasarlo explícito.

## 5. Precondiciones

- [ ] Cuenta de Google Cloud con **facturación habilitada** (exige tarjeta, aunque el gasto real esperado sea $0)
- [ ] `gcloud` instalado y autenticado
- [ ] Acceso al DNS de `iepedacitodecielo.edu.co` si se quiere dominio propio
- [ ] Decidir el subdominio: sugerencia `panel.iepedacitodecielo.edu.co`

## 6. Paso a paso

### 6.1 `Dockerfile` (en la raíz del repo)

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Dependencias primero: aprovecha la caché de capas de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Trampa verificada: sin secrets.toml, `"KEY" in st.secrets` lanza
# StreamlitSecretNotFoundError en vez de devolver False, y la app rompe.
# Con este archivo vacío, cae correctamente a os.getenv().
RUN mkdir -p .streamlit && touch .streamlit/secrets.toml

ENV PYTHONUNBUFFERED=1
EXPOSE 8080

# $PORT lo inyecta Cloud Run. El flag manda sobre el port del config.toml.
CMD streamlit run streamlit_app.py \
    --server.port=${PORT:-8080} \
    --server.address=0.0.0.0 \
    --server.headless=true \
    --browser.gatherUsageStats=false
```

### 6.2 `.dockerignore`

```
.git
.venv
venv
node_modules
.next
_backup-streamlit-deprecated
*.pdf
*.tar.gz
.streamlit/secrets.toml
docs/
docs-analisis/
docs-plan/
docs-proyecto/
```

Excluir `.streamlit/secrets.toml` es **obligatorio**: sin esa línea, las claves reales
locales se hornean en la imagen.

### 6.3 Secretos en Secret Manager

```bash
PROY=<tu-proyecto-gcp>
gcloud config set project "$PROY"
gcloud services enable run.googleapis.com cloudbuild.googleapis.com secretmanager.googleapis.com

printf '%s' "<ANTHROPIC_API_KEY>"    | gcloud secrets create anthropic-api-key    --data-file=-
printf '%s' "<BRAVE_SEARCH_API_KEY>" | gcloud secrets create brave-search-api-key --data-file=-
```

> Aprovecha para **rotar** ambas claves: hoy viven en un `secrets.toml` local en claro.
> El archivo está correctamente ignorado por git y nunca se publicó, pero rotarlas al
> migrar cuesta cinco minutos y cierra el tema.

### 6.4 Despliegue

```bash
gcloud run deploy panel-icfes \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --min-instances=0 \
  --max-instances=3 \
  --memory=1Gi \
  --timeout=3600 \
  --set-secrets=ANTHROPIC_API_KEY=anthropic-api-key:latest,BRAVE_SEARCH_API_KEY=brave-search-api-key:latest
```

Dos parámetros que no son cosméticos:

- **`--timeout=3600`**: la sesión de Streamlit es una petición larga (WebSocket). Con el
  timeout por defecto (5 min) las sesiones se cortan solas mientras el usuario navega.
- **`--min-instances=0`**: escala a cero, que es lo que hace que no cueste nada. Ponerlo
  en 1 elimina hasta la espera del arranque, pero ahí ya se paga todos los meses.

### 6.5 Dominio propio

```bash
gcloud beta run domain-mappings create \
  --service=panel-icfes --domain=panel.iepedacitodecielo.edu.co --region=us-central1
```

Devuelve los registros DNS a crear. Este paso es **el argumento fuerte de toda la migración**:
el enlace deja de pertenecer al proveedor. Si mañana cambias de plataforma otra vez, la URL
que repartiste sigue sirviendo.

### 6.6 Redespliegue automático

Streamlit Cloud redespliega solo con cada push; Cloud Run no. Reemplazo: un workflow
`deploy.yml` con `google-github-actions/auth` (usando **Workload Identity Federation**, no
claves de cuenta de servicio) + `google-github-actions/deploy-cloudrun`, disparado en push
a `main`. Es la hora de trabajo que más se subestima al planear esta migración.

## 7. Corte y convivencia

1. Desplegar en Cloud Run y verificar **sin** anunciar nada.
2. Dejar los dos enlaces vivos **dos semanas**.
3. Poner un aviso visible en el panel de Streamlit: «Este panel se mudó a
   panel.iepedacitodecielo.edu.co». Streamlit Cloud no permite redirección HTTP, así que
   el aviso va dentro de la app, con `st.warning` en la página de inicio.
4. Avisar por los canales por donde se repartió el enlace original.
5. Pasadas las dos semanas, borrar la app de Streamlit Cloud.

## 8. Qué desmontar después (no olvidar)

Migrar sin limpiar deja cuatro piezas corriendo contra una app que ya no existe, y
alertas falsas cada seis horas:

- [ ] `.github/workflows/keep-alive.yml`
- [ ] `.github/workflows/heartbeat.yml` (y la rama `ci-heartbeat`)
- [ ] `.github/scripts/keep-alive.mjs`, `verificar.sh`
- [ ] `systemctl --user disable --now icfes-streamlit-watchdog.timer` + quitar el bloque de `~/hermes-config/sync.sh`
- [ ] Secretos `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` del repo
- [ ] Actualizar `DIAGNOSTICO-STREAMLIT-CLOUD.md` y la memoria del proyecto

## 9. Rollback

Trivial mientras no se borre la app de Streamlit Cloud: el enlace viejo sigue funcionando
y el despertador sigue montado. El punto de no retorno es el paso 5 del corte, no el despliegue.

## 10. Costo

Cloud Run tiene capa gratuita mensual por peticiones, CPU y memoria. Un panel con escala a
cero y decenas de visitas al mes cae holgadamente dentro: el gasto esperado es **$0**.
**Verificar las cifras vigentes al ejecutar** —cambian— y dejar un **presupuesto con alerta
de correo** en GCP antes de desplegar, por si algo genera tráfico inesperado.

## 11. Criterios de aceptación

- [ ] La app responde en el dominio propio tras **más de 24 h sin visitas**, sin pantalla intermedia ni clic
- [ ] El primer byte llega en menos de 15 s tras ese arranque en frío
- [ ] El chat de IA responde (prueba de que los secretos llegaron como variables de entorno)
- [ ] Una sesión abierta sobrevive más de 10 minutos sin cortarse (prueba del `--timeout`)
- [ ] Un push a `main` redespliega solo
- [ ] Las cuatro piezas del despertador quedaron desmontadas y el vigía silenciado

## 12. Riesgos conocidos

| Riesgo | Mitigación |
|---|---|
| La facturación de GCP exige tarjeta | Presupuesto con alerta; `--min-instances=0` |
| Estado de sesión de Streamlit en memoria del proceso | `--max-instances` bajo; cada sesión vive en una instancia por su WebSocket |
| El `secrets.toml` real se hornea en la imagen | Línea explícita en `.dockerignore` (§6.2) |
| Usuarios con el enlace viejo guardado | Convivencia de dos semanas + aviso dentro de la app |
| Se migra y no se desmonta lo viejo | Checklist §8 |

---

*Los hallazgos de la §4 se verificaron contra el código y contra Streamlit 1.55 el
2026-09-18. Todo lo demás son decisiones y estimaciones, marcadas como tales.*
