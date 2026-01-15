# Plan de Implementación: Corrección de Datos y Nombres (Iteración 2)

Este plan tiene como objetivo re-aplicar las correcciones al código del proyecto (`streamlit_app.py`) para alinearlo con el `Reporte_Inconsistencias.md` y la "Fuente de Verdad" (PDF Oficial), recuperando el trabajo perdido tras el reinicio de git.

## Cambios en `streamlit_app.py`

### 1. Renombrar Modelos (Interfaz y Datos)
Actualizar todas las etiquetas visuales y claves de datos para cumplir con la solicitud del usuario:
- **"Aula Regular"** $\rightarrow$ **"Aula Regular (Jornada 1)"**
- **"Modelo Flexible"** $\rightarrow$ **"Modelo Flexible (Jornada 0)"**

### 2. Hardcodear Datos Oficiales (KPIs)
Para garantizar que los indicadores principales coincidan exactamente con el PDF oficial (y no dependan del cálculo variable de Excel):

```python
DATOS_OFICIALES_2025 = {
    'Todos': { 'puntaje_global': 221, ... },
    'Aula Regular (Jornada 1)': { 'puntaje_global': 234, ... },
    'Modelo Flexible (Jornada 0)': { 'puntaje_global': 214, ... }
}
```

### 3. Lógica Híbrida de Cálculo
Modificar `calcular_estadisticas_2025` para:
- Retornar los valores de `DATOS_OFICIALES_2025` si el modelo coincide.
- Calcular desde Excel solo si no hay dato oficial (o para histogramas/listados), agregando el disclaimer de fuente.

### 4. Disclaimer de Fuente
Re-implementar el aviso en la sección de estudiantes:
> "⚠️ Nota: Los datos a nivel de estudiante provienen de fuentes auxiliares (Excel) y no están disponibles en el reporte oficial agregado del ICFES (Fuente de Verdad)."

## Plan de Verificación

1.  **Verificación Visual (Browser)**:
    *   Confirmar que los selectores muestran "Aula Regular (Jornada 1)".
    *   Confirmar que el Promedio Global es **221**.
2.  **Verificación de Logs**:
    *   Asegurar que no hay errores de sintaxis al iniciar la app.
