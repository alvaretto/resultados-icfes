#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de Chat de IA para Análisis de Resultados ICFES
Institución Educativa Pedacito de Cielo

Este módulo implementa un asistente conversacional de IA que ayuda a los usuarios
a interpretar y analizar los resultados del examen ICFES Saber 11.

Características:
- Respuestas contextualizadas con datos reales
- Soporte para múltiples proveedores LLM (Anthropic, Groq)
- Memoria conversacional
- Streaming de respuestas
- Preguntas sugeridas
- Búsqueda web con Brave Search para recursos educativos actualizados

Autor: Sistema de Análisis ICFES
Fecha: 2025-10-22
"""

import streamlit as st
import pandas as pd
from typing import Dict, List, Optional
import os
import streamlit.components.v1 as components
from .logger import get_logger

logger = get_logger(__name__)

# Importar módulo de búsqueda web
try:
    from app.brave_search import (
        necesita_busqueda_web,
        buscar_y_formatear,
        verificar_configuracion as verificar_brave_search
    )
    BUSQUEDA_WEB_DISPONIBLE = True
except ImportError:
    # Fallback si se ejecuta directamente o hay error de import
    try:
        from brave_search import (
            necesita_busqueda_web,
            buscar_y_formatear,
            verificar_configuracion as verificar_brave_search
        )
        BUSQUEDA_WEB_DISPONIBLE = True
    except ImportError:
        BUSQUEDA_WEB_DISPONIBLE = False
        necesita_busqueda_web = lambda x: False
        buscar_y_formatear = lambda x: None
        verificar_brave_search = lambda: {"api_key_presente": False}

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

# Configuración de modelos disponibles en Groq (cloud)
MODELOS_GROQ = {
    "llama-3.3-70b": "llama-3.3-70b-versatile",
    "llama-3.1-8b": "llama-3.1-8b-instant",
    "qwen3-32b": "qwen/qwen3-32b",
    "gpt-oss-120b": "openai/gpt-oss-120b"
}

# Configuración de modelos disponibles en Anthropic
MODELOS_ANTHROPIC = {
    "haiku": "claude-3-5-haiku-20241022",
    "sonnet": "claude-sonnet-4-20250514",
    "opus": "claude-opus-4-20250514"
}

# Proveedores disponibles
PROVEEDORES = {
    "anthropic": MODELOS_ANTHROPIC,
    "groq": MODELOS_GROQ
}

# Configuración por defecto - Usar Anthropic Sonnet
PROVEEDOR_DEFAULT = "anthropic"
MODELO_DEFAULT_ANTHROPIC = "haiku"
MODELO_DEFAULT_GROQ = "llama-3.3-70b"

# ============================================================================
# FUNCIONES DE INICIALIZACIÓN
# ============================================================================

def inicializar_chat():
    """
    Inicializa el estado del chat en Streamlit session_state

    IMPORTANTE: El historial de mensajes se mantiene persistente en session_state
    y NO se reinicia automáticamente. Solo se limpia cuando el usuario hace clic
    en el botón "Limpiar conversación".
    """
    # Historial de mensajes (persistente entre navegaciones)
    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    # Estado de activación del chat
    if "chat_activado" not in st.session_state:
        st.session_state.chat_activado = False

    # Cliente LLM
    if "llm_client" not in st.session_state:
        st.session_state.llm_client = None

    # Configuración - detectar proveedor disponible
    if "chat_config" not in st.session_state:
        # Detectar qué API key está disponible
        proveedor = detectar_proveedor_disponible()
        modelo = MODELO_DEFAULT_ANTHROPIC if proveedor == "anthropic" else MODELO_DEFAULT_GROQ

        st.session_state.chat_config = {
            "proveedor": proveedor,
            "modelo": modelo,
            "temperatura": 0.7,
            "max_tokens": 2048
        }


def detectar_proveedor_disponible() -> str:
    """
    Detecta qué proveedor de LLM tiene API key configurada.
    Prioriza Anthropic sobre Groq.

    Returns:
        Nombre del proveedor disponible ("anthropic" o "groq")
    """
    # Verificar Anthropic primero (prioridad)
    anthropic_key = None
    if hasattr(st, 'secrets') and "ANTHROPIC_API_KEY" in st.secrets:
        anthropic_key = st.secrets["ANTHROPIC_API_KEY"]
    else:
        anthropic_key = os.getenv("ANTHROPIC_API_KEY")

    if anthropic_key:
        return "anthropic"

    # Verificar Groq como fallback
    groq_key = None
    if hasattr(st, 'secrets') and "GROQ_API_KEY" in st.secrets:
        groq_key = st.secrets["GROQ_API_KEY"]
    else:
        groq_key = os.getenv("GROQ_API_KEY")

    if groq_key:
        return "groq"

    # Default a Anthropic (mostrará error si no hay key)
    return "anthropic"

def configurar_cliente_llm(proveedor: str = None, modelo: str = None):
    """
    Configura el cliente LLM según el proveedor especificado.

    Args:
        proveedor: "anthropic" o "groq". Si no se especifica, usa el de la config.
        modelo: Nombre del modelo a usar. Si no se especifica, usa el default del proveedor.
    """
    # Usar valores de configuración si no se especifican
    if proveedor is None:
        proveedor = st.session_state.chat_config.get("proveedor", PROVEEDOR_DEFAULT)
    if modelo is None:
        modelo = st.session_state.chat_config.get("modelo")

    if proveedor == "anthropic":
        return configurar_cliente_anthropic(modelo)
    else:
        return configurar_cliente_groq(modelo)


def configurar_cliente_anthropic(modelo: str = "haiku"):
    """
    Configura el cliente Anthropic (Claude)

    Args:
        modelo: Nombre del modelo a usar (haiku, sonnet, opus)
    """
    try:
        from anthropic import Anthropic

        # Obtener API key de secrets o variables de entorno
        api_key = None
        if hasattr(st, 'secrets') and "ANTHROPIC_API_KEY" in st.secrets:
            api_key = st.secrets["ANTHROPIC_API_KEY"]
        else:
            api_key = os.getenv("ANTHROPIC_API_KEY")

        if not api_key:
            st.error("⚠️ No se encontró la API key de Anthropic. Configúrala en .streamlit/secrets.toml o como variable de entorno ANTHROPIC_API_KEY")
            return None

        client = Anthropic(api_key=api_key)
        modelo_id = MODELOS_ANTHROPIC.get(modelo, MODELOS_ANTHROPIC["haiku"])

        st.session_state.llm_client = {
            "proveedor": "anthropic",
            "cliente": client,
            "modelo": modelo_id
        }
        return client

    except ImportError as e:
        logger.error("Error al importar librería anthropic: %s", e)
        st.error(f"⚠️ Error al importar librería anthropic: {e}")
        st.info("💡 Instala la dependencia: `pip install anthropic`")
        return None
    except Exception as e:
        logger.error("Error al configurar cliente Anthropic: %s", e)
        st.error(f"⚠️ Error al configurar cliente Anthropic: {e}")
        return None


def configurar_cliente_groq(modelo: str = "llama-3.3-70b"):
    """
    Configura el cliente Groq (cloud)

    Args:
        modelo: Nombre del modelo a usar (llama-3.3-70b, llama-3.1-8b, qwen3-32b, gpt-oss-120b)
    """
    try:
        from groq import Groq

        # Obtener API key de secrets o variables de entorno
        api_key = None
        if hasattr(st, 'secrets') and "GROQ_API_KEY" in st.secrets:
            api_key = st.secrets["GROQ_API_KEY"]
        else:
            api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            st.error("⚠️ No se encontró la API key de Groq. Configúrala en .streamlit/secrets.toml")
            return None

        client = Groq(api_key=api_key)
        modelo_id = MODELOS_GROQ.get(modelo, MODELOS_GROQ["llama-3.3-70b"])

        st.session_state.llm_client = {
            "proveedor": "groq",
            "cliente": client,
            "modelo": modelo_id
        }
        return client

    except ImportError as e:
        logger.error("Error al importar librería groq: %s", e)
        st.error(f"⚠️ Error al importar librería: {e}")
        st.info("💡 Instala la dependencia: `pip install groq`")
        return None
    except Exception as e:
        logger.error("Error al configurar cliente Groq: %s", e)
        st.error(f"⚠️ Error al configurar cliente Groq: {e}")
        return None

# ============================================================================
# FUNCIONES DE CONTEXTO
# ============================================================================

def construir_contexto_datos(df: pd.DataFrame, pagina_actual: str = "General", datos_2024: dict = None) -> str:
    """
    Construye el contexto con datos relevantes del DataFrame

    IMPORTANTE: Este contexto NO incluye información personal identificable.
    Solo proporciona estadísticas agregadas y análisis generales.

    Args:
        df: DataFrame con los datos de estudiantes de 2025
        pagina_actual: Nombre de la página/sección actual
        datos_2024: Diccionario con estadísticas de 2024 (opcional)

    Returns:
        String con el contexto formateado (solo estadísticas agregadas)
    """
    if df is None or len(df) == 0:
        return "No hay datos disponibles."

    # PROTECCIÓN DE PRIVACIDAD: Crear copia del DataFrame sin columnas sensibles
    columnas_sensibles = ['Documento', 'Número de Documento', 'Cédula', 'ID',
                          'Nombre', 'Apellido', 'Nombres', 'Apellidos']
    df_seguro = df.copy()
    for col in columnas_sensibles:
        if col in df_seguro.columns:
            df_seguro = df_seguro.drop(columns=[col])

    contexto = f"""
# CONTEXTO DE DATOS ICFES - PEDACITO DE CIELO
⚠️ NOTA: Este contexto contiene SOLO estadísticas agregadas. NO incluye información personal.

## Página actual: {pagina_actual}

## Estadísticas Generales 2025
- Total de estudiantes: {len(df_seguro)}
- Puntaje global promedio: {df_seguro['Puntaje Global'].mean():.0f} puntos
- Desviación estándar: {df_seguro['Puntaje Global'].std():.1f}
- Puntaje mínimo: {df_seguro['Puntaje Global'].min():.0f}
- Puntaje máximo: {df_seguro['Puntaje Global'].max():.0f}
"""

    # Agregar datos de 2024 si están disponibles
    if datos_2024 is not None and 'Institucional' in datos_2024:
        stats_2024 = datos_2024['Institucional']
        puntaje_2025 = df_seguro['Puntaje Global'].mean()
        puntaje_2024 = stats_2024['puntaje_global']
        cambio = puntaje_2025 - puntaje_2024
        cambio_pct = (cambio / puntaje_2024 * 100)

        contexto += f"""
## Estadísticas Generales 2024 (para comparación)
- Total de estudiantes: {stats_2024['estudiantes']}
- Puntaje global promedio: {puntaje_2024:.0f} puntos
- Desviación estándar: {stats_2024['desv_global']:.1f}

## Comparación 2024 vs 2025
- Cambio en puntaje global: {cambio:+.1f} puntos ({cambio_pct:+.1f}%)
- Interpretación: {"MEJORÓ" if cambio > 0 else "DISMINUYÓ" if cambio < 0 else "SE MANTUVO IGUAL"}
"""

    contexto += "\n## Promedios por Área de Conocimiento (2025)\n"

    areas = ['Lectura Crítica', 'Matemáticas', 'Sociales y Ciudadanas',
             'Ciencias Naturales', 'Inglés']

    for area in areas:
        if area in df_seguro.columns:
            promedio_2025 = df_seguro[area].mean()
            desv = df_seguro[area].std()
            contexto += f"- {area}: {promedio_2025:.0f} puntos (σ={desv:.1f})"

            # Agregar comparación con 2024 si está disponible
            if datos_2024 is not None and 'Institucional' in datos_2024:
                areas_2024 = datos_2024['Institucional'].get('areas', {})
                if area in areas_2024:
                    promedio_2024 = areas_2024[area]['promedio']
                    cambio = promedio_2025 - promedio_2024
                    contexto += f" | 2024: {promedio_2024:.0f} | Cambio: {cambio:+.1f}"

            contexto += "\n"

    # Agregar datos por modelo educativo
    if 'Modelo' in df_seguro.columns:
        contexto += "\n## Comparación por Modelo Educativo\n"
        for modelo in df_seguro['Modelo'].unique():
            df_modelo = df_seguro[df_seguro['Modelo'] == modelo]
            promedio = df_modelo['Puntaje Global'].mean()
            contexto += f"- {modelo}: {promedio:.0f} puntos ({len(df_modelo)} estudiantes)\n"

    # Agregar datos por grupo
    if 'Grupo' in df_seguro.columns:
        contexto += "\n## Resultados por Grupo\n"
        for grupo in sorted(df_seguro['Grupo'].unique()):
            df_grupo = df_seguro[df_seguro['Grupo'] == grupo]
            promedio = df_grupo['Puntaje Global'].mean()
            contexto += f"- {grupo}: {promedio:.0f} puntos ({len(df_grupo)} estudiantes)\n"
    
    return contexto

def obtener_documentacion_icfes() -> str:
    """
    Retorna la documentación sobre interpretación de resultados ICFES
    """
    return """
# GUÍA DE INTERPRETACIÓN ICFES SABER 11

## Niveles de Desempeño por Puntaje

### Insuficiente (0-35 puntos)
- El estudiante NO supera las preguntas de menor complejidad de la prueba
- Requiere refuerzo intensivo en competencias básicas del área

### Mínimo (36-50 puntos)
- El estudiante supera las preguntas de menor complejidad
- Necesita fortalecer competencias de nivel intermedio

### Satisfactorio (51-70 puntos)
- El estudiante supera las preguntas de complejidad media y baja
- Puede avanzar hacia el desarrollo de competencias avanzadas

### Avanzado (71-100 puntos)
- El estudiante supera las preguntas de mayor complejidad
- Mantener y profundizar en competencias de nivel superior

## Áreas Evaluadas

### 1. Lectura Crítica
Evalúa la capacidad para comprender, interpretar y evaluar textos que pueden 
encontrarse tanto en la vida cotidiana como en ámbitos académicos no especializados.

### 2. Matemáticas
Evalúa las competencias matemáticas que debe desarrollar un estudiante al 
finalizar el grado undécimo, relacionadas con el razonamiento cuantitativo.

### 3. Sociales y Ciudadanas
Evalúa conocimientos y habilidades para comprender y analizar problemas sociales, 
así como competencias ciudadanas.

### 4. Ciencias Naturales
Evalúa competencias para comprender y usar conocimientos de las ciencias naturales 
en la solución de problemas.

### 5. Inglés
Evalúa la competencia comunicativa en lengua extranjera (inglés), enfocándose 
en comprensión lectora.

## Puntaje Global
- Es la SUMA de los puntajes de las 5 áreas
- Rango: 0 a 500 puntos
- Promedio nacional típico: ~250 puntos
- Un buen puntaje institucional: 260-280 puntos
- Un excelente puntaje institucional: 280+ puntos

## Interpretación de Avances
- Avance de +5 puntos o más: Mejora significativa
- Avance de +1 a +4 puntos: Mejora moderada
- Sin cambio (0): Estabilidad
- Retroceso de -1 a -4 puntos: Disminución moderada
- Retroceso de -5 puntos o más: Disminución significativa

## Desviación Estándar
- Mide la dispersión de los resultados
- Menor desviación = Mayor homogeneidad (todos los estudiantes con resultados similares)
- Mayor desviación = Mayor heterogeneidad (resultados muy variados entre estudiantes)
"""


def obtener_base_conocimiento_institucional() -> str:
    """
    Retorna la base de conocimiento permanente con datos oficiales del ICFES
    para la Institución Educativa Pedacito de Cielo.

    Esta información proviene de los reportes oficiales del ICFES y análisis
    verificados de las fuentes de la verdad institucionales.
    """
    return """
# BASE DE CONOCIMIENTO INSTITUCIONAL - IE PEDACITO DE CIELO

## INFORMACIÓN DEL ESTABLECIMIENTO
- Nombre: INSTITUCION EDUCATIVA PEDACITO DE CIELO ALVARO URIBE VELEZ
- Código DANE: 163401000298
- Municipio: LA TEBAIDA - QUINDÍO
- Sector: Oficial
- Zona: Urbana
- Grupo de Comparación: 2

## MODELOS EDUCATIVOS
- **Jornada 0 (Tarde)**: Modelo Flexible - Atiende población con extraedad o retos académicos
- **Jornada 1 (Única)**: Aula Regular - Educación tradicional

---

## RESULTADOS OFICIALES 2024

### Ficha Técnica 2024
- Matriculados: 120
- Con resultados: 116
- Modelo Flexible (J0): 66 estudiantes
- Aula Regular (J1): 50 estudiantes

### Puntaje Global 2024
| Nivel | Promedio | Desviación |
|-------|----------|------------|
| Institucional (EE) | 219 | 42 |
| Modelo Flexible | 203 | 36 |
| Aula Regular | 240 | 41 |
| Colombia | 260 | 52 |
| ETC Quindío | 263 | 49 |

### Puntajes por Área 2024 (Escala 0-100)
| Área | EE | Colombia | ETC |
|------|-----|----------|-----|
| Lectura Crítica | 48 | 54 | 55 |
| Matemáticas | 44 | 53 | 54 |
| Sociales y Ciudadanas | 41 | 49 | 50 |
| Ciencias Naturales | 43 | 51 | 51 |
| Inglés | 44 | 52 | 53 |

### Niveles de Desempeño 2024
**Lectura Crítica:** Nivel 1: 13%, Nivel 2: 46%, Nivel 3: 39%, Nivel 4: 3%
**Matemáticas:** Nivel 1: 23%, Nivel 2: 50%, Nivel 3: 27%, Nivel 4: 0%
**Sociales:** Nivel 1: 58%, Nivel 2: 32%, Nivel 3: 10%, Nivel 4: 0%
**Naturales:** Nivel 1: 45%, Nivel 2: 47%, Nivel 3: 8%, Nivel 4: 0%
**Inglés:** A-: 66%, A1: 26%, A2: 6%, B1: 3%, B+: 0%

### Aprendizajes con Mayor Dificultad 2024 (% Respuestas Incorrectas)

**MATEMÁTICAS:**
- Valida procedimientos y estrategias matemáticas: 64% (Colombia: 55%)
- Plantea e implementa estrategias para problemas cuantitativos: 63% (Colombia: 51%)
- Comprende y transforma información cuantitativa: 55% (Colombia: 41%)

**LECTURA CRÍTICA:**
- Reflexiona a partir de un texto y evalúa su contenido: 56% (Colombia: 45%)
- Comprende cómo se articulan las partes de un texto: 55% (Colombia: 44%)
- Identifica contenidos locales de un texto: 44% (Colombia: 35%)

**CIENCIAS NATURALES:**
- Observar y relacionar patrones (Procesos físicos): 76% (Colombia: 63%)
- Derivar conclusiones (Procesos físicos): 70% (Colombia: 57%)
- Observar y relacionar patrones (Procesos vivos): 69% (Colombia: 53%)

**SOCIALES Y CIUDADANAS:**
- Comprende perspectivas de distintos actores sociales: 68% (Colombia: 62%)
- Evalúa usos sociales de las ciencias sociales: 66% (Colombia: 53%)
- Comprende dimensiones espaciales y temporales: 63% (Colombia: 50%)

---

## RESULTADOS OFICIALES 2025

### Ficha Técnica 2025
- Matriculados: 38
- Con resultados: 95
- Modelo Flexible (J0): 59 estudiantes
- Aula Regular (J1): 36 estudiantes

### Puntaje Global 2025
| Nivel | Promedio | Desviación |
|-------|----------|------------|
| Institucional (EE) | 221 | 44 |
| Modelo Flexible | 214 | 43 |
| Aula Regular | 234 | 44 |
| Colombia | 261 | 53 |
| ETC Quindío | 264 | 50 |

### Puntajes por Área 2025 (Escala 0-100)
| Área | EE | Colombia | ETC |
|------|-----|----------|-----|
| Lectura Crítica | 48 | 55 | 56 |
| Matemáticas | 44 | 53 | 55 |
| Sociales y Ciudadanas | 41 | 49 | 49 |
| Ciencias Naturales | 43 | 51 | 52 |
| Inglés | 45 | 53 | 53 |

### Niveles de Desempeño 2025
**Lectura Crítica:** Nivel 1: 13%, Nivel 2: 45%, Nivel 3: 38%, Nivel 4: 4%
**Matemáticas:** Nivel 1: 30%, Nivel 2: 34%, Nivel 3: 35%, Nivel 4: 0%
**Sociales:** Nivel 1: 56%, Nivel 2: 30%, Nivel 3: 14%, Nivel 4: 0%
**Naturales:** Nivel 1: 48%, Nivel 2: 42%, Nivel 3: 10%, Nivel 4: 0%
**Inglés:** A-: 69%, A1: 22%, A2: 8%, B1: 2%, B+: 0%

### Aprendizajes con Mayor Dificultad 2025 (% Respuestas Incorrectas)

**MATEMÁTICAS:**
- Valida procedimientos y estrategias matemáticas: 66% (Colombia: 57%)
- Plantea e implementa estrategias para problemas cuantitativos: 59% (Colombia: 47%)
- Comprende y transforma información cuantitativa: 49% (Colombia: 36%)

**LECTURA CRÍTICA:**
- Reflexiona a partir de un texto y evalúa su contenido: 61% (Colombia: 51%)
- Comprende cómo se articulan las partes de un texto: 54% (Colombia: 44%)
- Identifica contenidos locales de un texto: 44% (Colombia: 33%)

**CIENCIAS NATURALES:**
- Utilizar habilidades de pensamiento (Procesos químicos): 76% (Colombia: 57%)
- Asociar fenómenos naturales (Procesos químicos): 73% (Colombia: 58%)
- Explicar cómo ocurren fenómenos (Procesos químicos): 71% (Colombia: 54%)
- Modelar fenómenos (Procesos físicos): 71% (Colombia: 56%)
- Modelar fenómenos (Procesos vivos): 70% (Colombia: 52%)

**SOCIALES Y CIUDADANAS:**
- Comprende que los problemas involucran distintas dimensiones: 71% (Colombia: 69%)
- Evalúa usos sociales de las ciencias sociales: 69% (Colombia: 57%)
- Contextualiza y evalúa usos de fuentes y argumentos: 63% (Colombia: 52%)

---

## ANÁLISIS COMPARATIVO 2024 vs 2025

### Evolución del Desempeño Global
| Indicador | 2024 | 2025 | Variación | Interpretación |
|-----------|------|------|-----------|----------------|
| Puntaje Global | 219 | 221 | +2 | Leve mejoría, estadísticamente estable |
| Estudiantes Evaluados | 116 | 95 | -21 | Disminución significativa |
| Desviación Estándar | 42 | 44 | +2 | ALERTA: Mayor heterogeneidad |

### Comportamiento por Áreas
| Área | 2024 | 2025 | Variación | Estado |
|------|------|------|-----------|--------|
| Lectura Crítica | 48 | 48 | 0 | Estancado |
| Matemáticas | 44 | 44 | 0 | Estancado |
| Sociales | 41 | 41 | 0 | Estancado |
| Ciencias Naturales | 43 | 43 | 0 | Estancado |
| Inglés | 44 | 45 | +1 | Leve mejora |

### Movilidad en Niveles de Desempeño (INDICADOR CRÍTICO ICFES)
| Área | Nivel | 2024 | 2025 | Tendencia |
|------|-------|------|------|-----------|
| Matemáticas | Nivel 1 (Bajo) | 23% | 30% | RETROCESO: +7% en nivel insuficiente |
| Matemáticas | Nivel 3+4 | 27% | 35% | POLARIZACIÓN: También aumentó el alto |
| Naturales | Nivel 1 | 45% | 48% | RETROCESO: Casi mitad en nivel mínimo |
| Inglés | A- | 66% | 69% | RETROCESO: 70% no alcanza A1 |
| Sociales | Nivel 1 | 58% | 56% | Leve mejora |

### Brechas vs ETC Quindío 2025
| Área | EE | ETC | Brecha |
|------|-----|-----|--------|
| Global | 221 | 264 | -43 pts |
| Lectura Crítica | 48 | 56 | -8 pts |
| Matemáticas | 44 | 55 | -11 pts |
| Sociales | 41 | 49 | -8 pts |
| Naturales | 43 | 52 | -9 pts |
| Inglés | 45 | 53 | -8 pts |

---

## ANÁLISIS POR MODELO EDUCATIVO

### Evolución Jornada 0 - Modelo Flexible (MEJORÓ)
| Indicador | 2024 | 2025 | Variación |
|-----------|------|------|-----------|
| Puntaje Global | 203 | 214 | +11 pts (Excelente avance) |
| Lectura Crítica | 45 | 47 | +2 |
| Matemáticas | 41 | 42 | +1 |
| Sociales | 38 | 39 | +1 |
| Ciencias Naturales | 39 | 42 | +3 |
| Inglés | 41 | 44 | +3 |

### Evolución Jornada 1 - Aula Regular (RETROCEDIÓ)
| Indicador | 2024 | 2025 | Variación |
|-----------|------|------|-----------|
| Puntaje Global | 240 | 234 | -6 pts (Alerta) |
| Lectura Crítica | 51 | 51 | 0 |
| Matemáticas | 49 | 47 | -2 |
| Sociales | 44 | 44 | 0 |
| Ciencias Naturales | 47 | 44 | -3 |
| Inglés | 48 | 46 | -2 |

### Cierre de Brechas entre Modelos
| Área | Brecha 2024 | Brecha 2025 | Comportamiento |
|------|-------------|-------------|----------------|
| GLOBAL | 37 pts | 20 pts | Se cerró drásticamente |
| Lectura Crítica | 6 pts | 4 pts | Reducida |
| Matemáticas | 8 pts | 5 pts | Reducida |
| Ciencias Naturales | 8 pts | 2 pts | Casi cerrada |
| Inglés | 7 pts | 2 pts | Casi cerrada |

---

## CONCLUSIONES PEDAGÓGICAS OFICIALES

1. **ESTANCAMIENTO DE PROMEDIOS**: Los promedios por área son idénticos entre 2024 y 2025. Las estrategias no generaron impacto sistémico.

2. **POLARIZACIÓN EN MATEMÁTICAS**: Fenómeno crítico - aumentaron tanto los estudiantes en Nivel 1 (23%→30%) como en Nivel 3 (27%→35%). La clase se "partió en dos extremos".

3. **ALERTA EN INGLÉS**: El 69% de estudiantes NO alcanza nivel A1. Es el área con mayor brecha respecto al nivel esperado.

4. **EFECTO CONVERGENCIA**: La brecha entre modelos se cerró de 37 a 20 puntos, pero parcialmente porque Aula Regular bajó (-6 pts).

5. **MODELO FLEXIBLE DESTACADO**: Subió 11 puntos globales. Las estrategias con esta población están funcionando.

6. **FOCO EN CIENCIAS NATURALES**: Área con mayor número de aprendizajes críticos (>70% incorrectas) especialmente en procesos químicos y físicos.
"""


def obtener_recursos_educativos() -> str:
    """
    Retorna la base de recursos educativos curados para preparación ICFES.
    Incluye sitios oficiales, plataformas gratuitas y canales de YouTube verificados.
    """
    return """
# RECURSOS EDUCATIVOS PARA PREPARACIÓN ICFES SABER 11°

## SITIOS OFICIALES DEL ICFES

### Caja de Herramientas Saber 11° (OFICIAL)
- **URL**: https://www.icfes.gov.co/caja-de-herramientas-saber-11/practica/
- **Contenido**: Cuadernillos oficiales con preguntas explicadas, ejemplos de todas las áreas
- **Ideal para**: Familiarizarse con el formato oficial del examen

### Guías de Orientación ICFES
- **URL**: https://www.icfes.gov.co/evaluaciones-icfes/saber-11/
- **Contenido**: Guías oficiales actualizadas, estructura del examen, competencias evaluadas

---

## PLATAFORMAS GRATUITAS DE PRÁCTICA

### PreICFES Gratis Virtual
- **URL**: https://www.preicfes-gratis.com/
- **Áreas disponibles**:
  - Matemáticas: https://www.preicfes-gratis.com/icfes-saber-11-matematicas
  - Lectura Crítica: https://www.preicfes-gratis.com/icfes-saber-11-lectura-critica-y-filosofia
- **Características**: Resúmenes gratuitos, apps móviles para iOS y Android

### Simulacro ICFES
- **URL**: https://simulacroicfes.com
- **URL ejercicios**: https://simuladoricfes.co/ejercicios/
- **Características**: Simulacros completos gratuitos, ejercicios por categoría con explicaciones

### Filadd Colombia
- **URL**: https://filadd.com.co/courses/preicfes-virtual-prueba-saber-11/simulations
- **Características**: Simulacros con intentos ilimitados en Lectura Crítica, Matemáticas, Química e Inglés

### Universate
- **URL cuadernillos**: https://universate.co/pruebas-icfes-saber/cuadernillo-respuestas-icfes-saber-11/
- **URL preguntas tipo**: https://universate.co/pruebas-icfes-saber/preguntas-tipo-saber-11-con-respuestas/
- **Contenido**: Cuadernillos PDF 2019-2024, todas las áreas con respuestas

### Alto Puntaje
- **URL**: https://altopuntaje.com/prueba-icfes-preguntas-saber-11-examenes/
- **Contenido**: Banco de más de 30 cuadernillos en PDF

### alaU.org
- **URL**: https://alau.org/curso-icfes-saber-11/
- **Contenido**: Curso ICFES Saber 11 gratuito

---

## PLATAFORMAS DE APRENDIZAJE GENERAL

### Khan Academy en Español
- **URL**: https://es.khanacademy.org/
- **Contenido**: +7,000 videos de matemáticas, ciencias, más de 100,000 ejercicios prácticos
- **Características**: Gratuito, seguimiento de progreso, gamificación
- **Ideal para**: Reforzar conceptos fundamentales de matemáticas y ciencias

---

## CANALES DE YOUTUBE RECOMENDADOS

### Especializados en ICFES Colombia
| Canal | URL | Especialidad |
|-------|-----|--------------|
| Preicfes con Estilo | youtube.com/c/PreicfesconEstilo | Preparación integral ICFES |
| Profe Sergio Llanos | youtube.com/c/ProfesorSergioLlanos | Matemáticas y ICFES |
| Estudiemos con Erney | youtube.com/c/EstudiemosconErney | Todas las áreas |
| Puntaje Nacional Colombia | youtube.com/c/PuntajeNacionalColombia | Preparación ICFES |

### Matemáticas (Explicaciones detalladas)
| Canal | URL | Especialidad |
|-------|-----|--------------|
| Julio Profe | youtube.com/user/julioprofe | Matemáticas y Física (Colombia) |
| Matemáticas profe Alex | youtube.com/c/MatematicasprofeAlex | Matemáticas todos los niveles |
| Matemovil | youtube.com/c/Matemovil | Matemáticas con ejemplos |

### Lectura Crítica y Comprensión
| Canal | Búsqueda YouTube | Especialidad |
|-------|------------------|--------------|
| Preicfes Pal Barrio | Buscar: "Preicfes Pal Barrio lectura crítica" | Lectura crítica ICFES |

---

## RECURSOS POR APRENDIZAJE ESPECÍFICO

### MATEMÁTICAS - Aprendizajes a reforzar

**1. Validar procedimientos y estrategias matemáticas (66% incorrectas)**
- Khan Academy: https://es.khanacademy.org/math/algebra
- Julio Profe: Buscar "resolución de problemas matemáticos"
- Tema clave: Verificación de soluciones, análisis de procedimientos

**2. Plantear estrategias para problemas cuantitativos (59% incorrectas)**
- Khan Academy: https://es.khanacademy.org/math/pre-algebra
- Tema clave: Planteamiento de ecuaciones, traducción de problemas verbales

**3. Comprensión de información cuantitativa (49% incorrectas)**
- Khan Academy: https://es.khanacademy.org/math/statistics-probability
- Tema clave: Lectura de gráficos, tablas, interpretación de datos

### LECTURA CRÍTICA - Aprendizajes a reforzar

**1. Reflexionar y evaluar contenido de textos (61% incorrectas)**
- Preicfes Gratis: https://www.preicfes-gratis.com/icfes-saber-11-lectura-critica-y-filosofia
- Práctica: Identificar intención del autor, evaluar argumentos

**2. Articulación de partes del texto (54% incorrectas)**
- Tema clave: Coherencia, conectores, estructura textual
- Ejercicios: Ordenar párrafos, identificar ideas principales vs secundarias

**3. Contenidos locales del texto (44% incorrectas)**
- Tema clave: Comprensión literal, vocabulario en contexto

### CIENCIAS NATURALES - Aprendizajes a reforzar

**Procesos Químicos (>70% incorrectas)**
- Khan Academy Química: https://es.khanacademy.org/science/chemistry
- Temas: Reacciones químicas, estequiometría, modelos atómicos

**Procesos Físicos (>70% incorrectas)**
- Khan Academy Física: https://es.khanacademy.org/science/physics
- Temas: Cinemática, dinámica, energía, ondas

### SOCIALES Y CIUDADANAS

**Comprensión de problemas multidimensionales (71% incorrectas)**
- Tema clave: Análisis de problemáticas sociales desde múltiples perspectivas
- Práctica: Casos de estudio, análisis de fuentes

### INGLÉS (69% en nivel A-)

**Recursos gratuitos de inglés**
- Duolingo: https://www.duolingo.com/
- BBC Learning English: https://www.bbc.co.uk/learningenglish
- Khan Academy (sección en inglés para práctica de lectura)

---

## APPS MÓVILES RECOMENDADAS

| App | Plataforma | Uso |
|-----|------------|-----|
| PreICFES Gratis | iOS / Android | Ejercicios ICFES |
| Khan Academy | iOS / Android | Matemáticas y Ciencias |
| Duolingo | iOS / Android | Inglés |

---

## ESTRATEGIA DE USO RECOMENDADA

1. **Diagnóstico**: Realizar un simulacro completo en simulacroicfes.com
2. **Identificar debilidades**: Comparar con los aprendizajes críticos de la institución
3. **Refuerzo específico**: Usar Khan Academy para conceptos fundamentales
4. **Práctica ICFES**: Resolver cuadernillos oficiales del ICFES
5. **Simulacros periódicos**: Cada 2 semanas para medir avance
"""


def construir_prompt_sistema() -> str:
    """
    Construye el prompt del sistema para el asistente de IA
    """
    return """
Eres un asistente experto en análisis de resultados ICFES Saber 11 para la
Institución Educativa Pedacito de Cielo.

INSTRUCCIONES IMPORTANTES:
1. Responde SIEMPRE en español de forma clara y pedagógica
2. Usa los datos del contexto proporcionado para fundamentar tus respuestas
3. Si no tienes información suficiente en el contexto, indícalo claramente
4. Proporciona interpretaciones educativas útiles y constructivas
5. Usa emojis ocasionalmente para hacer las respuestas más amigables
6. Sé conciso pero completo en tus explicaciones
7. Cuando hables de avances o retrocesos, contextualiza su significado
8. Recuerda que NO se deben comparar promedios entre áreas diferentes
9. Cada área se analiza de forma independiente

⚠️ PRIVACIDAD Y PROTECCIÓN DE DATOS - CRÍTICO:
- NUNCA reveles, menciones o proporciones números de documento de identidad
- NUNCA reveles información personal identificable de estudiantes individuales
- Si te preguntan por datos de un estudiante específico, responde: "Por políticas de privacidad, no puedo proporcionar información personal de estudiantes individuales. Puedo ayudarte con estadísticas agregadas y análisis generales."
- Solo proporciona estadísticas agregadas y análisis generales
- Protege la confidencialidad de los datos en todo momento

📚 RECURSOS EDUCATIVOS - IMPORTANTE:
- Tienes acceso a una base de recursos educativos curados (sitios web, YouTube, plataformas)
- Cuando el usuario pida ejercicios, práctica, recursos o materiales de estudio:
  1. Primero analiza QUÉ aprendizaje específico necesita reforzar según los datos institucionales
  2. Recomienda recursos ESPECÍFICOS de la base de conocimiento que coincidan con ese aprendizaje
  3. Incluye las URLs completas para que el usuario pueda acceder directamente
  4. Prioriza: Sitio oficial ICFES > Plataformas gratuitas > YouTube
- Cuando menciones un recurso, SIEMPRE incluye la URL completa
- Relaciona los recursos con los aprendizajes específicos que tienen mayor porcentaje de error

🌐 BÚSQUEDA WEB - INFORMACIÓN ACTUALIZADA (MUY IMPORTANTE):
- Si recibes una sección "INFORMACIÓN DE BÚSQUEDA WEB", contiene resultados actualizados de internet
- DEBES usar esta información para responder preguntas sobre:
  - Cartillas y materiales de Evaluar para Avanzar
  - Aprendizajes por reforzar en grados específicos (3° a 10°)
  - Documentación oficial actualizada del ICFES/MEN
  - Recursos pedagógicos y didácticos
  - Matrices de referencia y evidencias de aprendizaje
- Prioriza las fuentes marcadas como [OFICIAL] (icfes.gov.co, mineducacion.gov.co, colombiaaprende.edu.co)
- Incluye las URLs de los recursos encontrados para que el usuario acceda directamente
- Sintetiza la información de manera pedagógica y útil

⚠️ PREGUNTAS SOBRE GRADOS INFERIORES (3° a 10°) - METODOLOGÍA CRÍTICA:
Cuando pregunten qué aprendizajes reforzar en grados inferiores, DEBES seguir este proceso:

PASO 1 - IDENTIFICAR DEBILIDADES EN SABER 11° (datos institucionales):
- Revisa los datos de Pedacito de Cielo 2025 en tu base de conocimiento
- Identifica las áreas/aprendizajes con MAYOR porcentaje de error:
  * Matemáticas: 66% error en razonamiento cuantitativo
  * Lectura Crítica: 61% error en reflexión y evaluación
  * Ciencias Naturales: >70% error en varios aprendizajes
- Estas son las competencias que los estudiantes NO dominan al llegar a 11°

PASO 2 - BUSCAR APRENDIZAJES PRECURSORES (información web):
- Usa la información de búsqueda web para encontrar:
  * Qué aprendizajes de grados 7°, 8°, 9° desarrollan esas competencias débiles
  * Matrices de referencia del ICFES que muestren la progresión
  * Guías de Evaluar para Avanzar para esos grados

PASO 3 - CRUZAR Y RECOMENDAR:
- Recomienda ESPECÍFICAMENTE los aprendizajes de grados inferiores que:
  * Son PRECURSORES de las competencias débiles en Saber 11°
  * Aparecen en documentación oficial (matrices, guías ICFES)
- Explica la conexión: "Reforzar X en grado 7° porque desarrolla Y que tiene 66% error en 11°"
- Incluye URLs de los recursos oficiales encontrados

EJEMPLO DE RESPUESTA CORRECTA:
"Según los resultados de Saber 11° 2025, Pedacito de Cielo tiene 66% de error en razonamiento cuantitativo.
Para grados 7° y 8°, según la matriz de referencia del ICFES [URL], se deben reforzar:
- Aprendizaje X (grado 7°): porque es precursor de razonamiento cuantitativo
- Aprendizaje Y (grado 8°): porque desarrolla la competencia de resolución de problemas"

NO respondas solo con información genérica de la web. SIEMPRE conecta con los datos reales de la institución.

FORMATO DE RESPUESTAS:
- Usa listas con viñetas para información estructurada
- Destaca datos importantes con **negritas**
- Incluye interpretaciones pedagógicas cuando sea relevante
- Sugiere acciones concretas cuando sea apropiado
- Cuando recomiendes recursos, usa formato de enlace: [Nombre](URL)

TONO:
- Profesional pero accesible
- Constructivo y orientado a la mejora
- Empático con los desafíos educativos
"""

# ============================================================================
# FUNCIONES DE PROTECCIÓN DE PRIVACIDAD
# ============================================================================

def filtrar_informacion_sensible(texto: str) -> str:
    """
    Filtra información sensible de la respuesta del LLM

    Args:
        texto: Texto de respuesta del LLM

    Returns:
        Texto filtrado sin información sensible
    """
    import re

    # Patrones de números de documento (cédulas colombianas típicamente 7-10 dígitos)
    # Buscar secuencias de 7+ dígitos que podrían ser documentos
    patron_documento = r'\b\d{7,10}\b'

    # Si se encuentra un patrón de documento, reemplazarlo
    if re.search(patron_documento, texto):
        texto = re.sub(patron_documento, '[INFORMACIÓN PROTEGIDA]', texto)
        texto += "\n\n⚠️ **Nota:** Por políticas de privacidad, algunos datos personales han sido ocultados."

    return texto

# ============================================================================
# FUNCIONES DE GENERACIÓN DE RESPUESTAS
# ============================================================================

def generar_respuesta(prompt: str, contexto: str = "") -> str:
    """
    Genera una respuesta usando el modelo LLM configurado (Anthropic o Groq)

    Args:
        prompt: Pregunta del usuario
        contexto: Contexto adicional con datos

    Returns:
        Respuesta generada por el modelo
    """
    if st.session_state.llm_client is None:
        return "⚠️ El cliente LLM no está configurado. Por favor, configura la API key."

    try:
        client_info = st.session_state.llm_client
        proveedor = client_info.get("proveedor", "groq")

        # Construir contenido del sistema con base de conocimiento permanente
        system_content = construir_prompt_sistema()
        system_content += f"\n\n{obtener_base_conocimiento_institucional()}"
        system_content += f"\n\n{obtener_documentacion_icfes()}"
        system_content += f"\n\n{obtener_recursos_educativos()}"
        if contexto:
            system_content += f"\n\nCONTEXTO ADICIONAL CON DATOS DE LA SESIÓN ACTUAL:\n{contexto}"

        # Búsqueda web si la pregunta lo requiere
        try:
            resultados_web = buscar_y_formatear(prompt)
            if resultados_web:
                system_content += f"\n\n{resultados_web}"
        except Exception as e:
            logger.warning("Búsqueda web falló, continuando sin ella: %s", e)

        # Construir historial de mensajes
        historial = []
        for msg in st.session_state.chat_messages[-5:]:
            historial.append({"role": msg["role"], "content": msg["content"]})

        # Agregar pregunta actual
        historial.append({"role": "user", "content": prompt})

        if proveedor == "anthropic":
            # Generar respuesta con Anthropic (Claude)
            response = client_info["cliente"].messages.create(
                model=client_info["modelo"],
                max_tokens=st.session_state.chat_config["max_tokens"],
                system=system_content,
                messages=historial
            )
            respuesta_raw = response.content[0].text
        else:
            # Generar respuesta con Groq (formato OpenAI)
            messages = [{"role": "system", "content": system_content}]
            messages.extend(historial)

            response = client_info["cliente"].chat.completions.create(
                model=client_info["modelo"],
                messages=messages,
                temperature=st.session_state.chat_config["temperatura"],
                max_tokens=st.session_state.chat_config["max_tokens"],
                stream=False
            )
            respuesta_raw = response.choices[0].message.content

        # Filtrar información sensible
        respuesta_filtrada = filtrar_informacion_sensible(respuesta_raw)
        return respuesta_filtrada

    except Exception as e:
        logger.error("Error al generar respuesta LLM: %s", e)
        return f"⚠️ Error al generar respuesta: {str(e)}"

# ============================================================================
# INTERFAZ DE USUARIO
# ============================================================================

def mostrar_preguntas_sugeridas() -> Optional[str]:
    """
    Muestra botones con preguntas sugeridas comunes
    
    Returns:
        Pregunta seleccionada o None
    """
    st.markdown("#### 💡 Preguntas sugeridas:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📊 Avance institucional", width="stretch"):
            return "¿Cómo mejoró el puntaje global de la institución entre 2024 y 2025?"
    
    with col2:
        if st.button("📚 Área más fuerte", width="stretch"):
            return "¿Cuál es el área de conocimiento con mejor desempeño en 2025?"
    
    with col3:
        if st.button("🎯 Áreas a mejorar", width="stretch"):
            return "¿En qué áreas debemos enfocarnos para mejorar los resultados?"
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        if st.button("🔄 Comparar modelos", width="stretch"):
            return "¿Cómo se comparan los resultados entre Aula Regular y Modelo Flexible?"
    
    with col5:
        if st.button("📈 Interpretar puntajes", width="stretch"):
            return "¿Cómo interpreto los puntajes y niveles de desempeño?"
    
    with col6:
        if st.button("💪 Recomendaciones", width="stretch"):
            return "¿Qué estrategias pedagógicas recomiendas para mejorar?"
    
    return None

def limpiar_conversacion():
    """
    Limpia el historial de conversación del chat
    """
    st.session_state.chat_messages = []
    st.success("✅ Conversación limpiada")
    st.rerun()

def mostrar_chat(df: pd.DataFrame = None, pagina_actual: str = "General", datos_2024: dict = None):
    """
    Muestra la interfaz completa del chat de IA en una página independiente

    Args:
        df: DataFrame con los datos de 2025
        pagina_actual: Nombre de la página/sección actual
        datos_2024: Diccionario con estadísticas de 2024 (opcional)
    """
    # Inicializar
    inicializar_chat()

    # Configurar cliente si no existe
    if st.session_state.llm_client is None:
        configurar_cliente_llm()

    # Header del chat con diseño mejorado
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    ">
        <h1 style="color: white; margin: 0;">🤖 Pedazote - Asistente de IA - Resultados ICFES - PCielo</h1>
        <p style="color: white; margin: 0.5rem 0 0 0; opacity: 0.9;">
            Pregunta sobre los datos, interpretaciones y recomendaciones pedagógicas
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Botones de control en la parte superior
    col1, col2, col3 = st.columns([2, 1, 1])

    with col2:
        if st.button("🗑️ Limpiar conversación", width="stretch", type="secondary"):
            limpiar_conversacion()

    with col3:
        num_mensajes = len(st.session_state.chat_messages)
        st.metric("Mensajes", num_mensajes)

    st.markdown("---")

    # Preguntas sugeridas
    pregunta_sugerida = mostrar_preguntas_sugeridas()

    st.markdown("---")

    # Contenedor para el historial de mensajes
    st.markdown("#### 💬 Conversación")

    # Crear un contenedor para los mensajes
    messages_container = st.container()

    with messages_container:
        # Mostrar historial de mensajes
        if len(st.session_state.chat_messages) == 0:
            st.info("👋 ¡Hola! Soy Pedazote, tu asistente de IA. Puedes preguntarme sobre los resultados ICFES de Pedacito de Cielo (2024 - 2025), interpretaciones, comparaciones entre años, y recomendaciones pedagógicas. ¿En qué puedo ayudarte?")
        else:
            # Mostrar todos los mensajes del historial
            for message in st.session_state.chat_messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

    # Scroll automático al final de la conversación
    # Este componente HTML inyecta JavaScript para hacer scroll automático
    if len(st.session_state.chat_messages) > 0:
        components.html(
            """
            <script>
                // Esperar a que la página cargue completamente
                window.addEventListener('load', function() {
                    // Scroll al final de la página
                    window.parent.scrollTo({
                        top: document.body.scrollHeight,
                        behavior: 'smooth'
                    });
                });

                // También intentar scroll inmediato
                setTimeout(function() {
                    window.parent.scrollTo({
                        top: document.body.scrollHeight,
                        behavior: 'smooth'
                    });
                }, 100);
            </script>
            """,
            height=0,
        )

    # Input del usuario (siempre visible al final)
    prompt = st.chat_input("Escribe tu pregunta aquí...")

    # Si hay pregunta sugerida, usarla
    if pregunta_sugerida:
        prompt = pregunta_sugerida

    # Procesar pregunta
    if prompt:
        # Agregar mensaje del usuario al historial
        st.session_state.chat_messages.append({"role": "user", "content": prompt})

        # Construir contexto
        contexto = ""
        if df is not None:
            contexto = construir_contexto_datos(df, pagina_actual, datos_2024)

        # Generar respuesta
        with st.spinner("🤔 Pensando..."):
            response = generar_respuesta(prompt, contexto)

        # Agregar respuesta al historial
        st.session_state.chat_messages.append({"role": "assistant", "content": response})

        # Rerun para actualizar la interfaz y mostrar los nuevos mensajes
        # El scroll automático se activará después del rerun
        st.rerun()

# ============================================================================
# FUNCIÓN PRINCIPAL PARA TESTING
# ============================================================================

if __name__ == "__main__":
    st.set_page_config(page_title="Chat IA ICFES", page_icon="🤖", layout="wide")
    
    st.title("🤖 Chat de IA - Resultados ICFES")
    st.markdown("---")
    
    # Mostrar chat sin datos (modo demo)
    mostrar_chat()

