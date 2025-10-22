# 🔗 Ejemplos de Integración del Chat de IA

Este documento muestra diferentes formas de integrar el chat de IA en la aplicación existente de Resultados ICFES.

---

## 📋 Opción 1: Chat en el Sidebar (Recomendado)

### Ventajas:
- ✅ Siempre visible
- ✅ No interfiere con el contenido principal
- ✅ Fácil de implementar

### Código:

```python
# streamlit_app.py

# Al inicio, después de los imports existentes
from app.chat_ia_icfes import mostrar_chat, inicializar_chat

def main():
    # ... código existente ...
    
    # Inicializar chat
    inicializar_chat()
    
    # Cargar datos
    datos_2024 = cargar_datos_2024()
    datos_2025_raw = cargar_datos_2025()
    
    # ... código existente del sidebar ...
    
    with st.sidebar:
        # ... navegación existente ...
        
        st.markdown("---")
        st.markdown("### 🤖 Asistente de IA")
        
        # Toggle para activar/desactivar chat
        if st.checkbox("Activar chat", value=False, key="toggle_chat"):
            # Determinar página actual
            pagina_actual = pagina if 'pagina' in locals() else "General"
            
            # Obtener DataFrame actual según la página
            df_actual = datos_2025_raw['df_todos']
            
            # Mostrar chat en el sidebar
            with st.container():
                mostrar_chat(df=df_actual, pagina_actual=pagina_actual)
```

---

## 📋 Opción 2: Chat en Pestaña Separada

### Ventajas:
- ✅ Más espacio para el chat
- ✅ Experiencia dedicada
- ✅ No distrae del análisis principal

### Código:

```python
# streamlit_app.py

from app.chat_ia_icfes import mostrar_chat, inicializar_chat

def mostrar_pagina_inicio(datos_2024, stats_regular_2025, stats_flexible_2025, 
                          stats_institucional_2025, stats_grupos_2025, datos_2025_raw):
    """Página principal con comparativo general 2024 vs 2025"""
    
    # ... código existente ...
    
    # Crear pestañas principales (AGREGAR tab_chat)
    tab1, tab2, tab3, tab4, tab5, tab_chat = st.tabs([
        "🏫 Avance Institucional Global",
        "📚 Avances por Modelos Educativos",
        "📊 Avances por Áreas de Conocimiento",
        "👥 Resultados por Grupos",
        "🎯 Niveles de Desempeño",
        "🤖 Chat IA"  # Nueva pestaña
    ])
    
    # ... código de pestañas existentes ...
    
    # NUEVA PESTAÑA: Chat IA
    with tab_chat:
        st.markdown("### 🤖 Asistente de IA para Análisis ICFES")
        
        st.info("""
        💡 **¿Qué puedo preguntarle al asistente?**
        - Interpretación de resultados y puntajes
        - Comparaciones entre años, modelos y grupos
        - Recomendaciones pedagógicas
        - Explicación de conceptos estadísticos
        - Análisis de fortalezas y áreas de mejora
        """)
        
        # Inicializar chat
        inicializar_chat()
        
        # Mostrar chat con datos actuales
        df_actual = datos_2025_raw['df_todos']
        mostrar_chat(df=df_actual, pagina_actual="Comparativo General")
```

---

## 📋 Opción 3: Chat en Expander (Discreto)

### Ventajas:
- ✅ No ocupa espacio hasta que se necesita
- ✅ Disponible en cualquier página
- ✅ Flexible

### Código:

```python
# streamlit_app.py

from app.chat_ia_icfes import mostrar_chat, inicializar_chat

def main():
    # ... código existente ...
    
    # Inicializar chat
    inicializar_chat()
    
    # Cargar datos
    datos_2024 = cargar_datos_2024()
    datos_2025_raw = cargar_datos_2025()
    
    # ... código de navegación ...
    
    # AGREGAR: Expander con chat en la parte superior de cada página
    with st.expander("🤖 ¿Necesitas ayuda? Pregunta al Asistente de IA", expanded=False):
        st.markdown("*Haz preguntas sobre los datos, interpretaciones y recomendaciones*")
        
        # Obtener página actual
        pagina_actual = seccion_seleccionada if 'seccion_seleccionada' in locals() else "General"
        
        # Mostrar chat
        df_actual = datos_2025_raw['df_todos']
        mostrar_chat(df=df_actual, pagina_actual=pagina_actual)
    
    st.markdown("---")
    
    # ... resto del código de la página ...
```

---

## 📋 Opción 4: Chat Contextual por Sección

### Ventajas:
- ✅ Chat específico para cada sección
- ✅ Contexto más relevante
- ✅ Preguntas sugeridas personalizadas

### Código:

```python
# streamlit_app.py

from app.chat_ia_icfes import mostrar_chat, inicializar_chat

def mostrar_resultados_institucionales(df):
    """Sección de resultados institucionales"""
    
    st.header("🏫 Resultados Institucionales")
    
    # ... código existente de la sección ...
    
    # AGREGAR: Chat contextual al final de la sección
    st.markdown("---")
    st.markdown("### 💬 Preguntas sobre Resultados Institucionales")
    
    # Inicializar chat
    inicializar_chat()
    
    # Mostrar chat con contexto específico
    mostrar_chat(df=df, pagina_actual="Resultados Institucionales")

def mostrar_analisis_area(df):
    """Sección de análisis por área"""
    
    st.header("📚 Análisis por Área")
    
    # ... código existente de la sección ...
    
    # AGREGAR: Chat contextual
    st.markdown("---")
    st.markdown("### 💬 Preguntas sobre Áreas de Conocimiento")
    
    inicializar_chat()
    mostrar_chat(df=df, pagina_actual="Análisis por Área")
```

---

## 📋 Opción 5: Chat Flotante (Avanzado)

### Ventajas:
- ✅ Siempre accesible
- ✅ No ocupa espacio del layout
- ✅ Experiencia moderna

### Código:

```python
# streamlit_app.py

from app.chat_ia_icfes import mostrar_chat, inicializar_chat

def main():
    # ... código existente ...
    
    # CSS para chat flotante
    st.markdown("""
    <style>
    .floating-chat {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 400px;
        max-height: 600px;
        background: white;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 1000;
        overflow: hidden;
    }
    
    .chat-toggle {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 999;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Toggle para mostrar/ocultar chat flotante
    if "show_floating_chat" not in st.session_state:
        st.session_state.show_floating_chat = False
    
    # Botón flotante
    col1, col2, col3 = st.columns([8, 1, 1])
    with col3:
        if st.button("🤖", key="toggle_floating_chat"):
            st.session_state.show_floating_chat = not st.session_state.show_floating_chat
    
    # Mostrar chat flotante si está activado
    if st.session_state.show_floating_chat:
        with st.container():
            st.markdown('<div class="floating-chat">', unsafe_allow_html=True)
            inicializar_chat()
            df_actual = datos_2025_raw['df_todos']
            mostrar_chat(df=df_actual, pagina_actual="General")
            st.markdown('</div>', unsafe_allow_html=True)
```

---

## 🎨 Personalización del Chat

### Cambiar preguntas sugeridas por sección

```python
# Modificar app/chat_ia_icfes.py

def mostrar_preguntas_sugeridas(pagina_actual: str = "General") -> Optional[str]:
    """
    Muestra preguntas sugeridas según la página actual
    """
    st.markdown("#### 💡 Preguntas sugeridas:")
    
    if pagina_actual == "Resultados Institucionales":
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📊 Puntaje global", use_container_width=True):
                return "¿Cuál es el puntaje global institucional y cómo se compara con el promedio nacional?"
        with col2:
            if st.button("📈 Avance 2024-2025", use_container_width=True):
                return "¿Cuánto avanzó la institución entre 2024 y 2025?"
        with col3:
            if st.button("🎯 Fortalezas", use_container_width=True):
                return "¿Cuáles son las principales fortalezas institucionales?"
    
    elif pagina_actual == "Análisis por Área":
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📚 Mejor área", use_container_width=True):
                return "¿Cuál es el área con mejor desempeño?"
        with col2:
            if st.button("🔍 Área a mejorar", use_container_width=True):
                return "¿Qué área requiere más atención?"
        with col3:
            if st.button("💡 Estrategias", use_container_width=True):
                return "¿Qué estrategias recomiendas para mejorar en las áreas débiles?"
    
    # Preguntas generales por defecto
    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("📊 Resumen general", use_container_width=True):
                return "Dame un resumen general de los resultados ICFES 2025"
        with col2:
            if st.button("🔄 Comparar modelos", use_container_width=True):
                return "¿Cómo se comparan Aula Regular y Modelo Flexible?"
        with col3:
            if st.button("📈 Interpretar", use_container_width=True):
                return "¿Cómo interpreto los niveles de desempeño?"
    
    return None
```

### Agregar contexto específico por página

```python
# Modificar app/chat_ia_icfes.py

def construir_contexto_especifico(df: pd.DataFrame, pagina_actual: str) -> str:
    """
    Construye contexto específico según la página actual
    """
    contexto_base = construir_contexto_datos(df, pagina_actual)
    
    if pagina_actual == "Resultados Institucionales":
        contexto_adicional = """
## ENFOQUE: Resultados Institucionales

El usuario está viendo la página de resultados institucionales generales.
Enfócate en:
- Puntaje global institucional
- Comparación con años anteriores
- Visión general de todas las áreas
- Fortalezas y debilidades institucionales
"""
        return contexto_base + contexto_adicional
    
    elif pagina_actual == "Análisis por Área":
        contexto_adicional = """
## ENFOQUE: Análisis por Área

El usuario está analizando áreas de conocimiento específicas.
Enfócate en:
- Desempeño por área individual
- Comparación entre áreas (sin comparar promedios directamente)
- Niveles de desempeño por área
- Recomendaciones pedagógicas específicas por área
"""
        return contexto_base + contexto_adicional
    
    # Contexto general por defecto
    return contexto_base
```

---

## 🔧 Configuración Avanzada

### Múltiples modelos según el tipo de consulta

```python
# app/chat_ia_icfes.py

def seleccionar_modelo_optimo(prompt: str) -> str:
    """
    Selecciona el modelo óptimo según el tipo de consulta
    """
    # Para consultas simples, usar modelo rápido
    if len(prompt) < 50 or any(word in prompt.lower() for word in ['qué es', 'define', 'explica']):
        return "llama-3.3-70b"  # Más rápido
    
    # Para análisis complejos, usar modelo avanzado
    elif any(word in prompt.lower() for word in ['compara', 'analiza', 'recomienda', 'estrategia']):
        return "deepseek-r1"  # Mejor razonamiento
    
    # Por defecto
    return "deepseek-r1"
```

### Caché de respuestas frecuentes

```python
# app/chat_ia_icfes.py

import hashlib
from functools import lru_cache

@lru_cache(maxsize=100)
def generar_respuesta_cached(prompt_hash: str, contexto_hash: str) -> str:
    """
    Genera respuesta con caché para preguntas frecuentes
    """
    # Esta función se llamará desde generar_respuesta()
    # con hashes de prompt y contexto para cachear
    pass

def generar_respuesta(prompt: str, contexto: str = "") -> str:
    """
    Genera respuesta con caché
    """
    # Crear hashes para caché
    prompt_hash = hashlib.md5(prompt.encode()).hexdigest()
    contexto_hash = hashlib.md5(contexto.encode()).hexdigest()
    
    # Intentar obtener de caché
    try:
        return generar_respuesta_cached(prompt_hash, contexto_hash)
    except:
        # Si no está en caché, generar normalmente
        return generar_respuesta_sin_cache(prompt, contexto)
```

---

## 📊 Monitoreo y Analytics

### Logging de consultas

```python
# app/chat_ia_icfes.py

import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(
    filename='logs/chat_ia.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_consulta(prompt: str, respuesta: str, pagina: str):
    """
    Registra consultas para análisis posterior
    """
    logging.info(f"""
    CONSULTA:
    - Página: {pagina}
    - Prompt: {prompt[:100]}...
    - Longitud respuesta: {len(respuesta)} caracteres
    - Timestamp: {datetime.now().isoformat()}
    """)

# Usar en generar_respuesta()
def generar_respuesta(prompt: str, contexto: str = "") -> str:
    # ... código existente ...
    
    respuesta = # ... generar respuesta ...
    
    # Registrar consulta
    log_consulta(prompt, respuesta, st.session_state.get('pagina_actual', 'Unknown'))
    
    return respuesta
```

---

## ✅ Checklist de Integración

Antes de integrar el chat en producción:

- [ ] Decidir opción de integración (sidebar, pestaña, expander, etc.)
- [ ] Configurar API key en secrets.toml
- [ ] Probar chat en modo standalone
- [ ] Integrar en aplicación principal
- [ ] Personalizar preguntas sugeridas
- [ ] Ajustar contexto por página
- [ ] Implementar logging (opcional)
- [ ] Probar con usuarios reales
- [ ] Documentar para usuarios finales
- [ ] Desplegar en producción

---

## 📚 Recursos

- **Código completo:** `app/chat_ia_icfes.py`
- **Guía de implementación:** `GUIA-RAPIDA-CHAT-IA.md`
- **Propuesta técnica:** `PROPUESTA-CHAT-IA-ICFES.md`
- **Documentación Streamlit:** https://docs.streamlit.io/develop/api-reference/chat

---

**Última actualización:** 22 de octubre de 2025  
**Versión:** 1.0

