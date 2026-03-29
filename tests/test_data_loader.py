#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_data_loader.py — Tests de carga de datos, constantes y estructura

Verifica:
- Constantes AREAS y DATOS_OFICIALES_2025
- Estructura y contenido de cargar_datos_2024()
- Rangos de puntajes válidos
"""

import pytest

from app.data_loader import AREAS, DATOS_OFICIALES_2025, cargar_datos_2024


# ============================================================================
# Tests de constantes
# ============================================================================

def test_constantes_areas():
    """AREAS debe tener exactamente 5 elementos."""
    assert len(AREAS) == 5
    areas_esperadas = {
        'Lectura Crítica', 'Matemáticas', 'Sociales y Ciudadanas',
        'Ciencias Naturales', 'Inglés'
    }
    assert set(AREAS) == areas_esperadas


# ============================================================================
# Tests de cargar_datos_2024
# ============================================================================

def test_cargar_datos_2024_estructura():
    """cargar_datos_2024 debe retornar un dict con exactamente 3 modelos."""
    datos = cargar_datos_2024()
    assert isinstance(datos, dict)
    assert len(datos) == 3
    modelos_esperados = {
        'Aula Regular (Jornada 1)',
        'Modelo Flexible (Jornada 0)',
        'Institucional'
    }
    assert set(datos.keys()) == modelos_esperados


def test_cargar_datos_2024_areas_completas():
    """Cada modelo en 2024 debe tener las 5 áreas."""
    datos = cargar_datos_2024()
    for modelo, info in datos.items():
        assert 'areas' in info, f"Modelo '{modelo}' no tiene clave 'areas'"
        for area in AREAS:
            assert area in info['areas'], (
                f"Área '{area}' faltante en modelo '{modelo}'"
            )


def test_cargar_datos_2024_puntajes_rango():
    """Los puntajes promedio de área deben estar entre 0 y 100."""
    datos = cargar_datos_2024()
    for modelo, info in datos.items():
        for area, stats in info['areas'].items():
            promedio = stats['promedio']
            assert 0 <= promedio <= 100, (
                f"Promedio fuera de rango en {modelo}/{area}: {promedio}"
            )


# ============================================================================
# Tests de DATOS_OFICIALES_2025
# ============================================================================

def test_datos_oficiales_2025_estructura():
    """DATOS_OFICIALES_2025 debe tener los 3 modelos clave."""
    modelos_esperados = {
        'Todos',
        'Aula Regular (Jornada 1)',
        'Modelo Flexible (Jornada 0)'
    }
    assert set(DATOS_OFICIALES_2025.keys()) == modelos_esperados


def test_datos_oficiales_2025_areas_completas():
    """Cada modelo en DATOS_OFICIALES_2025 debe tener las 5 áreas."""
    for modelo, info in DATOS_OFICIALES_2025.items():
        assert 'areas' in info, f"Modelo '{modelo}' no tiene clave 'areas'"
        for area in AREAS:
            assert area in info['areas'], (
                f"Área '{area}' faltante en modelo '{modelo}'"
            )


def test_datos_oficiales_2025_puntaje_global_rango():
    """El puntaje global oficial debe estar entre 0 y 500."""
    for modelo, info in DATOS_OFICIALES_2025.items():
        pg = info['puntaje_global']
        assert 0 <= pg <= 500, (
            f"Puntaje global fuera de rango en '{modelo}': {pg}"
        )
