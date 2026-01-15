# Reporte de Inconsistencias: Fuentes de Verdad vs Análisis Detallado

**Fecha:** 14 de Enero de 2026
**Objetivo:** Alinear el análisis del proyecto con los documentos oficiales "Fuente de Verdad" del ICFES.

| Ítem | Fuente de Verdad (PDF Oficial 2025) | Análisis Detallado (PDF Meta) | Inconsistencia / Observación | Acción Requerida |
| :--- | :--- | :--- | :--- | :--- |
| **Nombres de Jornadas** | • **Sede 0 / Jornada 1**<br>• **Sede 0 / Jornada 0** | • **PEDACITO DE CIELO REGULAR**<br>• **PEDACITO DE CIELO PENSAR** | El análisis usa nombres internos/comerciales ("Regular", "Pensar") que no existen en el reporte oficial. | **RENOMBRAR EN PROYECTO:**<br>• "Aula Regular" $\rightarrow$ **"Aula Regular (Jornada 1)"**<br>• "Modelo Flexible" $\rightarrow$ **"Modelo Flexible (Jornada 0)"** |
| **Puntajes Globales** | • Jornada 1: **234**<br>• Jornada 0: **214**<br>• Institucional: **221** | • Regular: **234**<br>• Pensar: **214** | **No hay inconsistencia numérica.** El análisis refleja correctamente los valores oficiales agregados. | Mantener y asegurar que el aplicativo muestre estos valores exactos (hardcoded si es necesario). |
| **Puntajes por Área** | Ej. Lectura Crítica:<br>• Inst: 48<br>• Jornada 1: 51<br>• Jornada 0: 47 | Ej. Lectura Crítica:<br>• Regular: 51<br>• Pensar: 47 | **Valores consistentes.** | Alinear visualización para que coincida con el PDF. |
| **Población (Granularidad)** | Reporte Agregado (N=95):<br>• Jornada 1: 36<br>• Jornada 0: 59 | Análisis Detallado:<br>• Cita "estudiantes Convenio Univalle"<br>• Cita rangos específicos | El análisis incluye un nivel de detalle (subgrupos Univalle) que **no existe** en el PDF oficial. Implica una fuente de datos tercera (Excel/Base de Datos). | Mantener disclaimers sobre la fuente de datos detallados (Excel) vs datos oficiales (PDF). |

## Conclusión

El documento "ANALISIS DETALLADO" es numéricamente preciso respecto a los promedios del PDF Oficial, pero utiliza terminología no oficial ("Regular"/"Pensar").

**Acciones de Corrección Inmediata:**
1.  Aplicar el cambio de nombres en todo el código y documentación del proyecto.
2.  Garantizar que los promedios globales mostrados en la App sean **221** (Global), **234** (Jornada 1) y **214** (Jornada 0).

### 4. Discrepancia en Análisis Textual (Evolución)
- **Fuente (PDF Análisis Municipal):**
  - **Tabla de Resultados:** Muestra Pedacito Regular 2024 (240) -> 2025 (234). Diferencia matemática: **-6**.
  - **Texto de Análisis:** Menciona "disminución ... de (7 puntos)".
  - **Tabla de Resultados:** Muestra Pedacito Flexible 2024 (203) -> 2025 (214). Diferencia matemática: **+11**.
  - **Texto de Análisis:** Menciona "sube 9 puntos".
- **Observación:** Existe una contradicción interna en el PDF de Análisis entre sus propias tablas y su texto narrativo.
- **Acción:** Se mantiene el uso de los **Datos Numéricos de las Tablas** (234/214), ya que coinciden con los Reportes Oficiales (Fuente de Verdad Primaria 2024 y 2025).
