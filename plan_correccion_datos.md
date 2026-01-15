# Plan de Corrección de Datos - Proyecto ICFES 2025

Basado en el `Reporte_Inconsistencias.md`, se han identificado los siguientes cambios necesarios para alinear el proyecto con la Fuente de Verdad (PDF Oficial).

## 1. Actualización de Nombres de Modelo (Inconsistencia de Nombres)

El reporte indica que "Aula Regular" y "Modelo Flexible" son nombres internos no presentes en la fuente oficial.

**Cambios en `streamlit_app.py`:**
- **Variable `DATOS_INSTITUCIONES_TEBAIDA`**:
    - Cambiar `'PEDACITO DE CIELO (Aula Regular)'` por `'PEDACITO DE CIELO (Sede 0 / Jornada 1)'`.
    - Cambiar `'PEDACITO DE CIELO (Modelo Flexible)'` por `'PEDACITO DE CIELO (Sede 0 / Jornada 0)'`.

**Cambios en Visualización (UI):**
- Actualizar las etiquetas en los selectores y gráficos para usar "Jornada 1" y "Jornada 0" en lugar de "Aula Regular" y "Modelo Flexible", o usar un formato híbrido: "Jornada 1 (Aula Regular)".

## 2. Manejo de Datos Individuales (Inconsistencia de Granularidad)

El reporte establece que "Es imposible validar matemáticamente las afirmaciones... usando únicamente el PDF". El proyecto actualmente carga Excel (`RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx`) con datos individuales.

**Acciones Requeridas:**
- **Opción A (Estricta):** Eliminar la carga de archivos Excel y las secciones de "Estadísticas por Estudiante". (Recomendado si se exige estricta adherencia a la fuente PDF).
- **Opción B (Informativa):** Mantener la funcionalidad pero agregar un **Disclaimer Visible** en `mostrar_estadisticas_estudiante`:
    > *"⚠️ Nota: Los datos a nivel de estudiante provienen de fuentes auxiliares (Excel) y no están disponibles en el reporte oficial agregado del ICFES (Fuente de Verdad)."*

## 3. Verificación de Promedios Globales

El reporte indica:
- Promedio Institucional Real: **221**
- Jornada 0 (Flexible): **214**
- Jornada 1 (Regular): **234**

**Cambios en `streamlit_app.py`:**
- Verificar que la función `calcular_estadisticas_2025` calcule exactamente **214** y **234**.
- (El código actual ya tiene hardcodeados 234 y 214 en `DATOS_INSTITUCIONES_TEBAIDA`, lo cual es correcto según la fuente de verdad).
- Asegurar que el promedio institucional "Global" mostrado sea **221**. Actualmente se calcula como promedio de todos los estudiantes en el Excel. Se debe validar si `(234*40 + 214*66) / 106` da aprox 221.

## 4. Archivos Afectados

1.  `streamlit_app.py`: Etiquetas de texto, claves de diccionarios y disclaimers.
2.  `app_icfes_comparativo.py`: (Copia de respaldo) mismoscambios.
3.  `data/`: Los nombres de los archivos Excel (`...AULA-REGULAR...`) podrían renombrarse a `...JORNADA-1...` para consistencia, aunque no es estrictamente funcional.

---
**Recomendación Inmediata:** Aplicar los cambios de nombre en `streamlit_app.py` y agregar el disclaimer de fuente de datos.
