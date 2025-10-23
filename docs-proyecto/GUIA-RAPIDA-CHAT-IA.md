# 🚀 Guía Rápida: Implementación del Chat de IA

**Tiempo estimado:** 15-30 minutos
**Nivel:** Intermedio
**Requisitos:** Python 3.8+, cuenta en Groq (gratis)

---

## 📋 Paso 1: Obtener API Key de Groq (5 minutos)

### 1.1 Crear cuenta en Groq

1. Ve a: https://console.groq.com/
2. Haz clic en "Sign Up" (Registrarse)
3. Completa el registro con tu email
4. Verifica tu email

### 1.2 Obtener API Key

1. Inicia sesión en https://console.groq.com/
2. Ve a la sección "API Keys"
3. Haz clic en "Create API Key"
4. Copia la API key (empieza con `gsk_...`)
5. **¡IMPORTANTE!** Guarda la key en un lugar seguro, solo se muestra una vez

---

## 🔧 Paso 2: Configurar el Proyecto (5 minutos)

### 2.1 Instalar dependencias

```bash
# Activar entorno virtual (si lo usas)
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Instalar la librería de Groq
pip install groq>=0.4.0
```

### 2.2 Configurar secrets

```bash
# Crear directorio de configuración si no existe
mkdir -p .streamlit

# Copiar archivo de ejemplo
cp .streamlit/secrets.toml.example .streamlit/secrets.toml

# Editar el archivo con tu API key
nano .streamlit/secrets.toml
# o usa tu editor favorito
```

**Contenido de `.streamlit/secrets.toml`:**
```toml
# Reemplaza con tu API key real
GROQ_API_KEY = "gsk_tu_api_key_aqui"

[chat]
proveedor = "groq"
modelo = "deepseek-r1"
temperatura = 0.7
max_tokens = 2048
```

### 2.3 Verificar .gitignore

Asegúrate de que `.streamlit/secrets.toml` esté en tu `.gitignore`:

```bash
echo ".streamlit/secrets.toml" >> .gitignore
```

---

## 🧪 Paso 3: Probar el Chat (5 minutos)

### 3.1 Ejecutar módulo de prueba

```bash
# Probar el módulo de chat directamente
streamlit run app/chat_ia_icfes.py
```

### 3.2 Verificar funcionamiento

1. La aplicación debe abrir en tu navegador
2. Deberías ver la interfaz del chat
3. Prueba con una pregunta simple: "Hola, ¿qué puedes hacer?"
4. Deberías recibir una respuesta del asistente

---

## 🔗 Paso 4: Integrar con la Aplicación Principal (10 minutos)

### 4.1 Modificar streamlit_app.py

Agrega el chat a tu aplicación principal:

```python
# Al inicio del archivo, después de los imports existentes
from app.chat_ia_icfes import mostrar_chat, inicializar_chat

# En la función main(), después de cargar los datos
def main():
    # ... código existente ...

    # Cargar datos
    datos_2024 = cargar_datos_2024()
    datos_2025_raw = cargar_datos_2025()

    # ... código existente ...

    # AGREGAR: Inicializar chat
    inicializar_chat()

    # En el sidebar, agregar opción de chat
    with st.sidebar:
        # ... código existente del sidebar ...

        st.markdown("---")

        # AGREGAR: Toggle para mostrar/ocultar chat
        mostrar_chat_ia = st.checkbox("🤖 Activar Asistente de IA", value=False)

    # AGREGAR: Mostrar chat si está activado
    if mostrar_chat_ia:
        with st.expander("🤖 Chat con Asistente de IA", expanded=True):
            # Pasar los datos actuales al chat
            df_actual = datos_2025_raw['df_todos']
            mostrar_chat(df=df_actual, pagina_actual=pagina)
```

### 4.2 Alternativa: Chat en pestaña separada

Si prefieres el chat en una pestaña separada:

```python
# En la sección de pestañas
tab1, tab2, tab3, tab4, tab5, tab_chat = st.tabs([
    "🏫 Avance Institucional Global",
    "📚 Avances por Modelos Educativos",
    "📊 Avances por Áreas de Conocimiento",
    "👥 Resultados por Grupos",
    "🎯 Niveles de Desempeño",
    "🤖 Chat IA"  # Nueva pestaña
])

# ... código de otras pestañas ...

with tab_chat:
    st.markdown("### 🤖 Asistente de IA para Análisis ICFES")
    st.info("💡 Pregunta sobre los datos, interpretaciones y recomendaciones pedagógicas")

    df_actual = datos_2025_raw['df_todos']
    mostrar_chat(df=df_actual, pagina_actual="Chat IA")
```

---

## ✅ Paso 5: Verificar Integración (5 minutos)

### 5.1 Ejecutar aplicación completa

```bash
streamlit run streamlit_app.py
```

### 5.2 Probar funcionalidades

Prueba estas preguntas para verificar que el chat funciona correctamente:

1. **Pregunta básica:**
   - "¿Cuál es el puntaje global promedio de la institución?"

2. **Pregunta comparativa:**
   - "¿Cómo se comparan los resultados entre Aula Regular y Modelo Flexible?"

3. **Pregunta de interpretación:**
   - "¿Qué significa un puntaje de 45 en Matemáticas?"

4. **Pregunta de recomendaciones:**
   - "¿Qué estrategias recomiendas para mejorar en Lectura Crítica?"

### 5.3 Verificar que el chat:

- ✅ Responde en español
- ✅ Usa datos reales del contexto
- ✅ Proporciona interpretaciones pedagógicas
- ✅ Mantiene el historial de conversación
- ✅ Responde de forma coherente

---

## 🎨 Personalización Opcional

### Cambiar el modelo

En `.streamlit/secrets.toml`:

```toml
[chat]
modelo = "llama-3.3-70b"  # Alternativa a deepseek-r1
```

Modelos disponibles en Groq:
- `deepseek-r1` - Mejor razonamiento (recomendado)
- `llama-3.3-70b` - Más rápido
- `mixtral-8x7b` - Balance velocidad/calidad

### Ajustar temperatura

```toml
[chat]
temperatura = 0.5  # Más determinista (0.0-1.0)
```

- `0.0-0.3`: Respuestas muy consistentes y predecibles
- `0.4-0.7`: Balance (recomendado)
- `0.8-1.0`: Respuestas más creativas y variadas

### Limitar tokens

```toml
[chat]
max_tokens = 1024  # Respuestas más cortas
```

---

## 🐛 Solución de Problemas

### Error: "No se encontró la API key de Groq"

**Solución:**
1. Verifica que `.streamlit/secrets.toml` existe
2. Verifica que la API key está correctamente escrita
3. Reinicia la aplicación Streamlit

### Error: "ImportError: No module named 'groq'"

**Solución:**
```bash
pip install groq>=0.4.0
```

### Error: "Rate limit exceeded"

**Solución:**
- Groq tiene límite de 14,400 requests/día
- Espera unos minutos y vuelve a intentar
- Considera usar Ollama local para uso intensivo

### El chat no responde o responde muy lento

**Posibles causas:**
1. **Conexión a internet lenta:** Groq requiere conexión estable
2. **Contexto muy grande:** Reduce la cantidad de datos en el contexto
3. **Servidor de Groq saturado:** Intenta en otro momento

**Solución:**
- Verifica tu conexión a internet
- Reduce `max_tokens` en la configuración
- Considera usar un modelo más rápido (llama-3.3-70b)

### El chat no usa los datos actuales

**Solución:**
1. Verifica que estás pasando el DataFrame al chat:
   ```python
   mostrar_chat(df=df_actual, pagina_actual="nombre_pagina")
   ```
2. Verifica que el DataFrame tiene datos:
   ```python
   print(f"Datos en df: {len(df_actual)} filas")
   ```

---

## 📊 Monitoreo de Uso

### Ver uso de API en Groq

1. Ve a https://console.groq.com/
2. Sección "Usage" o "Dashboard"
3. Revisa requests realizados y límites

### Límites de Groq (tier gratuito)

- **Requests por día:** 14,400
- **Requests por minuto:** 30
- **Tokens por request:** Hasta 32K (contexto) + 8K (respuesta)

Para una institución educativa pequeña, estos límites son más que suficientes.

---

## 🚀 Próximos Pasos

### Mejoras recomendadas:

1. **Agregar más preguntas sugeridas** específicas para tu institución
2. **Personalizar el prompt del sistema** con información específica
3. **Implementar caché** para preguntas frecuentes
4. **Agregar exportación** de conversaciones
5. **Implementar feedback** de usuarios sobre respuestas

### Migración a producción:

1. **Considerar Ollama local** para mayor privacidad
2. **Implementar logging** de conversaciones
3. **Agregar analytics** de uso del chat
4. **Crear documentación** para usuarios finales

---

## 📚 Recursos Adicionales

### Documentación oficial:
- **Groq:** https://console.groq.com/docs
- **Streamlit Chat:** https://docs.streamlit.io/develop/api-reference/chat
- **DeepSeek:** https://github.com/deepseek-ai/DeepSeek-R1

### Tutoriales:
- [Streamlit Chat Tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)
- [Groq Quickstart](https://console.groq.com/docs/quickstart)

### Comunidad:
- [Streamlit Forum](https://discuss.streamlit.io/)
- [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA)

---

## ✅ Checklist Final

Antes de considerar la implementación completa:

- [ ] API key de Groq configurada
- [ ] Dependencias instaladas
- [ ] Chat funciona en modo standalone
- [ ] Chat integrado en aplicación principal
- [ ] Probado con preguntas reales
- [ ] Respuestas son relevantes y precisas
- [ ] Documentación actualizada
- [ ] Usuarios informados sobre el nuevo feature

---

**¿Necesitas ayuda?**

Revisa la documentación completa en `PROPUESTA-CHAT-IA-ICFES.md` o consulta los recursos adicionales.

---

---
**Última actualización:** 2025-10-23  
**Versión:** 2.0  

