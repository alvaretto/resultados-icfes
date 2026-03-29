"""
Funciones de visualización con Plotly: barras, radar, comparativos, distribuciones.
"""

import plotly.express as px
import plotly.graph_objects as go
from .data_loader import AREAS
from .estadisticas import calcular_avance, calcular_distribucion_niveles

# ============================================================================
# GRÁFICOS COMPARATIVOS
# ============================================================================

def crear_grafico_comparativo_areas(datos_2024, datos_2025, titulo):
    """Crea gráfico comparativo de áreas entre 2024 y 2025"""

    areas_list = list(AREAS)
    valores_2024 = [datos_2024['areas'][a]['promedio'] for a in areas_list]
    valores_2025 = [datos_2025['areas'][a]['promedio'] for a in areas_list]

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

    areas_list = list(AREAS)
    avances = [calcular_avance(datos_2024['areas'][a]['promedio'], datos_2025['areas'][a]['promedio'])
               for a in areas_list]
    colores = ['#28a745' if a > 0 else '#dc3545' if a < 0 else '#ffc107' for a in avances]

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


def crear_grafico_avances_modelo(df_avances, titulo):
    """Crea gráfico de barras de avances para un modelo educativo"""
    fig = go.Figure(go.Bar(
        x=df_avances['Área'],
        y=df_avances['Avance'],
        marker_color=['#28a745' if a > 0 else '#dc3545' if a < 0 else '#ffc107'
                      for a in df_avances['Avance']],
        text=[f"{a:+d}" for a in df_avances['Avance']],
        textposition='outside',
        name='Avance'
    ))

    fig.update_layout(
        title=titulo,
        xaxis_title="Áreas de Conocimiento",
        yaxis_title="Cambio en Puntos",
        height=400,
        showlegend=False
    )
    fig.add_hline(y=0, line_dash="dash", line_color="gray")
    fig.update_xaxes(tickangle=-45)

    return fig


def crear_grafico_global_evolucion(puntaje_2024, puntaje_2025):
    """Gráfico de evolución del puntaje global institucional"""
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=['2024', '2025'],
        y=[puntaje_2024, puntaje_2025],
        marker_color=['#667eea', '#764ba2'],
        text=[puntaje_2024, puntaje_2025],
        textposition='outside'
    ))
    fig.update_layout(
        title="Puntaje Global Institucional 2024 → 2025",
        yaxis_title="Puntaje Global",
        height=400,
        showlegend=False
    )
    return fig


def crear_grafico_dispersion(desv_2024, desv_2025):
    """Gráfico comparativo de desviaciones estándar"""
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Desviación Estándar',
        x=['2024', '2025'],
        y=[desv_2024, desv_2025],
        marker_color=['#667eea', '#764ba2'],
        text=[f"{desv_2024:.1f}", f"{desv_2025:.1f}"],
        textposition='outside'
    ))
    fig.update_layout(
        title="Desviación Estándar del Puntaje Global",
        yaxis_title="Desviación Estándar",
        height=350,
        showlegend=False
    )
    return fig


# ============================================================================
# GRÁFICOS DE GRUPOS
# ============================================================================

def crear_grafico_grupos(df_grupos):
    """Gráfico de puntaje global por grupo"""
    fig = px.bar(
        df_grupos,
        x='Grupo',
        y='Puntaje Global',
        color='Modelo',
        title="Puntaje Global por Grupo - Año 2025",
        color_discrete_map={'Aula Regular (Jornada 1)': '#667eea', 'Modelo Flexible (Jornada 0)': '#764ba2'},
        text='Puntaje Global'
    )
    fig.update_traces(textposition='outside')
    fig.update_layout(height=400)
    return fig


def crear_grafico_comparacion_modelos_areas(df_comp_modelos):
    """Gráfico de barras agrupadas: avances por área entre modelos"""
    fig = px.bar(
        df_comp_modelos,
        x='Área',
        y='Avance',
        color='Modelo',
        barmode='group',
        title="Comparación de Avances por Área entre Modelos Educativos",
        color_discrete_map={'Aula Regular (Jornada 1)': '#667eea', 'Modelo Flexible (Jornada 0)': '#764ba2'},
        text='Avance'
    )
    fig.update_traces(texttemplate='%{text:+d}', textposition='outside')
    fig.update_layout(height=450)
    fig.add_hline(y=0, line_dash="dash", line_color="gray")
    fig.update_xaxes(tickangle=-45)
    return fig


def crear_grafico_lineas_grupos(df_areas_grupos):
    """Gráfico de líneas para comparar todos los grupos en todas las áreas"""
    fig = px.line(
        df_areas_grupos,
        x='Área',
        y='Puntaje',
        color='Grupo',
        markers=True,
        title="Comparación de Todas las Áreas por Grupo - Año 2025",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_xaxes(tickangle=-45)
    fig.update_layout(height=500)
    return fig


# ============================================================================
# GRÁFICOS DE NIVELES DE DESEMPEÑO
# ============================================================================

COLORES_NIVELES = {
    'Insuficiente': '#dc3545',
    'Mínimo': '#ffc107',
    'Satisfactorio': '#28a745',
    'Avanzado': '#007bff'
}

NIVELES_ORDEN = ['Insuficiente', 'Mínimo', 'Satisfactorio', 'Avanzado']


def crear_grafico_niveles_area(distribucion, porcentajes, area):
    """Gráfico horizontal de barras apiladas para niveles de desempeño de un área"""
    fig = go.Figure()

    for nivel in NIVELES_ORDEN:
        fig.add_trace(go.Bar(
            name=nivel,
            y=['Institución'],
            x=[distribucion[nivel]],
            orientation='h',
            marker_color=COLORES_NIVELES[nivel],
            text=f"{distribucion[nivel]} ({porcentajes[nivel]}%)",
            textposition='inside',
            hovertemplate=f"<b>{nivel}</b><br>Estudiantes: {distribucion[nivel]}<br>Porcentaje: {porcentajes[nivel]}%<extra></extra>"
        ))

    fig.update_layout(
        title=f"Distribución por Niveles de Desempeño - {area}",
        xaxis_title="Número de Estudiantes",
        barmode='stack',
        height=200,
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    return fig


def crear_grafico_niveles_todas_areas(df):
    """Gráfico de barras apiladas para todas las áreas"""
    fig = go.Figure()

    for nivel in NIVELES_ORDEN:
        valores = []
        for area in AREAS:
            distribucion, _, _ = calcular_distribucion_niveles(df, area)
            valores.append(distribucion[nivel])

        fig.add_trace(go.Bar(
            name=nivel,
            x=list(AREAS),
            y=valores,
            marker_color=COLORES_NIVELES[nivel]
        ))

    fig.update_layout(
        title="Distribución de Estudiantes por Nivel en Cada Área",
        xaxis_title="Área de Conocimiento",
        yaxis_title="Número de Estudiantes",
        barmode='stack',
        height=500,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )

    return fig


# ============================================================================
# GRÁFICOS MUNICIPALES
# ============================================================================

def crear_grafico_ranking_municipal(instituciones, puntajes_2024, puntajes_2025,
                                    promedio_tebaida, promedio_colombia):
    """Gráfico comparativo de puntajes de todas las instituciones del municipio"""
    fig = go.Figure()
    fig.add_trace(go.Bar(name='2024', x=instituciones, y=puntajes_2024, marker_color='#636EFA'))
    fig.add_trace(go.Bar(name='2025', x=instituciones, y=puntajes_2025, marker_color='#00CC96'))

    fig.add_hline(y=promedio_tebaida, line_dash="dash",
                  line_color="orange", annotation_text="Promedio Tebaida 2025")
    fig.add_hline(y=promedio_colombia, line_dash="dash",
                  line_color="red", annotation_text="Promedio Colombia 2025")

    fig.update_layout(
        title="Puntaje Global por Institución Educativa",
        xaxis_title="Institución",
        yaxis_title="Puntaje Global",
        barmode='group',
        height=500,
        xaxis_tickangle=-45
    )
    return fig


def crear_grafico_avances_municipio(df_avance):
    """Gráfico de avances de instituciones del municipio"""
    colores = ['green' if a > 0 else ('red' if a < 0 else 'gray') for a in df_avance['Avance']]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_avance['Institución'],
        y=df_avance['Avance'],
        marker_color=colores,
        text=df_avance['Avance'].apply(lambda x: f"+{x}" if x > 0 else str(x)),
        textposition='outside'
    ))

    fig.update_layout(
        title="Avance en Puntaje Global 2024 → 2025",
        xaxis_title="Institución",
        yaxis_title="Puntos de Avance",
        height=450,
        xaxis_tickangle=-45
    )
    fig.add_hline(y=0, line_color="black", line_width=2)

    return fig


def crear_grafico_posicion_relativa(instituciones_7, puntajes_7, promedio_tebaida, promedio_colombia):
    """Gráfico de posición relativa de Pedacito de Cielo entre 7 instituciones"""
    colores_7 = ['lightblue'] * 6 + ['#FF6B6B']

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=instituciones_7,
        y=puntajes_7,
        marker_color=colores_7,
        text=puntajes_7,
        textposition='outside'
    ))

    fig.add_hline(y=promedio_tebaida, line_dash="dash", line_color="orange",
                  annotation_text="Promedio Tebaida")
    fig.add_hline(y=promedio_colombia, line_dash="dash", line_color="red",
                  annotation_text="Promedio Colombia")

    fig.update_layout(
        title="Comparativo 2025: 7 Instituciones de La Tebaida",
        xaxis_title="Institución",
        yaxis_title="Puntaje Global",
        height=500,
        xaxis_tickangle=-45,
        showlegend=False
    )

    return fig
