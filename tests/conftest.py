#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
conftest.py — Fixtures compartidos para la suite de tests ICFES

Provee DataFrames de ejemplo, mocks de APIs externas y datos de referencia.
Los tests deben funcionar sin .env.local ni API keys reales.
"""

import sys
import unittest.mock as mock

# Mockear streamlit ANTES de cualquier import de app/*
# Esto permite testear funciones decoradas con @st.cache_data sin Streamlit real
_mock_st = mock.MagicMock()
_mock_st.cache_data = lambda func: func
_mock_st.cache_resource = lambda func: func
sys.modules.setdefault('streamlit', _mock_st)

import pytest
import pandas as pd
import numpy as np
from unittest.mock import MagicMock


# ============================================================================
# CONSTANTES DE PRUEBA
# ============================================================================

AREAS = ['Lectura Crítica', 'Matemáticas', 'Sociales y Ciudadanas', 'Ciencias Naturales', 'Inglés']

COLUMNAS_EXCEL = [
    'Grupo', 'Primer Apellido', 'Segundo Apellido', 'Primer Nombre', 'Segundo Nombre',
    'Tipo documento', 'Número de documento',
    'Lectura Crítica', 'Matemáticas', 'Sociales y Ciudadanas', 'Ciencias Naturales', 'Inglés',
    'Puntaje Global'
]


# ============================================================================
# FIXTURES — DataFrames de ejemplo
# ============================================================================

@pytest.fixture
def df_estudiantes_ejemplo():
    """
    DataFrame con 10 estudiantes representativos de todos los niveles de desempeño.
    Cubre: Insuficiente (0-35), Mínimo (36-50), Satisfactorio (51-70), Avanzado (71-100).
    """
    datos = {
        'Grupo': ['11A', '11A', '11A', '11A', '11B', '11B', '11B', 'Media Flexible', 'Media Flexible', 'Media Flexible'],
        'Primer Apellido': ['García', 'López', 'Martínez', 'Rodríguez', 'González', 'Hernández', 'Díaz', 'Torres', 'Ramírez', 'Flores'],
        'Segundo Apellido': ['Pérez', 'Gómez', 'Ruiz', 'Jiménez', 'Morales', 'Álvarez', 'Romero', 'Alonso', 'Navarro', 'Molina'],
        'Primer Nombre': ['Ana', 'Carlos', 'Luis', 'María', 'José', 'Elena', 'Pedro', 'Rosa', 'Juan', 'Carmen'],
        'Segundo Nombre': ['Isabel', 'Eduardo', 'Miguel', 'Fernanda', 'Andrés', 'Patricia', 'Alberto', 'Cecilia', 'Daniel', 'Sofía'],
        'Tipo documento': ['RC'] * 10,
        'Número de documento': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
        # Puntajes que cubren todos los niveles de desempeño por área
        'Lectura Crítica':       [72.0, 55.0, 48.0, 30.0, 65.0, 42.0, 58.0, 35.0, 80.0, 20.0],
        'Matemáticas':           [68.0, 52.0, 45.0, 28.0, 71.0, 38.0, 55.0, 32.0, 75.0, 18.0],
        'Sociales y Ciudadanas': [60.0, 48.0, 40.0, 33.0, 62.0, 36.0, 52.0, 30.0, 70.0, 22.0],
        'Ciencias Naturales':    [65.0, 50.0, 42.0, 25.0, 68.0, 40.0, 54.0, 28.0, 72.0, 15.0],
        'Inglés':                [58.0, 44.0, 38.0, 20.0, 60.0, 35.0, 50.0, 25.0, 65.0, 10.0],
    }
    df = pd.DataFrame(datos)
    # Calcular Puntaje Global como suma de las 5 áreas
    df['Puntaje Global'] = df[AREAS].sum(axis=1)
    return df


@pytest.fixture
def df_estudiantes_con_modelo(df_estudiantes_ejemplo):
    """DataFrame con columna 'Modelo' agregada, como en la app real."""
    df = df_estudiantes_ejemplo.copy()
    df['Modelo'] = df['Grupo'].apply(
        lambda g: 'Aula Regular (Jornada 1)' if g in ['11A', '11B'] else 'Modelo Flexible (Jornada 0)'
    )
    return df


@pytest.fixture
def df_un_estudiante():
    """DataFrame con un único estudiante (edge case)."""
    return pd.DataFrame({
        'Grupo': ['11A'],
        'Primer Apellido': ['Solo'],
        'Segundo Apellido': ['Uno'],
        'Primer Nombre': ['Estudiante'],
        'Segundo Nombre': ['Unico'],
        'Tipo documento': ['RC'],
        'Número de documento': [9999],
        'Lectura Crítica': [55.0],
        'Matemáticas': [60.0],
        'Sociales y Ciudadanas': [50.0],
        'Ciencias Naturales': [45.0],
        'Inglés': [40.0],
        'Puntaje Global': [250.0],
    })


@pytest.fixture
def df_vacio():
    """DataFrame vacío con columnas correctas (edge case)."""
    return pd.DataFrame(columns=COLUMNAS_EXCEL)


@pytest.fixture
def df_con_nulos():
    """DataFrame con valores nulos en algunas áreas."""
    datos = {
        'Grupo': ['11A', '11A', '11B'],
        'Primer Apellido': ['Test1', 'Test2', 'Test3'],
        'Segundo Apellido': ['A', 'B', 'C'],
        'Primer Nombre': ['X', 'Y', 'Z'],
        'Segundo Nombre': ['', '', ''],
        'Tipo documento': ['RC', 'RC', 'RC'],
        'Número de documento': [101, 102, 103],
        'Lectura Crítica': [50.0, None, 60.0],
        'Matemáticas': [45.0, 40.0, None],
        'Sociales y Ciudadanas': [None, 38.0, 52.0],
        'Ciencias Naturales': [42.0, 35.0, 48.0],
        'Inglés': [38.0, None, 44.0],
        'Puntaje Global': [None, None, None],
    }
    return pd.DataFrame(datos)


@pytest.fixture
def df_todos_ceros():
    """DataFrame con puntajes en 0 (edge case extremo)."""
    datos = {
        'Grupo': ['11A'] * 3,
        'Primer Apellido': ['A', 'B', 'C'],
        'Segundo Apellido': ['X', 'Y', 'Z'],
        'Primer Nombre': ['P', 'Q', 'R'],
        'Segundo Nombre': ['', '', ''],
        'Tipo documento': ['RC'] * 3,
        'Número de documento': [1, 2, 3],
        'Lectura Crítica': [0.0, 0.0, 0.0],
        'Matemáticas': [0.0, 0.0, 0.0],
        'Sociales y Ciudadanas': [0.0, 0.0, 0.0],
        'Ciencias Naturales': [0.0, 0.0, 0.0],
        'Inglés': [0.0, 0.0, 0.0],
        'Puntaje Global': [0.0, 0.0, 0.0],
    }
    return pd.DataFrame(datos)


# ============================================================================
# FIXTURES — Datos oficiales de referencia (2024 y 2025)
# ============================================================================

@pytest.fixture
def datos_2024_referencia():
    """Datos oficiales 2024 para comparaciones."""
    return {
        'Aula Regular (Jornada 1)': {
            'modelo': 'Aula Regular (Jornada 1)',
            'estudiantes': 50,
            'puntaje_global': 240,
            'desv_global': 41,
            'areas': {
                'Lectura Crítica': {'promedio': 51, 'desviacion': 9},
                'Matemáticas': {'promedio': 49, 'desviacion': 10},
                'Sociales y Ciudadanas': {'promedio': 44, 'desviacion': 11},
                'Ciencias Naturales': {'promedio': 47, 'desviacion': 8},
                'Inglés': {'promedio': 48, 'desviacion': 10},
            }
        },
        'Modelo Flexible (Jornada 0)': {
            'modelo': 'Modelo Flexible (Jornada 0)',
            'estudiantes': 66,
            'puntaje_global': 203,
            'desv_global': 36,
            'areas': {
                'Lectura Crítica': {'promedio': 45, 'desviacion': 9},
                'Matemáticas': {'promedio': 41, 'desviacion': 11},
                'Sociales y Ciudadanas': {'promedio': 38, 'desviacion': 9},
                'Ciencias Naturales': {'promedio': 39, 'desviacion': 7},
                'Inglés': {'promedio': 41, 'desviacion': 9},
            }
        },
        'Institucional': {
            'modelo': 'Institucional',
            'estudiantes': 116,
            'puntaje_global': 219,
            'desv_global': 42,
            'areas': {
                'Lectura Crítica': {'promedio': 48, 'desviacion': 9},
                'Matemáticas': {'promedio': 44, 'desviacion': 11},
                'Sociales y Ciudadanas': {'promedio': 41, 'desviacion': 10},
                'Ciencias Naturales': {'promedio': 43, 'desviacion': 8},
                'Inglés': {'promedio': 44, 'desviacion': 10},
            }
        }
    }


@pytest.fixture
def datos_oficiales_2025():
    """Datos oficiales 2025 según el PDF del ICFES."""
    return {
        'Todos': {
            'puntaje_global': 221,
            'desv_global': 44,
            'areas': {
                'Lectura Crítica': {'promedio': 48, 'desviacion': 10},
                'Matemáticas': {'promedio': 44, 'desviacion': 11},
                'Sociales y Ciudadanas': {'promedio': 41, 'desviacion': 11},
                'Ciencias Naturales': {'promedio': 43, 'desviacion': 9},
                'Inglés': {'promedio': 45, 'desviacion': 10},
            }
        }
    }


# ============================================================================
# FIXTURES — Mocks de APIs externas
# ============================================================================

@pytest.fixture
def mock_anthropic_response():
    """Mock de respuesta exitosa de Anthropic API."""
    mock_message = MagicMock()
    mock_message.content = [MagicMock(text="Respuesta de ejemplo del asistente IA.")]
    mock_message.stop_reason = "end_turn"
    mock_message.usage.input_tokens = 100
    mock_message.usage.output_tokens = 50
    return mock_message


@pytest.fixture
def mock_anthropic_client(mock_anthropic_response):
    """Mock del cliente Anthropic completo."""
    client = MagicMock()
    client.messages.create.return_value = mock_anthropic_response
    return client


@pytest.fixture
def mock_groq_response():
    """Mock de respuesta exitosa de Groq API."""
    mock_choice = MagicMock()
    mock_choice.message.content = "Respuesta de ejemplo del asistente Groq."
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    return mock_response


@pytest.fixture
def mock_brave_search_exitoso():
    """Mock de respuesta exitosa de Brave Search API."""
    return {
        "exito": True,
        "query_usada": "cartillas ICFES Colombia",
        "total_resultados": 2,
        "resultados": [
            {
                "titulo": "Evaluar para Avanzar - ICFES",
                "url": "https://icfes.gov.co/evaluar-para-avanzar",
                "descripcion": "Recursos pedagógicos oficiales del ICFES.",
                "extra_snippets": ["Material oficial para docentes"],
                "es_dominio_educativo": True,
            },
            {
                "titulo": "Colombia Aprende - Recursos",
                "url": "https://colombiaaprende.edu.co/recursos",
                "descripcion": "Portal educativo nacional.",
                "extra_snippets": [],
                "es_dominio_educativo": True,
            }
        ]
    }


@pytest.fixture
def mock_brave_search_fallido():
    """Mock de respuesta fallida de Brave Search API."""
    return {
        "exito": False,
        "error": "API key de Brave Search no configurada.",
        "resultados": []
    }


@pytest.fixture
def mock_brave_sin_resultados():
    """Mock de Brave Search exitoso pero sin resultados."""
    return {
        "exito": True,
        "query_usada": "query sin resultados",
        "total_resultados": 0,
        "resultados": []
    }
