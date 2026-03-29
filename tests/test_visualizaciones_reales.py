#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_visualizaciones_reales.py — Tests de funciones reales de app/visualizaciones.py

Verifica que las funciones de visualización retornan objetos go.Figure válidos
importando directamente desde el módulo de la aplicación.
"""

import pytest
import pandas as pd
import plotly.graph_objects as go
from app.visualizaciones import (
    crear_grafico_comparativo_areas,
    crear_grafico_avances,
)
from app.data_loader import AREAS


# ============================================================================
# Datos de prueba
# ============================================================================

DATOS_2024 = {
    'areas': {
        'Lectura Crítica': {'promedio': 51, 'desviacion': 9},
        'Matemáticas': {'promedio': 49, 'desviacion': 10},
        'Sociales y Ciudadanas': {'promedio': 44, 'desviacion': 11},
        'Ciencias Naturales': {'promedio': 47, 'desviacion': 8},
        'Inglés': {'promedio': 48, 'desviacion': 10},
    }
}

DATOS_2025 = {
    'areas': {
        'Lectura Crítica': {'promedio': 48, 'desviacion': 10},
        'Matemáticas': {'promedio': 44, 'desviacion': 11},
        'Sociales y Ciudadanas': {'promedio': 41, 'desviacion': 11},
        'Ciencias Naturales': {'promedio': 43, 'desviacion': 9},
        'Inglés': {'promedio': 45, 'desviacion': 10},
    }
}


# ============================================================================
# Tests de crear_grafico_comparativo_areas
# ============================================================================

def test_grafico_comparativo_retorna_figure():
    """crear_grafico_comparativo_areas debe retornar un go.Figure."""
    fig = crear_grafico_comparativo_areas(DATOS_2024, DATOS_2025, "Test Comparativo")
    assert isinstance(fig, go.Figure)


def test_grafico_comparativo_tiene_dos_traces():
    """El comparativo 2024 vs 2025 debe tener 2 trazas."""
    fig = crear_grafico_comparativo_areas(DATOS_2024, DATOS_2025, "Comparativo")
    assert len(fig.data) == 2


def test_grafico_comparativo_traces_nombrados():
    """Las trazas deben llamarse '2024' y '2025'."""
    fig = crear_grafico_comparativo_areas(DATOS_2024, DATOS_2025, "Comparativo")
    nombres = [t.name for t in fig.data]
    assert '2024' in nombres
    assert '2025' in nombres


def test_grafico_comparativo_tiene_titulo():
    """El título debe ser el que se pasa como argumento."""
    titulo = "Mi título de prueba"
    fig = crear_grafico_comparativo_areas(DATOS_2024, DATOS_2025, titulo)
    assert titulo in fig.layout.title.text


# ============================================================================
# Tests de crear_grafico_avances
# ============================================================================

def test_grafico_avances_retorna_figure():
    """crear_grafico_avances debe retornar un go.Figure."""
    fig = crear_grafico_avances(DATOS_2024, DATOS_2025)
    assert isinstance(fig, go.Figure)


def test_grafico_avances_tiene_un_trace():
    """El gráfico de avances debe tener exactamente 1 traza de barras."""
    fig = crear_grafico_avances(DATOS_2024, DATOS_2025)
    assert len(fig.data) == 1


def test_grafico_avances_tiene_titulo():
    """El gráfico de avances debe tener un título definido."""
    fig = crear_grafico_avances(DATOS_2024, DATOS_2025)
    assert fig.layout.title.text is not None and fig.layout.title.text != ""
