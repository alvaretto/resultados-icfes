# 📖 Guía de Uso - Aplicación de Análisis ICFES Completa

## Institución Educativa Pedacito de Cielo

Esta guía te ayudará a utilizar todas las funcionalidades de la aplicación de análisis de resultados ICFES Saber 11.

---

## 🚀 Inicio Rápido

### 1. Ejecutar la Aplicación

```bash
cd /home/proyectos/Escritorio/Resultados-ICFES-2025
streamlit run app_resultados_icfes_completo.py
```

### 2. Acceder desde el Navegador

La aplicación se abrirá automáticamente en: `http://localhost:8501`

---

## 📊 Guía por Pestañas

### Pestaña 1: Vista General

**¿Qué puedo hacer aquí?**
- Ver un resumen general de ambos modelos educativos
- Comparar el número de estudiantes por modelo
- Ver la distribución de estudiantes por clasificación
- Comparar promedios generales entre modelos

**Casos de uso:**
- Obtener una visión panorámica de los resultados
- Identificar diferencias generales entre modelos
- Preparar presentaciones con datos generales

---

### Pestaña 2: Comparación entre Modelos

**¿Qué puedo hacer aquí?**
- Comparar el desempeño entre Aula Regular y Modelo Flexible
- Ver estadísticas descriptivas de cada modelo
- Realizar tests estadísticos de significancia
- Visualizar distribuciones comparativas

**Cómo usar:**
1. Selecciona el área que deseas analizar (o Puntaje Global)
2. Revisa las estadísticas comparativas en las columnas
3. Observa el test estadístico para determinar si hay diferencias significativas
4. Analiza los gráficos de caja y distribución

**Interpretación del test estadístico:**
- **p < 0.05**: Hay diferencia estadísticamente significativa
- **p ≥ 0.05**: No hay diferencia estadísticamente significativa

---

### Pestaña 3: Comparación entre Grupos

**¿Qué puedo hacer aquí?**
- Comparar grupos dentro del mismo modelo
- Ver estadísticas por grupo
- Realizar tests entre pares de grupos

**Cómo usar:**
1. Selecciona el modelo educativo (Aula Regular o Flexible)
2. Selecciona el área a analizar
3. Revisa la tabla de estadísticas por grupo
4. Observa los gráficos comparativos
5. (Opcional) Selecciona dos grupos para realizar un test estadístico

**Ejemplos de análisis:**
- ¿Hay diferencia entre 11A y 11B en Matemáticas?
- ¿Qué grupo del Modelo Flexible tiene mejor desempeño en Lectura Crítica?

---

### Pestaña 4: Análisis por Estudiante

**¿Qué puedo hacer aquí?**
- Ver el perfil completo de un estudiante
- Comparar su desempeño con los promedios
- Ver su posición en diferentes rankings
- Analizar sus percentiles por área

**Cómo usar:**
1. Selecciona el modelo educativo
2. Selecciona el estudiante de la lista
3. Revisa su información básica (grupo, puntaje global, clasificación)
4. Analiza la tabla comparativa con promedios
5. Observa el radar chart de competencias
6. Revisa sus posiciones en rankings
7. Analiza sus percentiles por área

**Casos de uso:**
- Reuniones con padres de familia
- Identificar fortalezas y debilidades del estudiante
- Planificar refuerzos académicos personalizados

---

### Pestaña 5: Análisis por Área

**¿Qué puedo hacer aquí?**
- Analizar en profundidad una área específica
- Comparar el área entre modelos y grupos
- Ver rankings del área
- Realizar análisis estadísticos del área

**Cómo usar:**
1. Selecciona el área a analizar
2. Revisa las estadísticas generales
3. Observa la comparación entre modelos
4. Analiza la comparación entre todos los grupos
5. Revisa el top 10 del área
6. (Opcional) Ver el ranking completo

**Ejemplos de análisis:**
- ¿En qué modelo se desempeñan mejor en Matemáticas?
- ¿Qué grupo tiene el mejor promedio en Inglés?
- ¿Quiénes son los mejores estudiantes en Ciencias Naturales?

---

### Pestaña 6: Rankings Generales

**¿Qué puedo hacer aquí?**
- Ver rankings de diferentes tipos
- Identificar a los mejores estudiantes
- Comparar posiciones entre modelos y grupos

**Tipos de ranking disponibles:**

1. **Global (Todos)**
   - Ranking de todos los estudiantes
   - Visualización de top 20
   - Opción de ver ranking completo

2. **Por Modelo**
   - Ranking dentro de Aula Regular
   - Ranking dentro de Modelo Flexible

3. **Por Grupo**
   - Ranking dentro de cada grupo específico

4. **Por Área**
   - Ranking de cada área específica

**Casos de uso:**
- Identificar estudiantes destacados
- Reconocimientos y estímulos académicos
- Análisis de competitividad entre grupos

---

### Pestaña 7: Análisis Estadístico Avanzado

**¿Qué puedo hacer aquí?**
- Ver correlaciones entre áreas
- Analizar percentiles
- Segmentar por clasificación

**Cómo usar:**

**Correlaciones:**
1. Selecciona el modelo (o "Todos")
2. Observa el mapa de calor de correlaciones
3. Identifica áreas con alta correlación (valores cercanos a 1)

**Interpretación de correlaciones:**
- **0.7 - 1.0**: Correlación fuerte positiva
- **0.3 - 0.7**: Correlación moderada
- **0.0 - 0.3**: Correlación débil
- **Negativas**: Relación inversa

**Percentiles:**
1. Selecciona un área
2. Revisa los valores de P10, P25, P50, P75, P90
3. Usa estos valores para clasificar estudiantes

**Segmentación:**
- Ver distribución por clasificación (Bajo, Medio, Alto, Superior)
- Identificar grupos que requieren atención

---

### Pestaña 8: Comparación Temporal

**¿Qué puedo hacer aquí?**
- Ver la evolución 2024-2025 de ambos modelos educativos
- Seleccionar entre Modelo Aula Regular o Modelo Flexible
- Identificar áreas con mejora o retroceso
- Analizar cambios porcentuales

**Nota sobre disponibilidad de datos:**
- **Modelo Aula Regular:** Datos completos 2024-2025 (todas las áreas disponibles)
- **Modelo Flexible:** Solo puntaje global 2024 disponible (203 puntos). Los datos por área de 2024 están pendientes de definición

**Cómo usar:**
1. Revisa la tabla comparativa 2024 vs 2025
2. Observa el gráfico de evolución de promedios
3. Analiza el gráfico de avances y retrocesos
4. Lee el análisis de áreas con mejora y retroceso
5. Revisa el resumen general

**Casos de uso:**
- Evaluar efectividad de estrategias pedagógicas
- Identificar áreas que requieren refuerzo
- Planificar mejoras para el próximo año

---

## 💡 Consejos y Mejores Prácticas

### Para Docentes

1. **Análisis Individual:**
   - Usa la pestaña "Análisis por Estudiante" para preparar reuniones con padres
   - Identifica fortalezas y debilidades específicas
   - Compara con promedios para contextualizar el desempeño

2. **Planificación de Refuerzos:**
   - Usa "Análisis por Área" para identificar áreas débiles
   - Revisa los rankings para identificar estudiantes que necesitan apoyo
   - Analiza correlaciones para entender relaciones entre áreas

3. **Seguimiento:**
   - Usa "Comparación Temporal" para evaluar el impacto de tus estrategias
   - Compara grupos para identificar mejores prácticas

### Para Coordinadores Académicos

1. **Evaluación de Modelos:**
   - Usa "Comparación entre Modelos" para evaluar efectividad
   - Realiza tests estadísticos para decisiones basadas en evidencia
   - Compara distribuciones para entender diferencias

2. **Gestión de Grupos:**
   - Usa "Comparación entre Grupos" para equilibrar grupos
   - Identifica grupos que requieren atención especial
   - Compara estrategias entre grupos exitosos

3. **Reportes Institucionales:**
   - Usa "Vista General" para presentaciones ejecutivas
   - Genera rankings para reconocimientos
   - Usa "Comparación Temporal" para mostrar evolución

### Para Directivos

1. **Toma de Decisiones:**
   - Basa decisiones en tests estadísticos, no solo en promedios
   - Considera el tamaño de muestra al comparar grupos
   - Analiza tendencias temporales para planificación estratégica

2. **Comunicación:**
   - Usa visualizaciones claras para comunicar resultados
   - Contextualiza los datos con promedios y percentiles
   - Destaca tanto logros como áreas de mejora

---

## ❓ Preguntas Frecuentes

**P: ¿Por qué no se comparan promedios entre áreas diferentes?**
R: Cada área del ICFES tiene escalas y criterios de evaluación diferentes. Comparar Matemáticas con Lectura Crítica no es metodológicamente válido según el ICFES.

**P: ¿Qué significa "p < 0.05" en los tests estadísticos?**
R: Significa que hay menos del 5% de probabilidad de que la diferencia observada sea por azar. Es decir, la diferencia es estadísticamente significativa.

**P: ¿Dónde están los datos 2024 del Modelo Flexible?**
R: Para el Modelo Flexible, solo el puntaje global de 2024 está disponible (203 puntos). Los datos por área de 2024 (Lectura Crítica, Matemáticas, Sociales y Ciudadanas, Ciencias Naturales e Inglés) aún no han sido definidos y se agregarán en futuras actualizaciones. Puedes ver el puntaje global en la pestaña "Comparación Temporal" seleccionando "Modelo Flexible".

**P: ¿Cómo interpreto el radar chart?**
R: El radar chart muestra el perfil de competencias del estudiante. Áreas más alejadas del centro indican mejor desempeño.

**P: ¿Qué es un percentil?**
R: El percentil indica el porcentaje de estudiantes que están por debajo de un puntaje dado. Por ejemplo, estar en el percentil 75 significa que el estudiante superó al 75% de sus compañeros.

---

## 🔧 Solución de Problemas

**Problema: La aplicación no carga**
- Verifica que los archivos Excel estén en la ubicación correcta
- Asegúrate de haber instalado todas las dependencias: `pip install -r requirements-webapp.txt`

**Problema: Error al cargar datos**
- Verifica que los archivos Excel no estén abiertos en otra aplicación
- Comprueba que los archivos no estén corruptos

**Problema: Gráficos no se muestran**
- Actualiza tu navegador
- Limpia la caché de Streamlit: `streamlit cache clear`

---

## 📞 Soporte

Para soporte técnico o preguntas sobre la aplicación, contacta al equipo de desarrollo.

---

**Última actualización:** 2025-10-16
**Versión de la aplicación:** 1.0 Completa

