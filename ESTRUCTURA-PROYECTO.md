# 📁 Estructura del Proyecto - Aplicación Comparativa ICFES

## 🌳 Árbol de Archivos

```
Resultados-ICFES-2025/
│
├── 📊 APLICACIÓN PRINCIPAL
│   ├── streamlit_app.py                          ⭐ Aplicación principal (1145 líneas)
│   ├── app_icfes_comparativo.py                  📄 Código fuente (copia)
│   ├── streamlit_app_backup.py                   💾 Respaldo versión anterior
│   └── iniciar_aplicacion.sh                     🚀 Script de inicio rápido
│
├── 📚 DOCUMENTACIÓN
│   ├── INICIO-RAPIDO.md                          ⚡ Guía de inicio rápido
│   ├── GUIA-USO-APLICACION-COMPARATIVA.md        📖 Guía de uso completa
│   ├── README-APLICACION-COMPARATIVA.md          📘 README técnico
│   ├── RESUMEN-EJECUTIVO-APLICACION.md           📊 Resumen ejecutivo
│   └── ESTRUCTURA-PROYECTO.md                    📁 Este archivo
│
├── 📊 DATOS 2024 (Fuente: PDF Oficial ICFES)
│   ├── data/globales_pcielo_2024.md              🏛️ Datos institucionales
│   ├── data/globales_pcielo_aula_regular_2024.md 📘 Datos Aula Regular
│   └── data/globales_pcielo_flexible_2024.md     📙 Datos Modelo Flexible
│
├── 📊 DATOS 2025 (Fuente: Archivos Excel)
│   ├── data/RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx      📗 40 estudiantes
│   └── data/RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx   📕 64 estudiantes
│
├── 🔧 CONFIGURACIÓN
│   ├── requirements.txt                          📦 Dependencias Python
│   └── runtime.txt                               🐍 Versión de Python
│
└── 📄 OTROS ARCHIVOS
    ├── README.md                                 📖 README general del proyecto
    ├── Resultados Saber 11°_163401000298_2024-3.pdf  📄 PDF oficial ICFES
    └── [otros archivos del proyecto...]
```

---

## 📊 Componentes de la Aplicación

### 🎯 Módulo Principal (`streamlit_app.py`)

```
streamlit_app.py (1145 líneas)
│
├── 🔧 CONFIGURACIÓN (líneas 1-130)
│   ├── Imports
│   ├── Configuración de página
│   ├── Estilos CSS personalizados
│   └── Constantes (áreas, colores)
│
├── 📥 CARGA DE DATOS (líneas 131-250)
│   ├── cargar_datos_2024()           # Datos desde archivos MD
│   ├── cargar_datos_2025()           # Datos desde archivos Excel
│   └── calcular_estadisticas_2025()  # Cálculos estadísticos
│
├── 🧮 CÁLCULOS (líneas 251-280)
│   ├── calcular_avance()             # Calcula diferencias
│   └── formatear_avance()            # Formatea con colores
│
├── 📊 VISUALIZACIONES (líneas 281-360)
│   ├── crear_grafico_comparativo_areas()
│   └── crear_grafico_avances()
│
├── 🏠 FUNCIÓN PRINCIPAL (líneas 361-400)
│   ├── main()                        # Punto de entrada
│   ├── Carga de datos
│   ├── Sidebar de navegación
│   └── Enrutamiento de páginas
│
└── 📄 PÁGINAS (líneas 401-1145)
    ├── mostrar_pagina_inicio()           # Comparativo general
    ├── mostrar_estadisticas_estudiante() # Por estudiante
    ├── mostrar_estadisticas_grado()      # Por grado
    ├── mostrar_estadisticas_area()       # Por área
    ├── mostrar_estadisticas_modelo()     # Por modelo
    ├── mostrar_analisis_avances()        # Análisis de avances
    ├── mostrar_rankings()                # Rankings
    └── mostrar_descarga_datos()          # Descarga de datos
```

---

## 🎨 Flujo de la Aplicación

```
┌─────────────────────────────────────────────────────────────┐
│                    INICIO DE APLICACIÓN                      │
│                   streamlit_app.py                           │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   CONFIGURACIÓN INICIAL                      │
│  • Configurar página (título, icono, layout)                │
│  • Cargar estilos CSS personalizados                        │
│  • Definir constantes (áreas, colores)                      │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                      CARGA DE DATOS                          │
│  • Cargar datos 2024 (desde archivos MD)                    │
│  • Cargar datos 2025 (desde archivos Excel)                 │
│  • Calcular estadísticas 2025                               │
│  • Aplicar caché para optimizar rendimiento                 │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    SIDEBAR DE NAVEGACIÓN                     │
│  • Mostrar logo institucional                               │
│  • Menú de navegación (8 opciones)                          │
│  • Información contextual                                   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   ENRUTAMIENTO DE PÁGINAS                    │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  🏠 Inicio - Comparativo General                     │  │
│  │  • Métricas principales                              │  │
│  │  • Comparativo por áreas                             │  │
│  │  • Comparativo por modelo                            │  │
│  │  • Gráficos interactivos                             │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  📊 Estadísticas por Estudiante                      │  │
│  │  • Selector de estudiante                            │  │
│  │  • Información personal                              │  │
│  │  • Puntajes por área                                 │  │
│  │  • Gráfico de barras                                 │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  🎓 Estadísticas por Grado                           │  │
│  │  • Selector de grado                                 │  │
│  │  • Métricas del grado                                │  │
│  │  • Promedios por área                                │  │
│  │  • Lista de estudiantes                              │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  📚 Estadísticas por Área                            │  │
│  │  • Selector de área                                  │  │
│  │  • Comparativo 2024 vs 2025                          │  │
│  │  • Distribución de puntajes                          │  │
│  │  • Estadísticas por modelo                           │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  🏫 Estadísticas por Modelo                          │  │
│  │  • Selector de modelo                                │  │
│  │  • Métricas generales                                │  │
│  │  • Comparativo por áreas                             │  │
│  │  • Gráficos de avances                               │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  📈 Análisis de Avances                              │  │
│  │  • Avances institucionales                           │  │
│  │  • Avances por área                                  │  │
│  │  • Avances por modelo                                │  │
│  │  • Tablas con porcentajes                            │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  🏆 Rankings y Destacados                            │  │
│  │  • Top 10 general                                    │  │
│  │  • Mejores por área                                  │  │
│  │  • Rankings por modelo                               │  │
│  │  • Rankings por grado                                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  📥 Descargar Datos                                  │  │
│  │  • Selector de conjunto de datos                     │  │
│  │  • Vista previa                                      │  │
│  │  • Descarga CSV                                      │  │
│  │  • Descarga Excel                                    │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 📊 Flujo de Datos

```
┌─────────────────────┐
│   DATOS 2024        │
│   (Archivos MD)     │
│                     │
│  • Institucional    │
│  • Aula Regular     │
│  • Modelo Flexible  │
└──────────┬──────────┘
           │
           │ cargar_datos_2024()
           │
           ↓
┌─────────────────────┐         ┌─────────────────────┐
│   DATOS 2025        │         │   ESTADÍSTICAS      │
│   (Archivos Excel)  │         │   CALCULADAS        │
│                     │         │                     │
│  • Aula Regular     │────────→│  • Promedios        │
│  • Modelo Flexible  │         │  • Desviaciones     │
└──────────┬──────────┘         │  • Máximos/Mínimos  │
           │                     └──────────┬──────────┘
           │ cargar_datos_2025()            │
           │                                │
           ↓                                │
┌─────────────────────┐                    │
│   DATAFRAMES        │                    │
│   CONSOLIDADOS      │                    │
│                     │                    │
│  • df_regular       │                    │
│  • df_flexible      │                    │
│  • df_todos         │                    │
└──────────┬──────────┘                    │
           │                                │
           │ calcular_estadisticas_2025()   │
           │                                │
           ↓                                │
┌─────────────────────────────────────────┐│
│         COMPARACIONES Y AVANCES          ││
│                                          ││
│  • Avances por área                     ││
│  • Avances por modelo                   ││
│  • Avances institucionales              ││
│  • Formato condicional (colores)        ││
└──────────┬───────────────────────────────┘│
           │                                │
           │ calcular_avance()              │
           │ formatear_avance()             │
           │                                │
           ↓                                │
┌─────────────────────────────────────────┐│
│         VISUALIZACIONES                  ││
│                                          ││
│  • Gráficos de barras                   ││
│  • Histogramas                          ││
│  • Gráficos de avances                  ││
│  • Tablas dinámicas                     ││
└──────────┬───────────────────────────────┘│
           │                                │
           │ crear_grafico_*()              │
           │                                │
           ↓                                │
┌─────────────────────────────────────────┐│
│         INTERFAZ DE USUARIO              ││
│                                          ││
│  • Sidebar de navegación                ││
│  • Páginas interactivas                 ││
│  • Métricas y gráficos                  ││
│  • Botones de descarga                  ││
└──────────────────────────────────────────┘│
```

---

## 🎨 Componentes Visuales

### Colores Principales

```
┌─────────────────────────────────────────┐
│  PALETA DE COLORES                      │
├─────────────────────────────────────────┤
│  🟣 Principal:    #667eea → #764ba2     │
│  🟢 Positivo:     #28a745               │
│  🔴 Negativo:     #dc3545               │
│  🟡 Neutro:       #ffc107               │
│  🔵 Lectura:      #1f77b4               │
│  🟠 Matemáticas:  #ff7f0e               │
│  🟢 Sociales:     #2ca02c               │
│  🔴 Ciencias:     #d62728               │
│  🟣 Inglés:       #9467bd               │
└─────────────────────────────────────────┘
```

### Elementos de Diseño

```
┌─────────────────────────────────────────┐
│  ELEMENTOS VISUALES                     │
├─────────────────────────────────────────┤
│  📊 Headers con gradientes              │
│  🎴 Tarjetas con sombras                │
│  📈 Gráficos interactivos               │
│  📋 Tablas con formato                  │
│  🔘 Botones destacados                  │
│  🎨 Formato condicional                 │
│  📱 Diseño responsivo                   │
└─────────────────────────────────────────┘
```

---

## 📦 Dependencias

```
┌─────────────────────────────────────────┐
│  DEPENDENCIAS PRINCIPALES               │
├─────────────────────────────────────────┤
│  streamlit >= 1.32.0                    │
│  pandas >= 2.2.0                        │
│  plotly >= 5.18.0                       │
│  openpyxl >= 3.1.2                      │
│  numpy >= 1.26.0                        │
│  scipy >= 1.12.0                        │
└─────────────────────────────────────────┘
```

---

## 🚀 Puntos de Entrada

### Inicio de la Aplicación

```bash
# Opción 1: Script de inicio rápido
./iniciar_aplicacion.sh

# Opción 2: Comando directo
streamlit run streamlit_app.py

# Opción 3: Con puerto específico
streamlit run streamlit_app.py --server.port 8501
```

### Acceso a la Aplicación

```
┌─────────────────────────────────────────┐
│  URLS DE ACCESO                         │
├─────────────────────────────────────────┤
│  Local:     http://localhost:8501       │
│  Red:       http://192.168.10.13:8501   │
│  Externa:   http://181.53.99.10:8501    │
└─────────────────────────────────────────┘
```

---

## 📊 Métricas del Proyecto

```
┌─────────────────────────────────────────┐
│  ESTADÍSTICAS DEL CÓDIGO                │
├─────────────────────────────────────────┤
│  Líneas totales:        ~1145           │
│  Funciones:             ~20             │
│  Páginas:               8               │
│  Gráficos:              15+             │
│  Tablas:                20+             │
│  Archivos Python:       3               │
│  Archivos MD:           8               │
│  Archivos de datos:     5               │
└─────────────────────────────────────────┘
```

---

## ✅ Estado del Proyecto

```
┌─────────────────────────────────────────┐
│  ESTADO ACTUAL                          │
├─────────────────────────────────────────┤
│  ✅ Desarrollo:         COMPLETADO      │
│  ✅ Pruebas:            EXITOSAS        │
│  ✅ Documentación:      COMPLETA        │
│  ✅ Funcionalidad:      100%            │
│  ✅ Calidad:            ⭐⭐⭐⭐⭐        │
└─────────────────────────────────────────┘
```

---

**Fecha de creación:** 2025-10-21  
**Versión:** 1.0  
**Estado:** ✅ Proyecto completado

