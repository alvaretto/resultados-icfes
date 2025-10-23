# 📊 Guía de Uso - Aplicación Comparativa ICFES 2024 vs 2025

## 🎯 Descripción General

Esta aplicación Streamlit permite analizar y comparar los resultados ICFES Saber 11° de la Institución Educativa Pedacito de Cielo entre los años 2024 y 2025.

## 🚀 Cómo Iniciar la Aplicación

### Opción 1: Desde la terminal

```bash
cd /home/proyectos/Escritorio/Resultados-ICFES-2025
streamlit run streamlit_app.py
```

### Opción 2: Con puerto específico

```bash
streamlit run streamlit_app.py --server.port 8501
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📑 Estructura de la Aplicación

### 🏠 Página Principal - Comparativo General

**Qué encontrarás:**
- Comparación del puntaje global institucional 2024 vs 2025
- Indicadores de avance con formato condicional:
  - ✅ Verde: "Avanzó X puntos" (mejora)
  - ❌ Rojo: "Retrocedió X puntos" (disminución)
  - ⚪ Amarillo: "No subió. No bajó" (sin cambio)
- Tabla comparativa por áreas de conocimiento
- Gráficos de barras comparativos
- Gráfico de avances por área
- Comparativo por modelo educativo (Aula Regular vs Modelo Flexible)

**Cómo usarla:**
1. Al abrir la aplicación, esta página se muestra por defecto
2. Revisa las métricas principales en la parte superior
3. Desplázate hacia abajo para ver los comparativos detallados
4. Los gráficos son interactivos: puedes hacer hover para ver valores exactos

---

### 📊 Estadísticas por Estudiante

**Qué encontrarás:**
- Selector desplegable con todos los estudiantes
- Información personal del estudiante (grupo, modelo, documento)
- Puntaje global del estudiante
- Tabla con puntajes por área
- Gráfico de barras con los puntajes del estudiante

**Cómo usarla:**
1. Selecciona un estudiante del menú desplegable
2. La información se actualiza automáticamente
3. Puedes comparar visualmente el desempeño en diferentes áreas

---

### 🎓 Estadísticas por Grado

**Qué encontrarás:**
- Selector de grado (11A, 11B, P3A, P3B, P3C)
- Métricas del grado:
  - Número de estudiantes
  - Puntaje global promedio
  - Puntaje máximo y mínimo
- Tabla de promedios por área con desviación estándar
- Gráfico de barras de promedios
- Lista completa de estudiantes del grado ordenados por puntaje

**Cómo usarla:**
1. Selecciona el grado que deseas analizar
2. Revisa las métricas generales
3. Analiza los promedios por área
4. Consulta la lista de estudiantes al final

---

### 📚 Estadísticas por Área

**Qué encontrarás:**
- Selector de área de conocimiento
- Comparativo 2024 vs 2025 para el área seleccionada
- Indicador de avance con formato condicional
- Histograma de distribución de puntajes por modelo
- Estadísticas detalladas por modelo educativo:
  - Promedio
  - Desviación estándar
  - Puntaje máximo y mínimo

**Cómo usarla:**
1. Selecciona el área que deseas analizar
2. Observa el comparativo 2024 vs 2025
3. Analiza la distribución de puntajes en el histograma
4. Compara el desempeño entre modelos educativos

---

### 🏫 Estadísticas por Modelo

**Qué encontrarás:**
- Selector de modelo educativo (Aula Regular o Modelo Flexible)
- Métricas generales del modelo:
  - Número de estudiantes 2024 y 2025
  - Puntaje global 2024 y 2025
- Indicador de avance global
- Tabla comparativa por áreas
- Gráficos comparativos y de avances

**Cómo usarla:**
1. Selecciona el modelo educativo que deseas analizar
2. Revisa las métricas generales
3. Analiza el avance global del modelo
4. Consulta la tabla y gráficos para ver el desempeño por área

---

### 📈 Análisis de Avances

**Qué encontrarás:**
- Avances institucionales generales
- Tabla detallada de avances por área con:
  - Puntajes 2024 y 2025
  - Avance en puntos
  - Avance en porcentaje
- Gráfico de avances por área
- Comparativo de avances por modelo educativo
- Tablas de avances por área para cada modelo

**Cómo usarla:**
1. Revisa el avance institucional general
2. Analiza qué áreas mejoraron y cuáles retrocedieron
3. Compara los avances entre modelos educativos
4. Identifica áreas de fortaleza y oportunidades de mejora

---

### 🏆 Rankings y Destacados

**Qué encontrarás:**
- Top 10 estudiantes por puntaje global
- Gráfico de barras del Top 10
- Mejores 5 estudiantes por cada área (en pestañas)
- Top 5 por modelo educativo:
  - Aula Regular
  - Modelo Flexible
- Ranking por grado (Top 10 del grado seleccionado)

**Cómo usarla:**
1. Revisa el Top 10 general
2. Navega por las pestañas para ver los mejores por área
3. Consulta los rankings por modelo educativo
4. Selecciona un grado para ver su ranking específico

---

### 📥 Descargar Datos

**Qué encontrarás:**
- Selector de conjunto de datos:
  - Todos los estudiantes
  - Aula Regular
  - Modelo Flexible
- Vista previa de los datos
- Botones de descarga en dos formatos:
  - 📄 CSV (para análisis en Excel, Google Sheets, etc.)
  - 📊 Excel (formato nativo de Excel)
- Tabla de estadísticas resumidas
- Botón para descargar estadísticas

**Cómo usarla:**
1. Selecciona el conjunto de datos que deseas descargar
2. Revisa la vista previa
3. Haz clic en el botón de descarga del formato deseado
4. El archivo se descargará automáticamente
5. Opcionalmente, descarga también las estadísticas resumidas

---

## 🎨 Características Visuales

### Formato Condicional de Avances

La aplicación utiliza colores para indicar el tipo de avance:

- **🟢 Verde (Positivo):** "Avanzó X puntos"
  - Indica mejora en el puntaje
  - Fondo verde claro con borde verde

- **🔴 Rojo (Negativo):** "Retrocedió X puntos"
  - Indica disminución en el puntaje
  - Fondo rojo claro con borde rojo

- **🟡 Amarillo (Neutro):** "No subió. No bajó"
  - Indica que no hubo cambio
  - Fondo amarillo claro con borde amarillo

### Gráficos Interactivos

Todos los gráficos son interactivos:
- **Hover:** Pasa el mouse sobre los elementos para ver valores exactos
- **Zoom:** Usa la rueda del mouse para hacer zoom
- **Pan:** Arrastra para mover el gráfico
- **Descargar:** Usa el botón de cámara para descargar el gráfico como imagen

---

## 📊 Datos Utilizados

### Datos 2024
- **Fuente:** Archivo PDF oficial del ICFES
- **Archivos MD:**
  - `data/globales_pcielo_2024.md` (Institucional)
  - `data/globales_pcielo_aula_regular_2024.md` (Aula Regular)
  - `data/globales_pcielo_flexible_2024.md` (Modelo Flexible)

### Datos 2025
- **Fuente:** Archivos Excel
- **Archivos:**
  - `data/RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx`
  - `data/RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx`

---

## 🔢 Reglas de Redondeo

**Importante:** La aplicación sigue estas reglas de redondeo:

- ✅ **Puntajes de área:** Redondeados a entero
- ✅ **Puntajes globales:** Redondeados a entero
- ✅ **Promedios:** Redondeados a entero
- ❌ **Desviaciones estándar:** NO se redondean (se muestran con 2 decimales)
- ❌ **Porcentajes:** NO se redondean (se muestran con 1 decimal)

---

## 🎯 Casos de Uso Comunes

### 1. Comparar el desempeño institucional general
1. Ve a "🏠 Inicio - Comparativo General"
2. Revisa las métricas principales
3. Analiza los gráficos comparativos

### 2. Identificar estudiantes destacados
1. Ve a "🏆 Rankings y Destacados"
2. Revisa el Top 10 general
3. Consulta los mejores por área en las pestañas

### 3. Analizar un área específica
1. Ve a "📚 Estadísticas por Área"
2. Selecciona el área de interés
3. Analiza el comparativo y la distribución

### 4. Evaluar el desempeño de un grado
1. Ve a "🎓 Estadísticas por Grado"
2. Selecciona el grado
3. Revisa las métricas y la lista de estudiantes

### 5. Exportar datos para análisis externo
1. Ve a "📥 Descargar Datos"
2. Selecciona el conjunto de datos
3. Descarga en el formato deseado

---

## 🛠️ Solución de Problemas

### La aplicación no inicia
```bash
# Verifica que estés en el directorio correcto
cd /home/proyectos/Escritorio/Resultados-ICFES-2025

# Verifica que tengas las dependencias instaladas
pip install -r requirements.txt

# Intenta iniciar nuevamente
streamlit run streamlit_app.py
```

### Error al cargar datos
- Verifica que los archivos Excel estén en la carpeta `data/`
- Asegúrate de que los nombres de los archivos sean correctos:
  - `RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx`
  - `RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx`

### Los gráficos no se muestran
- Actualiza la página (F5)
- Limpia la caché de Streamlit: presiona "C" en la aplicación

---

## 📞 Información Adicional

### Áreas Evaluadas
1. Lectura Crítica
2. Matemáticas
3. Sociales y Ciudadanas
4. Ciencias Naturales
5. Inglés

### Modelos Educativos
- **Aula Regular:** Educación presencial tradicional (Grados 11A y 11B)
- **Modelo Flexible:** Modelo Pensar (Grados P3A, P3B, P3C)

### Escalas de Puntaje
- **Puntajes por área:** 0 a 100 puntos
- **Puntaje global:** 0 a 500 puntos
- **Media de referencia:** 250 puntos (establecida en 2014-2)

---

## ✅ Checklist de Uso

- [ ] Iniciar la aplicación
- [ ] Revisar el comparativo general
- [ ] Analizar avances por área
- [ ] Consultar rankings
- [ ] Revisar estadísticas por grado
- [ ] Analizar estadísticas por modelo
- [ ] Descargar datos para análisis adicional

---

**Última actualización:** 2025-10-23  
**Versión:** 2.0  
**Estado:** ✅ Funcional
