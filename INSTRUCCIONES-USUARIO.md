# 📖 Instrucciones para el Usuario

Última actualización: 2025-10-23  
**Proyecto:** Análisis Resultados ICFES 2024-3 - Pedacito de Cielo

---

## 🎯 ¿QUÉ SE HA HECHO?

Se ha completado el análisis del documento PDF oficial del ICFES "Resultados Saber 11°_163401000298_2024-3.pdf" y se han actualizado todos los archivos del proyecto con los datos correctos.

### Resumen de Acciones:

✅ **Análisis completo del PDF oficial del ICFES**  
✅ **Extracción de todos los datos relevantes**  
✅ **Actualización de archivos de documentación**  
✅ **Verificación de datos existentes**  
✅ **Validación de la aplicación web**  
✅ **Creación de documentación detallada**

---

## 📂 ARCHIVOS IMPORTANTES PARA TI

### 1. Resumen Ejecutivo (EMPIEZA AQUÍ)

📄 **`RESUMEN-ANALISIS-PDF-2024-3.md`**

Este es el documento principal que debes leer primero. Contiene:
- Datos principales extraídos del PDF
- Hallazgos clave
- Comparaciones entre modelos educativos
- Estado de los archivos
- Conclusiones

### 2. Datos Oficiales Completos

📄 **`docs-analisis/DATOS-EXTRAIDOS-PDF-2024-3.md`**

Documento con TODOS los datos oficiales del PDF del ICFES:
- Ficha técnica completa
- Puntajes por área y jornada
- Desviaciones estándar
- Comparaciones con niveles de referencia
- Análisis detallado

**Este es tu "fuente de verdad" oficial.**

### 3. Resultados por Modelo Educativo

📄 **`data/globales_pcielo_aula_regular_2024.md`**
- Resultados del Aula Regular (Jornada 1)
- 50 estudiantes, grados 11A y 11B
- Puntaje global: 240

📄 **`data/globales_pcielo_flexible_2024.md`**
- Resultados del Modelo Flexible (Jornada 0)
- 66 estudiantes, grados P3A, P3B, P3C
- Puntaje global: 203

📄 **`data/globales_pcielo_2024.md`**
- Resultados del establecimiento completo
- 116 estudiantes en total
- Puntaje global: 219

---

## 🔍 DATOS CLAVE QUE DEBES CONOCER

### Estudiantes Evaluados

| Modelo | Estudiantes | Porcentaje |
|--------|-------------|------------|
| Modelo Flexible (Jornada 0) | 66 | 57% |
| Aula Regular (Jornada 1) | 50 | 43% |
| **TOTAL** | **116** | **100%** |

### Puntajes Globales

| Modelo | Puntaje | Comparación |
|--------|---------|-------------|
| **Aula Regular** | 240 | +37 vs Flexible |
| **Modelo Flexible** | 203 | -37 vs Regular |
| **Establecimiento** | 219 | -41 vs Nacional |
| **Colombia** | 260 | Referencia |

### Diferencias entre Modelos

El Aula Regular supera al Modelo Flexible en **todas las áreas**:

| Área | Aula Regular | Modelo Flexible | Diferencia |
|------|--------------|-----------------|------------|
| **Puntaje Global** | 240 | 203 | +37 |
| Lectura Crítica | 51 | 45 | +6 |
| Matemáticas | 49 | 41 | +8 |
| Sociales y Ciudadanas | 44 | 38 | +6 |
| Ciencias Naturales | 47 | 39 | +8 |
| Inglés | 48 | 41 | +7 |

---

## 💻 CÓMO USAR LA APLICACIÓN WEB

### Paso 1: Abrir Terminal

En Linux, abre una terminal en la carpeta del proyecto:
```bash
cd /home/proyectos/Escritorio/Resultados-ICFES-2025
```

### Paso 2: Activar Entorno Virtual (si existe)

```bash
source venv/bin/activate
```

### Paso 3: Ejecutar la Aplicación

```bash
streamlit run app/app_resultados_icfes.py
```

### Paso 4: Ver en el Navegador

La aplicación se abrirá automáticamente en tu navegador en:
```
http://localhost:8501
```

### Funcionalidades de la Aplicación:

- 📊 **Vista General:** Resumen de resultados
- 👤 **Por Estudiante:** Análisis individual
- 📚 **Por Área:** Comparación de áreas de conocimiento
- 🏆 **Rankings:** Mejores desempeños
- 📈 **Segmentación:** Análisis por grupos

---

## 📊 INTERPRETACIÓN DE RESULTADOS

### ¿Qué significan los puntajes?

#### Puntajes por Área (0-100)
- **0-40:** Bajo
- **40-60:** Medio
- **60-80:** Alto
- **80-100:** Superior

#### Puntaje Global (0-500)
- **0-200:** Bajo
- **200-300:** Medio
- **300-400:** Alto
- **400-500:** Superior

### Comparación con Promedios

| Nivel | Puntaje | Interpretación |
|-------|---------|----------------|
| **Tu institución** | 219 | Medio |
| Colombia | 260 | Referencia nacional |
| Quindío (ETC) | 263 | Referencia departamental |
| Privados Quindío | 315 | Alto |

**Tu institución está 41 puntos por debajo del promedio nacional.**

---

## 🎓 RECOMENDACIONES PEDAGÓGICAS

### Fortalezas a Mantener

1. **Lectura Crítica:** Mejor área en ambos modelos
   - Continuar estrategias de comprensión lectora
   - Mantener énfasis en análisis de textos

2. **Aula Regular:** Desempeño consistente
   - Documentar buenas prácticas
   - Compartir estrategias exitosas

### Áreas de Mejora Prioritaria

1. **Sociales y Ciudadanas:** Área más débil
   - Implementar estrategias específicas
   - Fortalecer competencias cívicas

2. **Modelo Flexible:** Requiere apoyo especial
   - Considerar contexto de vulnerabilidad
   - Implementar estrategias diferenciadas
   - Reforzar áreas de Matemáticas y Ciencias

3. **Brecha con promedio nacional:** 41 puntos
   - Establecer plan de mejoramiento institucional
   - Focalizar en áreas más débiles
   - Implementar seguimiento continuo

---

## 📁 ESTRUCTURA DE CARPETAS

```
Resultados-ICFES-2025/
│
├── 📄 RESUMEN-ANALISIS-PDF-2024-3.md          ← LEE ESTO PRIMERO
├── 📄 INSTRUCCIONES-USUARIO.md                ← Estás aquí
│
├── 📁 docs-analisis/
│   ├── DATOS-EXTRAIDOS-PDF-2024-3.md          ← Fuente de verdad
│   ├── RESUMEN-ACTUALIZACION-2024-3.md        ← Detalles técnicos
│   └── VERIFICACION-FINAL-ACTUALIZACION.md    ← Verificación
│
├── 📁 data/
│   ├── globales_pcielo_2024.md                ← Resultados generales
│   ├── globales_pcielo_aula_regular_2024.md   ← Aula Regular
│   ├── globales_pcielo_flexible_2024.md       ← Modelo Flexible
│   └── *.xlsx                                 ← Archivos de datos
│
└── 📁 app/
    └── app_resultados_icfes.py                ← Aplicación web
```

---

## ❓ PREGUNTAS FRECUENTES

### ¿Los datos son correctos?

✅ **SÍ.** Todos los datos han sido extraídos del PDF oficial del ICFES y verificados. Los archivos Excel del proyecto coinciden con los datos del PDF (diferencias menores a 2 puntos).

### ¿Por qué hay diferencias en el número de estudiantes?

Algunos archivos tienen menos estudiantes porque:
- Estudiantes ausentes (no presentaron el examen)
- Datos incompletos en algunos registros
- Filtros aplicados en la aplicación web

**Total oficial:** 116 estudiantes con resultados publicados.

### ¿Qué archivo debo usar como referencia?

📄 **`docs-analisis/DATOS-EXTRAIDOS-PDF-2024-3.md`**

Este es tu fuente de verdad oficial con todos los datos del PDF del ICFES.

### ¿La aplicación web funciona correctamente?

✅ **SÍ.** La aplicación ha sido verificada y funciona correctamente con los datos actualizados. Carga ambos modelos educativos y genera análisis comparativos.

### ¿Qué significan las jornadas?

- **Jornada 0 (TARDE):** Modelo Flexible (Pensar) - Grados P3A, P3B, P3C
- **Jornada 1 (ÚNICA):** Aula Regular - Grados 11A, 11B

### ¿Por qué el Modelo Flexible tiene menor puntaje?

El Modelo Flexible atiende población con características especiales:
- Estudiantes en situación de vulnerabilidad
- Personas con extra-edad
- Requieren flexibilidad horaria
- Contexto socioeconómico diferente

Estos factores contextuales explican las diferencias en desempeño.

---

## 🚀 PRÓXIMOS PASOS SUGERIDOS

### Inmediatos:

1. ✅ **Leer el resumen ejecutivo:** `RESUMEN-ANALISIS-PDF-2024-3.md`
2. ✅ **Revisar datos oficiales:** `docs-analisis/DATOS-EXTRAIDOS-PDF-2024-3.md`
3. ✅ **Ejecutar la aplicación web** para ver visualizaciones

### Corto Plazo:

4. 📊 **Analizar resultados por área** en los documentos específicos
5. 🎓 **Identificar estrategias de mejora** basadas en los hallazgos
6. 📈 **Establecer metas** para la próxima aplicación

### Mediano Plazo:

7. 📋 **Crear plan de mejoramiento** institucional
8. 👥 **Socializar resultados** con docentes y directivos
9. 🔄 **Implementar estrategias** diferenciadas por modelo
10. 📊 **Hacer seguimiento** continuo del progreso

---

## 📞 SOPORTE

### Documentos de Ayuda:

- **Resumen ejecutivo:** `RESUMEN-ANALISIS-PDF-2024-3.md`
- **Datos completos:** `docs-analisis/DATOS-EXTRAIDOS-PDF-2024-3.md`
- **Verificación técnica:** `docs-analisis/VERIFICACION-FINAL-ACTUALIZACION.md`

### Archivos de Datos:

- **Aula Regular:** `data/PCIELO-RESULTADOS-ICFES-MODELO-AULA-REGULAR-2025.xlsx`
- **Modelo Flexible:** `data/PCIELO-RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx`
- **Todos:** `data/PCIELO-RESULTADOS-ICFES-TODOS-2025.xlsx`

---

## ✅ CHECKLIST PARA EL USUARIO

- [ ] He leído el resumen ejecutivo
- [ ] He revisado los datos oficiales del PDF
- [ ] He ejecutado la aplicación web
- [ ] He revisado los resultados por modelo educativo
- [ ] He identificado fortalezas y áreas de mejora
- [ ] He compartido los resultados con el equipo directivo
- [ ] He iniciado el plan de mejoramiento

---

---

**Última actualización:** 2025-10-23  
**Versión:** 2.0  
**Estado:** ✅ Funcional

