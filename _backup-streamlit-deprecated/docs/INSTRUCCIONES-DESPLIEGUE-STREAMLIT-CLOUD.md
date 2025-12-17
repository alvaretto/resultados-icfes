# 🚀 Instrucciones para Desplegar en Streamlit Cloud

## ✅ Estado Actual

**Commit exitoso en GitHub:**
- **Commit Hash:** `94a9dd1c286c39e828e1d0c40575a1b272612f81`
- **Fecha:** 2025-10-21 22:06:06 UTC
- **Repositorio:** https://github.com/alvaretto/resultados-icfes
- **Rama:** main
- **Archivos subidos:** 16 archivos (4179 adiciones, 243 eliminaciones)

**Verificación del repositorio:**
✅ Puedes verificar que los cambios están en GitHub visitando:
https://github.com/alvaretto/resultados-icfes/commit/94a9dd1c286c39e828e1d0c40575a1b272612f81

---

## 📋 Archivos Necesarios para Streamlit Cloud

### ✅ Archivos Confirmados en el Repositorio:

1. **streamlit_app.py** ✅
   - Archivo principal de la aplicación
   - Ubicación: raíz del proyecto
   - 1145 líneas de código

2. **requirements.txt** ✅
   - Dependencias de Python
   - Contenido:
     ```
     streamlit>=1.32.0
     pandas>=2.2.0
     plotly>=5.18.0
     openpyxl>=3.1.2
     numpy>=1.26.0
     scipy>=1.12.0
     ```

3. **runtime.txt** ✅
   - Versión de Python
   - Contenido: `python-3.11`

4. **Archivos de datos** ✅
   - `data/RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx`
   - `data/RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx`
   - `data/globales_pcielo_2024.md`
   - `data/globales_pcielo_aula_regular_2024.md`
   - `data/globales_pcielo_flexible_2024.md`

5. **.gitignore** ✅
   - Actualizado para NO excluir archivos Excel (según instrucciones)

---

## 🌐 Pasos para Conectar con Streamlit Cloud

### Opción A: Si la App Ya Está Conectada

Si ya tienes la aplicación conectada en https://resultados-icfes-pcielo-2025.streamlit.app/, simplemente:

1. **Accede a Streamlit Cloud:**
   - Ve a: https://share.streamlit.io/
   - Inicia sesión con tu cuenta de GitHub

2. **Verifica el despliegue automático:**
   - Streamlit Cloud detectará automáticamente el nuevo commit
   - La aplicación se redesplegar automáticamente
   - Esto puede tomar 2-5 minutos

3. **Verifica el estado:**
   - En el dashboard de Streamlit Cloud, busca tu app: `resultados-icfes-pcielo-2025`
   - Verifica que el estado sea "Running" (verde)
   - Si hay errores, revisa los logs

4. **Accede a la aplicación:**
   - URL: https://resultados-icfes-pcielo-2025.streamlit.app/
   - La aplicación debería mostrar la nueva versión comparativa

---

### Opción B: Si la App NO Está Conectada (Primera Vez)

Si aún no has conectado el repositorio con Streamlit Cloud:

#### Paso 1: Acceder a Streamlit Cloud

1. Ve a: https://share.streamlit.io/
2. Haz clic en **"Sign in"** o **"Get started"**
3. Inicia sesión con tu cuenta de GitHub (usuario: **alvaretto**)

#### Paso 2: Crear Nueva App

1. Haz clic en **"New app"** o **"Create app"**
2. Selecciona las siguientes opciones:

   **Repository:**
   ```
   alvaretto/resultados-icfes
   ```

   **Branch:**
   ```
   main
   ```

   **Main file path:**
   ```
   streamlit_app.py
   ```

   **App URL (custom subdomain):**
   ```
   resultados-icfes-pcielo-2025
   ```

3. Haz clic en **"Deploy!"**

#### Paso 3: Esperar el Despliegue

1. Streamlit Cloud comenzará a:
   - Clonar el repositorio
   - Instalar las dependencias de `requirements.txt`
   - Configurar el entorno con Python 3.11 (según `runtime.txt`)
   - Iniciar la aplicación

2. Este proceso puede tomar **2-5 minutos**

3. Verás un indicador de progreso con los logs en tiempo real

#### Paso 4: Verificar el Despliegue

1. Una vez completado, verás el mensaje: **"Your app is live!"**
2. La URL será: https://resultados-icfes-pcielo-2025.streamlit.app/
3. Haz clic en la URL para abrir la aplicación

---

## 🔍 Verificación Post-Despliegue

### Checklist de Verificación:

- [ ] **La aplicación carga correctamente**
  - No hay errores en la página principal
  - El título y header se muestran correctamente

- [ ] **Los datos se cargan correctamente**
  - Los datos de 2024 se muestran (116 estudiantes)
  - Los datos de 2025 se muestran (104 estudiantes)
  - No hay errores de "archivo no encontrado"

- [ ] **Las 8 páginas funcionan:**
  - [ ] 🏠 Inicio - Comparativo General
  - [ ] 📊 Estadísticas por Estudiante
  - [ ] 🎓 Estadísticas por Grado
  - [ ] 📚 Estadísticas por Área
  - [ ] 🏫 Estadísticas por Modelo
  - [ ] 📈 Análisis de Avances
  - [ ] 🏆 Rankings y Destacados
  - [ ] 💾 Descargar Datos

- [ ] **Los gráficos se renderizan correctamente**
  - Gráficos de barras comparativos
  - Histogramas de distribución
  - Gráficos de avances con colores

- [ ] **El formato condicional funciona:**
  - ✅ Verde para avances positivos
  - ❌ Rojo para retrocesos
  - ⚪ Amarillo para sin cambios

- [ ] **Las descargas funcionan:**
  - Descarga CSV
  - Descarga Excel

---

## 🐛 Solución de Problemas Comunes

### Problema 1: Error "File not found"

**Causa:** Los archivos de datos no se encuentran en la ruta esperada.

**Solución:**
1. Verifica que los archivos estén en el repositorio:
   ```bash
   git ls-files | grep "data/"
   ```
2. Asegúrate de que las rutas en `streamlit_app.py` sean correctas
3. Los archivos Excel deben estar en `data/` (no en la raíz)

### Problema 2: Error "Module not found"

**Causa:** Falta una dependencia en `requirements.txt`.

**Solución:**
1. Verifica que `requirements.txt` contenga todas las dependencias
2. Asegúrate de que las versiones sean compatibles
3. Si agregaste una nueva dependencia, actualiza `requirements.txt` y haz push

### Problema 3: La aplicación se queda "cargando"

**Causa:** Puede haber un error en el código o los datos son muy grandes.

**Solución:**
1. Revisa los logs en Streamlit Cloud (botón "Manage app" → "Logs")
2. Verifica que los archivos Excel no sean demasiado grandes
3. Asegúrate de que el código no tenga bucles infinitos

### Problema 4: Error de memoria

**Causa:** Los datos son demasiado grandes para el plan gratuito de Streamlit Cloud.

**Solución:**
1. Optimiza el código para usar menos memoria
2. Usa `@st.cache_data` para cachear los datos
3. Considera reducir el tamaño de los archivos de datos

### Problema 5: La aplicación no se actualiza

**Causa:** Streamlit Cloud no detectó el nuevo commit.

**Solución:**
1. Ve al dashboard de Streamlit Cloud
2. Haz clic en "Manage app"
3. Haz clic en "Reboot app" para forzar una actualización

---

## 📊 Monitoreo de la Aplicación

### Dashboard de Streamlit Cloud

1. **Acceder al dashboard:**
   - URL: https://share.streamlit.io/
   - Inicia sesión con GitHub

2. **Ver métricas:**
   - Número de visitantes
   - Tiempo de actividad
   - Uso de recursos

3. **Ver logs:**
   - Haz clic en "Manage app"
   - Selecciona "Logs" para ver los logs en tiempo real
   - Útil para debugging

4. **Reiniciar la app:**
   - Haz clic en "Manage app"
   - Selecciona "Reboot app" para reiniciar

---

## 🔒 Configuración de Privacidad

### Opciones de Privacidad:

1. **Pública (Recomendado para este caso):**
   - Cualquiera con la URL puede acceder
   - No requiere autenticación
   - Ideal para compartir resultados

2. **Privada:**
   - Solo usuarios autorizados pueden acceder
   - Requiere configuración adicional
   - Disponible en planes pagos

### Para cambiar la privacidad:

1. Ve al dashboard de Streamlit Cloud
2. Haz clic en "Manage app"
3. Selecciona "Settings"
4. Cambia la configuración de privacidad

---

## 📞 Soporte y Recursos

### Documentación Oficial:

- **Streamlit Cloud Docs:** https://docs.streamlit.io/streamlit-community-cloud
- **Deployment Guide:** https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app
- **Troubleshooting:** https://docs.streamlit.io/streamlit-community-cloud/troubleshooting

### Recursos del Proyecto:

- **Guía de Uso:** `GUIA-USO-APLICACION-COMPARATIVA.md`
- **Inicio Rápido:** `INICIO-RAPIDO.md`
- **README Técnico:** `README-APLICACION-COMPARATIVA.md`

---

## ✅ Resumen de URLs

| Recurso | URL |
|---------|-----|
| **Aplicación Desplegada** | https://resultados-icfes-pcielo-2025.streamlit.app/ |
| **Repositorio GitHub** | https://github.com/alvaretto/resultados-icfes |
| **Último Commit** | https://github.com/alvaretto/resultados-icfes/commit/94a9dd1c286c39e828e1d0c40575a1b272612f81 |
| **Streamlit Cloud Dashboard** | https://share.streamlit.io/ |

---

## 🎉 ¡Listo!

Una vez completados estos pasos, tu aplicación estará disponible públicamente en:

**https://resultados-icfes-pcielo-2025.streamlit.app/**

La aplicación se actualizará automáticamente cada vez que hagas push a la rama `main` del repositorio.

---

**Última actualización:** 2025-10-23  
**Versión:** 2.0  
**Estado:** ✅ Funcional

