"""
Cálculos estadísticos: promedios, desviaciones, niveles de desempeño, rankings.
"""

import streamlit as st
import pandas as pd
from .data_loader import AREAS, DATOS_OFICIALES_2025

# ============================================================================
# CÁLCULO DE ESTADÍSTICAS
# ============================================================================

@st.cache_data
def calcular_estadisticas_2025(df, modelo='Todos'):
    """Calcula estadísticas para 2025 o retorna valores oficiales si existen"""

    if modelo in DATOS_OFICIALES_2025:
        datos_oficiales = DATOS_OFICIALES_2025[modelo]
        estudiantes = len(df) if df is not None else 0

        stats = {
            'modelo': modelo,
            'estudiantes': estudiantes,
            'puntaje_global': datos_oficiales['puntaje_global'],
            'desv_global': datos_oficiales['desv_global'],
            'areas': {}
        }

        for area in AREAS:
            stats['areas'][area] = {
                'promedio': datos_oficiales['areas'][area]['promedio'],
                'desviacion': datos_oficiales['areas'][area]['desviacion']
            }

        return stats

    if df is None or len(df) == 0:
        return None

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

        if grupo in ['11A', '11B']:
            modelo = 'Aula Regular (Jornada 1)'
        else:
            modelo = 'Modelo Flexible (Jornada 0)'

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
# CÁLCULO DE AVANCES
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
# NIVELES DE DESEMPEÑO
# ============================================================================

def clasificar_nivel_desempeno(puntaje):
    """
    Clasifica el puntaje en uno de los 4 niveles de desempeño según estándares ICFES.
    Niveles: Insuficiente (0-35), Mínimo (36-50), Satisfactorio (51-70), Avanzado (71-100)
    """
    if puntaje < 36:
        return "Insuficiente"
    elif puntaje < 51:
        return "Mínimo"
    elif puntaje < 71:
        return "Satisfactorio"
    else:
        return "Avanzado"


def obtener_interpretacion_nivel(nivel):
    """Retorna la interpretación pedagógica de cada nivel de desempeño"""
    interpretaciones = {
        'Insuficiente': {
            'descripcion': 'El estudiante no supera las preguntas de menor complejidad de la prueba.',
            'recomendacion': 'Requiere refuerzo intensivo en competencias básicas del área.',
            'color': '#dc3545',
            'emoji': '🔴'
        },
        'Mínimo': {
            'descripcion': 'El estudiante supera las preguntas de menor complejidad de la prueba.',
            'recomendacion': 'Necesita fortalecer competencias de nivel intermedio.',
            'color': '#ffc107',
            'emoji': '🟡'
        },
        'Satisfactorio': {
            'descripcion': 'El estudiante supera las preguntas de complejidad media y baja de la prueba.',
            'recomendacion': 'Puede avanzar hacia el desarrollo de competencias avanzadas.',
            'color': '#28a745',
            'emoji': '🟢'
        },
        'Avanzado': {
            'descripcion': 'El estudiante supera las preguntas de mayor complejidad de la prueba.',
            'recomendacion': 'Mantener y profundizar en competencias de nivel superior.',
            'color': '#007bff',
            'emoji': '🔵'
        }
    }
    return interpretaciones.get(nivel, interpretaciones['Mínimo'])


def calcular_distribucion_niveles(df, area):
    """Calcula la distribución de estudiantes por niveles para un área"""
    niveles_orden = ['Insuficiente', 'Mínimo', 'Satisfactorio', 'Avanzado']
    df_temp = df.copy()
    df_temp['Nivel'] = df_temp[area].apply(clasificar_nivel_desempeno)
    distribucion = df_temp['Nivel'].value_counts()
    total = len(df_temp)

    for nivel in niveles_orden:
        if nivel not in distribucion.index:
            distribucion[nivel] = 0

    distribucion = distribucion[niveles_orden]
    porcentajes = (distribucion / total * 100).round(1)
    return distribucion, porcentajes, total
