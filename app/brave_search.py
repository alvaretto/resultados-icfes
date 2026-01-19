#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de Búsqueda Web con Brave Search API

Este módulo implementa búsqueda web para el asistente de IA,
permitiendo obtener información actualizada sobre recursos educativos ICFES,
cartillas de Evaluar para Avanzar, y otros materiales pedagógicos.

Autor: Sistema de Análisis ICFES
Fecha: 2025-01-18
"""

import os
import requests
from typing import Optional, List, Dict, Any
import re

# Import condicional de Streamlit (para permitir uso fuera de Streamlit)
try:
    import streamlit as st
    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False
    st = None

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

BRAVE_SEARCH_ENDPOINT = "https://api.search.brave.com/res/v1/web/search"

# Dominios educativos prioritarios para búsquedas ICFES
DOMINIOS_EDUCATIVOS = [
    "icfes.gov.co",
    "mineducacion.gov.co",
    "colombiaaprende.edu.co",
    "eduteka.icesi.edu.co",
    "aprendoencasa.gov.co",
    "banrep.gov.co",  # Recursos educativos del Banco de la República
]

# Palabras clave que indican necesidad de búsqueda web
KEYWORDS_BUSQUEDA_WEB = [
    # Recursos específicos ICFES
    "evaluar para avanzar",
    "cartilla",
    "cartillas",
    "caja de herramientas",
    "material de apoyo",
    "guía",
    "guías",
    "manual",
    "documento oficial",
    "lineamientos",
    "orientaciones",

    # Competencias y aprendizajes (CRÍTICO para grados inferiores)
    "aprendizajes",
    "aprendizajes saber",
    "competencias",
    "dba",
    "derechos básicos",
    "estándares",
    "mallas curriculares",
    "matriz de referencia",
    "evidencias de aprendizaje",

    # TODOS los grados (preparación temprana para Saber 11)
    "grado 3",
    "grado 4",
    "grado 5",
    "grado 6",
    "grado 7",
    "grado 8",
    "grado 9",
    "grado 10",
    "tercero",
    "cuarto",
    "quinto",
    "sexto",
    "séptimo",
    "septimo",
    "octavo",
    "noveno",
    "décimo",
    "decimo",
    "primaria",
    "secundaria",
    "básica",
    "basica",
    "media",

    # Pruebas Saber por grado
    "saber 3",
    "saber 5",
    "saber 7",
    "saber 9",
    "saber 11",
    "pruebas saber",

    # Prácticas y preparación
    "simulacro",
    "preicfes",
    "pre-icfes",
    "banco de preguntas",
    "cuadernillos",
    "ejemplos de preguntas",
    "preparar",
    "preparación",

    # Temas pedagógicos
    "reforzar",
    "refuerzo",
    "nivelación",
    "estrategias didácticas",
    "secuencia didáctica",
    "plan de mejoramiento",
    "fortalecer",
    "mejorar",
    "desarrollar",

    # Áreas específicas (cuando se pregunta sobre contenidos)
    "lectura crítica",
    "matemáticas",
    "ciencias naturales",
    "sociales y ciudadanas",
    "inglés",
    "competencias ciudadanas",
    "razonamiento cuantitativo",

    # Actualidad
    "calendario icfes 2025",
    "calendario icfes 2026",
    "inscripciones",
    "fechas",
    "novedades",
    "nuevas pruebas",
]


def obtener_api_key() -> Optional[str]:
    """
    Obtiene la API key de Brave Search desde secrets o variables de entorno.

    Returns:
        API key o None si no está configurada
    """
    # Intentar desde Streamlit secrets (solo si Streamlit está disponible)
    if STREAMLIT_AVAILABLE and st is not None:
        try:
            if hasattr(st, 'secrets') and "BRAVE_SEARCH_API_KEY" in st.secrets:
                return st.secrets["BRAVE_SEARCH_API_KEY"]
        except Exception:
            pass

    # Intentar desde variables de entorno
    return os.getenv("BRAVE_SEARCH_API_KEY")


def necesita_busqueda_web(pregunta: str) -> bool:
    """
    Determina si una pregunta requiere búsqueda web.

    Args:
        pregunta: Texto de la pregunta del usuario

    Returns:
        True si se debería realizar búsqueda web
    """
    pregunta_lower = pregunta.lower()

    # Verificar si contiene palabras clave de búsqueda
    for keyword in KEYWORDS_BUSQUEDA_WEB:
        if keyword in pregunta_lower:
            return True

    # Patrones adicionales que sugieren búsqueda web
    patrones = [
        r"dónde\s+(encuentro|puedo encontrar|hay|están)",
        r"cómo\s+(enseño|refuerzo|trabajo|desarrollo)",
        r"qué\s+(recursos|materiales|herramientas|actividades)",
        r"(dame|muéstrame|necesito|busco)\s+.*(recurso|material|guía|cartilla)",
        r"(actualización|última versión|versión actual)",
        r"(según|dice|indica)\s+(el|la)\s+(icfes|ministerio|men)",
        # Preguntas sobre qué enseñar/reforzar por grado
        r"(qué|cuáles?)\s+(aprendizajes?|competencias?|contenidos?|temas?)",
        r"(preparar|preparación)\s+.*(para|hacia)\s+(saber|icfes|11)",
        # Grados específicos con números
        r"grados?\s+\d",
        r"\d+[°º]?\s*(grado)?",
    ]

    for patron in patrones:
        if re.search(patron, pregunta_lower):
            return True

    return False


def construir_query_educativa(pregunta: str) -> str:
    """
    Construye una query optimizada para búsqueda de recursos educativos ICFES.

    Args:
        pregunta: Pregunta original del usuario

    Returns:
        Query optimizada para Brave Search
    """
    pregunta_lower = pregunta.lower()

    # Términos de contexto base
    contexto_adicional = []

    # Detectar si menciona grados específicos (para agregar contexto de Saber/Evaluar)
    grados_inferiores = re.search(r"grados?\s*([3-9]|10)|([3-9]|10)[°º]", pregunta_lower)
    menciona_aprendizajes = any(term in pregunta_lower for term in [
        "aprendizaje", "competencia", "contenido", "reforzar", "preparar", "fortalecer"
    ])

    # Si pregunta sobre grados inferiores y aprendizajes, agregar contexto específico
    if grados_inferiores and menciona_aprendizajes:
        if "evaluar para avanzar" not in pregunta_lower:
            contexto_adicional.append("Evaluar para Avanzar")
        if "matriz de referencia" not in pregunta_lower:
            contexto_adicional.append("matriz de referencia")

    # Agregar contexto ICFES/Colombia si no está presente
    if "icfes" not in pregunta_lower:
        contexto_adicional.append("ICFES")

    if "colombia" not in pregunta_lower and "mineducacion" not in pregunta_lower:
        contexto_adicional.append("Colombia")

    # Si menciona aprendizajes sin especificar programa
    if "aprendizaje" in pregunta_lower and "evaluar para avanzar" not in pregunta_lower:
        if "Evaluar para Avanzar" not in contexto_adicional:
            contexto_adicional.append("Saber")

    # Construir query final
    query = pregunta
    if contexto_adicional:
        query = f"{pregunta} {' '.join(contexto_adicional)}"

    return query


def buscar_en_web(
    pregunta: str,
    max_resultados: int = 5
) -> Dict[str, Any]:
    """
    Realiza una búsqueda web usando Brave Search API.

    Args:
        pregunta: Consulta de búsqueda
        max_resultados: Número máximo de resultados

    Returns:
        Diccionario con resultados y metadatos
    """
    api_key = obtener_api_key()

    if not api_key:
        return {
            "exito": False,
            "error": "API key de Brave Search no configurada. Agrega BRAVE_SEARCH_API_KEY en secrets.",
            "resultados": []
        }

    # Construir query optimizada (incluye contexto Colombia/ICFES)
    query = construir_query_educativa(pregunta)

    # Parámetros de la búsqueda (tier gratuito - solo q y count)
    params = {
        "q": query,
        "count": max_resultados,
    }

    headers = {
        "X-Subscription-Token": api_key,
        "Accept": "application/json"
    }

    try:
        response = requests.get(
            BRAVE_SEARCH_ENDPOINT,
            params=params,
            headers=headers,
            timeout=10
        )

        if response.status_code == 401:
            return {
                "exito": False,
                "error": "API key de Brave Search inválida o expirada.",
                "resultados": []
            }

        if response.status_code == 429:
            return {
                "exito": False,
                "error": "Límite de búsquedas alcanzado. Intenta más tarde.",
                "resultados": []
            }

        response.raise_for_status()
        data = response.json()

        # Extraer resultados web
        resultados = []
        web_results = data.get("web", {}).get("results", [])

        for item in web_results:
            resultado = {
                "titulo": item.get("title", ""),
                "url": item.get("url", ""),
                "descripcion": item.get("description", ""),
                "extra_snippets": item.get("extra_snippets", []),
                "es_dominio_educativo": any(
                    dominio in item.get("url", "").lower()
                    for dominio in DOMINIOS_EDUCATIVOS
                )
            }
            resultados.append(resultado)

        # Ordenar: dominios educativos primero
        resultados.sort(key=lambda x: (not x["es_dominio_educativo"], x["titulo"]))

        return {
            "exito": True,
            "query_usada": query,
            "total_resultados": len(resultados),
            "resultados": resultados
        }

    except requests.exceptions.Timeout:
        return {
            "exito": False,
            "error": "La búsqueda tardó demasiado. Intenta de nuevo.",
            "resultados": []
        }
    except requests.exceptions.RequestException as e:
        return {
            "exito": False,
            "error": f"Error de conexión: {str(e)}",
            "resultados": []
        }
    except Exception as e:
        return {
            "exito": False,
            "error": f"Error inesperado: {str(e)}",
            "resultados": []
        }


def formatear_resultados_para_contexto(resultados: Dict[str, Any]) -> str:
    """
    Formatea los resultados de búsqueda para incluir en el contexto del LLM.

    Args:
        resultados: Diccionario con resultados de búsqueda

    Returns:
        Texto formateado para el prompt del LLM
    """
    if not resultados.get("exito"):
        return f"⚠️ No se pudo realizar búsqueda web: {resultados.get('error', 'Error desconocido')}"

    if not resultados.get("resultados"):
        return "🔍 No se encontraron resultados relevantes en la web."

    texto = "## 🌐 INFORMACIÓN DE BÚSQUEDA WEB (Resultados actualizados)\n\n"
    texto += f"*Query: {resultados.get('query_usada', '')}*\n\n"

    for i, resultado in enumerate(resultados["resultados"], 1):
        # Indicador si es dominio educativo oficial
        indicador = "📚 [OFICIAL]" if resultado["es_dominio_educativo"] else "🔗"

        texto += f"### {indicador} {i}. {resultado['titulo']}\n"
        texto += f"**URL**: {resultado['url']}\n"
        texto += f"**Resumen**: {resultado['descripcion']}\n"

        # Agregar snippets adicionales si hay
        if resultado.get("extra_snippets"):
            texto += "**Extractos adicionales**:\n"
            for snippet in resultado["extra_snippets"][:2]:  # Máximo 2 snippets
                texto += f"- {snippet}\n"

        texto += "\n"

    texto += """
---
**Instrucciones para usar esta información**:
1. Prioriza información de fuentes oficiales (ICFES, MEN, Colombia Aprende)
2. Incluye las URLs cuando recomiendes recursos
3. Sintetiza y contextualiza la información para el usuario
4. Si la información es sobre recursos, explica cómo usarlos
"""

    return texto


def buscar_y_formatear(pregunta: str) -> Optional[str]:
    """
    Función de conveniencia que busca y formatea en un solo paso.

    Args:
        pregunta: Pregunta del usuario

    Returns:
        Texto formateado con resultados o None si no aplica búsqueda
    """
    if not necesita_busqueda_web(pregunta):
        return None

    resultados = buscar_en_web(pregunta)
    return formatear_resultados_para_contexto(resultados)


# ============================================================================
# FUNCIONES DE UTILIDAD
# ============================================================================

def verificar_configuracion() -> Dict[str, bool]:
    """
    Verifica si la búsqueda web está correctamente configurada.

    Returns:
        Diccionario con estado de configuración
    """
    api_key = obtener_api_key()

    return {
        "api_key_presente": api_key is not None,
        "api_key_longitud_valida": len(api_key) > 20 if api_key else False,
    }


def obtener_estadisticas_busqueda() -> Dict[str, Any]:
    """
    Obtiene estadísticas de uso de búsqueda (para monitoreo).

    Returns:
        Estadísticas de la sesión actual
    """
    if not STREAMLIT_AVAILABLE or st is None:
        return {
            "busquedas_realizadas": 0,
            "busquedas_exitosas": 0,
            "busquedas_fallidas": 0,
        }

    if "brave_search_stats" not in st.session_state:
        st.session_state.brave_search_stats = {
            "busquedas_realizadas": 0,
            "busquedas_exitosas": 0,
            "busquedas_fallidas": 0,
        }

    return st.session_state.brave_search_stats


def incrementar_estadistica(tipo: str):
    """
    Incrementa contador de estadísticas.

    Args:
        tipo: Tipo de estadística a incrementar
    """
    if not STREAMLIT_AVAILABLE or st is None:
        return

    stats = obtener_estadisticas_busqueda()
    if tipo in stats:
        stats[tipo] += 1


# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    # Test básico
    print("=== Test de Brave Search ===\n")

    # Verificar configuración
    config = verificar_configuracion()
    print(f"API Key presente: {config['api_key_presente']}")

    if config['api_key_presente']:
        # Test de búsqueda
        pregunta_test = "¿Cuáles son los aprendizajes de Evaluar para Avanzar para grado 8?"

        print(f"\nPregunta: {pregunta_test}")
        print(f"¿Necesita búsqueda web?: {necesita_busqueda_web(pregunta_test)}")

        resultado = buscar_en_web(pregunta_test, max_resultados=3)
        print(f"\nResultado: {resultado}")
    else:
        print("\n⚠️ Configura BRAVE_SEARCH_API_KEY para probar")
