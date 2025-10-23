# 🎯 Guía: Editar Aplicación en Streamlit Cloud

## 📍 Ubicación Actual

Estás en: **https://share.streamlit.io** → **My apps**

Ves tu aplicación:
```
resultados-icfes · main · app_resultados_icfes.py
```

---

## ⚠️ Problema Identificado

**Archivo actual:** `app_resultados_icfes.py` (versión antigua, solo Aula Regular)
**Archivo necesario:** `app_resultados_icfes_completo.py` (versión completa con Modelo Flexible)

**Por eso no ves el Modelo Flexible** - Streamlit Cloud está ejecutando el archivo incorrecto.

---

## ✅ Solución: Cambiar el Archivo Principal

### **Paso 1: Acceder a Settings**

1. Localiza tu app: **resultados-icfes**
2. En el lado derecho, verás **3 puntos verticales (⋮)**
3. **Click en los 3 puntos (⋮)**
4. Aparecerá un menú desplegable
5. **Click en "Settings"** (primera opción)

```
┌────────────────────────────────────────────────┐
│ resultados-icfes · main · app_resultados...  ⋮ │ ← Click aquí
└────────────────────────────────────────────────┘
                                               │
                                               ▼
                                         ┌─────────────┐
                                         │ Settings    │ ← Click aquí
                                         │ Reboot app  │
                                         │ Delete app  │
                                         │ Manage app  │
                                         └─────────────┘
```

---

### **Paso 2: Cambiar Main File Path**

En la página de Settings verás varios campos:

#### **General Settings**

1. **App name:** resultados-icfes (dejar como está)

2. **Main file path:** `app_resultados_icfes.py` ← **CAMBIAR ESTO**

   **Cambiar a:** `app_resultados_icfes_completo.py`

   ```
   ┌─────────────────────────────────────────┐
   │ Main file path                          │
   │ ┌─────────────────────────────────────┐ │
   │ │ app_resultados_icfes_completo.py    │ │ ← Escribir esto
   │ └─────────────────────────────────────┘ │
   └─────────────────────────────────────────┘
   ```

3. **Python version:** (dejar como está, probablemente 3.11 o 3.12)

4. **Repository:** alvaretto/resultados-icfes (dejar como está)

5. **Branch:** main (dejar como está)

#### **Botón Save**

6. **Scroll hacia abajo**
7. **Click en el botón "Save"** (azul, esquina inferior derecha)

---

### **Paso 3: Reboot la Aplicación**

Después de guardar:

1. **Volver a "My apps"** (click en "My apps" en el menú superior)
2. **Localizar tu app:** resultados-icfes
3. **Click en los 3 puntos (⋮)** nuevamente
4. **Click en "Reboot app"**
5. **Confirmar** si te pide confirmación
6. **Esperar 1-2 minutos** (verás un spinner/loading)

```
Estado durante reboot:
┌────────────────────────────────────────┐
│ resultados-icfes                       │
│ 🔄 Rebooting...                        │
│ This may take a minute                 │
└────────────────────────────────────────┘
```

---

### **Paso 4: Verificar Cambios**

Una vez que la app se reinicie:

1. **Click en el nombre de la app** para abrirla
2. O **Click en el ícono de cuadrados (⋮⋮)** al lado izquierdo
3. La app se abrirá en una nueva pestaña

**Deberías ver:**
- ✅ Título: "Análisis Resultados ICFES - Pedacito de Cielo 2025"
- ✅ Pestaña "Vista General"
- ✅ "Modelo Aula Regular: 36 estudiantes"
- ✅ "Modelo Flexible: 62 estudiantes"
- ✅ Total: 98 estudiantes
- ✅ 8 pestañas de análisis

---

## 🔍 Si No Ves los Cambios

### **Opción A: Limpiar Caché**

En la aplicación web:
1. Presionar tecla **"C"** en el teclado
2. Aparecerá mensaje: "Cache cleared"
3. La app se recargará automáticamente

### **Opción B: Recarga Forzada del Navegador**

1. Presionar **Ctrl + Shift + R** (Windows/Linux)
2. O **Cmd + Shift + R** (Mac)
3. Esto fuerza al navegador a descargar todo de nuevo

### **Opción C: Verificar Logs**

1. En "My apps", click en los 3 puntos (⋮)
2. Click en **"Manage app"**
3. Ver la pestaña **"Logs"**
4. Buscar errores en rojo

Errores comunes:
- `FileNotFoundError`: Archivo no encontrado
- `ModuleNotFoundError`: Falta instalar dependencia
- `KeyError`: Error en los datos

---

## ⚠️ Antes de Cambiar el Archivo

### **IMPORTANTE: Verificar que el Push se Hizo**

Antes de cambiar a `app_resultados_icfes_completo.py`, asegúrate de que el archivo está en GitHub:

1. **Ir a tu repositorio:**
   https://github.com/alvaretto/resultados-icfes

2. **Verificar que existe:**
   - Buscar `app_resultados_icfes_completo.py` en la lista de archivos
   - Debería tener ~49 KB
   - Última modificación: reciente

3. **Si NO está en GitHub:**
   - Primero hacer el push (ver SOLUCION-PUSH-GITHUB.md)
   - Luego cambiar el Main file path

---

## 📋 Checklist Completo

### Antes de Editar:
- [ ] Verificar que `app_resultados_icfes_completo.py` está en GitHub
- [ ] Verificar que los archivos Excel están en GitHub (si es necesario)
- [ ] Tener acceso a Streamlit Cloud

### Durante la Edición:
- [ ] Click en los 3 puntos (⋮) de la app
- [ ] Click en "Settings"
- [ ] Cambiar Main file path a `app_resultados_icfes_completo.py`
- [ ] Click en "Save"
- [ ] Volver a "My apps"
- [ ] Click en los 3 puntos (⋮) nuevamente
- [ ] Click en "Reboot app"
- [ ] Esperar 1-2 minutos

### Después de Editar:
- [ ] Abrir la aplicación
- [ ] Presionar "C" para limpiar caché
- [ ] Ctrl+Shift+R para recarga forzada
- [ ] Verificar que aparece "Modelo Flexible"
- [ ] Verificar que hay 98 estudiantes totales
- [ ] Verificar que hay 8 pestañas

---

## 🎯 Alternativa: Crear Nueva App

Si tienes problemas editando, puedes crear una nueva app:

### **Paso 1: Click en "Create app"**

En la esquina superior derecha de "My apps"

### **Paso 2: Configurar la Nueva App**

1. **Repository:** alvaretto/resultados-icfes
2. **Branch:** main
3. **Main file path:** `app_resultados_icfes_completo.py` ← **IMPORTANTE**
4. **App URL:** resultados-icfes-completo (o el nombre que quieras)

### **Paso 3: Deploy**

1. Click en "Deploy!"
2. Esperar 2-3 minutos
3. La app se abrirá automáticamente

### **Paso 4: Eliminar App Antigua (Opcional)**

1. Volver a "My apps"
2. En la app antigua, click en los 3 puntos (⋮)
3. Click en "Delete app"
4. Confirmar

---

## 🔧 Opciones del Menú (⋮)

Cuando haces click en los 3 puntos, tienes estas opciones:

### **1. Settings** ⚙️
- Cambiar Main file path
- Cambiar Python version
- Configurar Secrets (variables de entorno)
- Cambiar recursos (CPU/memoria)

### **2. Reboot app** 🔄
- Reinicia la aplicación
- Carga cambios desde GitHub
- Limpia caché del servidor
- Toma 1-2 minutos

### **3. Delete app** 🗑️
- Elimina la aplicación permanentemente
- No se puede deshacer
- La URL dejará de funcionar

### **4. Manage app** 📊
- Ver logs en tiempo real
- Ver métricas de uso
- Ver estado de la app
- Ver errores

### **5. Favorite** ⭐
- Marca la app como favorita
- Aparece con estrella en la lista

### **6. Analytics** 📈
- Ver estadísticas de uso
- Número de visitantes
- Tiempo de uso
- Errores frecuentes

---

## 📞 Ayuda Adicional

### **Si el archivo no aparece en Settings:**

Puede ser que el archivo no esté en GitHub. Verifica:

```bash
# En tu terminal local
cd /home/proyectos/Escritorio/Resultados-ICFES-2025
git status
git log origin/main..HEAD

# Si hay commits pendientes
./push_a_github.sh
```

### **Si la app no arranca después del cambio:**

1. Click en los 3 puntos (⋮)
2. Click en "Manage app"
3. Ver la pestaña "Logs"
4. Buscar el error en rojo
5. Copiar el error y pedir ayuda

### **Si ves "File not found":**

El archivo no está en GitHub. Hacer push:

```bash
git add app_resultados_icfes_completo.py
git commit -m "Añadir versión completa"
git push origin main
```

---

## ✅ Resultado Final

Después de completar todos los pasos, tu app en Streamlit Cloud mostrará:

**URL:** https://[tu-app].streamlit.app

**Contenido:**
- 📊 Análisis Resultados ICFES - Pedacito de Cielo 2025
- 🏫 Modelo Aula Regular: 36 estudiantes (11A, 11B)
- 🎓 Modelo Flexible: 62 estudiantes (P3A, P3B, P3C)
- 📈 8 pestañas de análisis comparativo
- 📊 Gráficos interactivos
- 📋 Tablas de datos
- 🔍 Análisis estadísticos

---

## 🎉 ¡Listo!

Una vez que cambies el Main file path y hagas Reboot, deberías ver toda la funcionalidad del Modelo Flexible.

**¿Necesitas ayuda con algún paso específico?**

---

**Creado:** 2025-10-16
---
**Última actualización:** 2025-10-23  

