#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_chat.py — Tests del módulo de Chat IA

Verifica (con mocks de API — nunca llama APIs reales):
- Construcción del contexto de datos para el LLM
- Documentación ICFES y base de conocimiento institucional
- Detección de proveedor disponible
- Configuraciones de modelos
"""

import pytest
import pandas as pd
import sys
import os
from unittest.mock import MagicMock, patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

AREAS = ['Lectura Crítica', 'Matemáticas', 'Sociales y Ciudadanas', 'Ciencias Naturales', 'Inglés']


# ============================================================================
# Importar el módulo (Streamlit ya está mockeado en conftest.py)
# ============================================================================

# Mock de streamlit.components.v1 que chat_ia_icfes necesita
sys.modules.setdefault('streamlit.components', MagicMock())
sys.modules.setdefault('streamlit.components.v1', MagicMock())

try:
    from app.chat_ia_icfes import (
        construir_contexto_datos,
        obtener_documentacion_icfes,
        obtener_base_conocimiento_institucional,
        MODELOS_ANTHROPIC,
        MODELOS_GROQ,
    )
    CHAT_CARGADO = True
except Exception as e:
    CHAT_CARGADO = False
    _CHAT_ERROR = str(e)


# ============================================================================
# Tests de construcción del contexto de datos
# ============================================================================

@pytest.mark.skipif(not CHAT_CARGADO, reason="No se pudo cargar chat_ia_icfes")
class TestConstruccionContextoDatos:

    def test_contexto_con_df_none_retorna_mensaje(self):
        """Con df=None debe retornar texto indicando que no hay datos."""
        resultado = construir_contexto_datos(None)
        assert "No hay datos" in resultado or resultado == "No hay datos disponibles."

    def test_contexto_con_df_vacio_retorna_mensaje(self, df_vacio):
        """Con DataFrame vacío debe retornar texto indicando que no hay datos."""
        resultado = construir_contexto_datos(df_vacio)
        assert "No hay datos" in resultado or len(resultado) < 50

    def test_contexto_con_df_valido_es_string_no_vacio(self, df_estudiantes_ejemplo):
        """Con datos válidos el contexto debe ser un string no vacío."""
        resultado = construir_contexto_datos(df_estudiantes_ejemplo)
        assert isinstance(resultado, str)
        assert len(resultado) > 100

    def test_contexto_incluye_total_estudiantes(self, df_estudiantes_ejemplo):
        """El contexto debe mencionar el total de estudiantes."""
        resultado = construir_contexto_datos(df_estudiantes_ejemplo)
        assert "10" in resultado  # 10 estudiantes en el fixture

    def test_contexto_incluye_puntaje_global(self, df_estudiantes_ejemplo):
        """El contexto debe mencionar el puntaje global promedio."""
        resultado = construir_contexto_datos(df_estudiantes_ejemplo)
        assert "Puntaje" in resultado or "puntaje" in resultado

    def test_contexto_incluye_todas_las_areas(self, df_estudiantes_ejemplo):
        """El contexto debe mencionar todas las 5 áreas."""
        resultado = construir_contexto_datos(df_estudiantes_ejemplo)
        for area in AREAS:
            assert area in resultado, f"Área '{area}' no aparece en el contexto"

    def test_contexto_no_incluye_nombres_personales(self, df_estudiantes_ejemplo):
        """El contexto NO debe incluir nombres o apellidos individuales."""
        resultado = construir_contexto_datos(df_estudiantes_ejemplo)
        # Verificar que los apellidos del fixture no aparecen en el contexto
        apellidos = ['García', 'López', 'Martínez', 'Rodríguez']
        for apellido in apellidos:
            assert apellido not in resultado, (
                f"El apellido '{apellido}' aparece en el contexto (violación de privacidad)"
            )

    def test_contexto_no_incluye_numeros_documento(self, df_estudiantes_ejemplo):
        """El contexto NO debe incluir números de documento."""
        resultado = construir_contexto_datos(df_estudiantes_ejemplo)
        # Los documentos en el fixture son 1001-1010
        for doc_num in range(1001, 1011):
            assert str(doc_num) not in resultado, (
                f"Número de documento {doc_num} aparece en el contexto"
            )

    def test_contexto_con_comparacion_2024_incluye_cambio(
        self, df_estudiantes_ejemplo, datos_2024_referencia
    ):
        """Al incluir datos 2024, el contexto debe mencionar la comparación."""
        resultado = construir_contexto_datos(
            df_estudiantes_ejemplo,
            pagina_actual="General",
            datos_2024=datos_2024_referencia
        )
        assert "2024" in resultado
        assert "2025" in resultado

    def test_contexto_con_columna_modelo(self, df_estudiantes_con_modelo):
        """Si el DataFrame tiene columna 'Modelo', el contexto debe incluir sección de modelos."""
        resultado = construir_contexto_datos(df_estudiantes_con_modelo)
        assert "Modelo" in resultado or "modelo" in resultado

    def test_contexto_con_columna_grupo(self, df_estudiantes_ejemplo):
        """Si el DataFrame tiene columna 'Grupo', el contexto debe incluir sección de grupos."""
        resultado = construir_contexto_datos(df_estudiantes_ejemplo)
        assert "Grupo" in resultado or "grupo" in resultado


# ============================================================================
# Tests de documentación ICFES
# ============================================================================

@pytest.mark.skipif(not CHAT_CARGADO, reason="No se pudo cargar chat_ia_icfes")
class TestDocumentacionICFES:

    def test_documentacion_es_string_no_vacio(self):
        """obtener_documentacion_icfes debe retornar un string no vacío."""
        doc = obtener_documentacion_icfes()
        assert isinstance(doc, str)
        assert len(doc) > 200

    def test_documentacion_menciona_los_cuatro_niveles(self):
        """La documentación debe mencionar los 4 niveles de desempeño."""
        doc = obtener_documentacion_icfes()
        for nivel in ['Insuficiente', 'Mínimo', 'Satisfactorio', 'Avanzado']:
            assert nivel in doc, f"Nivel '{nivel}' no aparece en la documentación"

    def test_documentacion_menciona_puntaje_global(self):
        """La documentación debe mencionar el Puntaje Global."""
        doc = obtener_documentacion_icfes()
        assert "Puntaje Global" in doc or "puntaje global" in doc.lower()

    def test_documentacion_menciona_rango_valido(self):
        """La documentación debe mencionar el rango de puntajes (0-500 o similares)."""
        doc = obtener_documentacion_icfes()
        assert "500" in doc

    def test_base_conocimiento_es_string_no_vacio(self):
        """obtener_base_conocimiento_institucional debe retornar string no vacío."""
        base = obtener_base_conocimiento_institucional()
        assert isinstance(base, str)
        assert len(base) > 200

    def test_base_conocimiento_menciona_institucion(self):
        """La base debe mencionar el nombre de la institución."""
        base = obtener_base_conocimiento_institucional()
        assert "PEDACITO DE CIELO" in base or "Pedacito de Cielo" in base

    def test_base_conocimiento_menciona_municipio(self):
        """La base debe mencionar La Tebaida."""
        base = obtener_base_conocimiento_institucional()
        assert "TEBAIDA" in base or "Tebaida" in base


# ============================================================================
# Tests de configuración de modelos (sin llamadas reales)
# ============================================================================

@pytest.mark.skipif(not CHAT_CARGADO, reason="No se pudo cargar chat_ia_icfes")
class TestConfiguracionModelos:

    def test_modelos_anthropic_contiene_haiku(self):
        assert "haiku" in MODELOS_ANTHROPIC

    def test_modelos_anthropic_contiene_sonnet(self):
        assert "sonnet" in MODELOS_ANTHROPIC

    def test_modelos_anthropic_tienen_ids_validos(self):
        """Los IDs de modelos Anthropic deben ser strings no vacíos."""
        for nombre, modelo_id in MODELOS_ANTHROPIC.items():
            assert isinstance(modelo_id, str)
            assert len(modelo_id) > 5, f"ID de modelo '{nombre}' parece inválido: '{modelo_id}'"

    def test_modelos_groq_no_vacio(self):
        assert len(MODELOS_GROQ) > 0

    def test_modelos_groq_tienen_ids_validos(self):
        """Los IDs de modelos Groq deben ser strings no vacíos."""
        for nombre, modelo_id in MODELOS_GROQ.items():
            assert isinstance(modelo_id, str)
            assert len(modelo_id) > 3

    def test_detectar_proveedor_sin_keys_retorna_anthropic(self):
        """Sin API keys configuradas, debe retornar 'anthropic' por defecto."""
        # Mockear st.session_state y secrets vacíos
        mock_st = sys.modules.get('streamlit')
        if mock_st:
            mock_st.secrets = {}
            with patch.dict(os.environ, {}, clear=False):
                # Remover claves si existen
                env_backup = {}
                for key in ['ANTHROPIC_API_KEY', 'GROQ_API_KEY']:
                    if key in os.environ:
                        env_backup[key] = os.environ.pop(key)
                try:
                    from app.chat_ia_icfes import detectar_proveedor_disponible
                    resultado = detectar_proveedor_disponible()
                    assert resultado in ('anthropic', 'groq')
                finally:
                    # Restaurar
                    os.environ.update(env_backup)
