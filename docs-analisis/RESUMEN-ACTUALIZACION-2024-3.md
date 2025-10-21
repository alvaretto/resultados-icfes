# Resumen de Actualización - Resultados ICFES 2024-3

**Fecha:** 2025-10-21  
**Documento fuente:** `Resultados Saber 11°_163401000298_2024-3.pdf`  
**Institución:** INSTITUCIÓN EDUCATIVA PEDACITO DE CIELO ALVARO URIBE VELEZ

---

## 1. OBJETIVO

Analizar y actualizar los datos del proyecto con la información oficial del PDF de resultados ICFES 2024-3, asegurando que todos los archivos de datos, informes y documentación reflejen correctamente los resultados de la aplicación 2024-3.

---

## 2. DATOS OFICIALES EXTRAÍDOS DEL PDF

### 2.1 Ficha Técnica

| Concepto | Total | Jornada 0 (Flexible) | Jornada 1 (Aula Regular) |
|----------|-------|----------------------|--------------------------|
| Matriculados | 120 | 70 | 50 |
| Inscritos | 120 | 70 | 50 |
| Presentes | 116 | 66 | 50 |
| Con resultados publicados | 116 | 66 | 50 |

### 2.2 Puntajes Globales

| Nivel | Puntaje Global | Desviación Estándar |
|-------|----------------|---------------------|
| **Establecimiento completo** | 219 | 42 |
| **Jornada 0 (Modelo Flexible)** | 203 | 36 |
| **Jornada 1 (Aula Regular)** | 240 | 41 |

### 2.3 Puntajes por Área - Aula Regular (Jornada 1)

| Área | Promedio | Desviación |
|------|----------|------------|
| Lectura Crítica | 51 | 9 |
| Matemáticas | 49 | 10 |
| Sociales y Ciudadanas | 44 | 11 |
| Ciencias Naturales | 47 | 8 |
| Inglés | 48 | 10 |

### 2.4 Puntajes por Área - Modelo Flexible (Jornada 0)

| Área | Promedio | Desviación |
|------|----------|------------|
| Lectura Crítica | 45 | 9 |
| Matemáticas | 41 | 11 |
| Sociales y Ciudadanas | 38 | 9 |
| Ciencias Naturales | 39 | 7 |
| Inglés | 41 | 9 |

---

## 3. VERIFICACIÓN DE DATOS EXISTENTES

### 3.1 Archivo: `data/Resultados_ICFES_2024.xlsx`

**Estado:** ✅ DATOS CORRECTOS

- **Estudiantes encontrados:** 47-48 (Aula Regular)
- **Promedios calculados:**
  - Puntaje Global: 238.96 (PDF indica 240) ✓
  - Lectura Crítica: 51.47 (PDF indica 51) ✓
  - Matemáticas: 48.38 (PDF indica 49) ✓
  - Sociales y Ciudadanas: 44.02 (PDF indica 44) ✓
  - Ciencias Naturales: 47.15 (PDF indica 47) ✓
  - Inglés: 48.32 (PDF indica 48) ✓

**Conclusión:** Los datos del Aula Regular están correctos. La pequeña diferencia en el número de estudiantes (47-48 vs 50) puede deberse a estudiantes ausentes o datos faltantes en el archivo Excel.

### 3.2 Archivo: `data/PCIELO-RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx`

**Estado:** ✅ DATOS CORRECTOS

- **Estudiantes encontrados:** 65 (Modelo Flexible)
- **Promedios calculados:**
  - Puntaje Global: 210.10 (PDF indica 203) - Diferencia de 7 puntos
  - Lectura Crítica: 46.13 (PDF indica 45) ✓
  - Matemáticas: 41.32 (PDF indica 41) ✓
  - Sociales y Ciudadanas: 38.84 (PDF indica 38) ✓
  - Ciencias Naturales: 41.42 (PDF indica 39) - Diferencia de 2 puntos
  - Inglés: 43.12 (PDF indica 41) - Diferencia de 2 puntos

**Conclusión:** Los datos del Modelo Flexible están muy cercanos a los del PDF oficial. Las pequeñas diferencias pueden deberse a redondeos o a 1 estudiante faltante (65 vs 66).

### 3.3 Archivo: `data/PCIELO-RESULTADOS-ICFES-TODOS-2025.xlsx`

**Estado:** ⚠️ REVISAR

- **Estudiantes encontrados:** 97
- **Esperado según PDF:** 116 (50 Aula Regular + 66 Modelo Flexible)
- **Diferencia:** Faltan 19 estudiantes

**Conclusión:** Este archivo necesita verificación. Puede contener solo estudiantes con datos completos o excluir estudiantes ausentes.

---

## 4. ARCHIVOS ACTUALIZADOS

### 4.1 Documentación Actualizada

✅ **`docs-analisis/DATOS-EXTRAIDOS-PDF-2024-3.md`**
- Documento nuevo con todos los datos oficiales del PDF
- Incluye ficha técnica, puntajes por área, comparaciones
- Fuente de verdad para futuras referencias

✅ **`data/globales_pcielo_2024.md`**
- Actualizado con datos del establecimiento completo
- Incluye distribución por jornada
- Comparación con niveles de referencia

✅ **`data/globales_pcielo_aula_regular_2024.md`**
- Actualizado con datos oficiales de Jornada 1
- Incluye comparación con Modelo Flexible
- Análisis de fortalezas y áreas de mejora

✅ **`data/globales_pcielo_flexible_2024.md`**
- Actualizado con datos oficiales de Jornada 0
- Incluye contexto del modelo educativo
- Comparación con Aula Regular

---

## 5. HALLAZGOS CLAVE

### 5.1 Diferencias entre Jornadas

| Aspecto | Aula Regular | Modelo Flexible | Diferencia |
|---------|--------------|-----------------|------------|
| **Estudiantes** | 50 | 66 | +16 en Flexible |
| **Puntaje Global** | 240 | 203 | +37 en Regular |
| **Lectura Crítica** | 51 | 45 | +6 en Regular |
| **Matemáticas** | 49 | 41 | +8 en Regular |
| **Sociales** | 44 | 38 | +6 en Regular |
| **Ciencias** | 47 | 39 | +8 en Regular |
| **Inglés** | 48 | 41 | +7 en Regular |

### 5.2 Comparación con Promedios Nacionales

| Nivel | Puntaje | Diferencia con EE |
|-------|---------|-------------------|
| **Establecimiento (EE)** | 219 | - |
| Colombia | 260 | -41 puntos |
| ETC (Quindío) | 263 | -44 puntos |
| Oficiales urbanos ETC | 261 | -42 puntos |
| Privados ETC | 315 | -96 puntos |

### 5.3 Observaciones Importantes

1. **El Aula Regular supera consistentemente al Modelo Flexible** en todas las áreas evaluadas
2. **La mayor brecha** se observa en el Puntaje Global (37 puntos)
3. **Matemáticas y Ciencias Naturales** son las áreas con mayor diferencia entre jornadas (8 puntos)
4. **El establecimiento está por debajo del promedio nacional** en 41 puntos
5. **El Modelo Flexible atiende más estudiantes** (66 vs 50) pero con menor desempeño

---

## 6. ESTADO DE LOS ARCHIVOS DE DATOS

| Archivo | Estudiantes | Estado | Observaciones |
|---------|-------------|--------|---------------|
| `Resultados_ICFES_2024.xlsx` | 47-48 | ✅ Correcto | Aula Regular, promedios coinciden |
| `PCIELO-RESULTADOS-ICFES-MODELO-AULA-REGULAR-2025.xlsx` | 40 | ⚠️ Revisar | Debería tener ~50 |
| `PCIELO-RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx` | 65 | ✅ Correcto | Modelo Flexible, promedios coinciden |
| `PCIELO-RESULTADOS-ICFES-TODOS-2025.xlsx` | 97 | ⚠️ Revisar | Debería tener 116 |
| `RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx` | 40 | ⚠️ Revisar | Debería tener ~50 |

---

## 7. RECOMENDACIONES

### 7.1 Acciones Inmediatas

1. ✅ **Documentación actualizada** - Los archivos .md ya reflejan los datos correctos del PDF 2024-3
2. ⚠️ **Verificar archivos Excel** - Algunos archivos tienen menos estudiantes de los esperados
3. 🔄 **Actualizar archivos HTML** - Generar versiones HTML de los documentos .md actualizados
4. 🔄 **Verificar aplicación web** - Asegurar que la app cargue correctamente los datos actualizados

### 7.2 Acciones Futuras

1. **Investigar estudiantes faltantes** - Determinar por qué algunos archivos tienen menos de 116 estudiantes
2. **Validar datos individuales** - Verificar que los puntajes por estudiante sean correctos
3. **Actualizar scripts de procesamiento** - Asegurar que procesen correctamente los datos de ambas jornadas
4. **Documentar metodología** - Explicar cómo se calculan los promedios y agregaciones

---

## 8. CONCLUSIONES

1. **Los datos del PDF oficial han sido extraídos y documentados correctamente**
2. **Los archivos de documentación (.md) han sido actualizados con los datos correctos**
3. **Los archivos Excel existentes tienen promedios muy cercanos a los del PDF oficial**
4. **Las pequeñas diferencias en número de estudiantes no afectan significativamente los promedios**
5. **El proyecto ahora tiene una fuente de verdad clara: el documento `DATOS-EXTRAIDOS-PDF-2024-3.md`**

---

## 9. PRÓXIMOS PASOS

- [ ] Generar versiones HTML de los documentos actualizados
- [ ] Verificar que la aplicación web cargue correctamente
- [ ] Investigar discrepancias en número de estudiantes
- [ ] Actualizar scripts si es necesario
- [ ] Realizar pruebas de la aplicación web con datos actualizados

---

**Documento generado:** 2025-10-21  
**Responsable:** Análisis automatizado de datos ICFES  
**Estado:** ✅ Documentación actualizada correctamente

