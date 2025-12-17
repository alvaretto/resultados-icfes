# 📊 Proyecto Resultados ICFES – 3 Fases: Descarga, Extracción y App Comparativa

Este proyecto está organizado en 3 fases complementarias que cubren el flujo completo:

- Fase 1. Descarga de resultados desde la página oficial del ICFES
- Fase 2. Extracción de puntajes por área y globales de cada PDF descargado y organización de datos
- Fase 3. Generación de una aplicación en Streamlit con análisis estadísticos de 2025 y comparativas/avances 2024 → 2025

La solución incluye scripts de automatización asistida, utilidades de verificación, documentación y una app web interactiva.

---

## Índice

1. Requisitos
2. Estructura del proyecto
3. Fase 1 – Descarga oficial de resultados ICFES
4. Fase 2 – Extracción de puntajes y organización de datos
5. Fase 3 – App Streamlit: análisis 2025 y comparativos 2024 → 2025
6. Datos requeridos y formatos
7. Inicio rápido (app)
8. Solución de problemas
9. Scripts y utilidades
10. Despliegue (local y Streamlit Cloud)
11. Capturas
12. Créditos

---

## 1) Requisitos

- Python 3.10+
- Dependencias (instalar):
  - `pip install -r requirements.txt`
- Navegador Firefox/Chrome instalado (para inspección/descarga asistida cuando aplique)

Tecnologías: Python + Streamlit + Pandas + Plotly + OpenPyXL.

---

## 2) Estructura del proyecto

- `scripts/`: Inspección del sitio, utilidades de descarga, verificación de PDFs y extracción.
- `scripts-shell/`: Scripts de shell para diagnóstico e inicio.
- `data/`: Almacenamiento de excels resultantes y fuentes de datos.
- `streamlit_app.py` y `app/`: Aplicación Streamlit principal y variantes/pruebas.
- `docs-analisis/`, `docs-proyecto/`, `docs-plan/`: Documentación técnica y guías.
- `.streamlit/` y `config/`: Configuración de la aplicación y requisitos para despliegue.

Para un diagrama más detallado: `ESTRUCTURA-PROYECTO.md`.

---

## 3) Fase 1 – Descarga oficial de resultados ICFES

Objetivo: Obtener los PDFs de resultados por estudiante desde la plataforma oficial del ICFES (acceso institucional, con validaciones/captcha).

Flujo sugerido:

- Inspección y verificación de la página de resultados:
  - `scripts/06-inspeccionar_sitio_simple.py`
  - `scripts/07-inspeccionar_sitio.py`
  - `scripts/08-inspeccionar_con_firefox.py`
  - `scripts/11-inspeccionar_pagina_resultados.py`
- Descarga guiada/asistida de resultados y PDFs:
  - `scripts/12-descargar_resultados_icfes.py`
  - `scripts/21-extraer_puntajes_desde_web.py` (apoyo a extracción desde web, si aplica)
- Verificación de PDFs descargados:
  - `scripts/13-verificar_pdfs_completos.py`

Entradas/salidas:

- Entrada: credenciales institucionales y parámetros de consulta (año/periodo).
- Salida: PDFs individuales por estudiante en `pdfs_descargados/` (u otra ruta configurada) + registros de descarga.

Notas:

- La resolución de CAPTCHA y la autenticación requieren intervención humana.
- Revisa `docs-proyecto/INSTRUCCIONES-SIGUIENTES-PASOS.md` y capturas `captura_login_firefox.png` para guía visual.

---

## 4) Fase 2 – Extracción de puntajes y organización de datos

Objetivo: Extraer puntajes por área (Lectura, Matemáticas, Sociales, Ciencias, Inglés) y puntaje global de cada PDF y consolidarlos en estructuras tabulares listas para análisis.

Herramientas y scripts:

- Exploración del PDF y OCR (si es necesario):
  - `explorar_estructura_pdf.py`, `explorar_pdf_con_ocr.py`, `analizar_pdf_detallado.py`
- Pipeline de extracción:
  - `scripts/extraer_puntajes_de_pdfs.py`
- Procesamiento/validación de Excel:
  - `scripts/04-analizar_excel.py`

Salidas esperadas (en `data/`):

- `RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx`
- `RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx`
- `Resultados_ICFES_2024.xlsx` (para comparativa)
- Opcional: `RESULTADOS-ICFES-EJEMPLO.xlsx` para pruebas

Buenas prácticas:

- Validar columnas y formatos con `docs-proyecto/README-WEBAPP.md`.
- Usar `docs-analisis/DATOS-EXTRAIDOS-PDF-2024-3.md` y resúmenes en `docs-analisis/` para contrastar resultados.

---

## 5) Fase 3 – App Streamlit: análisis 2025 y comparativos 2024 → 2025

Objetivo: Visualizar análisis estadísticos del 2025 y comparar contra 2024 por estudiante, grado, área y modelo.

Inicio rápido:

- Ejecutar: `./iniciar_aplicacion.sh`
- Alternativa: `streamlit run streamlit_app.py`
- Acceso:
  - Local: http://localhost:8501
  - Red local: http://<IP_LOCAL>:8501

Características principales:

- Inicio: comparativo general 2024 vs 2025.
- Estadísticas por estudiante, grado, área y modelo (Aula Regular vs Flexible).
- Análisis de avances 2024 → 2025 con formato condicional (mejora, disminución, sin cambio).
- Rankings y destacados, tablas ordenables y gráficos interactivos (zoom/pan/exportar).

Detalles de la app y configuración:

- Documentación funcional: `README-APLICACION-COMPARATIVA.md` y `docs-proyecto/README-WEBAPP.md`.
- Personalización visual/caché: `.streamlit/config.toml`.

---

## 6) Datos requeridos y formatos

Colocar en `data/` para que la app funcione:

- `RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx`
- `RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx`
- `Resultados_ICFES_2024.xlsx`

Estructuras de columnas esperadas y ejemplos: ver `docs-proyecto/README-WEBAPP.md`.

---

## 7) Inicio rápido (app)

1) `pip install -r requirements.txt`
2) Copia los Excel a `data/` (ver sección anterior)
3) `./iniciar_aplicacion.sh`  (o `streamlit run streamlit_app.py`)

Guía paso a paso: `INICIO-RAPIDO.md`.

---

## 8) Solución de problemas

- Dependencias: `pip install -r requirements.txt`
- Verificar datos: `ls -la data/RESULTADOS-ICFES-*.xlsx`
- Diagnóstico Streamlit: `scripts-shell/diagnosticar_streamlit.sh`
- Guías: `docs-proyecto/DIAGNOSTICO-STREAMLIT.md` y `docs-proyecto/DIAGNOSTICO-ERRORES-STREAMLIT.md`

---

## 9) Scripts y utilidades

Descarga/inspección (Fase 1):

- `scripts/06–13`: inspección del sitio, scraping asistido, verificación de PDFs
- `scripts/12-descargar_resultados_icfes.py`
- `scripts/21-extraer_puntajes_desde_web.py`

Extracción/organización (Fase 2):

- `scripts/extraer_puntajes_de_pdfs.py`
- `scripts/04-analizar_excel.py`

App/diagnóstico (Fase 3):

- `scripts-shell/iniciar_app_completa.sh`
- `scripts-shell/diagnosticar_streamlit.sh`

---

## 10) Despliegue

- Local: `./iniciar_aplicacion.sh` o `streamlit run streamlit_app.py`.
- Streamlit Cloud: ver `INSTRUCCIONES-STREAMLIT-CLOUD.md` e `INSTRUCCIONES-DESPLIEGUE-STREAMLIT-CLOUD.md`. Revisa `config/requirements-webapp.txt` si aplica.

---

## 11) Capturas

- `captura_login_firefox.png`: Flujo de acceso al sitio oficial de resultados
- `captura_resultados.png`: Vista general de la app
- `nop.png`: Imagen auxiliar

---

## 12) Créditos

Institución: Pedacito de Cielo (La Tebaida, Quindío)
Años comparados: 2024 vs 2025
Modelos: Aula Regular y Modelo Flexible

Documentación relacionada:

- `GUIA-USO-APLICACION-COMPARATIVA.md`
- `README-APLICACION-COMPARATIVA.md`
- `RESUMEN-EJECUTIVO-APLICACION.md`
- `ESTRUCTURA-PROYECTO.md`
- `INICIO-RAPIDO.md`
- `docs-proyecto/README-WEBAPP.md`

Última actualización: 2025-10-23  
Versión: 2.0  
Estado: ✅ Funcional