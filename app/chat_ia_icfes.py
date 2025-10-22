#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo de Chat de IA para Análisis de Resultados ICFES
Institución Educativa Pedacito de Cielo

Este módulo implementa un asistente conversacional de IA que ayuda a los usuarios
a interpretar y analizar los resultados del examen ICFES Saber 11.

Características:
- Respuestas contextualizadas con datos reales
- Soporte para múltiples proveedores LLM (Groq, Ollama, Together.ai)
- Memoria conversacional
- Streaming de respuestas
- Preguntas sugeridas

Autor: Sistema de Análisis ICFES
Fecha: 2025-10-22
"""

import streamlit as st
import pandas as pd
from typing import Dict, List, Optional
import os

# ============================================================================
# CONFIGURACIÓN
# ============================================================================

# Configuración de modelos disponibles en Groq (cloud)
MODELOS_DISPONIBLES = {
    "llama-3.3-70b": "llama-3.3-70b-versatile",
    "llama-3.1-8b": "llama-3.1-8b-instant",
    "qwen3-32b": "qwen/qwen3-32b",
    "gpt-oss-120b": "openai/gpt-oss-120b"
}

# Configuración por defecto
MODELO_DEFAULT = "llama-3.3-70b"

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

    # Configuración
    if "chat_config" not in st.session_state:
        st.session_state.chat_config = {
            "modelo": MODELO_DEFAULT,
            "temperatura": 0.7,
            "max_tokens": 2048
        }

def configurar_cliente_llm(modelo: str = "llama-3.3-70b"):
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
        st.session_state.llm_client = {
            "cliente": client,
            "modelo": MODELOS_DISPONIBLES[modelo]
        }
        return client

    except ImportError as e:
        st.error(f"⚠️ Error al importar librería: {e}")
        st.info("💡 Instala la dependencia: `pip install groq`")
        return None
    except Exception as e:
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

FORMATO DE RESPUESTAS:
- Usa listas con viñetas para información estructurada
- Destaca datos importantes con **negritas**
- Incluye interpretaciones pedagógicas cuando sea relevante
- Sugiere acciones concretas cuando sea apropiado

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
    Genera una respuesta usando el modelo LLM configurado
    
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
        
        # Construir mensajes
        messages = [
            {"role": "system", "content": construir_prompt_sistema()},
        ]
        
        # Agregar contexto si existe
        if contexto:
            messages.append({
                "role": "system", 
                "content": f"CONTEXTO CON DATOS ACTUALES:\n{contexto}\n\n{obtener_documentacion_icfes()}"
            })
        
        # Agregar historial de conversación (últimos 5 mensajes)
        for msg in st.session_state.chat_messages[-5:]:
            messages.append({"role": msg["role"], "content": msg["content"]})
        
        # Agregar pregunta actual
        messages.append({"role": "user", "content": prompt})

        # Generar respuesta con Groq
        response = client_info["cliente"].chat.completions.create(
            model=client_info["modelo"],
            messages=messages,
            temperature=st.session_state.chat_config["temperatura"],
            max_tokens=st.session_state.chat_config["max_tokens"],
            stream=False
        )

        # Obtener respuesta y filtrar información sensible
        respuesta_raw = response.choices[0].message.content
        respuesta_filtrada = filtrar_informacion_sensible(respuesta_raw)

        return respuesta_filtrada

    except Exception as e:
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
        if st.button("📊 Avance institucional", use_container_width=True):
            return "¿Cómo mejoró el puntaje global de la institución entre 2024 y 2025?"
    
    with col2:
        if st.button("📚 Área más fuerte", use_container_width=True):
            return "¿Cuál es el área de conocimiento con mejor desempeño en 2025?"
    
    with col3:
        if st.button("🎯 Áreas a mejorar", use_container_width=True):
            return "¿En qué áreas debemos enfocarnos para mejorar los resultados?"
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        if st.button("🔄 Comparar modelos", use_container_width=True):
            return "¿Cómo se comparan los resultados entre Aula Regular y Modelo Flexible?"
    
    with col5:
        if st.button("📈 Interpretar puntajes", use_container_width=True):
            return "¿Cómo interpreto los puntajes y niveles de desempeño?"
    
    with col6:
        if st.button("💪 Recomendaciones", use_container_width=True):
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
        <h1 style="color: white; margin: 0;">🤖 Asistente de IA - Resultados ICFES</h1>
        <p style="color: white; margin: 0.5rem 0 0 0; opacity: 0.9;">
            Pregunta sobre los datos, interpretaciones y recomendaciones pedagógicas
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Botones de control en la parte superior
    col1, col2, col3 = st.columns([2, 1, 1])

    with col2:
        if st.button("🗑️ Limpiar conversación", use_container_width=True, type="secondary"):
            limpiar_conversacion()

    with col3:
        num_mensajes = len(st.session_state.chat_messages)
        st.metric("Mensajes", num_mensajes)

    st.markdown("---")

    # Preguntas sugeridas
    st.markdown("#### 💡 Preguntas Sugeridas")
    pregunta_sugerida = mostrar_preguntas_sugeridas()

    st.markdown("---")

    # Contenedor para el historial de mensajes
    st.markdown("#### 💬 Conversación")

    # Mostrar historial de mensajes
    if len(st.session_state.chat_messages) == 0:
        st.info("👋 ¡Hola! Soy tu asistente de IA. Puedes preguntarme sobre los resultados ICFES, interpretaciones, comparaciones entre años, y recomendaciones pedagógicas. ¿En qué puedo ayudarte?")
    else:
        for message in st.session_state.chat_messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Input del usuario (siempre visible al final)
    prompt = st.chat_input("Escribe tu pregunta aquí...")

    # Si hay pregunta sugerida, usarla
    if pregunta_sugerida:
        prompt = pregunta_sugerida

    # Procesar pregunta
    if prompt:
        # Agregar mensaje del usuario
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Construir contexto
        contexto = ""
        if df is not None:
            contexto = construir_contexto_datos(df, pagina_actual, datos_2024)

        # Generar y mostrar respuesta
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                response = generar_respuesta(prompt, contexto)
                st.markdown(response)

        # Agregar respuesta al historial
        st.session_state.chat_messages.append({"role": "assistant", "content": response})

        # Rerun para actualizar la interfaz
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

