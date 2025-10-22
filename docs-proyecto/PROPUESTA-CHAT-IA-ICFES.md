# 🤖 Propuesta: Chat de IA Integrado para Análisis de Resultados ICFES

**Fecha:** 22 de octubre de 2025  
**Proyecto:** Resultados ICFES - Pedacito de Cielo  
**Objetivo:** Implementar un asistente de IA conversacional para ayudar a usuarios a interpretar y analizar datos del ICFES

---

## 📋 Índice

1. [Resumen Ejecutivo](#resumen-ejecutivo)
2. [Análisis de Modelos LLM Open Source](#análisis-de-modelos-llm-open-source)
3. [Arquitectura Propuesta](#arquitectura-propuesta)
4. [Opciones de Hosting](#opciones-de-hosting)
5. [Plan de Implementación](#plan-de-implementación)
6. [Estimación de Costos](#estimación-de-costos)
7. [Recomendaciones](#recomendaciones)

---

## 🎯 Resumen Ejecutivo

### Objetivo
Integrar un chat de IA en la aplicación Streamlit de Resultados ICFES que permita a los usuarios:
- Hacer preguntas sobre los datos y estadísticas mostrados
- Obtener interpretaciones pedagógicas de los resultados
- Recibir explicaciones sobre puntajes y áreas evaluadas
- Comparar resultados entre años, modelos educativos y grupos

### Requisitos Técnicos Clave
✅ **Modelo open source** (código abierto)  
✅ **Ventana de contexto grande** (mínimo 32K, idealmente 128K+ tokens)  
✅ **Soporte de español de alta calidad**  
✅ **API gratuita o económica**  
✅ **Integración con Streamlit**

---

## 🔍 Análisis de Modelos LLM Open Source

### 1. **DeepSeek V3 / DeepSeek R1** ⭐ RECOMENDADO

**Características:**
- **Parámetros:** 671B (Mixture of Experts - 37B activos)
- **Ventana de contexto:** 128K tokens
- **Español:** Excelente calidad (entrenado multilingüe)
- **Rendimiento:** Comparable a GPT-4 en benchmarks
- **Licencia:** MIT (completamente open source)

**Ventajas:**
- ✅ Mejor modelo open source disponible actualmente (2025)
- ✅ Razonamiento avanzado (DeepSeek R1)
- ✅ Excelente en español
- ✅ APIs gratuitas disponibles (Groq, Together.ai, OpenRouter)
- ✅ Puede ejecutarse localmente con Ollama

**Desventajas:**
- ⚠️ Requiere ~40GB RAM para ejecución local (versión cuantizada)
- ⚠️ Versión completa requiere múltiples GPUs

**APIs Gratuitas:**
- **Groq:** Gratis con límites generosos (14,400 req/día)
- **Together.ai:** $1M tokens gratis al mes
- **OpenRouter:** Versión gratuita disponible
- **Scaleway:** 1M tokens gratis

---

### 2. **Llama 3.3 70B** ⭐ ALTERNATIVA SÓLIDA

**Características:**
- **Parámetros:** 70B
- **Ventana de contexto:** 128K tokens
- **Español:** Muy buena calidad
- **Rendimiento:** Excelente en tareas generales
- **Licencia:** Llama 3 Community License (open source)

**Ventajas:**
- ✅ Modelo probado y confiable de Meta
- ✅ Amplio soporte en APIs gratuitas
- ✅ Buena documentación y comunidad
- ✅ Ejecutable localmente con Ollama

**Desventajas:**
- ⚠️ Requiere ~40GB RAM para ejecución local
- ⚠️ Español ligeramente inferior a DeepSeek

**APIs Gratuitas:**
- **Groq:** Gratis (ultra rápido)
- **Together.ai:** Gratis
- **OpenRouter:** Gratis
- **NVIDIA NIM:** Gratis con límites

---

### 3. **Qwen 2.5 / Qwen 3** 🌟 MEJOR PARA ESPAÑOL

**Características:**
- **Parámetros:** 7B, 14B, 32B, 72B, 235B (MoE)
- **Ventana de contexto:** 128K tokens (hasta 1M en Qwen 2.5)
- **Español:** Excelente (mejor que Llama en idiomas no ingleses)
- **Rendimiento:** Muy competitivo
- **Licencia:** Apache 2.0 (completamente open source)

**Ventajas:**
- ✅ Excelente en español y multilingüe
- ✅ Versiones pequeñas (7B, 14B) ejecutables en hardware modesto
- ✅ Ventana de contexto masiva (hasta 1M tokens)
- ✅ Muy eficiente

**Desventajas:**
- ⚠️ Menos APIs gratuitas que Llama/DeepSeek
- ⚠️ Documentación principalmente en inglés/chino

**APIs Gratuitas:**
- **Alibaba Cloud:** Gratis con límites
- **Together.ai:** Disponible
- **OpenRouter:** Disponible

---

### 4. **Mixtral 8x7B / 8x22B**

**Características:**
- **Parámetros:** 47B total (8 expertos x 7B, 12.9B activos)
- **Ventana de contexto:** 32K tokens
- **Español:** Buena calidad
- **Licencia:** Apache 2.0

**Ventajas:**
- ✅ Eficiente (MoE)
- ✅ Bueno en español
- ✅ Ejecutable localmente

**Desventajas:**
- ⚠️ Ventana de contexto menor (32K)
- ⚠️ Superado por modelos más recientes

---

## 🏗️ Arquitectura Propuesta

### Componentes del Sistema

```
┌─────────────────────────────────────────────────────────────┐
│                    APLICACIÓN STREAMLIT                      │
│                  (streamlit_app.py)                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    MÓDULO CHAT IA                            │
│                  (chat_ia_icfes.py)                          │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  • Interfaz de chat (st.chat_message)                 │  │
│  │  • Gestión de historial de conversación              │  │
│  │  • Procesamiento de consultas                         │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  CAPA DE CONTEXTO (RAG)                      │
│                  (contexto_icfes.py)                         │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  • Extracción de datos relevantes                     │  │
│  │  • Construcción de contexto dinámico                  │  │
│  │  • Embeddings de documentación ICFES                  │  │
│  │  • Recuperación de información (RAG)                  │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    CLIENTE LLM                               │
│                  (llm_client.py)                             │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  • Conexión a API (Groq/Together.ai/Ollama)          │  │
│  │  • Gestión de prompts                                 │  │
│  │  • Streaming de respuestas                            │  │
│  │  • Manejo de errores y reintentos                     │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    FUENTES DE DATOS                          │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  • DataFrames de Pandas (datos 2024/2025)            │  │
│  │  • Archivos Excel (resultados estudiantes)           │  │
│  │  • Documentación ICFES (MD files)                    │  │
│  │  • Estadísticas calculadas en tiempo real            │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Flujo de Interacción

1. **Usuario hace una pregunta** en el chat de Streamlit
2. **Módulo Chat IA** recibe la consulta y la procesa
3. **Capa de Contexto (RAG)** extrae datos relevantes:
   - Estadísticas actuales de la página
   - Datos históricos (2024 vs 2025)
   - Documentación ICFES relevante
4. **Cliente LLM** envía la consulta + contexto al modelo
5. **Modelo LLM** genera respuesta en español
6. **Respuesta se muestra** en el chat con streaming

---

## 🌐 Opciones de Hosting

### Opción 1: **API Gratuita (Groq)** ⭐ RECOMENDADO PARA INICIO

**Proveedor:** Groq Cloud  
**Modelo:** DeepSeek R1 o Llama 3.3 70B  
**Costo:** Gratis  
**Límites:** 14,400 requests/día, 30 req/min

**Ventajas:**
- ✅ Cero costo
- ✅ Ultra rápido (hardware especializado)
- ✅ Fácil integración
- ✅ No requiere infraestructura local

**Desventajas:**
- ⚠️ Límites de uso
- ⚠️ Dependencia de servicio externo
- ⚠️ Datos enviados a terceros

**Implementación:**
```python
from groq import Groq

client = Groq(api_key="tu_api_key_gratis")
response = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=[{"role": "user", "content": "pregunta"}],
    temperature=0.7,
    max_tokens=2048
)
```

---

### Opción 2: **Ollama Local** 🏠 RECOMENDADO PARA PRIVACIDAD

**Proveedor:** Ollama (local)  
**Modelo:** Qwen 2.5 14B o Llama 3.3 70B  
**Costo:** Gratis (hardware propio)  
**Requisitos:** 16GB+ RAM, GPU opcional

**Ventajas:**
- ✅ 100% privado (datos no salen del servidor)
- ✅ Sin límites de uso
- ✅ Sin costos recurrentes
- ✅ Control total

**Desventajas:**
- ⚠️ Requiere hardware adecuado
- ⚠️ Más lento que APIs cloud
- ⚠️ Mantenimiento local

**Implementación:**
```bash
# Instalar Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Descargar modelo
ollama pull qwen2.5:14b

# Ejecutar
ollama serve
```

```python
import ollama

response = ollama.chat(
    model='qwen2.5:14b',
    messages=[{'role': 'user', 'content': 'pregunta'}]
)
```

---

### Opción 3: **Together.ai** 💰 ECONÓMICO Y ESCALABLE

**Proveedor:** Together.ai  
**Modelo:** DeepSeek V3, Llama 3.3, Qwen 2.5  
**Costo:** $1M tokens gratis/mes, luego $0.20-0.60 por 1M tokens  
**Límites:** Muy generosos

**Ventajas:**
- ✅ Tier gratuito generoso
- ✅ Múltiples modelos disponibles
- ✅ Buena velocidad
- ✅ Escalable

**Desventajas:**
- ⚠️ Costo después del tier gratuito
- ⚠️ Datos enviados a terceros

---

## 📦 Frameworks y Librerías

### LangChain vs LlamaIndex

| Característica | LangChain | LlamaIndex |
|---------------|-----------|------------|
| **Propósito** | Framework general para LLMs | Especializado en RAG |
| **Curva de aprendizaje** | Moderada | Más simple para RAG |
| **Flexibilidad** | Muy alta | Enfocada en datos |
| **Documentación** | Extensa | Buena |
| **Integración Streamlit** | Excelente | Excelente |
| **Recomendación** | ✅ Para proyecto complejo | ✅ Para RAG simple |

### Recomendación: **LangChain** 

**Razones:**
- Más flexible para futuras expansiones
- Mejor integración con múltiples proveedores
- Excelente para gestión de memoria conversacional
- Amplia comunidad y recursos

**Dependencias:**
```txt
langchain>=0.1.0
langchain-groq>=0.0.1  # Para Groq
langchain-community>=0.0.1
streamlit>=1.32.0
pandas>=2.2.0
```

---

## 📝 Plan de Implementación

### Fase 1: Configuración Básica (1-2 días)

**Tareas:**
1. ✅ Crear cuenta en Groq (API gratuita)
2. ✅ Instalar dependencias necesarias
3. ✅ Crear módulo básico de chat en Streamlit
4. ✅ Implementar cliente LLM con Groq

**Entregables:**
- Chat funcional con respuestas básicas
- Integración con DeepSeek R1 o Llama 3.3

**Código ejemplo:**
```python
# chat_ia_icfes.py
import streamlit as st
from groq import Groq

def inicializar_chat():
    """Inicializa el chat de IA"""
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "groq_client" not in st.session_state:
        st.session_state.groq_client = Groq(
            api_key=st.secrets["GROQ_API_KEY"]
        )

def mostrar_chat():
    """Muestra la interfaz del chat"""
    st.markdown("### 🤖 Asistente de IA - Resultados ICFES")

    # Mostrar historial
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input del usuario
    if prompt := st.chat_input("Pregunta sobre los resultados ICFES..."):
        # Agregar mensaje del usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generar respuesta
        with st.chat_message("assistant"):
            response = generar_respuesta(prompt)
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})

def generar_respuesta(prompt):
    """Genera respuesta usando Groq"""
    client = st.session_state.groq_client

    response = client.chat.completions.create(
        model="deepseek-r1-distill-llama-70b",
        messages=[
            {"role": "system", "content": "Eres un asistente experto en análisis de resultados ICFES Saber 11. Respondes en español de forma clara y pedagógica."},
            *st.session_state.messages,
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2048,
        stream=False
    )

    return response.choices[0].message.content
```

---

### Fase 2: Integración con Datos (2-3 días)

**Tareas:**
1. ✅ Crear módulo de contexto RAG
2. ✅ Extraer datos relevantes de DataFrames
3. ✅ Construir prompts con contexto dinámico
4. ✅ Implementar recuperación de documentación ICFES

**Entregables:**
- Chat que responde con datos reales
- Contexto dinámico basado en la página actual

**Código ejemplo:**
```python
# contexto_icfes.py
import pandas as pd
from typing import Dict, List

def construir_contexto_datos(df: pd.DataFrame, pagina_actual: str) -> str:
    """Construye contexto con datos relevantes"""

    contexto = f"""
# CONTEXTO DE DATOS ICFES

## Página actual: {pagina_actual}

## Estadísticas Generales 2025
- Total estudiantes: {len(df)}
- Puntaje global promedio: {df['Puntaje Global'].mean():.0f}
- Desviación estándar: {df['Puntaje Global'].std():.1f}

## Promedios por Área
"""

    areas = ['Lectura Crítica', 'Matemáticas', 'Sociales y Ciudadanas',
             'Ciencias Naturales', 'Inglés']

    for area in areas:
        if area in df.columns:
            promedio = df[area].mean()
            contexto += f"- {area}: {promedio:.0f}\n"

    # Agregar datos por modelo
    contexto += "\n## Comparación por Modelo Educativo\n"
    for modelo in df['Modelo'].unique():
        df_modelo = df[df['Modelo'] == modelo]
        promedio = df_modelo['Puntaje Global'].mean()
        contexto += f"- {modelo}: {promedio:.0f} ({len(df_modelo)} estudiantes)\n"

    return contexto

def construir_contexto_comparativo(datos_2024: Dict, datos_2025: Dict) -> str:
    """Construye contexto comparativo 2024 vs 2025"""

    contexto = """
# COMPARACIÓN 2024 vs 2025

## Puntaje Global Institucional
"""

    puntaje_2024 = datos_2024['Institucional']['puntaje_global']
    puntaje_2025 = datos_2025['puntaje_global']
    avance = puntaje_2025 - puntaje_2024

    contexto += f"- 2024: {puntaje_2024}\n"
    contexto += f"- 2025: {puntaje_2025}\n"
    contexto += f"- Avance: {avance:+d} puntos\n"

    return contexto

def obtener_documentacion_icfes() -> str:
    """Retorna documentación sobre interpretación ICFES"""

    return """
# GUÍA DE INTERPRETACIÓN ICFES

## Niveles de Desempeño
- **Insuficiente (0-35)**: No supera preguntas de menor complejidad
- **Mínimo (36-50)**: Supera preguntas de menor complejidad
- **Satisfactorio (51-70)**: Supera preguntas de complejidad media y baja
- **Avanzado (71-100)**: Supera preguntas de mayor complejidad

## Áreas Evaluadas
1. **Lectura Crítica**: Comprensión, interpretación y evaluación de textos
2. **Matemáticas**: Razonamiento cuantitativo y resolución de problemas
3. **Sociales y Ciudadanas**: Pensamiento social y competencias ciudadanas
4. **Ciencias Naturales**: Indagación y explicación de fenómenos
5. **Inglés**: Comprensión lectora en lengua extranjera

## Puntaje Global
- Suma de los puntajes de las 5 áreas
- Rango: 0 a 500 puntos
- Promedio nacional típico: 250 puntos
"""
```

---

### Fase 3: Mejoras Avanzadas (3-5 días)

**Tareas:**
1. ✅ Implementar memoria conversacional
2. ✅ Agregar streaming de respuestas
3. ✅ Crear prompts especializados por tipo de consulta
4. ✅ Implementar caché de respuestas comunes
5. ✅ Agregar botones de preguntas sugeridas

**Entregables:**
- Chat con memoria de conversación
- Respuestas en tiempo real (streaming)
- Experiencia de usuario mejorada

**Código ejemplo:**
```python
# chat_avanzado.py
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_groq import ChatGroq

def crear_cadena_conversacional(contexto: str):
    """Crea cadena conversacional con LangChain"""

    llm = ChatGroq(
        model="deepseek-r1-distill-llama-70b",
        temperature=0.7,
        max_tokens=2048,
        groq_api_key=st.secrets["GROQ_API_KEY"]
    )

    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"
    )

    system_prompt = f"""
Eres un asistente experto en análisis de resultados ICFES Saber 11 para la
Institución Educativa Pedacito de Cielo.

CONTEXTO ACTUAL:
{contexto}

INSTRUCCIONES:
- Responde SIEMPRE en español
- Usa los datos del contexto para responder
- Sé claro, conciso y pedagógico
- Si no tienes información suficiente, indícalo
- Proporciona interpretaciones educativas útiles
- Usa emojis para hacer las respuestas más amigables
"""

    return llm, memory, system_prompt

def mostrar_preguntas_sugeridas():
    """Muestra botones con preguntas comunes"""

    st.markdown("#### 💡 Preguntas sugeridas:")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📊 ¿Cómo mejoró la institución?"):
            return "¿Cómo mejoró el puntaje global de la institución entre 2024 y 2025?"

    with col2:
        if st.button("📚 ¿Cuál es el área más fuerte?"):
            return "¿Cuál es el área de conocimiento con mejor desempeño?"

    with col3:
        if st.button("🎯 ¿Qué áreas mejorar?"):
            return "¿En qué áreas debemos enfocarnos para mejorar?"

    return None
```

---

### Fase 4: Optimización y Testing (2-3 días)

**Tareas:**
1. ✅ Optimizar prompts para mejor calidad
2. ✅ Implementar manejo de errores robusto
3. ✅ Agregar logging y monitoreo
4. ✅ Testing con usuarios reales
5. ✅ Documentación de uso

**Entregables:**
- Sistema estable y optimizado
- Documentación completa
- Guía de usuario

---

## 💰 Estimación de Costos

### Opción 1: Groq (Gratis)
- **Costo mensual:** $0
- **Límites:** 14,400 requests/día
- **Estimación de uso:** ~500 requests/día (suficiente para institución)
- **Costo anual:** $0

### Opción 2: Together.ai (Freemium)
- **Tier gratuito:** 1M tokens/mes
- **Estimación de uso:** ~200K tokens/mes
- **Costo mensual:** $0 (dentro del tier gratuito)
- **Si se excede:** ~$0.20-0.60 por 1M tokens adicionales
- **Costo anual estimado:** $0-50

### Opción 3: Ollama Local
- **Costo inicial:** $0 (si ya tienes hardware)
- **Hardware recomendado:**
  - CPU: 8+ cores
  - RAM: 32GB (para Llama 3.3 70B) o 16GB (para Qwen 2.5 14B)
  - GPU: Opcional (NVIDIA con 8GB+ VRAM acelera 5-10x)
- **Costo mensual:** $0 (solo electricidad ~$5-10)
- **Costo anual:** $60-120 (electricidad)

### Recomendación de Costos

**Para comenzar:** Groq (gratis)
**Para producción:** Together.ai o Ollama local
**Para máxima privacidad:** Ollama local

---

## 🎯 Recomendaciones Finales

### Recomendación Principal: **Enfoque Híbrido**

1. **Fase Inicial (Mes 1-2):**
   - Usar **Groq** con **DeepSeek R1**
   - Validar funcionalidad y aceptación de usuarios
   - Costo: $0

2. **Fase de Producción (Mes 3+):**
   - Migrar a **Ollama local** con **Qwen 2.5 14B**
   - Mantener Groq como backup
   - Costo: ~$10/mes (electricidad)

3. **Escalamiento (Si es necesario):**
   - Considerar **Together.ai** para mayor capacidad
   - O actualizar hardware para Llama 3.3 70B local

### Modelo Recomendado por Caso de Uso

| Caso de Uso | Modelo Recomendado | Razón |
|-------------|-------------------|-------|
| **Prototipo rápido** | DeepSeek R1 (Groq) | Gratis, rápido, excelente calidad |
| **Producción privada** | Qwen 2.5 14B (Ollama) | Privacidad, español excelente, eficiente |
| **Máximo rendimiento** | Llama 3.3 70B (Ollama) | Mejor calidad, requiere más hardware |
| **Escalabilidad** | DeepSeek V3 (Together.ai) | Balance costo/rendimiento |

### Próximos Pasos Inmediatos

1. ✅ **Crear cuenta en Groq** (5 minutos)
2. ✅ **Instalar dependencias** (10 minutos)
3. ✅ **Implementar chat básico** (2-3 horas)
4. ✅ **Probar con datos reales** (1 hora)
5. ✅ **Iterar y mejorar** (continuo)

---

## 📚 Recursos Adicionales

### Documentación Oficial
- **Groq:** https://console.groq.com/docs
- **LangChain:** https://python.langchain.com/docs
- **Streamlit Chat:** https://docs.streamlit.io/develop/api-reference/chat
- **Ollama:** https://ollama.com/docs

### Tutoriales Recomendados
- [Building RAG with LangChain and Streamlit](https://blog.streamlit.io/build-a-real-time-rag-chatbot-google-drive-sharepoint/)
- [Groq + LangChain Integration](https://console.groq.com/docs/langchain)
- [Ollama Local Setup](https://ollama.com/blog)

### Comunidades
- r/LocalLLaMA (Reddit)
- LangChain Discord
- Streamlit Community Forum

---

## ✅ Checklist de Implementación

### Configuración Inicial
- [ ] Crear cuenta en Groq
- [ ] Obtener API key
- [ ] Configurar secrets en Streamlit
- [ ] Instalar dependencias

### Desarrollo
- [ ] Crear módulo chat_ia_icfes.py
- [ ] Implementar interfaz de chat
- [ ] Crear módulo contexto_icfes.py
- [ ] Integrar con datos existentes
- [ ] Implementar cliente LLM

### Testing
- [ ] Probar con preguntas básicas
- [ ] Validar respuestas con datos reales
- [ ] Testing con usuarios
- [ ] Optimizar prompts

### Despliegue
- [ ] Documentar uso
- [ ] Agregar a aplicación principal
- [ ] Configurar en Streamlit Cloud
- [ ] Monitorear uso

---

## 📞 Contacto y Soporte

Para dudas sobre la implementación:
- Revisar documentación oficial de cada herramienta
- Consultar ejemplos en el repositorio
- Buscar en comunidades especializadas

---

**Documento creado:** 22 de octubre de 2025
**Última actualización:** 22 de octubre de 2025
**Versión:** 1.0


