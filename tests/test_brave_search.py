#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_brave_search.py — Tests del módulo de búsqueda web con Brave Search

Verifica (con mocks — NUNCA llama la API real):
- Detección de preguntas que requieren búsqueda web
- Construcción de queries educativas optimizadas
- Formateo de resultados para el contexto del LLM
- Manejo de errores y edge cases
- Verificación de configuración
"""

import pytest
import sys
import os
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


# ============================================================================
# Importar el módulo (Streamlit ya está mockeado en conftest.py)
# ============================================================================

try:
    from app.brave_search import (
        necesita_busqueda_web,
        construir_query_educativa,
        formatear_resultados_para_contexto,
        buscar_en_web,
        buscar_y_formatear,
        verificar_configuracion,
    )
    BRAVE_CARGADO = True
except Exception as e:
    BRAVE_CARGADO = False
    _BRAVE_ERROR = str(e)


# ============================================================================
# Tests de detección de búsqueda web necesaria
# ============================================================================

@pytest.mark.skipif(not BRAVE_CARGADO, reason="No se pudo cargar brave_search")
class TestNecesitaBusquedaWeb:

    def test_pregunta_sobre_cartillas_necesita_busqueda(self):
        assert necesita_busqueda_web("¿Dónde encuentro cartillas del ICFES?") is True

    def test_pregunta_sobre_evaluar_para_avanzar_necesita_busqueda(self):
        assert necesita_busqueda_web("¿Qué es Evaluar para Avanzar?") is True

    def test_pregunta_sobre_simulacro_necesita_busqueda(self):
        assert necesita_busqueda_web("Necesito un simulacro para grado 11") is True

    def test_pregunta_sobre_grado_especifico_necesita_busqueda(self):
        assert necesita_busqueda_web("¿Qué competencias se evalúan en grado 8?") is True

    def test_pregunta_sobre_calendario_necesita_busqueda(self):
        assert necesita_busqueda_web("calendario icfes 2025") is True

    def test_pregunta_sobre_matematicas_necesita_busqueda(self):
        assert necesita_busqueda_web("cómo enseño matemáticas para el ICFES") is True

    def test_pregunta_sobre_lectura_critica_necesita_busqueda(self):
        assert necesita_busqueda_web("recursos para lectura crítica") is True

    def test_pregunta_generica_no_necesita_busqueda(self):
        """Una pregunta genérica sin keywords específicos no debe requerir búsqueda."""
        assert necesita_busqueda_web("¿cuál es el promedio de la institución?") is False

    def test_pregunta_sobre_resultados_no_necesita_busqueda(self):
        """Una pregunta sin keywords educativos no debe requerir búsqueda web."""
        assert necesita_busqueda_web("¿cuál es el nombre del rector?") is False

    def test_string_vacio_no_necesita_busqueda(self):
        """Un string vacío no debe requerir búsqueda."""
        assert necesita_busqueda_web("") is False

    def test_pregunta_sobre_dba_necesita_busqueda(self):
        """Preguntas sobre DBA (Derechos Básicos de Aprendizaje) requieren búsqueda."""
        assert necesita_busqueda_web("¿cuáles son los DBA de matemáticas?") is True

    def test_pregunta_sobre_plan_mejoramiento_necesita_busqueda(self):
        assert necesita_busqueda_web("cómo hacer un plan de mejoramiento") is True

    def test_pregunta_sobre_saber_11_necesita_busqueda(self):
        assert necesita_busqueda_web("¿cómo preparar a los estudiantes para saber 11?") is True

    def test_pregunta_sobre_banco_preguntas_necesita_busqueda(self):
        assert necesita_busqueda_web("banco de preguntas ICFES") is True


# ============================================================================
# Tests de construcción de queries educativas
# ============================================================================

@pytest.mark.skipif(not BRAVE_CARGADO, reason="No se pudo cargar brave_search")
class TestConstruirQueryEducativa:

    def test_query_agrega_contexto_icfes_si_no_esta(self):
        """Si la pregunta no menciona ICFES, debe agregar contexto ICFES."""
        query = construir_query_educativa("cartillas de matemáticas")
        assert "ICFES" in query

    def test_query_agrega_colombia_si_no_esta(self):
        """Si la pregunta no menciona Colombia, debe agregar Colombia."""
        query = construir_query_educativa("recursos educativos matemáticas")
        assert "Colombia" in query

    def test_query_no_duplica_icfes(self):
        """Si la pregunta ya menciona ICFES, no debe duplicarlo."""
        pregunta = "ICFES resultados 2025"
        query = construir_query_educativa(pregunta)
        count_icfes = query.lower().count("icfes")
        assert count_icfes == 1, f"ICFES aparece {count_icfes} veces: '{query}'"

    def test_query_retorna_string(self):
        """La función debe retornar siempre un string."""
        resultado = construir_query_educativa("cualquier pregunta")
        assert isinstance(resultado, str)

    def test_query_no_vacia(self):
        """La query resultante no debe estar vacía."""
        resultado = construir_query_educativa("alguna pregunta educativa")
        assert len(resultado) > 0

    def test_query_contiene_pregunta_original(self):
        """La query debe contener la pregunta original."""
        pregunta = "recursos evaluar para avanzar"
        query = construir_query_educativa(pregunta)
        assert pregunta in query

    def test_query_grado_con_aprendizajes_agrega_evaluar_para_avanzar(self):
        """Para preguntas sobre grados con aprendizajes, debe agregar 'Evaluar para Avanzar'."""
        query = construir_query_educativa("aprendizajes de grado 7")
        assert "Evaluar para Avanzar" in query or "evaluar para avanzar" in query.lower()


# ============================================================================
# Tests de formateo de resultados
# ============================================================================

@pytest.mark.skipif(not BRAVE_CARGADO, reason="No se pudo cargar brave_search")
class TestFormatearResultados:

    def test_formateo_exitoso_retorna_string(self, mock_brave_search_exitoso):
        """Con resultados exitosos debe retornar un string."""
        resultado = formatear_resultados_para_contexto(mock_brave_search_exitoso)
        assert isinstance(resultado, str)

    def test_formateo_exitoso_incluye_titulos(self, mock_brave_search_exitoso):
        """El texto formateado debe incluir los títulos de los resultados."""
        resultado = formatear_resultados_para_contexto(mock_brave_search_exitoso)
        assert "Evaluar para Avanzar - ICFES" in resultado

    def test_formateo_exitoso_incluye_urls(self, mock_brave_search_exitoso):
        """El texto formateado debe incluir las URLs de los resultados."""
        resultado = formatear_resultados_para_contexto(mock_brave_search_exitoso)
        assert "icfes.gov.co" in resultado

    def test_formateo_exitoso_incluye_query_usada(self, mock_brave_search_exitoso):
        """El texto formateado debe mencionar la query usada."""
        resultado = formatear_resultados_para_contexto(mock_brave_search_exitoso)
        assert "cartillas ICFES Colombia" in resultado

    def test_formateo_fallido_menciona_error(self, mock_brave_search_fallido):
        """Con búsqueda fallida debe retornar un mensaje de error."""
        resultado = formatear_resultados_para_contexto(mock_brave_search_fallido)
        assert isinstance(resultado, str)
        assert len(resultado) > 0
        # Debe indicar el error
        assert "API key" in resultado or "No se pudo" in resultado or "error" in resultado.lower()

    def test_formateo_sin_resultados_retorna_mensaje(self, mock_brave_sin_resultados):
        """Sin resultados debe retornar un mensaje apropiado."""
        resultado = formatear_resultados_para_contexto(mock_brave_sin_resultados)
        assert isinstance(resultado, str)
        assert "No se encontraron" in resultado or len(resultado) > 0

    def test_formateo_marca_dominios_oficiales(self, mock_brave_search_exitoso):
        """Los resultados de dominios educativos deben marcarse como oficiales."""
        resultado = formatear_resultados_para_contexto(mock_brave_search_exitoso)
        assert "OFICIAL" in resultado or "oficial" in resultado.lower()


# ============================================================================
# Tests de buscar_en_web (con mock de requests)
# ============================================================================

@pytest.mark.skipif(not BRAVE_CARGADO, reason="No se pudo cargar brave_search")
class TestBuscarEnWeb:

    def test_sin_api_key_retorna_error(self):
        """Sin API key configurada, debe retornar resultado de error."""
        with patch.dict(os.environ, {}, clear=False):
            # Asegurar que no hay API key
            if 'BRAVE_SEARCH_API_KEY' in os.environ:
                del os.environ['BRAVE_SEARCH_API_KEY']

            # También asegurar que st.secrets está vacío
            mock_st = sys.modules.get('streamlit')
            if mock_st:
                mock_st.secrets = {}

            resultado = buscar_en_web("cartillas ICFES")

        assert resultado['exito'] is False
        assert 'error' in resultado
        assert len(resultado['resultados']) == 0

    def test_con_timeout_retorna_error(self):
        """Si requests.get lanza Timeout, debe retornar error apropiado."""
        import requests

        # Simular que hay una API key
        with patch.dict(os.environ, {'BRAVE_SEARCH_API_KEY': 'fake-key-12345'}):
            with patch('requests.get', side_effect=requests.exceptions.Timeout):
                resultado = buscar_en_web("cartillas ICFES")

        assert resultado['exito'] is False
        assert "tardó" in resultado['error'] or "Timeout" in resultado['error'] or "timeout" in resultado['error'].lower()

    def test_con_error_de_conexion_retorna_error(self):
        """Si requests.get lanza ConnectionError, debe retornar error apropiado."""
        import requests

        with patch.dict(os.environ, {'BRAVE_SEARCH_API_KEY': 'fake-key-12345'}):
            with patch('requests.get', side_effect=requests.exceptions.ConnectionError("connection refused")):
                resultado = buscar_en_web("cartillas ICFES")

        assert resultado['exito'] is False
        assert 'error' in resultado

    def test_con_api_key_invalida_retorna_error_401(self):
        """Con API key inválida (respuesta 401), debe retornar error apropiado."""
        import requests

        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError()

        with patch.dict(os.environ, {'BRAVE_SEARCH_API_KEY': 'invalid-key'}):
            with patch('requests.get', return_value=mock_response):
                resultado = buscar_en_web("cartillas ICFES")

        assert resultado['exito'] is False
        assert "inválida" in resultado['error'] or "invalid" in resultado['error'].lower() or "401" in resultado['error']

    def test_con_limite_alcanzado_retorna_error_429(self):
        """Con límite de búsquedas (429), debe retornar error apropiado."""
        mock_response = MagicMock()
        mock_response.status_code = 429

        with patch.dict(os.environ, {'BRAVE_SEARCH_API_KEY': 'valid-key-12345'}):
            with patch('requests.get', return_value=mock_response):
                resultado = buscar_en_web("cartillas ICFES")

        assert resultado['exito'] is False
        assert "Límite" in resultado['error'] or "limite" in resultado['error'].lower()

    def test_busqueda_exitosa_formatea_resultados_correctamente(self):
        """Con respuesta exitosa de la API, debe parsear y retornar resultados."""
        import requests

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "web": {
                "results": [
                    {
                        "title": "ICFES Oficial",
                        "url": "https://icfes.gov.co/test",
                        "description": "Descripción del resultado",
                        "extra_snippets": ["Snippet 1"]
                    }
                ]
            }
        }

        with patch.dict(os.environ, {'BRAVE_SEARCH_API_KEY': 'valid-key-12345'}):
            with patch('requests.get', return_value=mock_response):
                resultado = buscar_en_web("cartillas ICFES", max_resultados=1)

        assert resultado['exito'] is True
        assert len(resultado['resultados']) == 1
        assert resultado['resultados'][0]['titulo'] == "ICFES Oficial"
        assert resultado['resultados'][0]['es_dominio_educativo'] is True


# ============================================================================
# Tests de buscar_y_formatear (función de conveniencia)
# ============================================================================

@pytest.mark.skipif(not BRAVE_CARGADO, reason="No se pudo cargar brave_search")
class TestBuscarYFormatear:

    def test_pregunta_sin_keywords_retorna_none(self):
        """Si la pregunta no requiere búsqueda, debe retornar None."""
        resultado = buscar_y_formatear("¿cuál es el promedio general?")
        assert resultado is None

    def test_pregunta_con_keywords_llama_busqueda(self):
        """Si la pregunta requiere búsqueda, debe intentar buscar (puede fallar sin key)."""
        # Sin API key, retorna texto de error — pero no None
        with patch.dict(os.environ, {}, clear=False):
            if 'BRAVE_SEARCH_API_KEY' in os.environ:
                del os.environ['BRAVE_SEARCH_API_KEY']
            mock_st = sys.modules.get('streamlit')
            if mock_st:
                mock_st.secrets = {}

            resultado = buscar_y_formatear("cartillas evaluar para avanzar")

        # Con keyword de búsqueda pero sin key: retorna mensaje de error (no None)
        assert resultado is not None
        assert isinstance(resultado, str)


# ============================================================================
# Tests de verificación de configuración
# ============================================================================

@pytest.mark.skipif(not BRAVE_CARGADO, reason="No se pudo cargar brave_search")
class TestVerificarConfiguracion:

    def test_sin_api_key_api_key_presente_es_false(self):
        """Sin API key configurada, api_key_presente debe ser False."""
        with patch.dict(os.environ, {}, clear=False):
            if 'BRAVE_SEARCH_API_KEY' in os.environ:
                del os.environ['BRAVE_SEARCH_API_KEY']
            mock_st = sys.modules.get('streamlit')
            if mock_st:
                mock_st.secrets = {}

            config = verificar_configuracion()

        assert config['api_key_presente'] is False

    def test_con_api_key_valida_api_key_presente_es_true(self):
        """Con API key configurada, api_key_presente debe ser True."""
        with patch.dict(os.environ, {'BRAVE_SEARCH_API_KEY': 'clave-de-prueba-muy-larga-12345'}):
            config = verificar_configuracion()

        assert config['api_key_presente'] is True

    def test_retorna_dict_con_claves_esperadas(self):
        """La función debe retornar un dict con las claves documentadas."""
        with patch.dict(os.environ, {}, clear=False):
            if 'BRAVE_SEARCH_API_KEY' in os.environ:
                del os.environ['BRAVE_SEARCH_API_KEY']
            config = verificar_configuracion()

        assert 'api_key_presente' in config
        assert 'api_key_longitud_valida' in config

    def test_api_key_corta_longitud_invalida(self):
        """Una API key muy corta (menos de 20 chars) debe indicar longitud inválida."""
        with patch.dict(os.environ, {'BRAVE_SEARCH_API_KEY': 'corta'}):
            config = verificar_configuracion()

        assert config['api_key_longitud_valida'] is False

    def test_api_key_larga_longitud_valida(self):
        """Una API key de más de 20 caracteres debe indicar longitud válida."""
        key_larga = 'a' * 30
        with patch.dict(os.environ, {'BRAVE_SEARCH_API_KEY': key_larga}):
            config = verificar_configuracion()

        assert config['api_key_longitud_valida'] is True
