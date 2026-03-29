#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_data_loading.py — Tests de carga de datos desde Excel y validación de estructura

Verifica:
- Que el archivo Excel de ejemplo carga correctamente
- Que las columnas esperadas están presentes
- Que los tipos de datos son correctos
- Manejo de archivos inexistentes
- Manejo de valores nulos
"""

import pytest
import pandas as pd
import numpy as np
import os

# Ruta al archivo de ejemplo real
RUTA_EXCEL_EJEMPLO = os.path.join(
    os.path.dirname(__file__), '..', 'data', 'RESULTADOS-ICFES-EJEMPLO.xlsx'
)

COLUMNAS_REQUERIDAS = [
    'Grupo',
    'Lectura Crítica',
    'Matemáticas',
    'Sociales y Ciudadanas',
    'Ciencias Naturales',
    'Inglés',
    'Puntaje Global',
]

AREAS = ['Lectura Crítica', 'Matemáticas', 'Sociales y Ciudadanas', 'Ciencias Naturales', 'Inglés']


# ============================================================================
# Tests de carga del Excel real
# ============================================================================

class TestCargaExcelEjemplo:

    def test_archivo_ejemplo_existe(self):
        """El archivo RESULTADOS-ICFES-EJEMPLO.xlsx debe existir."""
        assert os.path.isfile(RUTA_EXCEL_EJEMPLO), (
            f"Archivo de ejemplo no encontrado: {RUTA_EXCEL_EJEMPLO}"
        )

    def test_excel_carga_sin_error(self):
        """El archivo Excel debe cargarse sin lanzar excepciones."""
        df = pd.read_excel(RUTA_EXCEL_EJEMPLO)
        assert df is not None

    def test_excel_tiene_registros(self):
        """El archivo Excel debe contener al menos 1 registro."""
        df = pd.read_excel(RUTA_EXCEL_EJEMPLO)
        assert len(df) > 0, "El archivo Excel está vacío"

    def test_excel_tiene_columnas_requeridas(self):
        """Todas las columnas requeridas deben estar presentes."""
        df = pd.read_excel(RUTA_EXCEL_EJEMPLO)
        for col in COLUMNAS_REQUERIDAS:
            assert col in df.columns, f"Columna faltante: '{col}'"

    def test_columnas_areas_son_numericas(self):
        """Las columnas de áreas deben tener tipo numérico."""
        df = pd.read_excel(RUTA_EXCEL_EJEMPLO)
        for area in AREAS:
            assert pd.api.types.is_numeric_dtype(df[area]), (
                f"Columna '{area}' debería ser numérica, es {df[area].dtype}"
            )

    def test_puntaje_global_es_numerico(self):
        """La columna Puntaje Global debe ser numérica."""
        df = pd.read_excel(RUTA_EXCEL_EJEMPLO)
        assert pd.api.types.is_numeric_dtype(df['Puntaje Global'])

    def test_puntajes_areas_en_rango_valido(self):
        """Los puntajes de área deben estar en el rango 0-100."""
        df = pd.read_excel(RUTA_EXCEL_EJEMPLO)
        for area in AREAS:
            col = df[area].dropna()
            assert (col >= 0).all(), f"{area}: hay puntajes negativos"
            assert (col <= 100).all(), f"{area}: hay puntajes mayores a 100"

    def test_puntaje_global_en_rango_valido(self):
        """El Puntaje Global debe estar entre 0 y 500."""
        df = pd.read_excel(RUTA_EXCEL_EJEMPLO)
        col = df['Puntaje Global'].dropna()
        assert (col >= 0).all(), "Hay puntajes globales negativos"
        assert (col <= 500).all(), "Hay puntajes globales mayores a 500"

    def test_columna_grupo_no_vacia(self):
        """La columna Grupo no debe estar completamente vacía."""
        df = pd.read_excel(RUTA_EXCEL_EJEMPLO)
        assert df['Grupo'].notna().any(), "La columna Grupo está completamente vacía"


# ============================================================================
# Tests con archivo inexistente
# ============================================================================

class TestCargaArchivoInexistente:

    def test_archivo_inexistente_lanza_excepcion(self):
        """Intentar cargar un archivo que no existe debe lanzar una excepción."""
        with pytest.raises((FileNotFoundError, Exception)):
            pd.read_excel('/tmp/archivo_que_no_existe_icfes.xlsx')


# ============================================================================
# Tests de validación de estructura del DataFrame (usando fixtures)
# ============================================================================

class TestValidacionEstructuraDataFrame:

    def test_fixture_df_tiene_columnas_correctas(self, df_estudiantes_ejemplo):
        """El fixture de prueba debe tener todas las columnas requeridas."""
        for col in COLUMNAS_REQUERIDAS:
            assert col in df_estudiantes_ejemplo.columns

    def test_fixture_df_tiene_10_estudiantes(self, df_estudiantes_ejemplo):
        """El fixture de ejemplo debe tener exactamente 10 estudiantes."""
        assert len(df_estudiantes_ejemplo) == 10

    def test_df_vacio_tiene_columnas(self, df_vacio):
        """El DataFrame vacío debe conservar las columnas."""
        assert len(df_vacio) == 0
        assert 'Puntaje Global' in df_vacio.columns

    def test_df_con_nulos_permite_conteo(self, df_con_nulos):
        """DataFrame con nulos: la operación notna() debe funcionar."""
        total_nulos_global = df_con_nulos['Puntaje Global'].isna().sum()
        assert total_nulos_global > 0, "Se esperaban nulos en Puntaje Global"

    def test_puntaje_global_consistente_con_suma(self, df_estudiantes_ejemplo):
        """Puntaje Global debe ser aproximadamente igual a la suma de las 5 áreas."""
        suma_areas = df_estudiantes_ejemplo[AREAS].sum(axis=1)
        diferencia = (df_estudiantes_ejemplo['Puntaje Global'] - suma_areas).abs()
        assert (diferencia < 1.0).all(), "Puntaje Global no es consistente con la suma de áreas"

    def test_grupos_son_strings(self, df_estudiantes_ejemplo):
        """La columna Grupo debe contener strings."""
        assert df_estudiantes_ejemplo['Grupo'].dtype == object

    def test_no_hay_grupos_nulos_en_datos_limpios(self, df_estudiantes_ejemplo):
        """En datos bien formados no debe haber grupos nulos."""
        assert df_estudiantes_ejemplo['Grupo'].isna().sum() == 0
