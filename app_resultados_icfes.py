#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aplicación Web Interactiva para Visualización y Análisis de Resultados ICFES Saber 11
Análisis Comparativo: Modelo Aula Regular vs Modelo Flexible
Institución Educativa Pedacito de Cielo
Autor: Sistema de Análisis ICFES
Fecha: 2025-10-16
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from scipy import stats
from datetime import datetime
import warnings
import os
warnings.filterwarnings('ignore')

# ============================================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================================

st.set_page_config(
    page_title="Análisis Resultados ICFES - Pedacito de Cielo 2025",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# ESTILOS CSS PERSONALIZADOS
# ============================================================================

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
        border-bottom: 3px solid #1f77b4;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2c3e50;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .info-box {
        background-color: #e8f4f8;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #3498db;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2rem;
    }
    .stTabs [data-baseweb="tab"] {
        height: 3rem;
        padding: 0 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# CONSTANTES GLOBALES
# ============================================================================

# Archivos de datos
ARCHIVO_AULA_REGULAR = 'PCIELO-RESULTADOS-ICFES-MODELO-AULA-REGULAR-2025.xlsx'
ARCHIVO_MODELO_FLEXIBLE = 'PCIELO-RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx'

# Áreas de evaluación
AREAS = ['Lectura Crítica', 'Matemáticas', 'Sociales y Ciudadanas', 'Ciencias Naturales', 'Inglés']

# Colores por área
COLORES_AREAS = {
    'Lectura Crítica': '#1f77b4',
    'Matemáticas': '#ff7f0e',
    'Sociales y Ciudadanas': '#2ca02c',
    'Ciencias Naturales': '#d62728',
    'Inglés': '#9467bd',
    'Puntaje Global': '#8c564b'
}

# Colores por modelo
COLORES_MODELOS = {
    'Aula Regular': '#3498db',
    'Modelo Flexible': '#e74c3c'
}

# Colores por grupo
COLORES_GRUPOS = {
    '11A': '#3498db',
    '11B': '#2ecc71',
    'P3A': '#e74c3c',
    'P3B': '#f39c12',
    'P3C': '#9b59b6'
}

# Clasificaciones por puntaje global
def clasificar_puntaje(puntaje):
    """Clasifica el puntaje global según rangos establecidos"""
    if pd.isna(puntaje):
        return 'Sin datos'
    elif puntaje < 200:
        return 'Bajo'
    elif puntaje < 300:
        return 'Medio'
    elif puntaje < 400:
        return 'Alto'
    else:
        return 'Superior'

# ============================================================================
# FUNCIONES DE CARGA DE DATOS
# ============================================================================

@st.cache_data
def cargar_datos_unificados():
    """
    Carga y unifica los datos de ambos modelos educativos.
    
    Returns:
        pd.DataFrame: DataFrame unificado con todos los estudiantes
        dict: Información sobre la carga de datos
    """
    info = {
        'aula_regular_cargado': False,
        'modelo_flexible_cargado': False,
        'total_estudiantes': 0,
        'estudiantes_aula_regular': 0,
        'estudiantes_modelo_flexible': 0
    }
    
    dfs = []
    
    # Cargar Modelo Aula Regular
    if os.path.exists(ARCHIVO_AULA_REGULAR):
        try:
            df_regular = pd.read_excel(ARCHIVO_AULA_REGULAR)
            # Filtrar solo estudiantes (excluir filas de estadísticas)
            df_regular = df_regular[df_regular['Grupo'].notna()].copy()
            df_regular['Modelo'] = 'Aula Regular'
            dfs.append(df_regular)
            info['aula_regular_cargado'] = True
            info['estudiantes_aula_regular'] = len(df_regular)
        except Exception as e:
            st.error(f"Error al cargar {ARCHIVO_AULA_REGULAR}: {e}")
    
    # Cargar Modelo Flexible
    if os.path.exists(ARCHIVO_MODELO_FLEXIBLE):
        try:
            df_flexible = pd.read_excel(ARCHIVO_MODELO_FLEXIBLE)
            # Filtrar solo estudiantes (excluir filas de estadísticas)
            df_flexible = df_flexible[df_flexible['Grupo'].notna()].copy()
            df_flexible['Modelo'] = 'Modelo Flexible'
            # Eliminar columna extra si existe
            if 'Unnamed: 13' in df_flexible.columns:
                df_flexible = df_flexible.drop(columns=['Unnamed: 13'])
            dfs.append(df_flexible)
            info['modelo_flexible_cargado'] = True
            info['estudiantes_modelo_flexible'] = len(df_flexible)
        except Exception as e:
            st.error(f"Error al cargar {ARCHIVO_MODELO_FLEXIBLE}: {e}")
    
    # Verificar que al menos un archivo se haya cargado
    if not dfs:
        return None, info
    
    # Unificar DataFrames
    df_unificado = pd.concat(dfs, ignore_index=True)
    
    # Crear nombre completo
    df_unificado['Nombre Completo'] = (
        df_unificado['Primer Nombre'].fillna('') + ' ' +
        df_unificado['Segundo Nombre'].fillna('') + ' ' +
        df_unificado['Primer Apellido'].fillna('') + ' ' +
        df_unificado['Segundo Apellido'].fillna('')
    ).str.strip().str.replace(r'\s+', ' ', regex=True)
    
    # Aplicar clasificación
    df_unificado['Clasificación'] = df_unificado['Puntaje Global'].apply(clasificar_puntaje)
    
    info['total_estudiantes'] = len(df_unificado)
    
    return df_unificado, info

@st.cache_data
def cargar_datos_historicos():
    """
    Carga los datos históricos de comparación entre años (2024-2025).
    Solo disponible para Modelo Aula Regular.
    
    Returns:
        dict: Datos históricos por modelo
    """
    historicos = {
        'Aula Regular': None,
        'Modelo Flexible': None
    }
    
    # Cargar históricos de Aula Regular
    if os.path.exists(ARCHIVO_AULA_REGULAR):
        try:
            df_completo = pd.read_excel(ARCHIVO_AULA_REGULAR)
            if len(df_completo) >= 40:
                datos_2025 = df_completo.iloc[37][AREAS + ['Puntaje Global']].to_dict()
                datos_2024 = df_completo.iloc[38][AREAS + ['Puntaje Global']].to_dict()
                avance = df_completo.iloc[39][AREAS + ['Puntaje Global']].to_dict()
                
                historicos['Aula Regular'] = {
                    '2025': datos_2025,
                    '2024': datos_2024,
                    'Avance': avance
                }
        except Exception as e:
            st.warning(f"No se pudieron cargar datos históricos de Aula Regular: {e}")
    
    # Nota: Modelo Flexible no tiene datos 2024 aún
    
    return historicos

# ============================================================================
# FUNCIONES DE ANÁLISIS ESTADÍSTICO
# ============================================================================

def calcular_estadisticas_descriptivas(df, columna, grupo_por=None):
    """
    Calcula estadísticas descriptivas para una columna.

    Args:
        df: DataFrame
        columna: Nombre de la columna a analizar
        grupo_por: Columna por la cual agrupar (opcional)

    Returns:
        dict o DataFrame: Estadísticas descriptivas
    """
    if grupo_por:
        stats = df.groupby(grupo_por)[columna].agg([
            ('Promedio', 'mean'),
            ('Mediana', 'median'),
            ('Desv. Estándar', 'std'),
            ('Mínimo', 'min'),
            ('Máximo', 'max'),
            ('Cuenta', 'count')
        ])
        # Redondear promedios, medianas, mínimos y máximos a enteros
        # Mantener decimales para desviación estándar
        # Usar fillna para manejar valores NaN antes de redondear
        stats['Promedio'] = stats['Promedio'].fillna(0).round(0)
        stats['Mediana'] = stats['Mediana'].fillna(0).round(0)
        stats['Mínimo'] = stats['Mínimo'].fillna(0).round(0)
        stats['Máximo'] = stats['Máximo'].fillna(0).round(0)
        stats['Desv. Estándar'] = stats['Desv. Estándar'].fillna(0).round(2)
        return stats
    else:
        # Manejar valores NaN con pd.isna()
        promedio = df[columna].mean()
        mediana = df[columna].median()
        desv_std = df[columna].std()
        minimo = df[columna].min()
        maximo = df[columna].max()

        return {
            'Promedio': round(promedio, 0) if pd.notna(promedio) else 0,
            'Mediana': round(mediana, 0) if pd.notna(mediana) else 0,
            'Desv. Estándar': round(desv_std, 2) if pd.notna(desv_std) else 0,
            'Mínimo': round(minimo, 0) if pd.notna(minimo) else 0,
            'Máximo': round(maximo, 0) if pd.notna(maximo) else 0,
            'Cuenta': df[columna].count()
        }


def realizar_test_comparacion(df, area, grupo1_filtro, grupo2_filtro, nombre_grupo1, nombre_grupo2):
    """
    Realiza un test t de Student para comparar dos grupos.

    Args:
        df: DataFrame
        area: Área a comparar
        grupo1_filtro: Filtro booleano para grupo 1
        grupo2_filtro: Filtro booleano para grupo 2
        nombre_grupo1: Nombre del grupo 1
        nombre_grupo2: Nombre del grupo 2

    Returns:
        dict: Resultados del test estadístico
    """
    datos_grupo1 = df[grupo1_filtro][area].dropna()
    datos_grupo2 = df[grupo2_filtro][area].dropna()

    if len(datos_grupo1) < 2 or len(datos_grupo2) < 2:
        return {
            'valido': False,
            'mensaje': 'Datos insuficientes para realizar el test'
        }

    # Test t de Student
    t_stat, p_value = stats.ttest_ind(datos_grupo1, datos_grupo2)

    # Interpretación
    if p_value < 0.05:
        significativo = "Sí (p < 0.05)"
        interpretacion = f"Existe una diferencia estadísticamente significativa entre {nombre_grupo1} y {nombre_grupo2}"
    else:
        significativo = "No (p ≥ 0.05)"
        interpretacion = f"No existe una diferencia estadísticamente significativa entre {nombre_grupo1} y {nombre_grupo2}"

    # Calcular medias con manejo de NaN
    media1 = datos_grupo1.mean()
    media2 = datos_grupo2.mean()

    return {
        'valido': True,
        'n_grupo1': len(datos_grupo1),
        'n_grupo2': len(datos_grupo2),
        'media_grupo1': round(media1, 0) if pd.notna(media1) else 0,
        'media_grupo2': round(media2, 0) if pd.notna(media2) else 0,
        'diferencia_medias': round(media1 - media2, 0) if pd.notna(media1) and pd.notna(media2) else 0,
        't_statistic': t_stat,
        'p_value': p_value,
        'significativo': significativo,
        'interpretacion': interpretacion
    }

def calcular_percentil(df, area, valor):
    """
    Calcula el percentil de un valor en una distribución.

    Args:
        df: DataFrame
        area: Área a analizar
        valor: Valor para calcular percentil

    Returns:
        float: Percentil (0-100)
    """
    datos = df[area].dropna()
    percentil = stats.percentileofscore(datos, valor, kind='rank')
    return percentil

def obtener_ranking(df, criterio, top_n=None, ascendente=False):
    """
    Obtiene un ranking de estudiantes según un criterio.

    Args:
        df: DataFrame
        criterio: Columna por la cual rankear
        top_n: Número de resultados a retornar (None = todos)
        ascendente: Si True, ordena de menor a mayor

    Returns:
        pd.DataFrame: DataFrame rankeado
    """
    df_ranking = df[['Nombre Completo', 'Modelo', 'Grupo', criterio]].copy()
    df_ranking = df_ranking.sort_values(criterio, ascending=ascendente).reset_index(drop=True)
    df_ranking.index = df_ranking.index + 1
    df_ranking.index.name = 'Posición'

    if top_n:
        return df_ranking.head(top_n)
    return df_ranking

# ============================================================================
# FUNCIONES DE VISUALIZACIÓN
# ============================================================================

def crear_grafico_comparacion_modelos(df, area):
    """
    Crea un box plot comparando modelos para un área específica.

    Args:
        df: DataFrame
        area: Área a comparar

    Returns:
        plotly.graph_objects.Figure
    """
    fig = go.Figure()

    for modelo in df['Modelo'].unique():
        datos = df[df['Modelo'] == modelo][area].dropna()
        fig.add_trace(go.Box(
            y=datos,
            name=modelo,
            marker_color=COLORES_MODELOS.get(modelo, '#999999'),
            boxmean='sd'
        ))

    fig.update_layout(
        title=f'Comparación de {area} entre Modelos Educativos',
        yaxis_title='Puntaje',
        xaxis_title='Modelo',
        showlegend=True,
        height=500
    )

    return fig

def crear_grafico_comparacion_grupos(df, modelo, area):
    """
    Crea un box plot comparando grupos dentro de un modelo.

    Args:
        df: DataFrame
        modelo: Modelo a filtrar
        area: Área a comparar

    Returns:
        plotly.graph_objects.Figure
    """
    df_filtrado = df[df['Modelo'] == modelo]

    fig = go.Figure()

    for grupo in sorted(df_filtrado['Grupo'].unique()):
        datos = df_filtrado[df_filtrado['Grupo'] == grupo][area].dropna()
        fig.add_trace(go.Box(
            y=datos,
            name=grupo,
            marker_color=COLORES_GRUPOS.get(grupo, '#999999'),
            boxmean='sd'
        ))

    fig.update_layout(
        title=f'Comparación de {area} entre Grupos - {modelo}',
        yaxis_title='Puntaje',
        xaxis_title='Grupo',
        showlegend=True,
        height=500
    )

    return fig

def crear_grafico_barras_promedios(df, areas, grupo_por, titulo):
    """
    Crea un gráfico de barras agrupadas para comparar promedios.

    Args:
        df: DataFrame
        areas: Lista de áreas a comparar
        grupo_por: Columna por la cual agrupar
        titulo: Título del gráfico

    Returns:
        plotly.graph_objects.Figure
    """
    fig = go.Figure()

    grupos = sorted(df[grupo_por].unique())

    for area in areas:
        promedios = []
        for grupo in grupos:
            prom = df[df[grupo_por] == grupo][area].mean()
            promedios.append(round(prom, 0) if pd.notna(prom) else 0)

        fig.add_trace(go.Bar(
            name=area,
            x=grupos,
            y=promedios,
            marker_color=COLORES_AREAS.get(area, '#999999'),
            text=[f'{int(p)}' for p in promedios],
            textposition='outside'
        ))

    fig.update_layout(
        title=titulo,
        xaxis_title=grupo_por,
        yaxis_title='Promedio',
        barmode='group',
        showlegend=True,
        height=500
    )

    return fig

def crear_radar_chart(estudiante, areas):
    """
    Crea un gráfico de radar para el perfil de un estudiante.

    Args:
        estudiante: Serie con datos del estudiante
        areas: Lista de áreas a incluir

    Returns:
        plotly.graph_objects.Figure
    """
    valores = [estudiante[area] for area in areas]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=valores,
        theta=areas,
        fill='toself',
        name='Estudiante',
        line_color='#3498db'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=True,
        height=400
    )

    return fig

def crear_heatmap_correlaciones(df, modelo):
    """
    Crea un mapa de calor de correlaciones entre áreas.

    Args:
        df: DataFrame
        modelo: Modelo a filtrar

    Returns:
        plotly.graph_objects.Figure
    """
    df_filtrado = df[df['Modelo'] == modelo][AREAS + ['Puntaje Global']]
    correlaciones = df_filtrado.corr()

    fig = go.Figure(data=go.Heatmap(
        z=correlaciones.values,
        x=correlaciones.columns,
        y=correlaciones.columns,
        colorscale='RdBu',
        zmid=0,
        text=correlaciones.values.round(2),
        texttemplate='%{text}',
        textfont={"size": 10},
        colorbar=dict(title="Correlación")
    ))

    fig.update_layout(
        title=f'Correlaciones entre Áreas - {modelo}',
        height=500,
        xaxis={'side': 'bottom'}
    )

    return fig

def crear_grafico_distribucion(df, area, modelo=None):
    """
    Crea un histograma con curva de densidad.

    Args:
        df: DataFrame
        area: Área a analizar
        modelo: Modelo a filtrar (opcional)

    Returns:
        plotly.graph_objects.Figure
    """
    if modelo:
        df = df[df['Modelo'] == modelo]
        titulo = f'Distribución de {area} - {modelo}'
    else:
        titulo = f'Distribución de {area} - Todos los Modelos'

    fig = px.histogram(
        df,
        x=area,
        nbins=20,
        marginal='box',
        color='Modelo' if not modelo else None,
        color_discrete_map=COLORES_MODELOS,
        labels={area: 'Puntaje', 'count': 'Frecuencia'}
    )

    fig.update_layout(
        title=titulo,
        showlegend=True,
        height=500
    )

    return fig


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """Función principal de la aplicación"""

    # Header
    st.markdown(
        '<div class="main-header">📊 Análisis de Resultados ICFES Saber 11 - 2025<br>'
        '<small style="font-size: 1.2rem;">Institución Educativa Pedacito de Cielo</small></div>',
        unsafe_allow_html=True
    )

    # Cargar datos
    df, info = cargar_datos_unificados()

    if df is None or len(df) == 0:
        st.error("❌ No se pudieron cargar los datos. Verifica que los archivos Excel existan.")
        st.info(f"""
        **Archivos requeridos:**
        - {ARCHIVO_AULA_REGULAR}
        - {ARCHIVO_MODELO_FLEXIBLE}
        """)
        return

    # Mostrar información de carga
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            "Total Estudiantes",
            info['total_estudiantes'],
            help="Total de estudiantes analizados"
        )
    with col2:
        st.metric(
            "Modelo Aula Regular",
            info['estudiantes_aula_regular'],
            help="Estudiantes en grupos 11A y 11B"
        )
    with col3:
        st.metric(
            "Modelo Flexible",
            info['estudiantes_modelo_flexible'],
            help="Estudiantes en grupos P3A, P3B y P3C"
        )

    # Nota metodológica
    st.markdown("""
    <div class="info-box">
    <strong>📚 Nota Metodológica Importante:</strong><br>
    Las áreas del ICFES Saber 11 utilizan escalas y criterios de evaluación diferentes.
    Por esta razón, <strong>NO se comparan promedios entre áreas diferentes</strong> en esta aplicación.
    Los análisis se realizan por área individual, siguiendo las recomendaciones del ICFES Colombia.
    </div>
    """, unsafe_allow_html=True)

    # Tabs principales
    tabs = st.tabs([
        "📊 Vista General",
        "🔄 Comparación entre Modelos",
        "👥 Comparación entre Grupos",
        "👤 Análisis por Estudiante",
        "📚 Análisis por Área",
        "🏆 Rankings Generales",
        "📈 Análisis Estadístico Avanzado",
        "📅 Comparación Temporal"
    ])

    # TAB 1: Vista General
    with tabs[0]:
        mostrar_vista_general(df, info)

    # TAB 2: Comparación entre Modelos
    with tabs[1]:
        mostrar_comparacion_modelos(df)

    # TAB 3: Comparación entre Grupos
    with tabs[2]:
        mostrar_comparacion_grupos(df)

    # TAB 4: Análisis por Estudiante
    with tabs[3]:
        mostrar_analisis_estudiante(df)

    # TAB 5: Análisis por Área
    with tabs[4]:
        mostrar_analisis_area(df)

    # TAB 6: Rankings Generales
    with tabs[5]:
        mostrar_rankings(df)

    # TAB 7: Análisis Estadístico Avanzado
    with tabs[6]:
        mostrar_analisis_avanzado(df)

    # TAB 8: Comparación Temporal
    with tabs[7]:
        mostrar_comparacion_temporal(df)

# ============================================================================
# PESTAÑAS DE LA APLICACIÓN
# ============================================================================

def mostrar_vista_general(df, info):
    """Pestaña 1: Vista General"""
    st.header("📊 Vista General de Resultados")

    # Resumen por modelo
    st.subheader("📋 Resumen por Modelo Educativo")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Modelo Aula Regular")
        if info['aula_regular_cargado']:
            df_regular = df[df['Modelo'] == 'Aula Regular']
            promedio_regular = df_regular['Puntaje Global'].mean()
            st.metric("Estudiantes", len(df_regular))
            st.metric("Promedio Global", f"{round(promedio_regular, 0) if pd.notna(promedio_regular) else 0:.0f}")
            st.metric("Grupos", ", ".join(sorted(df_regular['Grupo'].unique())))
        else:
            st.warning("No se cargaron datos de Aula Regular")

    with col2:
        st.markdown("### Modelo Flexible")
        if info['modelo_flexible_cargado']:
            df_flexible = df[df['Modelo'] == 'Modelo Flexible']
            promedio_flexible = df_flexible['Puntaje Global'].mean()
            st.metric("Estudiantes", len(df_flexible))
            st.metric("Promedio Global", f"{round(promedio_flexible, 0) if pd.notna(promedio_flexible) else 0:.0f}")
            st.metric("Grupos", ", ".join(sorted(df_flexible['Grupo'].unique())))
        else:
            st.warning("No se cargaron datos de Modelo Flexible")

    st.markdown("---")

    # Distribución de estudiantes por clasificación
    st.subheader("📊 Distribución por Clasificación de Puntaje")

    col1, col2 = st.columns(2)

    with col1:
        # Gráfico de pastel por modelo
        clasificacion_modelo = df.groupby(['Modelo', 'Clasificación']).size().reset_index(name='Cantidad')
        fig = px.sunburst(
            clasificacion_modelo,
            path=['Modelo', 'Clasificación'],
            values='Cantidad',
            color='Modelo',
            color_discrete_map=COLORES_MODELOS,
            title='Distribución por Modelo y Clasificación'
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Tabla de distribución
        tabla_dist = df.groupby(['Modelo', 'Clasificación']).size().unstack(fill_value=0)
        st.markdown("### Tabla de Distribución")
        st.dataframe(tabla_dist, use_container_width=True)

    st.markdown("---")

    # Promedios por área y modelo
    st.subheader("📚 Promedios por Área y Modelo")

    promedios_modelo = df.groupby('Modelo')[AREAS + ['Puntaje Global']].mean().fillna(0).round(0)

    # Gráfico de barras agrupadas
    fig = crear_grafico_barras_promedios(
        df,
        AREAS,
        'Modelo',
        'Comparación de Promedios por Área entre Modelos'
    )
    st.plotly_chart(fig, use_container_width=True)

    # Tabla de promedios
    st.markdown("### Tabla de Promedios")
    st.dataframe(promedios_modelo, use_container_width=True)

    st.markdown("---")

    # Distribución de puntaje global
    st.subheader("📈 Distribución de Puntaje Global")

    fig = px.histogram(
        df,
        x='Puntaje Global',
        color='Modelo',
        nbins=25,
        marginal='box',
        color_discrete_map=COLORES_MODELOS,
        labels={'Puntaje Global': 'Puntaje', 'count': 'Frecuencia'},
        title='Distribución de Puntaje Global por Modelo'
    )
    st.plotly_chart(fig, use_container_width=True)

def mostrar_comparacion_modelos(df):
    """Pestaña 2: Comparación entre Modelos"""
    st.header("🔄 Comparación entre Modelos Educativos")

    st.markdown("""
    <div class="info-box">
    <strong>ℹ️ Información:</strong><br>
    Esta sección compara el desempeño entre el <strong>Modelo Aula Regular</strong> (grupos 11A y 11B)
    y el <strong>Modelo Flexible</strong> (grupos P3A, P3B y P3C).
    </div>
    """, unsafe_allow_html=True)

    # Selector de área
    area_seleccionada = st.selectbox(
        "Selecciona un área para análisis detallado:",
        ['Puntaje Global'] + AREAS,
        key='area_comp_modelos'
    )

    st.markdown("---")

    # Estadísticas comparativas
    st.subheader(f"📊 Estadísticas Comparativas - {area_seleccionada}")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Modelo Aula Regular")
        df_regular = df[df['Modelo'] == 'Aula Regular']
        stats_regular = calcular_estadisticas_descriptivas(df_regular, area_seleccionada)
        for key, value in stats_regular.items():
            if key == 'Desv. Estándar':
                st.metric(key, f"{value:.2f}")
            else:
                st.metric(key, f"{value:.0f}")

    with col2:
        st.markdown("### Modelo Flexible")
        df_flexible = df[df['Modelo'] == 'Modelo Flexible']
        stats_flexible = calcular_estadisticas_descriptivas(df_flexible, area_seleccionada)
        for key, value in stats_flexible.items():
            if key == 'Desv. Estándar':
                st.metric(key, f"{value:.2f}")
            else:
                st.metric(key, f"{value:.0f}")

    st.markdown("---")

    # Test estadístico
    st.subheader("🔬 Test Estadístico de Comparación")

    resultado_test = realizar_test_comparacion(
        df,
        area_seleccionada,
        df['Modelo'] == 'Aula Regular',
        df['Modelo'] == 'Modelo Flexible',
        'Aula Regular',
        'Modelo Flexible'
    )

    if resultado_test['valido']:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Diferencia de Medias", f"{resultado_test['diferencia_medias']:.0f}")
        with col2:
            st.metric("Valor p", f"{resultado_test['p_value']:.4f}")
        with col3:
            st.metric("¿Significativo?", resultado_test['significativo'])

        st.info(f"**Interpretación:** {resultado_test['interpretacion']}")
    else:
        st.warning(resultado_test['mensaje'])

    st.markdown("---")

    # Visualizaciones
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📦 Diagrama de Caja")
        fig = crear_grafico_comparacion_modelos(df, area_seleccionada)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("📊 Distribución")
        fig = crear_grafico_distribucion(df, area_seleccionada)
        st.plotly_chart(fig, use_container_width=True)


def mostrar_comparacion_grupos(df):
    """Pestaña 3: Comparación entre Grupos"""
    st.header("👥 Comparación entre Grupos")

    # Selector de modelo
    modelo_seleccionado = st.radio(
        "Selecciona el modelo educativo:",
        df['Modelo'].unique(),
        horizontal=True,
        key='modelo_comp_grupos'
    )

    df_modelo = df[df['Modelo'] == modelo_seleccionado]
    grupos = sorted(df_modelo['Grupo'].unique())

    st.info(f"**Grupos en {modelo_seleccionado}:** {', '.join(grupos)}")

    # Selector de área
    area_seleccionada = st.selectbox(
        "Selecciona un área para análisis:",
        ['Puntaje Global'] + AREAS,
        key='area_comp_grupos'
    )

    st.markdown("---")

    # Estadísticas por grupo
    st.subheader(f"📊 Estadísticas por Grupo - {area_seleccionada}")

    stats_grupos = calcular_estadisticas_descriptivas(df_modelo, area_seleccionada, 'Grupo')
    st.dataframe(stats_grupos, use_container_width=True)

    st.markdown("---")

    # Visualizaciones
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📦 Comparación entre Grupos")
        fig = crear_grafico_comparacion_grupos(df, modelo_seleccionado, area_seleccionada)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("📊 Promedios por Grupo")
        promedios = df_modelo.groupby('Grupo')[area_seleccionada].mean().fillna(0).round(0).sort_values(ascending=False)
        fig = go.Figure(data=[
            go.Bar(
                x=promedios.index,
                y=promedios.values,
                marker_color=[COLORES_GRUPOS.get(g, '#999999') for g in promedios.index],
                text=[f'{int(v)}' for v in promedios.values],
                textposition='outside'
            )
        ])
        fig.update_layout(
            title=f'Promedio de {area_seleccionada} por Grupo',
            xaxis_title='Grupo',
            yaxis_title='Promedio',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Comparación de todas las áreas
    st.subheader("📚 Comparación de Todas las Áreas")

    fig = crear_grafico_barras_promedios(
        df_modelo,
        AREAS,
        'Grupo',
        f'Promedios por Área y Grupo - {modelo_seleccionado}'
    )
    st.plotly_chart(fig, use_container_width=True)

    # Tests estadísticos entre grupos (si hay más de un grupo)
    if len(grupos) >= 2:
        st.markdown("---")
        st.subheader("🔬 Tests Estadísticos entre Grupos")

        # Selector de grupos a comparar
        col1, col2 = st.columns(2)
        with col1:
            grupo1 = st.selectbox("Grupo 1:", grupos, key='grupo1_test')
        with col2:
            grupos_disponibles = [g for g in grupos if g != grupo1]
            if grupos_disponibles:
                grupo2 = st.selectbox("Grupo 2:", grupos_disponibles, key='grupo2_test')

                resultado_test = realizar_test_comparacion(
                    df_modelo,
                    area_seleccionada,
                    df_modelo['Grupo'] == grupo1,
                    df_modelo['Grupo'] == grupo2,
                    grupo1,
                    grupo2
                )

                if resultado_test['valido']:
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Diferencia de Medias", f"{resultado_test['diferencia_medias']:.0f}")
                    with col2:
                        st.metric("Valor p", f"{resultado_test['p_value']:.4f}")
                    with col3:
                        st.metric("¿Significativo?", resultado_test['significativo'])

                    st.info(f"**Interpretación:** {resultado_test['interpretacion']}")

def mostrar_analisis_estudiante(df):
    """Pestaña 4: Análisis por Estudiante"""
    st.header("👤 Análisis Individual por Estudiante")

    # Selector de modelo
    modelo_seleccionado = st.selectbox(
        "Selecciona el modelo educativo:",
        df['Modelo'].unique(),
        key='modelo_estudiante'
    )

    df_modelo = df[df['Modelo'] == modelo_seleccionado]

    # Selector de estudiante
    estudiantes = sorted(df_modelo['Nombre Completo'].unique())
    estudiante_seleccionado = st.selectbox(
        "Selecciona un estudiante:",
        estudiantes,
        key='estudiante_sel'
    )

    # Obtener datos del estudiante
    estudiante = df_modelo[df_modelo['Nombre Completo'] == estudiante_seleccionado].iloc[0]

    st.markdown("---")

    # Información básica
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Modelo", estudiante['Modelo'])
    with col2:
        st.metric("Grupo", estudiante['Grupo'])
    with col3:
        st.metric("Puntaje Global", f"{estudiante['Puntaje Global']:.0f}")
    with col4:
        st.metric("Clasificación", estudiante['Clasificación'])

    st.markdown("---")

    # Comparación con promedios
    st.subheader("📊 Comparación con Promedios")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Puntajes por Área")

        # Calcular promedios con manejo de NaN
        promedio_modelo = df_modelo[AREAS].mean().fillna(0).round(0)
        promedio_grupo = df_modelo[df_modelo['Grupo'] == estudiante['Grupo']][AREAS].mean().fillna(0).round(0)

        # Tabla comparativa
        datos_comparacion = []
        for area in AREAS:
            puntaje_est = estudiante[area] if pd.notna(estudiante[area]) else 0
            prom_mod = promedio_modelo[area]
            prom_grp = promedio_grupo[area]

            datos_comparacion.append({
                'Área': area,
                'Estudiante': f"{puntaje_est:.0f}",
                'Prom. Modelo': f"{prom_mod:.0f}",
                'Dif. Modelo': f"{puntaje_est - prom_mod:+.0f}",
                'Prom. Grupo': f"{prom_grp:.0f}",
                'Dif. Grupo': f"{puntaje_est - prom_grp:+.0f}"
            })

        df_comparacion = pd.DataFrame(datos_comparacion)
        st.dataframe(df_comparacion, use_container_width=True, hide_index=True)

    with col2:
        st.markdown("### Perfil de Competencias")
        fig = crear_radar_chart(estudiante, AREAS)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Posición en rankings
    st.subheader("🏆 Posición en Rankings")

    col1, col2, col3 = st.columns(3)

    with col1:
        # Ranking global
        ranking_global = obtener_ranking(df, 'Puntaje Global')
        posicion_global = ranking_global[ranking_global['Nombre Completo'] == estudiante_seleccionado].index[0]
        st.metric("Ranking Global", f"#{posicion_global} de {len(df)}")

    with col2:
        # Ranking en modelo
        ranking_modelo = obtener_ranking(df_modelo, 'Puntaje Global')
        posicion_modelo = ranking_modelo[ranking_modelo['Nombre Completo'] == estudiante_seleccionado].index[0]
        st.metric(f"Ranking en {modelo_seleccionado}", f"#{posicion_modelo} de {len(df_modelo)}")

    with col3:
        # Ranking en grupo
        df_grupo = df_modelo[df_modelo['Grupo'] == estudiante['Grupo']]
        ranking_grupo = obtener_ranking(df_grupo, 'Puntaje Global')
        posicion_grupo = ranking_grupo[ranking_grupo['Nombre Completo'] == estudiante_seleccionado].index[0]
        st.metric(f"Ranking en {estudiante['Grupo']}", f"#{posicion_grupo} de {len(df_grupo)}")

    st.markdown("---")

    # Percentiles
    st.subheader("📈 Percentiles por Área")

    percentiles_data = []
    for area in AREAS:
        percentil = calcular_percentil(df_modelo, area, estudiante[area])
        percentiles_data.append({
            'Área': area,
            'Puntaje': f"{estudiante[area]:.1f}",
            'Percentil': f"{percentil:.1f}%"
        })

    df_percentiles = pd.DataFrame(percentiles_data)

    fig = go.Figure(data=[
        go.Bar(
            x=df_percentiles['Área'],
            y=[float(p.strip('%')) for p in df_percentiles['Percentil']],
            marker_color=[COLORES_AREAS.get(area, '#999999') for area in df_percentiles['Área']],
            text=df_percentiles['Percentil'],
            textposition='outside'
        )
    ])
    fig.update_layout(
        title='Percentiles del Estudiante por Área',
        xaxis_title='Área',
        yaxis_title='Percentil (%)',
        yaxis_range=[0, 105],
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)


def mostrar_analisis_area(df):
    """Pestaña 5: Análisis por Área"""
    st.header("📚 Análisis por Área")

    # Selector de área
    area_seleccionada = st.selectbox(
        "Selecciona un área para análisis detallado:",
        AREAS,
        key='area_analisis'
    )

    st.markdown("---")

    # Estadísticas generales del área
    st.subheader(f"📊 Estadísticas Generales - {area_seleccionada}")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Todos los Estudiantes")
        stats_general = calcular_estadisticas_descriptivas(df, area_seleccionada)
        for key, value in stats_general.items():
            if key == 'Desv. Estándar':
                st.metric(key, f"{value:.2f}")
            else:
                st.metric(key, f"{value:.0f}")

    with col2:
        st.markdown("### Por Modelo")
        stats_modelo = calcular_estadisticas_descriptivas(df, area_seleccionada, 'Modelo')
        st.dataframe(stats_modelo, use_container_width=True)

    with col3:
        st.markdown("### Por Grupo")
        stats_grupo = calcular_estadisticas_descriptivas(df, area_seleccionada, 'Grupo')
        st.dataframe(stats_grupo, use_container_width=True)

    st.markdown("---")

    # Comparación entre modelos
    st.subheader("🔄 Comparación entre Modelos")

    col1, col2 = st.columns(2)

    with col1:
        fig = crear_grafico_comparacion_modelos(df, area_seleccionada)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Test estadístico
        resultado_test = realizar_test_comparacion(
            df,
            area_seleccionada,
            df['Modelo'] == 'Aula Regular',
            df['Modelo'] == 'Modelo Flexible',
            'Aula Regular',
            'Modelo Flexible'
        )

        if resultado_test['valido']:
            st.markdown("### Test Estadístico")
            st.metric("Diferencia de Medias", f"{resultado_test['diferencia_medias']:.0f}")
            st.metric("Valor p", f"{resultado_test['p_value']:.4f}")
            st.metric("¿Significativo?", resultado_test['significativo'])
            st.info(resultado_test['interpretacion'])

    st.markdown("---")

    # Comparación entre todos los grupos
    st.subheader("👥 Comparación entre Todos los Grupos")

    fig = crear_grafico_barras_promedios(
        df,
        [area_seleccionada],
        'Grupo',
        f'Promedio de {area_seleccionada} por Grupo'
    )
    st.plotly_chart(fig, use_container_width=True)

    # Box plot de todos los grupos
    fig = go.Figure()
    for grupo in sorted(df['Grupo'].unique()):
        datos = df[df['Grupo'] == grupo][area_seleccionada].dropna()
        fig.add_trace(go.Box(
            y=datos,
            name=grupo,
            marker_color=COLORES_GRUPOS.get(grupo, '#999999'),
            boxmean='sd'
        ))

    fig.update_layout(
        title=f'Distribución de {area_seleccionada} por Grupo',
        yaxis_title='Puntaje',
        xaxis_title='Grupo',
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Rankings del área
    st.subheader(f"🏆 Top 10 en {area_seleccionada}")

    ranking_area = obtener_ranking(df, area_seleccionada, top_n=10)
    st.dataframe(ranking_area, use_container_width=True)

    # Opción de ver ranking completo
    if st.checkbox(f"Ver ranking completo de {area_seleccionada}", key=f'ranking_completo_{area_seleccionada}'):
        ranking_completo = obtener_ranking(df, area_seleccionada)
        st.dataframe(ranking_completo, use_container_width=True, height=400)

def mostrar_rankings(df):
    """Pestaña 6: Rankings Generales"""
    st.header("🏆 Rankings Generales")

    # Tipo de ranking
    tipo_ranking = st.radio(
        "Selecciona el tipo de ranking:",
        ["Global (Todos)", "Por Modelo", "Por Grupo", "Por Área"],
        horizontal=True,
        key='tipo_ranking'
    )

    st.markdown("---")

    if tipo_ranking == "Global (Todos)":
        st.subheader("🥇 Ranking Global por Puntaje Global")

        ranking = obtener_ranking(df, 'Puntaje Global')

        # Top 10
        st.markdown("### Top 10")
        st.dataframe(ranking.head(10), use_container_width=True)

        # Opción de ver completo
        if st.checkbox("Ver ranking completo", key='ranking_global_completo'):
            st.dataframe(ranking, use_container_width=True, height=400)

        # Gráfico de top 20
        st.markdown("### Visualización Top 20")
        top_20 = ranking.head(20).reset_index()
        fig = go.Figure(data=[
            go.Bar(
                x=top_20['Puntaje Global'],
                y=top_20['Nombre Completo'],
                orientation='h',
                marker_color=[COLORES_MODELOS.get(m, '#999999') for m in top_20['Modelo']],
                text=top_20['Puntaje Global'].round(0).astype(int),
                textposition='outside'
            )
        ])
        fig.update_layout(
            title='Top 20 Estudiantes por Puntaje Global',
            xaxis_title='Puntaje Global',
            yaxis_title='',
            height=600,
            yaxis={'categoryorder': 'total ascending'}
        )
        st.plotly_chart(fig, use_container_width=True)

    elif tipo_ranking == "Por Modelo":
        modelo_seleccionado = st.selectbox(
            "Selecciona el modelo:",
            df['Modelo'].unique(),
            key='modelo_ranking'
        )

        df_modelo = df[df['Modelo'] == modelo_seleccionado]

        st.subheader(f"🥇 Ranking de {modelo_seleccionado}")

        ranking = obtener_ranking(df_modelo, 'Puntaje Global')

        # Top 10
        st.markdown("### Top 10")
        st.dataframe(ranking.head(10), use_container_width=True)

        # Opción de ver completo
        if st.checkbox(f"Ver ranking completo de {modelo_seleccionado}", key='ranking_modelo_completo'):
            st.dataframe(ranking, use_container_width=True, height=400)

    elif tipo_ranking == "Por Grupo":
        grupo_seleccionado = st.selectbox(
            "Selecciona el grupo:",
            sorted(df['Grupo'].unique()),
            key='grupo_ranking'
        )

        df_grupo = df[df['Grupo'] == grupo_seleccionado]

        st.subheader(f"🥇 Ranking del Grupo {grupo_seleccionado}")

        ranking = obtener_ranking(df_grupo, 'Puntaje Global')
        st.dataframe(ranking, use_container_width=True)

    else:  # Por Área
        area_seleccionada = st.selectbox(
            "Selecciona el área:",
            AREAS,
            key='area_ranking'
        )

        st.subheader(f"🥇 Ranking por {area_seleccionada}")

        ranking = obtener_ranking(df, area_seleccionada)

        # Top 10
        st.markdown("### Top 10")
        st.dataframe(ranking.head(10), use_container_width=True)

        # Opción de ver completo
        if st.checkbox(f"Ver ranking completo de {area_seleccionada}", key='ranking_area_completo'):
            st.dataframe(ranking, use_container_width=True, height=400)

def mostrar_analisis_avanzado(df):
    """Pestaña 7: Análisis Estadístico Avanzado"""
    st.header("📈 Análisis Estadístico Avanzado")

    # Selector de modelo para análisis
    modelo_seleccionado = st.selectbox(
        "Selecciona el modelo para análisis:",
        ['Todos'] + list(df['Modelo'].unique()),
        key='modelo_avanzado'
    )

    if modelo_seleccionado != 'Todos':
        df_analisis = df[df['Modelo'] == modelo_seleccionado]
    else:
        df_analisis = df

    st.markdown("---")

    # Correlaciones entre áreas
    st.subheader("🔗 Correlaciones entre Áreas")

    st.info("""
    **Nota:** Las correlaciones muestran la relación entre diferentes áreas.
    Un valor cercano a 1 indica una correlación positiva fuerte,
    mientras que un valor cercano a -1 indica una correlación negativa fuerte.
    """)

    if modelo_seleccionado != 'Todos':
        fig = crear_heatmap_correlaciones(df, modelo_seleccionado)
        st.plotly_chart(fig, use_container_width=True)
    else:
        col1, col2 = st.columns(2)
        with col1:
            if 'Aula Regular' in df['Modelo'].unique():
                fig = crear_heatmap_correlaciones(df, 'Aula Regular')
                st.plotly_chart(fig, use_container_width=True)
        with col2:
            if 'Modelo Flexible' in df['Modelo'].unique():
                fig = crear_heatmap_correlaciones(df, 'Modelo Flexible')
                st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Análisis de percentiles
    st.subheader("📊 Análisis de Percentiles")

    area_percentil = st.selectbox(
        "Selecciona un área:",
        ['Puntaje Global'] + AREAS,
        key='area_percentil'
    )

    # Calcular percentiles
    percentiles = [10, 25, 50, 75, 90]
    valores_percentiles = [np.percentile(df_analisis[area_percentil].dropna(), p) for p in percentiles]

    df_percentiles = pd.DataFrame({
        'Percentil': [f'P{p}' for p in percentiles],
        'Valor': valores_percentiles
    })

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Tabla de Percentiles")
        st.dataframe(df_percentiles, use_container_width=True, hide_index=True)

    with col2:
        st.markdown("### Visualización")
        fig = go.Figure(data=[
            go.Bar(
                x=df_percentiles['Percentil'],
                y=df_percentiles['Valor'],
                marker_color='#3498db',
                text=[f'{v:.1f}' for v in df_percentiles['Valor']],
                textposition='outside'
            )
        ])
        fig.update_layout(
            title=f'Percentiles de {area_percentil}',
            xaxis_title='Percentil',
            yaxis_title='Puntaje',
            height=400
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Segmentación por clasificación
    st.subheader("📋 Segmentación por Clasificación")

    segmentacion = df_analisis.groupby('Clasificación').agg({
        'Nombre Completo': 'count',
        'Puntaje Global': ['mean', 'min', 'max']
    })

    # Redondear con manejo de NaN
    segmentacion = segmentacion.fillna(0).round(0)

    segmentacion.columns = ['Cantidad', 'Promedio', 'Mínimo', 'Máximo']
    segmentacion = segmentacion.reset_index()

    col1, col2 = st.columns(2)

    with col1:
        st.dataframe(segmentacion, use_container_width=True, hide_index=True)

    with col2:
        fig = px.pie(
            segmentacion,
            values='Cantidad',
            names='Clasificación',
            title='Distribución por Clasificación'
        )
        st.plotly_chart(fig, use_container_width=True)


def mostrar_comparacion_temporal(df):
    """Pestaña 8: Comparación Temporal (2024-2025)"""
    st.header("📅 Comparación Temporal 2024-2025")

    st.markdown("""
    <div class="warning-box">
    <strong>⚠️ Advertencia:</strong><br>
    Los datos históricos de comparación 2024-2025 solo están disponibles para el
    <strong>Modelo Aula Regular</strong>. El Modelo Flexible aún no cuenta con datos del año 2024.
    </div>
    """, unsafe_allow_html=True)

    # Cargar datos históricos
    historicos = cargar_datos_historicos()

    if historicos['Aula Regular'] is None:
        st.error("No se pudieron cargar los datos históricos de Aula Regular.")
        return

    datos_hist = historicos['Aula Regular']

    st.markdown("---")

    # Tabla comparativa
    st.subheader("📊 Comparación de Promedios 2024 vs 2025")

    # Crear DataFrame comparativo
    areas_comparacion = AREAS + ['Puntaje Global']
    datos_comparacion = []

    for area in areas_comparacion:
        val_2024 = datos_hist['2024'][area]
        val_2025 = datos_hist['2025'][area]
        avance = datos_hist['Avance'][area]

        # Calcular cambio porcentual con manejo de división por cero
        cambio_pct = (avance / val_2024 * 100) if val_2024 != 0 else 0

        datos_comparacion.append({
            'Área': area,
            '2024': f"{val_2024:.0f}",
            '2025': f"{val_2025:.0f}",
            'Avance': f"{avance:+.0f}",
            'Cambio %': f"{cambio_pct:+.2f}%"
        })

    df_comparacion = pd.DataFrame(datos_comparacion)
    st.dataframe(df_comparacion, use_container_width=True, hide_index=True)

    st.markdown("---")

    # Gráfico de barras comparativo
    st.subheader("📈 Evolución de Promedios por Área")

    fig = go.Figure()

    # Datos 2024
    valores_2024 = []
    for area in AREAS:
        val = datos_hist['2024'][area]
        valores_2024.append(round(val, 0) if pd.notna(val) else 0)

    fig.add_trace(go.Bar(
        name='2024',
        x=AREAS,
        y=valores_2024,
        marker_color='#95a5a6',
        text=[f'{int(v)}' for v in valores_2024],
        textposition='outside'
    ))

    # Datos 2025
    valores_2025 = []
    for area in AREAS:
        val = datos_hist['2025'][area]
        valores_2025.append(round(val, 0) if pd.notna(val) else 0)

    fig.add_trace(go.Bar(
        name='2025',
        x=AREAS,
        y=valores_2025,
        marker_color='#3498db',
        text=[f'{int(v)}' for v in valores_2025],
        textposition='outside'
    ))

    fig.update_layout(
        title='Comparación de Promedios 2024 vs 2025 - Modelo Aula Regular',
        xaxis_title='Área',
        yaxis_title='Promedio',
        barmode='group',
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Gráfico de avances
    st.subheader("📊 Avances y Retrocesos por Área")

    avances = []
    for area in AREAS:
        val = datos_hist['Avance'][area]
        avances.append(round(val, 0) if pd.notna(val) else 0)

    colores_avance = ['#2ecc71' if a > 0 else '#e74c3c' for a in avances]

    fig = go.Figure(data=[
        go.Bar(
            x=AREAS,
            y=avances,
            marker_color=colores_avance,
            text=[f'{int(a):+d}' for a in avances],
            textposition='outside'
        )
    ])

    fig.add_hline(y=0, line_dash="dash", line_color="gray")

    fig.update_layout(
        title='Avances (+) y Retrocesos (-) por Área',
        xaxis_title='Área',
        yaxis_title='Cambio en Promedio',
        height=500
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # Análisis de avances
    st.subheader("📋 Análisis de Avances")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Áreas con Mejora")
        mejoras = [(area, datos_hist['Avance'][area]) for area in AREAS if datos_hist['Avance'][area] > 0]
        if mejoras:
            for area, avance in sorted(mejoras, key=lambda x: x[1], reverse=True):
                avance_val = round(avance, 0) if pd.notna(avance) else 0
                st.success(f"**{area}:** +{int(avance_val)} puntos")
        else:
            st.info("No hay áreas con mejora")

    with col2:
        st.markdown("### Áreas con Retroceso")
        retrocesos = [(area, datos_hist['Avance'][area]) for area in AREAS if datos_hist['Avance'][area] < 0]
        if retrocesos:
            for area, avance in sorted(retrocesos, key=lambda x: x[1]):
                avance_val = round(avance, 0) if pd.notna(avance) else 0
                st.error(f"**{area}:** {int(avance_val)} puntos")
        else:
            st.info("No hay áreas con retroceso")

    # Resumen general
    st.markdown("---")
    st.subheader("📌 Resumen General")

    avance_global_val = datos_hist['Avance']['Puntaje Global']
    avance_global = round(avance_global_val, 0) if pd.notna(avance_global_val) else 0

    if avance_global > 0:
        st.success(f"""
        **Resultado General:** El Modelo Aula Regular muestra una **mejora** en el puntaje global
        de **+{int(avance_global)} puntos** respecto al año 2024.
        """)
    elif avance_global < 0:
        st.error(f"""
        **Resultado General:** El Modelo Aula Regular muestra un **retroceso** en el puntaje global
        de **{int(avance_global)} puntos** respecto al año 2024.
        """)
    else:
        st.info("""
        **Resultado General:** El Modelo Aula Regular mantiene el mismo puntaje global
        respecto al año 2024.
        """)

# ============================================================================
# PUNTO DE ENTRADA DE LA APLICACIÓN
# ============================================================================

if __name__ == "__main__":
    main()


