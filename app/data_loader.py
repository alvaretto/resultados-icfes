"""
Carga de datos, constantes y validación.
Fuente de verdad para todos los datos históricos y oficiales.
"""

import streamlit as st
import pandas as pd
from .logger import get_logger

logger = get_logger(__name__)

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

# Datos de instituciones educativas de La Tebaida (fuente: análisis municipal 2024-2025)
DATOS_INSTITUCIONES_TEBAIDA = {
    'ANTONIO NARIÑO': {'2024': 253, '2025': 283},
    'LUIS ARANGO CARDONA': {'2024': 285, '2025': 277},
    'GABRIELA MISTRAL': {'2024': 241, '2025': 268},
    'LA POPA': {'2024': 254, '2025': 264},
    'SANTA TERESITA': {'2024': 265, '2025': 262},
    'INSTITUTO TEBAIDA': {'2024': 252, '2025': 252},
    'PEDACITO DE CIELO (Aula Regular - Jornada 1)': {'2024': 240, '2025': 234},
    'PEDACITO DE CIELO (Modelo Flexible - Jornada 0)': {'2024': 203, '2025': 214},
    'PEDACITO DE CIELO (Institucional)': {'2024': 219, '2025': 221},
}

# Datos Oficiales 2025 (Fuente: PDF resultados agregados - 95 estudiantes)
DATOS_OFICIALES_2025 = {
    'Todos': {
        'puntaje_global': 221,
        'desv_global': 44,
        'areas': {
            'Lectura Crítica': {'promedio': 48, 'desviacion': 10},
            'Matemáticas': {'promedio': 44, 'desviacion': 11},
            'Sociales y Ciudadanas': {'promedio': 41, 'desviacion': 11},
            'Ciencias Naturales': {'promedio': 43, 'desviacion': 9},
            'Inglés': {'promedio': 45, 'desviacion': 10}
        }
    },
    'Aula Regular (Jornada 1)': {
        'puntaje_global': 234,
        'desv_global': 44,
        'areas': {
            'Lectura Crítica': {'promedio': 51, 'desviacion': 10},
            'Matemáticas': {'promedio': 47, 'desviacion': 10},
            'Sociales y Ciudadanas': {'promedio': 44, 'desviacion': 12},
            'Ciencias Naturales': {'promedio': 44, 'desviacion': 8},
            'Inglés': {'promedio': 46, 'desviacion': 9}
        }
    },
    'Modelo Flexible (Jornada 0)': {
        'puntaje_global': 214,
        'desv_global': 43,
        'areas': {
            'Lectura Crítica': {'promedio': 47, 'desviacion': 10},
            'Matemáticas': {'promedio': 42, 'desviacion': 11},
            'Sociales y Ciudadanas': {'promedio': 39, 'desviacion': 10},
            'Ciencias Naturales': {'promedio': 42, 'desviacion': 9},
            'Inglés': {'promedio': 44, 'desviacion': 10}
        }
    }
}

PROMEDIOS_REFERENCIA = {
    'PROMEDIO TEBAIDA': {'2024': 249, '2025': 257},
    'PROMEDIO QUINDÍO': {'2024': 263, '2025': 264},
    'PROMEDIO COLOMBIA': {'2024': 260, '2025': 261},
}

# ============================================================================
# FUNCIONES DE CARGA
# ============================================================================

@st.cache_data
def cargar_datos_2024():
    """Carga los datos consolidados de 2024 desde archivos MD"""

    datos_regular_2024 = {
        'modelo': 'Aula Regular (Jornada 1)',
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

    datos_flexible_2024 = {
        'modelo': 'Modelo Flexible (Jornada 0)',
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
        'Aula Regular (Jornada 1)': datos_regular_2024,
        'Modelo Flexible (Jornada 0)': datos_flexible_2024,
        'Institucional': datos_institucional_2024
    }


@st.cache_data
def cargar_datos_2025():
    """Carga los datos de 2025 desde archivos Excel"""

    try:
        df_regular = pd.read_excel('data/RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx')
        df_regular = df_regular[df_regular['Grupo'].notna()].copy()

        df_flexible = pd.read_excel('data/RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx')
        df_flexible = df_flexible[df_flexible['Grupo'].notna()].copy()

        df_regular['Modelo'] = 'Aula Regular (Jornada 1)'
        df_flexible['Modelo'] = 'Modelo Flexible (Jornada 0)'

        df_todos = pd.concat([df_regular, df_flexible], ignore_index=True)

        # Validar columnas esperadas
        COLUMNAS_REQUERIDAS = ['Grupo', 'Puntaje Global'] + AREAS
        for col in COLUMNAS_REQUERIDAS:
            if col not in df_regular.columns:
                logger.warning("Columna faltante en Aula Regular: %s", col)
            if col not in df_flexible.columns:
                logger.warning("Columna faltante en Modelo Flexible: %s", col)

        # Validar rangos de puntajes
        for area in AREAS:
            if area in df_todos.columns:
                fuera_rango = df_todos[(df_todos[area] < 0) | (df_todos[area] > 100)]
                if len(fuera_rango) > 0:
                    logger.warning("%d puntajes fuera de rango en %s", len(fuera_rango), area)

        logger.info("Datos 2025 cargados: %d regular, %d flexible, %d total",
                     len(df_regular), len(df_flexible), len(df_todos))

        return {
            'df_regular': df_regular,
            'df_flexible': df_flexible,
            'df_todos': df_todos
        }
    except Exception as e:
        logger.error("Error al cargar datos 2025: %s", e)
        st.error(f"Error al cargar datos 2025: {e}")
        return None
