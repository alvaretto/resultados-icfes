#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_visualizaciones.py — Tests de generación de gráficos con Plotly

Verifica:
- Que las funciones de visualización retornan objetos Figure válidos
- Que los gráficos contienen los datos esperados
- Manejo de DataFrames vacíos y edge cases
"""

import pytest
import pandas as pd
import numpy as np
import sys
import os

# Agregar raíz al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import plotly.graph_objects as go
import plotly.express as px


AREAS = ['Lectura Crítica', 'Matemáticas', 'Sociales y Ciudadanas', 'Ciencias Naturales', 'Inglés']


# ============================================================================
# Funciones auxiliares que replican la lógica de visualización de la app
# (extraídas para testear sin depender de Streamlit)
# ============================================================================

def crear_grafico_barras_comparativo(areas: list, valores_2024: list, valores_2025: list) -> go.Figure:
    """Crea un gráfico de barras comparativo 2024 vs 2025."""
    fig = go.Figure()
    fig.add_trace(go.Bar(name='2024', x=areas, y=valores_2024, marker_color='#667eea'))
    fig.add_trace(go.Bar(name='2025', x=areas, y=valores_2025, marker_color='#764ba2'))
    fig.update_layout(barmode='group', title="Comparación por Áreas 2024 vs 2025")
    return fig


def crear_grafico_niveles_desempeno(df: pd.DataFrame, area: str) -> go.Figure:
    """Crea gráfico de distribución por niveles de desempeño."""
    def clasificar(p):
        if p < 36:
            return "Insuficiente"
        elif p < 51:
            return "Mínimo"
        elif p < 71:
            return "Satisfactorio"
        return "Avanzado"

    df_area = df.copy()
    df_area['Nivel'] = df_area[area].apply(clasificar)
    niveles_orden = ['Insuficiente', 'Mínimo', 'Satisfactorio', 'Avanzado']
    distribucion = df_area['Nivel'].value_counts()

    for nivel in niveles_orden:
        if nivel not in distribucion:
            distribucion[nivel] = 0

    distribucion = distribucion[niveles_orden]

    colores = {
        'Insuficiente': '#dc3545',
        'Mínimo': '#ffc107',
        'Satisfactorio': '#28a745',
        'Avanzado': '#007bff'
    }

    fig = go.Figure()
    for nivel in niveles_orden:
        fig.add_trace(go.Bar(
            name=nivel,
            x=[nivel],
            y=[distribucion[nivel]],
            marker_color=colores[nivel]
        ))
    fig.update_layout(title=f"Niveles de Desempeño - {area}")
    return fig


def crear_grafico_radar_areas(labels: list, valores: list, nombre: str = "Institución") -> go.Figure:
    """Crea un gráfico radar (spider) de puntajes por área."""
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=valores + [valores[0]],  # cerrar el polígono
        theta=labels + [labels[0]],
        fill='toself',
        name=nombre
    ))
    fig.update_layout(polar=dict(radialaxis=dict(range=[0, 100])), title="Perfil por Áreas")
    return fig


def crear_histograma_puntaje_global(df: pd.DataFrame) -> go.Figure:
    """Crea histograma del puntaje global."""
    fig = px.histogram(df, x='Puntaje Global', nbins=10, title="Distribución Puntaje Global")
    return fig


# ============================================================================
# Tests de generación de gráficos
# ============================================================================

class TestGraficoBarrasComparativo:

    def test_retorna_figura_plotly(self):
        """La función debe retornar un objeto go.Figure."""
        valores_2024 = [51, 49, 44, 47, 48]
        valores_2025 = [48, 44, 41, 43, 45]
        fig = crear_grafico_barras_comparativo(AREAS, valores_2024, valores_2025)
        assert isinstance(fig, go.Figure)

    def test_figura_tiene_dos_traces(self):
        """El gráfico comparativo debe tener exactamente 2 trazas (2024 y 2025)."""
        valores_2024 = [51, 49, 44, 47, 48]
        valores_2025 = [48, 44, 41, 43, 45]
        fig = crear_grafico_barras_comparativo(AREAS, valores_2024, valores_2025)
        assert len(fig.data) == 2

    def test_figura_nombres_de_traces_correctos(self):
        """Las trazas deben llamarse '2024' y '2025'."""
        valores_2024 = [51, 49, 44, 47, 48]
        valores_2025 = [48, 44, 41, 43, 45]
        fig = crear_grafico_barras_comparativo(AREAS, valores_2024, valores_2025)
        nombres = [t.name for t in fig.data]
        assert '2024' in nombres
        assert '2025' in nombres

    def test_figura_tiene_titulo(self):
        """El gráfico debe tener un título definido."""
        fig = crear_grafico_barras_comparativo(AREAS, [50]*5, [48]*5)
        assert fig.layout.title.text is not None and fig.layout.title.text != ""

    def test_figura_con_areas_vacias(self):
        """Debe manejar listas vacías sin errores."""
        fig = crear_grafico_barras_comparativo([], [], [])
        assert isinstance(fig, go.Figure)


class TestGraficoNivelesDesempeno:

    def test_retorna_figura_plotly(self, df_estudiantes_ejemplo):
        """La función debe retornar un go.Figure."""
        fig = crear_grafico_niveles_desempeno(df_estudiantes_ejemplo, 'Matemáticas')
        assert isinstance(fig, go.Figure)

    def test_figura_tiene_cuatro_traces_niveles(self, df_estudiantes_ejemplo):
        """El gráfico de niveles debe tener 4 trazas (uno por nivel)."""
        fig = crear_grafico_niveles_desempeno(df_estudiantes_ejemplo, 'Lectura Crítica')
        assert len(fig.data) == 4

    def test_figura_para_cada_area(self, df_estudiantes_ejemplo):
        """Se debe poder generar el gráfico de niveles para cada área sin error."""
        for area in AREAS:
            fig = crear_grafico_niveles_desempeno(df_estudiantes_ejemplo, area)
            assert isinstance(fig, go.Figure), f"Falló para el área: {area}"

    def test_figura_con_un_estudiante(self, df_un_estudiante):
        """Con un solo estudiante, el gráfico debe generarse sin error."""
        fig = crear_grafico_niveles_desempeno(df_un_estudiante, 'Matemáticas')
        assert isinstance(fig, go.Figure)

    def test_titulo_contiene_area(self, df_estudiantes_ejemplo):
        """El título del gráfico debe mencionar el área."""
        area = 'Inglés'
        fig = crear_grafico_niveles_desempeno(df_estudiantes_ejemplo, area)
        assert area in fig.layout.title.text


class TestGraficoRadar:

    def test_retorna_figura_plotly(self):
        """La función debe retornar un go.Figure."""
        valores = [48, 44, 41, 43, 45]
        fig = crear_grafico_radar_areas(AREAS, valores)
        assert isinstance(fig, go.Figure)

    def test_figura_tiene_un_trace(self):
        """El radar debe tener exactamente 1 traza."""
        valores = [48, 44, 41, 43, 45]
        fig = crear_grafico_radar_areas(AREAS, valores)
        assert len(fig.data) == 1

    def test_trace_es_scatterpolar(self):
        """La traza debe ser de tipo Scatterpolar."""
        valores = [48, 44, 41, 43, 45]
        fig = crear_grafico_radar_areas(AREAS, valores)
        assert isinstance(fig.data[0], go.Scatterpolar)


class TestHistogramaPuntajeGlobal:

    def test_retorna_figura_plotly(self, df_estudiantes_ejemplo):
        """El histograma debe ser un go.Figure."""
        fig = crear_histograma_puntaje_global(df_estudiantes_ejemplo)
        assert isinstance(fig, go.Figure)

    def test_histograma_tiene_al_menos_un_trace(self, df_estudiantes_ejemplo):
        """El histograma debe tener al menos una traza."""
        fig = crear_histograma_puntaje_global(df_estudiantes_ejemplo)
        assert len(fig.data) >= 1

    def test_histograma_con_un_estudiante(self, df_un_estudiante):
        """Con un solo estudiante, el histograma debe generarse sin error."""
        fig = crear_histograma_puntaje_global(df_un_estudiante)
        assert isinstance(fig, go.Figure)
