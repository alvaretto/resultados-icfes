# 📊 Aplicación Comparativa ICFES 2024 vs 2025

## 🎯 Descripción

Aplicación web interactiva desarrollada en Streamlit para analizar y comparar los resultados ICFES Saber 11° de la Institución Educativa Pedacito de Cielo entre los años 2024 y 2025.

## ✨ Características Principales

### 📈 Análisis Comparativo Completo
- Comparación institucional 2024 vs 2025
- Análisis por modelo educativo (Aula Regular vs Modelo Flexible)
- Comparación por áreas de conocimiento
- Análisis por grado y por estudiante

### 🎨 Visualizaciones Interactivas
- Gráficos de barras comparativos
- Histogramas de distribución
- Gráficos de avances con colores condicionales
- Tablas dinámicas y ordenables

### 📊 Indicadores de Avance
- **✅ Verde:** Avanzó X puntos (mejora)
- **❌ Rojo:** Retrocedió X puntos (disminución)
- **⚪ Amarillo:** No subió. No bajó (sin cambio)

### 🏆 Rankings y Destacados
- Top 10 estudiantes por puntaje global
- Mejores estudiantes por área
- Rankings por modelo educativo
- Rankings por grado

### 📥 Exportación de Datos
- Descarga en formato CSV
- Descarga en formato Excel
- Estadísticas resumidas exportables

## 🚀 Instalación y Uso

### Requisitos Previos

```bash
Python 3.8 o superior
pip (gestor de paquetes de Python)
```

### Instalación de Dependencias

```bash
cd /home/proyectos/Escritorio/Resultados-ICFES-2025
pip install -r requirements.txt
```

### Iniciar la Aplicación

```bash
streamlit run streamlit_app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## 📁 Estructura de Archivos

```
Resultados-ICFES-2025/
│
├── streamlit_app.py                          # Aplicación principal
├── app_icfes_comparativo.py                  # Código fuente de la aplicación
├── requirements.txt                          # Dependencias
│
├── data/
│   ├── globales_pcielo_2024.md              # Datos institucionales 2024
│   ├── globales_pcielo_aula_regular_2024.md # Datos Aula Regular 2024
│   ├── globales_pcielo_flexible_2024.md     # Datos Modelo Flexible 2024
│   ├── RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx
│   └── RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx
│
└── GUIA-USO-APLICACION-COMPARATIVA.md       # Guía de uso detallada
```

## 📑 Páginas de la Aplicación

### 1. 🏠 Inicio - Comparativo General
Página principal con comparación institucional 2024 vs 2025, incluyendo:
- Métricas principales
- Comparativo por áreas
- Comparativo por modelo educativo
- Gráficos interactivos

### 2. 📊 Estadísticas por Estudiante
Análisis individual de cada estudiante:
- Información personal
- Puntaje global
- Puntajes por área
- Gráfico de desempeño

### 3. 🎓 Estadísticas por Grado
Análisis por grado (11A, 11B, P3A, P3B, P3C):
- Métricas del grado
- Promedios por área
- Lista de estudiantes
- Gráficos comparativos

### 4. 📚 Estadísticas por Área
Análisis por área de conocimiento:
- Comparativo 2024 vs 2025
- Distribución de puntajes
- Estadísticas por modelo
- Histogramas interactivos

### 5. 🏫 Estadísticas por Modelo
Análisis por modelo educativo:
- Métricas generales
- Comparativo por áreas
- Avances y retrocesos
- Gráficos detallados

### 6. 📈 Análisis de Avances
Análisis detallado de avances:
- Avances institucionales
- Avances por área
- Avances por modelo
- Tablas con porcentajes

### 7. 🏆 Rankings y Destacados
Rankings de estudiantes:
- Top 10 general
- Mejores por área
- Rankings por modelo
- Rankings por grado

### 8. 📥 Descargar Datos
Exportación de datos:
- Descarga en CSV
- Descarga en Excel
- Estadísticas resumidas
- Vista previa de datos

## 🔢 Reglas de Cálculo

### Redondeo
- **Puntajes de área:** Redondeados a entero
- **Puntajes globales:** Redondeados a entero
- **Promedios:** Redondeados a entero
- **Desviaciones estándar:** 2 decimales (NO redondeadas a entero)
- **Porcentajes:** 1 decimal

### Cálculo de Avances
```
Avance = Puntaje 2025 - Puntaje 2024

Si Avance > 0: "Avanzó X puntos" (Verde)
Si Avance < 0: "Retrocedió X puntos" (Rojo)
Si Avance = 0: "No subió. No bajó" (Amarillo)
```

## 📊 Fuentes de Datos

### Datos 2024
- **Fuente:** PDF oficial del ICFES
- **Archivo:** `Resultados Saber 11°_163401000298_2024-3.pdf`
- **Procesamiento:** Datos extraídos y consolidados en archivos MD

### Datos 2025
- **Fuente:** Archivos Excel
- **Archivos:**
  - `RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx` (40 estudiantes)
  - `RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx` (64 estudiantes)

## 🎨 Tecnologías Utilizadas

- **Streamlit:** Framework de aplicación web
- **Pandas:** Procesamiento de datos
- **Plotly:** Visualizaciones interactivas
- **NumPy:** Cálculos numéricos
- **OpenPyXL:** Lectura/escritura de archivos Excel

## 📈 Métricas Disponibles

### Por Estudiante
- Puntaje global
- Puntajes por área (5 áreas)
- Información personal (grupo, modelo, documento)

### Por Grado
- Número de estudiantes
- Puntaje global promedio
- Puntaje máximo y mínimo
- Promedios por área
- Desviaciones estándar

### Por Área
- Promedio institucional
- Promedio por modelo
- Distribución de puntajes
- Comparativo 2024 vs 2025
- Avances/retrocesos

### Por Modelo Educativo
- Número de estudiantes
- Puntaje global promedio
- Promedios por área
- Comparativo 2024 vs 2025
- Avances/retrocesos por área

### Institucional
- Puntaje global promedio
- Promedios por área
- Comparativo 2024 vs 2025
- Distribución por modelo
- Avances/retrocesos generales

## 🎯 Casos de Uso

### Para Directivos
- Evaluar el desempeño institucional general
- Identificar áreas de mejora
- Comparar modelos educativos
- Tomar decisiones basadas en datos

### Para Docentes
- Analizar el desempeño por área
- Identificar estudiantes destacados
- Evaluar el progreso del grado
- Planificar estrategias de mejora

### Para Coordinadores
- Generar reportes por modelo
- Comparar grados
- Identificar tendencias
- Exportar datos para análisis adicional

### Para Padres de Familia
- Consultar el desempeño individual
- Comparar con promedios del grado
- Ver el ranking del estudiante
- Entender las áreas de fortaleza y mejora

## 🛠️ Personalización

### Cambiar Colores
Edita la sección de CSS en `streamlit_app.py`:

```python
COLORES_AREAS = {
    'Lectura Crítica': '#1f77b4',
    'Matemáticas': '#ff7f0e',
    'Sociales y Ciudadanas': '#2ca02c',
    'Ciencias Naturales': '#d62728',
    'Inglés': '#9467bd'
}
```

### Agregar Nuevas Métricas
Modifica las funciones de cálculo en `streamlit_app.py`:

```python
def calcular_estadisticas_2025(df, modelo='Todos'):
    # Agrega tus cálculos personalizados aquí
    pass
```

## 📝 Notas Importantes

1. **Datos 2024:** Provienen del PDF oficial del ICFES y están consolidados en archivos MD
2. **Datos 2025:** Provienen de archivos Excel con datos individuales de estudiantes
3. **Redondeo:** Todos los puntajes se redondean a entero, excepto desviaciones estándar
4. **Caché:** Streamlit cachea los datos para mejorar el rendimiento
5. **Interactividad:** Todos los gráficos son interactivos (hover, zoom, pan)

## 🐛 Solución de Problemas

### Error al cargar datos
```bash
# Verifica que los archivos existan
ls -la data/RESULTADOS-ICFES-*.xlsx

# Verifica los permisos
chmod 644 data/RESULTADOS-ICFES-*.xlsx
```

### Error de dependencias
```bash
# Reinstala las dependencias
pip install --upgrade -r requirements.txt
```

### La aplicación no inicia
```bash
# Verifica la versión de Python
python3 --version

# Verifica que Streamlit esté instalado
streamlit --version

# Limpia la caché
streamlit cache clear
```

## 📞 Soporte

Para más información, consulta:
- **Guía de uso:** `GUIA-USO-APLICACION-COMPARATIVA.md`
- **Documentación de Streamlit:** https://docs.streamlit.io
- **Documentación de Plotly:** https://plotly.com/python/

## 📄 Licencia

Este proyecto es de uso interno para la Institución Educativa Pedacito de Cielo.

## 👥 Créditos

- **Desarrollo:** Aplicación desarrollada para análisis de resultados ICFES
- **Institución:** Institución Educativa Pedacito de Cielo Álvaro Uribe Vélez
- **Municipio:** La Tebaida, Quindío
- **Año:** 2025

---

**Última actualización:** 2025-10-23  
**Versión:** 2.0  
**Estado:** ✅ Funcional

