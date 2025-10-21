#!/usr/bin/env python3
"""
Aplicación Streamlit para Análisis Comparativo de Resultados ICFES Saber 11°
Institución Educativa Pedacito de Cielo
Comparación 2024 vs 2025
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime
import io
import re

# ============================================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================================

st.set_page_config(
    page_title="Análisis ICFES - Pedacito de Cielo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CONSTANTES
# ============================================================================

AREAS = ['Lectura Crítica', 'Matemáticas', 'Sociales y Ciudadanas', 'Ciencias Naturales', 'Inglés']

COLORES_AREAS = {
    'Lectura Crítica': '#1f77b4',
    'Matemáticas': '#ff7f0e',
    'Sociales y Ciudadanas': '#2ca02c',
    'Ciencias Naturales': '#d62728',
    'Inglés': '#9467bd'
}

# ============================================================================
# ESTILOS CSS PERSONALIZADOS
# ============================================================================

st.markdown("""
<style>
    /* Header principal */
    .main-header {
        font-size: 2.8rem;
        font-weight: bold;
        color: #1e3a8a;
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Tarjetas de métricas */
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #667eea;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    
    /* Avance positivo */
    .avance-positivo {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        color: #155724;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    
    /* Avance negativo */
    .avance-negativo {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
        color: #721c24;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    
    /* Sin cambio */
    .avance-neutro {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        color: #856404;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    
    /* Subtítulos */
    .subtitle {
        font-size: 1.5rem;
        font-weight: 600;
        color: #4a5568;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #667eea;
        padding-bottom: 0.5rem;
    }
    
    /* Tablas */
    .dataframe {
        font-size: 0.9rem;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# FUNCIONES DE CARGA DE DATOS
# ============================================================================

@st.cache_data
def cargar_datos_2024():
    """Carga los datos consolidados de 2024 desde archivos MD"""
    
    # Datos Aula Regular 2024
    datos_regular_2024 = {
        'modelo': 'Aula Regular',
        'estudiantes': 50,
        'puntaje_global': 240,
        'desv_global': 41,
        'areas': {
            'Lectura Crítica': {'promedio': 51, 'desviacion': 9},
            'Matemáticas': {'promedio': 49, 'desviacion': 10},
            'Sociales y Ciudadanas': {'promedio': 44, 'desviacion': 11},
            'Ciencias Naturales': {'promedio': 47, 'desviacion': 8},
            'Inglés': {'promedio': 48, 'desviacion': 10}
        }
    }
    
    # Datos Modelo Flexible 2024
    datos_flexible_2024 = {
        'modelo': 'Modelo Flexible',
        'estudiantes': 66,
        'puntaje_global': 203,
        'desv_global': 36,
        'areas': {
            'Lectura Crítica': {'promedio': 45, 'desviacion': 9},
            'Matemáticas': {'promedio': 41, 'desviacion': 11},
            'Sociales y Ciudadanas': {'promedio': 38, 'desviacion': 9},
            'Ciencias Naturales': {'promedio': 39, 'desviacion': 7},
            'Inglés': {'promedio': 41, 'desviacion': 9}
        }
    }
    
    # Datos Institucionales 2024 (consolidado)
    datos_institucional_2024 = {
        'modelo': 'Institucional',
        'estudiantes': 116,
        'puntaje_global': 219,
        'desv_global': 42,
        'areas': {
            'Lectura Crítica': {'promedio': 48, 'desviacion': 9},
            'Matemáticas': {'promedio': 44, 'desviacion': 11},
            'Sociales y Ciudadanas': {'promedio': 41, 'desviacion': 10},
            'Ciencias Naturales': {'promedio': 43, 'desviacion': 8},
            'Inglés': {'promedio': 44, 'desviacion': 10}
        }
    }
    
    return {
        'Aula Regular': datos_regular_2024,
        'Modelo Flexible': datos_flexible_2024,
        'Institucional': datos_institucional_2024
    }

@st.cache_data
def cargar_datos_2025():
    """Carga los datos de 2025 desde archivos Excel"""
    
    try:
        # Cargar Excel Aula Regular
        df_regular = pd.read_excel('data/RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx')
        df_regular = df_regular[df_regular['Grupo'].notna()].copy()
        
        # Cargar Excel Modelo Flexible
        df_flexible = pd.read_excel('data/RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx')
        df_flexible = df_flexible[df_flexible['Grupo'].notna()].copy()
        
        # Agregar columna de modelo
        df_regular['Modelo'] = 'Aula Regular'
        df_flexible['Modelo'] = 'Modelo Flexible'
        
        # Consolidar
        df_todos = pd.concat([df_regular, df_flexible], ignore_index=True)
        
        return {
            'df_regular': df_regular,
            'df_flexible': df_flexible,
            'df_todos': df_todos
        }
    except Exception as e:
        st.error(f"Error al cargar datos 2025: {e}")
        return None

@st.cache_data
def calcular_estadisticas_2025(df, modelo='Todos'):
    """Calcula estadísticas para datos de 2025"""

    if df is None or len(df) == 0:
        return None

    # Filtrar por modelo si es necesario
    if modelo != 'Todos':
        df = df[df['Modelo'] == modelo].copy()

    estadisticas = {
        'modelo': modelo,
        'estudiantes': len(df),
        'puntaje_global': int(round(df['Puntaje Global'].mean())),
        'desv_global': df['Puntaje Global'].std(),
        'areas': {}
    }

    for area in AREAS:
        if area in df.columns:
            estadisticas['areas'][area] = {
                'promedio': int(round(df[area].mean())),
                'desviacion': df[area].std()
            }

    return estadisticas

@st.cache_data
def calcular_estadisticas_por_grupo(df):
    """Calcula estadísticas para cada grupo individual"""

    if df is None or len(df) == 0:
        return None

    grupos_stats = {}
    grupos_unicos = sorted(df['Grupo'].dropna().unique())

    for grupo in grupos_unicos:
        df_grupo = df[df['Grupo'] == grupo].copy()

        # Determinar el modelo del grupo
        if grupo in ['11A', '11B']:
            modelo = 'Aula Regular'
        else:
            modelo = 'Modelo Flexible'

        grupos_stats[grupo] = {
            'grupo': grupo,
            'modelo': modelo,
            'estudiantes': len(df_grupo),
            'puntaje_global': int(round(df_grupo['Puntaje Global'].mean())),
            'desv_global': df_grupo['Puntaje Global'].std(),
            'areas': {}
        }

        for area in AREAS:
            if area in df_grupo.columns:
                grupos_stats[grupo]['areas'][area] = {
                    'promedio': int(round(df_grupo[area].mean())),
                    'desviacion': df_grupo[area].std()
                }

    return grupos_stats

# ============================================================================
# FUNCIONES DE CÁLCULO DE AVANCES
# ============================================================================

def calcular_avance(valor_2024, valor_2025):
    """Calcula el avance entre 2024 y 2025"""
    return valor_2025 - valor_2024

def formatear_avance(avance):
    """Formatea el avance con el texto y estilo apropiado"""
    if avance > 0:
        return f"✅ Avanzó {avance} puntos", "avance-positivo"
    elif avance < 0:
        return f"❌ Retrocedió {abs(avance)} puntos", "avance-negativo"
    else:
        return "⚪ No subió. No bajó", "avance-neutro"

# ============================================================================
# FUNCIONES DE VISUALIZACIÓN
# ============================================================================

def crear_grafico_comparativo_areas(datos_2024, datos_2025, titulo):
    """Crea gráfico comparativo de áreas entre 2024 y 2025"""
    
    areas_list = []
    valores_2024 = []
    valores_2025 = []
    
    for area in AREAS:
        areas_list.append(area)
        valores_2024.append(datos_2024['areas'][area]['promedio'])
        valores_2025.append(datos_2025['areas'][area]['promedio'])
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='2024',
        x=areas_list,
        y=valores_2024,
        marker_color='#667eea',
        text=valores_2024,
        textposition='outside'
    ))
    
    fig.add_trace(go.Bar(
        name='2025',
        x=areas_list,
        y=valores_2025,
        marker_color='#764ba2',
        text=valores_2025,
        textposition='outside'
    ))
    
    fig.update_layout(
        title=titulo,
        xaxis_title="Áreas de Conocimiento",
        yaxis_title="Puntaje Promedio",
        barmode='group',
        height=500,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    return fig

def crear_grafico_avances(datos_2024, datos_2025):
    """Crea gráfico de avances por área"""
    
    areas_list = []
    avances = []
    colores = []
    
    for area in AREAS:
        areas_list.append(area)
        avance = calcular_avance(
            datos_2024['areas'][area]['promedio'],
            datos_2025['areas'][area]['promedio']
        )
        avances.append(avance)
        colores.append('#28a745' if avance > 0 else '#dc3545' if avance < 0 else '#ffc107')
    
    fig = go.Figure(go.Bar(
        x=areas_list,
        y=avances,
        marker_color=colores,
        text=[f"{a:+d}" for a in avances],
        textposition='outside'
    ))
    
    fig.update_layout(
        title="Avances por Área (2024 → 2025)",
        xaxis_title="Áreas de Conocimiento",
        yaxis_title="Cambio en Puntos",
        height=400,
        showlegend=False
    )
    
    fig.add_hline(y=0, line_dash="dash", line_color="gray")
    
    return fig

# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    # Header principal
    st.markdown('<div class="main-header">📊 Análisis Comparativo ICFES Saber 11°<br>Institución Educativa Pedacito de Cielo<br>2024 vs 2025</div>', unsafe_allow_html=True)
    
    # Cargar datos
    datos_2024 = cargar_datos_2024()
    datos_2025_raw = cargar_datos_2025()
    
    if datos_2025_raw is None:
        st.error("No se pudieron cargar los datos de 2025")
        return
    
    # Calcular estadísticas 2025
    stats_regular_2025 = calcular_estadisticas_2025(datos_2025_raw['df_regular'], 'Aula Regular')
    stats_flexible_2025 = calcular_estadisticas_2025(datos_2025_raw['df_flexible'], 'Modelo Flexible')
    stats_institucional_2025 = calcular_estadisticas_2025(datos_2025_raw['df_todos'], 'Todos')

    # Calcular estadísticas por grupo
    stats_grupos_2025 = calcular_estadisticas_por_grupo(datos_2025_raw['df_todos'])

    # ========================================================================
    # SIDEBAR - NAVEGACIÓN
    # ========================================================================

    with st.sidebar:
        st.image("https://via.placeholder.com/300x100/667eea/ffffff?text=Pedacito+de+Cielo", use_container_width=True)
        st.markdown("---")

        pagina = st.radio(
            "📑 Navegación",
            [
                "🏠 Inicio - Comparativo General",
                "📊 Estadísticas por Estudiante",
                "🎓 Estadísticas por Grado",
                "📚 Estadísticas por Área",
                "🏫 Estadísticas por Modelo",
                "📈 Análisis de Avances",
                "🏆 Rankings y Destacados",
                "📥 Descargar Datos"
            ]
        )

        st.markdown("---")
        st.markdown("### 📅 Información")
        st.info(f"""
        **Año de comparación:** 2024 vs 2025

        **Estudiantes 2024:** {datos_2024['Institucional']['estudiantes']}

        **Estudiantes 2025:** {stats_institucional_2025['estudiantes']}
        """)

    # ========================================================================
    # PÁGINA PRINCIPAL - COMPARATIVO GENERAL
    # ========================================================================

    if pagina == "🏠 Inicio - Comparativo General":
        mostrar_pagina_inicio(datos_2024, stats_regular_2025, stats_flexible_2025, stats_institucional_2025, stats_grupos_2025, datos_2025_raw)

    elif pagina == "📊 Estadísticas por Estudiante":
        mostrar_estadisticas_estudiante(datos_2025_raw)

    elif pagina == "🎓 Estadísticas por Grado":
        mostrar_estadisticas_grado(datos_2025_raw)

    elif pagina == "📚 Estadísticas por Área":
        mostrar_estadisticas_area(datos_2024, datos_2025_raw, stats_institucional_2025)

    elif pagina == "🏫 Estadísticas por Modelo":
        mostrar_estadisticas_modelo(datos_2024, stats_regular_2025, stats_flexible_2025)

    elif pagina == "📈 Análisis de Avances":
        mostrar_analisis_avances(datos_2024, stats_regular_2025, stats_flexible_2025, stats_institucional_2025)

    elif pagina == "🏆 Rankings y Destacados":
        mostrar_rankings(datos_2025_raw)

    elif pagina == "📥 Descargar Datos":
        mostrar_descarga_datos(datos_2025_raw)

# ============================================================================
# PÁGINAS DE LA APLICACIÓN
# ============================================================================

def mostrar_pagina_inicio(datos_2024, stats_regular_2025, stats_flexible_2025, stats_institucional_2025, stats_grupos_2025, datos_2025_raw):
    """Página principal con comparativo general 2024 vs 2025"""

    st.markdown('<div class="subtitle">📊 Comparativo Institucional 2024 vs 2025</div>', unsafe_allow_html=True)

    # Métricas principales
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Puntaje Global 2024",
            datos_2024['Institucional']['puntaje_global'],
            delta=None
        )

    with col2:
        st.metric(
            "Puntaje Global 2025",
            stats_institucional_2025['puntaje_global'],
            delta=None
        )

    with col3:
        avance_global = calcular_avance(
            datos_2024['Institucional']['puntaje_global'],
            stats_institucional_2025['puntaje_global']
        )
        texto_avance, clase_avance = formatear_avance(avance_global)
        st.markdown(f'<div class="{clase_avance}">{texto_avance}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Comparativo por áreas
    st.markdown('<div class="subtitle">📚 Comparativo por Áreas de Conocimiento</div>', unsafe_allow_html=True)

    # Tabla comparativa
    tabla_comparativa = []
    for area in AREAS:
        puntaje_2024 = datos_2024['Institucional']['areas'][area]['promedio']
        puntaje_2025 = stats_institucional_2025['areas'][area]['promedio']
        avance = calcular_avance(puntaje_2024, puntaje_2025)
        texto_avance, _ = formatear_avance(avance)

        tabla_comparativa.append({
            'Área': area,
            '2024': puntaje_2024,
            '2025': puntaje_2025,
            'Avance': texto_avance
        })

    df_comparativa = pd.DataFrame(tabla_comparativa)
    st.dataframe(df_comparativa, use_container_width=True, hide_index=True)

    # Gráficos
    col1, col2 = st.columns(2)

    with col1:
        fig1 = crear_grafico_comparativo_areas(
            datos_2024['Institucional'],
            stats_institucional_2025,
            "Comparativo por Áreas - Institucional"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = crear_grafico_avances(datos_2024['Institucional'], stats_institucional_2025)
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # Comparativo por modelo educativo
    st.markdown('<div class="subtitle">🏫 Comparativo por Modelo Educativo</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📘 Aula Regular")
        avance_regular = calcular_avance(
            datos_2024['Aula Regular']['puntaje_global'],
            stats_regular_2025['puntaje_global']
        )
        texto_avance_regular, clase_avance_regular = formatear_avance(avance_regular)

        st.metric("Puntaje Global 2024", datos_2024['Aula Regular']['puntaje_global'])
        st.metric("Puntaje Global 2025", stats_regular_2025['puntaje_global'])
        st.markdown(f'<div class="{clase_avance_regular}">{texto_avance_regular}</div>', unsafe_allow_html=True)

    with col2:
        st.markdown("#### 📙 Modelo Flexible")
        avance_flexible = calcular_avance(
            datos_2024['Modelo Flexible']['puntaje_global'],
            stats_flexible_2025['puntaje_global']
        )
        texto_avance_flexible, clase_avance_flexible = formatear_avance(avance_flexible)

        st.metric("Puntaje Global 2024", datos_2024['Modelo Flexible']['puntaje_global'])
        st.metric("Puntaje Global 2025", stats_flexible_2025['puntaje_global'])
        st.markdown(f'<div class="{clase_avance_flexible}">{texto_avance_flexible}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Comparativo por grupos individuales
    st.markdown('<div class="subtitle">👥 Comparativo por Grupos 2025</div>', unsafe_allow_html=True)

    # Tabla comparativa de todos los grupos
    tabla_grupos = []
    for grupo in sorted(stats_grupos_2025.keys()):
        stats = stats_grupos_2025[grupo]
        tabla_grupos.append({
            'Grupo': grupo,
            'Modelo': stats['modelo'],
            'Estudiantes': stats['estudiantes'],
            'Puntaje Global': stats['puntaje_global'],
            'Lectura Crítica': stats['areas']['Lectura Crítica']['promedio'],
            'Matemáticas': stats['areas']['Matemáticas']['promedio'],
            'Sociales y Ciudadanas': stats['areas']['Sociales y Ciudadanas']['promedio'],
            'Ciencias Naturales': stats['areas']['Ciencias Naturales']['promedio'],
            'Inglés': stats['areas']['Inglés']['promedio']
        })

    df_grupos = pd.DataFrame(tabla_grupos)
    st.dataframe(df_grupos, use_container_width=True, hide_index=True)

    # Gráfico comparativo de puntaje global por grupo
    fig_grupos = px.bar(
        df_grupos,
        x='Grupo',
        y='Puntaje Global',
        color='Modelo',
        title="Puntaje Global por Grupo",
        color_discrete_map={'Aula Regular': '#667eea', 'Modelo Flexible': '#764ba2'},
        text='Puntaje Global'
    )
    fig_grupos.update_traces(textposition='outside')
    fig_grupos.update_layout(height=400)
    st.plotly_chart(fig_grupos, use_container_width=True)

    st.markdown("---")

    # Comparación entre grupos del mismo modelo
    st.markdown('<div class="subtitle">🔄 Comparación entre Grupos por Modelo</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📘 Grupos de Aula Regular (11A vs 11B)")

        # Comparar 11A vs 11B
        grupos_regular = ['11A', '11B']
        datos_regular = []
        for grupo in grupos_regular:
            if grupo in stats_grupos_2025:
                for area in AREAS:
                    datos_regular.append({
                        'Grupo': grupo,
                        'Área': area,
                        'Puntaje': stats_grupos_2025[grupo]['areas'][area]['promedio']
                    })

        df_regular = pd.DataFrame(datos_regular)
        fig_regular = px.bar(
            df_regular,
            x='Área',
            y='Puntaje',
            color='Grupo',
            barmode='group',
            title="Comparación por Áreas - Aula Regular",
            color_discrete_sequence=['#667eea', '#4c5fd5']
        )
        fig_regular.update_xaxes(tickangle=-45)
        fig_regular.update_layout(height=400)
        st.plotly_chart(fig_regular, use_container_width=True)

        # Métricas comparativas
        if '11A' in stats_grupos_2025 and '11B' in stats_grupos_2025:
            diff = stats_grupos_2025['11A']['puntaje_global'] - stats_grupos_2025['11B']['puntaje_global']
            if diff > 0:
                st.info(f"📊 11A supera a 11B por {diff} puntos en puntaje global")
            elif diff < 0:
                st.info(f"📊 11B supera a 11A por {abs(diff)} puntos en puntaje global")
            else:
                st.info(f"📊 11A y 11B tienen el mismo puntaje global")

    with col2:
        st.markdown("#### 📙 Grupos de Modelo Flexible (P3A vs P3B vs P3C)")

        # Comparar P3A vs P3B vs P3C
        grupos_flexible = ['P3A', 'P3B', 'P3C']
        datos_flexible = []
        for grupo in grupos_flexible:
            if grupo in stats_grupos_2025:
                for area in AREAS:
                    datos_flexible.append({
                        'Grupo': grupo,
                        'Área': area,
                        'Puntaje': stats_grupos_2025[grupo]['areas'][area]['promedio']
                    })

        df_flexible = pd.DataFrame(datos_flexible)
        fig_flexible = px.bar(
            df_flexible,
            x='Área',
            y='Puntaje',
            color='Grupo',
            barmode='group',
            title="Comparación por Áreas - Modelo Flexible",
            color_discrete_sequence=['#764ba2', '#9b59b6', '#8e44ad']
        )
        fig_flexible.update_xaxes(tickangle=-45)
        fig_flexible.update_layout(height=400)
        st.plotly_chart(fig_flexible, use_container_width=True)

        # Métricas comparativas
        grupos_flex_ordenados = sorted(
            [(g, stats_grupos_2025[g]['puntaje_global']) for g in grupos_flexible if g in stats_grupos_2025],
            key=lambda x: x[1],
            reverse=True
        )
        if grupos_flex_ordenados:
            mejor_grupo = grupos_flex_ordenados[0][0]
            mejor_puntaje = grupos_flex_ordenados[0][1]
            st.info(f"🏆 {mejor_grupo} es el mejor grupo de Modelo Flexible con {mejor_puntaje} puntos")

    st.markdown("---")

    # Comparación de todos los grupos combinados
    st.markdown('<div class="subtitle">🌐 Comparación Global de Todos los Grupos</div>', unsafe_allow_html=True)

    # Crear datos para gráfico de radar/spider
    df_todos = datos_2025_raw['df_todos']

    # Gráfico de áreas por grupo
    datos_areas_grupos = []
    for grupo in sorted(stats_grupos_2025.keys()):
        for area in AREAS:
            datos_areas_grupos.append({
                'Grupo': grupo,
                'Área': area,
                'Puntaje': stats_grupos_2025[grupo]['areas'][area]['promedio'],
                'Modelo': stats_grupos_2025[grupo]['modelo']
            })

    df_areas_grupos = pd.DataFrame(datos_areas_grupos)

    # Gráfico de líneas para comparar todos los grupos
    fig_lineas = px.line(
        df_areas_grupos,
        x='Área',
        y='Puntaje',
        color='Grupo',
        markers=True,
        title="Comparación de Todas las Áreas por Grupo",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_lineas.update_xaxes(tickangle=-45)
    fig_lineas.update_layout(height=500)
    st.plotly_chart(fig_lineas, use_container_width=True)

    # Ranking de grupos por puntaje global
    st.markdown("#### 🏆 Ranking de Grupos por Puntaje Global")
    df_ranking = df_grupos[['Grupo', 'Modelo', 'Estudiantes', 'Puntaje Global']].sort_values('Puntaje Global', ascending=False)
    df_ranking.insert(0, 'Posición', range(1, len(df_ranking) + 1))
    st.dataframe(df_ranking, use_container_width=True, hide_index=True)

def mostrar_estadisticas_estudiante(datos_2025_raw):
    """Página de estadísticas por estudiante individual"""

    st.markdown('<div class="subtitle">👨‍🎓 Estadísticas por Estudiante</div>', unsafe_allow_html=True)

    df_todos = datos_2025_raw['df_todos']

    # Crear nombre completo
    df_todos['Nombre Completo'] = (
        df_todos['Primer Nombre'].fillna('') + ' ' +
        df_todos['Segundo Nombre'].fillna('') + ' ' +
        df_todos['Primer Apellido'].fillna('') + ' ' +
        df_todos['Segundo Apellido'].fillna('')
    ).str.strip().str.replace(r'\s+', ' ', regex=True)

    # Selector de estudiante
    estudiante_seleccionado = st.selectbox(
        "Seleccione un estudiante:",
        df_todos['Nombre Completo'].sort_values().unique()
    )

    # Filtrar datos del estudiante
    estudiante_data = df_todos[df_todos['Nombre Completo'] == estudiante_seleccionado].iloc[0]

    # Mostrar información
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(f"**Grupo:** {estudiante_data['Grupo']}")
        st.info(f"**Modelo:** {estudiante_data['Modelo']}")

    with col2:
        st.info(f"**Documento:** {estudiante_data['Número de documento']}")

    with col3:
        st.metric("Puntaje Global", int(estudiante_data['Puntaje Global']))

    # Puntajes por área
    st.markdown("#### 📚 Puntajes por Área")

    areas_estudiante = []
    for area in AREAS:
        areas_estudiante.append({
            'Área': area,
            'Puntaje': int(estudiante_data[area])
        })

    df_areas_estudiante = pd.DataFrame(areas_estudiante)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.dataframe(df_areas_estudiante, use_container_width=True, hide_index=True)

    with col2:
        fig = px.bar(
            df_areas_estudiante,
            x='Área',
            y='Puntaje',
            color='Puntaje',
            color_continuous_scale='Viridis',
            title=f"Puntajes de {estudiante_seleccionado}"
        )
        st.plotly_chart(fig, use_container_width=True)

def mostrar_estadisticas_grado(datos_2025_raw):
    """Página de estadísticas por grado"""

    st.markdown('<div class="subtitle">🎓 Estadísticas por Grado</div>', unsafe_allow_html=True)

    df_todos = datos_2025_raw['df_todos']

    # Selector de grado
    grado_seleccionado = st.selectbox(
        "Seleccione un grado:",
        sorted(df_todos['Grupo'].unique())
    )

    # Filtrar por grado
    df_grado = df_todos[df_todos['Grupo'] == grado_seleccionado]

    # Métricas del grado
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Estudiantes", len(df_grado))

    with col2:
        st.metric("Puntaje Global Promedio", int(round(df_grado['Puntaje Global'].mean())))

    with col3:
        st.metric("Puntaje Máximo", int(df_grado['Puntaje Global'].max()))

    with col4:
        st.metric("Puntaje Mínimo", int(df_grado['Puntaje Global'].min()))

    # Estadísticas por área
    st.markdown("#### 📚 Promedios por Área")

    promedios_grado = []
    for area in AREAS:
        promedios_grado.append({
            'Área': area,
            'Promedio': int(round(df_grado[area].mean())),
            'Desv. Estándar': round(df_grado[area].std(), 2)
        })

    df_promedios_grado = pd.DataFrame(promedios_grado)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.dataframe(df_promedios_grado, use_container_width=True, hide_index=True)

    with col2:
        fig = px.bar(
            df_promedios_grado,
            x='Área',
            y='Promedio',
            color='Promedio',
            color_continuous_scale='Blues',
            title=f"Promedios por Área - {grado_seleccionado}"
        )
        st.plotly_chart(fig, use_container_width=True)

    # Lista de estudiantes del grado
    st.markdown("#### 👥 Estudiantes del Grado")

    df_grado_display = df_grado[['Primer Nombre', 'Primer Apellido', 'Puntaje Global'] + AREAS].copy()
    df_grado_display = df_grado_display.sort_values('Puntaje Global', ascending=False)

    st.dataframe(df_grado_display, use_container_width=True, hide_index=True)

def mostrar_estadisticas_area(datos_2024, datos_2025_raw, stats_institucional_2025):
    """Página de estadísticas por área de conocimiento"""

    st.markdown('<div class="subtitle">📚 Estadísticas por Área de Conocimiento</div>', unsafe_allow_html=True)

    # Selector de área
    area_seleccionada = st.selectbox("Seleccione un área:", AREAS)

    # Comparativo 2024 vs 2025
    st.markdown(f"#### 📊 Comparativo {area_seleccionada} - 2024 vs 2025")

    col1, col2, col3 = st.columns(3)

    with col1:
        puntaje_2024 = datos_2024['Institucional']['areas'][area_seleccionada]['promedio']
        st.metric("Promedio 2024", puntaje_2024)

    with col2:
        puntaje_2025 = stats_institucional_2025['areas'][area_seleccionada]['promedio']
        st.metric("Promedio 2025", puntaje_2025)

    with col3:
        avance = calcular_avance(puntaje_2024, puntaje_2025)
        texto_avance, clase_avance = formatear_avance(avance)
        st.markdown(f'<div class="{clase_avance}">{texto_avance}</div>', unsafe_allow_html=True)

    # Distribución de puntajes 2025
    st.markdown(f"#### 📈 Distribución de Puntajes - {area_seleccionada} (2025)")

    df_todos = datos_2025_raw['df_todos']

    fig = px.histogram(
        df_todos,
        x=area_seleccionada,
        nbins=20,
        color='Modelo',
        title=f"Distribución de Puntajes - {area_seleccionada}",
        labels={area_seleccionada: 'Puntaje'},
        color_discrete_map={'Aula Regular': '#667eea', 'Modelo Flexible': '#764ba2'}
    )
    st.plotly_chart(fig, use_container_width=True)

    # Estadísticas por modelo
    st.markdown(f"#### 🏫 Comparativo por Modelo Educativo - {area_seleccionada}")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**📘 Aula Regular**")
        df_regular = datos_2025_raw['df_regular']
        promedio_regular = int(round(df_regular[area_seleccionada].mean()))
        desv_regular = round(df_regular[area_seleccionada].std(), 2)

        st.metric("Promedio", promedio_regular)
        st.metric("Desviación Estándar", desv_regular)
        st.metric("Máximo", int(df_regular[area_seleccionada].max()))
        st.metric("Mínimo", int(df_regular[area_seleccionada].min()))

    with col2:
        st.markdown("**📙 Modelo Flexible**")
        df_flexible = datos_2025_raw['df_flexible']
        promedio_flexible = int(round(df_flexible[area_seleccionada].mean()))
        desv_flexible = round(df_flexible[area_seleccionada].std(), 2)

        st.metric("Promedio", promedio_flexible)
        st.metric("Desviación Estándar", desv_flexible)
        st.metric("Máximo", int(df_flexible[area_seleccionada].max()))
        st.metric("Mínimo", int(df_flexible[area_seleccionada].min()))

def mostrar_estadisticas_modelo(datos_2024, stats_regular_2025, stats_flexible_2025):
    """Página de estadísticas por modelo educativo"""

    st.markdown('<div class="subtitle">🏫 Estadísticas por Modelo Educativo</div>', unsafe_allow_html=True)

    # Selector de modelo
    modelo_seleccionado = st.radio(
        "Seleccione un modelo:",
        ["Aula Regular", "Modelo Flexible"],
        horizontal=True
    )

    if modelo_seleccionado == "Aula Regular":
        datos_2024_modelo = datos_2024['Aula Regular']
        datos_2025_modelo = stats_regular_2025
        color = '#667eea'
    else:
        datos_2024_modelo = datos_2024['Modelo Flexible']
        datos_2025_modelo = stats_flexible_2025
        color = '#764ba2'

    # Métricas generales
    st.markdown(f"#### 📊 Métricas Generales - {modelo_seleccionado}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Estudiantes 2024", datos_2024_modelo['estudiantes'])

    with col2:
        st.metric("Estudiantes 2025", datos_2025_modelo['estudiantes'])

    with col3:
        st.metric("Puntaje Global 2024", datos_2024_modelo['puntaje_global'])

    with col4:
        st.metric("Puntaje Global 2025", datos_2025_modelo['puntaje_global'])

    # Avance global
    avance_global = calcular_avance(
        datos_2024_modelo['puntaje_global'],
        datos_2025_modelo['puntaje_global']
    )
    texto_avance, clase_avance = formatear_avance(avance_global)
    st.markdown(f'<div class="{clase_avance}">{texto_avance}</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Comparativo por áreas
    st.markdown(f"#### 📚 Comparativo por Áreas - {modelo_seleccionado}")

    tabla_areas = []
    for area in AREAS:
        puntaje_2024 = datos_2024_modelo['areas'][area]['promedio']
        puntaje_2025 = datos_2025_modelo['areas'][area]['promedio']
        avance = calcular_avance(puntaje_2024, puntaje_2025)
        texto_avance, _ = formatear_avance(avance)

        tabla_areas.append({
            'Área': area,
            '2024': puntaje_2024,
            '2025': puntaje_2025,
            'Avance': texto_avance
        })

    df_tabla_areas = pd.DataFrame(tabla_areas)
    st.dataframe(df_tabla_areas, use_container_width=True, hide_index=True)

    # Gráficos
    col1, col2 = st.columns(2)

    with col1:
        fig1 = crear_grafico_comparativo_areas(
            datos_2024_modelo,
            datos_2025_modelo,
            f"Comparativo por Áreas - {modelo_seleccionado}"
        )
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = crear_grafico_avances(datos_2024_modelo, datos_2025_modelo)
        st.plotly_chart(fig2, use_container_width=True)

def mostrar_analisis_avances(datos_2024, stats_regular_2025, stats_flexible_2025, stats_institucional_2025):
    """Página de análisis detallado de avances"""

    st.markdown('<div class="subtitle">📈 Análisis Detallado de Avances 2024 → 2025</div>', unsafe_allow_html=True)

    # Avances institucionales
    st.markdown("#### 🏛️ Avances Institucionales")

    avance_institucional = calcular_avance(
        datos_2024['Institucional']['puntaje_global'],
        stats_institucional_2025['puntaje_global']
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Puntaje Global 2024", datos_2024['Institucional']['puntaje_global'])

    with col2:
        st.metric("Puntaje Global 2025", stats_institucional_2025['puntaje_global'])

    with col3:
        texto_avance, clase_avance = formatear_avance(avance_institucional)
        st.markdown(f'<div class="{clase_avance}">{texto_avance}</div>', unsafe_allow_html=True)

    # Tabla de avances por área
    st.markdown("#### 📚 Avances por Área de Conocimiento")

    tabla_avances = []
    for area in AREAS:
        puntaje_2024 = datos_2024['Institucional']['areas'][area]['promedio']
        puntaje_2025 = stats_institucional_2025['areas'][area]['promedio']
        avance = calcular_avance(puntaje_2024, puntaje_2025)

        tabla_avances.append({
            'Área': area,
            '2024': puntaje_2024,
            '2025': puntaje_2025,
            'Avance (puntos)': avance,
            'Avance (%)': round((avance / puntaje_2024) * 100, 1) if puntaje_2024 > 0 else 0
        })

    df_avances = pd.DataFrame(tabla_avances)
    st.dataframe(df_avances, use_container_width=True, hide_index=True)

    # Gráfico de avances
    fig = crear_grafico_avances(datos_2024['Institucional'], stats_institucional_2025)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Avances por modelo educativo
    st.markdown("#### 🏫 Avances por Modelo Educativo")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**📘 Aula Regular**")
        avance_regular = calcular_avance(
            datos_2024['Aula Regular']['puntaje_global'],
            stats_regular_2025['puntaje_global']
        )
        texto_avance_regular, clase_avance_regular = formatear_avance(avance_regular)
        st.markdown(f'<div class="{clase_avance_regular}">{texto_avance_regular}</div>', unsafe_allow_html=True)

        # Tabla de avances por área - Aula Regular
        tabla_regular = []
        for area in AREAS:
            avance = calcular_avance(
                datos_2024['Aula Regular']['areas'][area]['promedio'],
                stats_regular_2025['areas'][area]['promedio']
            )
            tabla_regular.append({'Área': area, 'Avance': avance})

        df_regular = pd.DataFrame(tabla_regular)
        st.dataframe(df_regular, use_container_width=True, hide_index=True)

    with col2:
        st.markdown("**📙 Modelo Flexible**")
        avance_flexible = calcular_avance(
            datos_2024['Modelo Flexible']['puntaje_global'],
            stats_flexible_2025['puntaje_global']
        )
        texto_avance_flexible, clase_avance_flexible = formatear_avance(avance_flexible)
        st.markdown(f'<div class="{clase_avance_flexible}">{texto_avance_flexible}</div>', unsafe_allow_html=True)

        # Tabla de avances por área - Modelo Flexible
        tabla_flexible = []
        for area in AREAS:
            avance = calcular_avance(
                datos_2024['Modelo Flexible']['areas'][area]['promedio'],
                stats_flexible_2025['areas'][area]['promedio']
            )
            tabla_flexible.append({'Área': area, 'Avance': avance})

        df_flexible = pd.DataFrame(tabla_flexible)
        st.dataframe(df_flexible, use_container_width=True, hide_index=True)

def mostrar_rankings(datos_2025_raw):
    """Página de rankings y estudiantes destacados"""

    st.markdown('<div class="subtitle">🏆 Rankings y Estudiantes Destacados</div>', unsafe_allow_html=True)

    df_todos = datos_2025_raw['df_todos']

    # Crear nombre completo
    df_todos['Nombre Completo'] = (
        df_todos['Primer Nombre'].fillna('') + ' ' +
        df_todos['Segundo Nombre'].fillna('') + ' ' +
        df_todos['Primer Apellido'].fillna('') + ' ' +
        df_todos['Segundo Apellido'].fillna('')
    ).str.strip().str.replace(r'\s+', ' ', regex=True)

    # Top 10 Puntaje Global
    st.markdown("#### 🥇 Top 10 - Puntaje Global")

    df_top10 = df_todos.nlargest(10, 'Puntaje Global')[
        ['Nombre Completo', 'Grupo', 'Modelo', 'Puntaje Global'] + AREAS
    ].copy()
    df_top10['Posición'] = range(1, len(df_top10) + 1)
    df_top10 = df_top10[['Posición', 'Nombre Completo', 'Grupo', 'Modelo', 'Puntaje Global'] + AREAS]

    st.dataframe(df_top10, use_container_width=True, hide_index=True)

    # Gráfico Top 10
    fig = px.bar(
        df_top10,
        x='Nombre Completo',
        y='Puntaje Global',
        color='Modelo',
        title="Top 10 Estudiantes - Puntaje Global",
        color_discrete_map={'Aula Regular': '#667eea', 'Modelo Flexible': '#764ba2'}
    )
    fig.update_xaxes(tickangle=-45)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Mejores por área
    st.markdown("#### 🌟 Mejores Estudiantes por Área")

    tabs = st.tabs(AREAS)

    for i, area in enumerate(AREAS):
        with tabs[i]:
            df_top_area = df_todos.nlargest(5, area)[
                ['Nombre Completo', 'Grupo', 'Modelo', area, 'Puntaje Global']
            ].copy()
            df_top_area['Posición'] = range(1, len(df_top_area) + 1)
            df_top_area = df_top_area[['Posición', 'Nombre Completo', 'Grupo', 'Modelo', area, 'Puntaje Global']]

            st.dataframe(df_top_area, use_container_width=True, hide_index=True)

    st.markdown("---")

    # Rankings por modelo
    st.markdown("#### 🏫 Rankings por Modelo Educativo")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**📘 Top 5 - Aula Regular**")
        df_regular = datos_2025_raw['df_regular']
        df_regular['Nombre Completo'] = (
            df_regular['Primer Nombre'].fillna('') + ' ' +
            df_regular['Segundo Nombre'].fillna('') + ' ' +
            df_regular['Primer Apellido'].fillna('') + ' ' +
            df_regular['Segundo Apellido'].fillna('')
        ).str.strip().str.replace(r'\s+', ' ', regex=True)

        df_top_regular = df_regular.nlargest(5, 'Puntaje Global')[
            ['Nombre Completo', 'Grupo', 'Puntaje Global']
        ].copy()
        df_top_regular['Posición'] = range(1, len(df_top_regular) + 1)
        df_top_regular = df_top_regular[['Posición', 'Nombre Completo', 'Grupo', 'Puntaje Global']]

        st.dataframe(df_top_regular, use_container_width=True, hide_index=True)

    with col2:
        st.markdown("**📙 Top 5 - Modelo Flexible**")
        df_flexible = datos_2025_raw['df_flexible']
        df_flexible['Nombre Completo'] = (
            df_flexible['Primer Nombre'].fillna('') + ' ' +
            df_flexible['Segundo Nombre'].fillna('') + ' ' +
            df_flexible['Primer Apellido'].fillna('') + ' ' +
            df_flexible['Segundo Apellido'].fillna('')
        ).str.strip().str.replace(r'\s+', ' ', regex=True)

        df_top_flexible = df_flexible.nlargest(5, 'Puntaje Global')[
            ['Nombre Completo', 'Grupo', 'Puntaje Global']
        ].copy()
        df_top_flexible['Posición'] = range(1, len(df_top_flexible) + 1)
        df_top_flexible = df_top_flexible[['Posición', 'Nombre Completo', 'Grupo', 'Puntaje Global']]

        st.dataframe(df_top_flexible, use_container_width=True, hide_index=True)

    st.markdown("---")

    # Rankings por grado
    st.markdown("#### 🎓 Rankings por Grado")

    grado_seleccionado = st.selectbox(
        "Seleccione un grado:",
        sorted(df_todos['Grupo'].unique()),
        key='ranking_grado'
    )

    df_grado = df_todos[df_todos['Grupo'] == grado_seleccionado].copy()
    df_grado_ranking = df_grado.nlargest(10, 'Puntaje Global')[
        ['Nombre Completo', 'Modelo', 'Puntaje Global'] + AREAS
    ].copy()
    df_grado_ranking['Posición'] = range(1, len(df_grado_ranking) + 1)
    df_grado_ranking = df_grado_ranking[['Posición', 'Nombre Completo', 'Modelo', 'Puntaje Global'] + AREAS]

    st.dataframe(df_grado_ranking, use_container_width=True, hide_index=True)

def mostrar_descarga_datos(datos_2025_raw):
    """Página para descargar datos en diferentes formatos"""

    st.markdown('<div class="subtitle">📥 Descargar Datos</div>', unsafe_allow_html=True)

    st.info("Descargue los datos en formato CSV o Excel para análisis adicionales.")

    df_todos = datos_2025_raw['df_todos']
    df_regular = datos_2025_raw['df_regular']
    df_flexible = datos_2025_raw['df_flexible']

    # Preparar datos para descarga
    for df in [df_todos, df_regular, df_flexible]:
        df['Nombre Completo'] = (
            df['Primer Nombre'].fillna('') + ' ' +
            df['Segundo Nombre'].fillna('') + ' ' +
            df['Primer Apellido'].fillna('') + ' ' +
            df['Segundo Apellido'].fillna('')
        ).str.strip().str.replace(r'\s+', ' ', regex=True)

    # Seleccionar conjunto de datos
    conjunto_datos = st.radio(
        "Seleccione el conjunto de datos a descargar:",
        ["Todos los estudiantes", "Aula Regular", "Modelo Flexible"],
        horizontal=True
    )

    if conjunto_datos == "Todos los estudiantes":
        df_descarga = df_todos
        nombre_archivo = "resultados_icfes_2025_todos"
    elif conjunto_datos == "Aula Regular":
        df_descarga = df_regular
        nombre_archivo = "resultados_icfes_2025_aula_regular"
    else:
        df_descarga = df_flexible
        nombre_archivo = "resultados_icfes_2025_modelo_flexible"

    # Mostrar preview
    st.markdown("#### 👀 Vista Previa de los Datos")
    st.dataframe(df_descarga.head(10), use_container_width=True)

    st.markdown(f"**Total de registros:** {len(df_descarga)}")

    # Botones de descarga
    st.markdown("#### 💾 Descargar")

    col1, col2 = st.columns(2)

    with col1:
        # Descargar CSV
        csv = df_descarga.to_csv(index=False, encoding='utf-8-sig')
        st.download_button(
            label="📄 Descargar CSV",
            data=csv,
            file_name=f"{nombre_archivo}.csv",
            mime="text/csv",
            use_container_width=True
        )

    with col2:
        # Descargar Excel
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df_descarga.to_excel(writer, index=False, sheet_name='Resultados')
        buffer.seek(0)

        st.download_button(
            label="📊 Descargar Excel",
            data=buffer,
            file_name=f"{nombre_archivo}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )

    st.markdown("---")

    # Estadísticas resumidas para descarga
    st.markdown("#### 📊 Estadísticas Resumidas")

    estadisticas_resumen = {
        'Métrica': [
            'Total Estudiantes',
            'Puntaje Global Promedio',
            'Puntaje Global Máximo',
            'Puntaje Global Mínimo',
            'Desviación Estándar Global'
        ],
        'Valor': [
            len(df_descarga),
            int(round(df_descarga['Puntaje Global'].mean())),
            int(df_descarga['Puntaje Global'].max()),
            int(df_descarga['Puntaje Global'].min()),
            round(df_descarga['Puntaje Global'].std(), 2)
        ]
    }

    # Agregar promedios por área
    for area in AREAS:
        estadisticas_resumen['Métrica'].append(f'Promedio {area}')
        estadisticas_resumen['Valor'].append(int(round(df_descarga[area].mean())))

    df_estadisticas = pd.DataFrame(estadisticas_resumen)
    st.dataframe(df_estadisticas, use_container_width=True, hide_index=True)

    # Descargar estadísticas
    csv_stats = df_estadisticas.to_csv(index=False, encoding='utf-8-sig')
    st.download_button(
        label="📄 Descargar Estadísticas (CSV)",
        data=csv_stats,
        file_name=f"{nombre_archivo}_estadisticas.csv",
        mime="text/csv"
    )

if __name__ == "__main__":
    main()

