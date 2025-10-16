# 🔐 Solución: Push a GitHub para Streamlit Cloud

## 🎯 Problema Actual

**Error detectado:**
```
remote: Permission to alvaretto/resultados-icfes.git denied to alvarettosky.
fatal: The requested URL returned error: 403
```

**Causa:** Hay credenciales almacenadas de otro usuario (`alvarettosky`) que no tiene permisos en el repositorio `alvaretto/resultados-icfes`.

**Impacto:** Streamlit Cloud no puede ver los cambios porque no están en GitHub.

---

## ✅ Solución Rápida (Recomendada)

### Opción 1: Usar Token de Acceso Personal

Esta es la forma más rápida y segura:

#### 1. Crear Token en GitHub (si no tienes uno)

1. Ir a: https://github.com/settings/tokens
2. Click en **"Generate new token"** → **"Generate new token (classic)"**
3. Configurar:
   - **Note:** "Streamlit ICFES App"
   - **Expiration:** 90 días (o lo que prefieras)
   - **Scopes:** Marcar `repo` (acceso completo a repositorios)
4. Click en **"Generate token"**
5. **COPIAR EL TOKEN** (solo se muestra una vez)

#### 2. Hacer Push con el Token

```bash
cd /home/proyectos/Escritorio/Resultados-ICFES-2025

# Reemplaza TU_TOKEN con el token que copiaste
git push https://TU_TOKEN@github.com/alvaretto/resultados-icfes.git main
```

**Ejemplo:**
```bash
git push https://ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxx@github.com/alvaretto/resultados-icfes.git main
```

#### 3. Guardar Credenciales (Opcional)

Para no tener que usar el token cada vez:

```bash
# Actualizar la URL del remote con el token
git remote set-url origin https://TU_TOKEN@github.com/alvaretto/resultados-icfes.git

# Ahora puedes hacer push normalmente
git push origin main
```

---

### Opción 2: Limpiar Credenciales y Volver a Autenticar

```bash
# 1. Limpiar credenciales almacenadas
git credential reject <<EOF
protocol=https
host=github.com
EOF

# 2. Intentar push (te pedirá usuario y contraseña/token)
git push origin main

# Cuando te pida:
# Username: alvaretto
# Password: [pegar tu token de acceso personal]
```

---

### Opción 3: Usar SSH (Más Seguro a Largo Plazo)

#### 1. Verificar si tienes clave SSH

```bash
ls -la ~/.ssh/id_*.pub
```

Si no tienes, crear una:

```bash
ssh-keygen -t ed25519 -C "37968648+alvaretto@users.noreply.github.com"
# Presionar Enter para aceptar ubicación por defecto
# Presionar Enter para sin contraseña (o poner una)
```

#### 2. Copiar la clave pública

```bash
cat ~/.ssh/id_ed25519.pub
```

#### 3. Añadir a GitHub

1. Ir a: https://github.com/settings/keys
2. Click en **"New SSH key"**
3. **Title:** "Laptop ICFES"
4. **Key:** Pegar el contenido de `id_ed25519.pub`
5. Click en **"Add SSH key"**

#### 4. Cambiar remote a SSH

```bash
git remote set-url origin git@github.com:alvaretto/resultados-icfes.git
git push origin main
```

---

## 🚀 Después del Push Exitoso

Una vez que el push funcione, verás algo como:

```
Enumerando objetos: 11, listo.
Contando objetos: 100% (11/11), listo.
Compresión delta usando hasta 12 hilos
Comprimiendo objetos: 100% (9/9), listo.
Escribiendo objetos: 100% (9/9), 25.67 KiB | 25.67 MiB/s, listo.
Total 9 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/alvaretto/resultados-icfes.git
   adf0125..7fd337f  main -> main
```

### Siguiente Paso: Actualizar Streamlit Cloud

1. **Ir a Streamlit Cloud:** https://share.streamlit.io
2. **Acceder a tu aplicación**
3. **Verificar configuración:**
   - Click en **Settings** (⚙️)
   - **Main file path:** Debe ser `app_resultados_icfes_completo.py`
   - Si está en `app.py` o `app_resultados_icfes.py`, **CÁMBIALO**
4. **Reboot la aplicación:**
   - Click en el menú (⋮)
   - Click en **"Reboot app"**
   - Esperar 1-2 minutos
5. **Limpiar caché:**
   - En la aplicación web, presionar tecla **"C"**
   - O usar el menú: **Clear cache**
6. **Refrescar navegador:**
   - Presionar **Ctrl+Shift+R** (recarga forzada)

---

## 📋 Checklist Completo

### Fase 1: Push a GitHub
- [ ] Obtener token de acceso personal de GitHub
- [ ] Ejecutar push con token
- [ ] Verificar que el push fue exitoso
- [ ] Verificar en GitHub que los cambios están visibles

### Fase 2: Configurar Streamlit Cloud
- [ ] Acceder a Streamlit Cloud
- [ ] Verificar Main file path = `app_resultados_icfes_completo.py`
- [ ] Hacer Reboot app
- [ ] Esperar 1-2 minutos

### Fase 3: Verificar Cambios
- [ ] Limpiar caché (tecla "C")
- [ ] Refrescar navegador (Ctrl+Shift+R)
- [ ] Verificar que aparece "Modelo Flexible"
- [ ] Verificar estadísticas de ambos modelos
- [ ] Verificar comparativas

---

## 🔍 Verificar que los Cambios Están en GitHub

Después del push, verifica en tu navegador:

**URL:** https://github.com/alvaretto/resultados-icfes/blob/main/app_resultados_icfes_completo.py

Deberías ver:
- Archivo de 49 KB
- 1,600 líneas
- Última modificación: hace unos minutos
- Contenido con "Modelo Flexible"

---

## ⚠️ Problemas Comunes

### Problema 1: "Token inválido"
**Solución:** Generar un nuevo token con permisos `repo`

### Problema 2: "Streamlit Cloud sigue mostrando versión antigua"
**Solución:**
1. Verificar que Main file path es correcto
2. Hacer Reboot app (no solo Clear cache)
3. Esperar 2-3 minutos completos
4. Verificar logs en Streamlit Cloud por errores

### Problema 3: "Error al cargar datos en Streamlit Cloud"
**Causa:** Los archivos Excel no están en GitHub

**Solución:**
```bash
# Verificar si los archivos están en .gitignore
cat .gitignore | grep xlsx

# Si están en .gitignore, quitarlos o añadir excepción
# Luego hacer commit y push de los archivos Excel
git add PCIELO-RESULTADOS-ICFES-*.xlsx
git commit -m "Añadir archivos de datos Excel"
git push origin main
```

---

## 📞 Comandos de Verificación

```bash
# Ver estado actual
git status

# Ver último commit
git log --oneline -1

# Ver diferencia con remoto
git log origin/main..HEAD

# Verificar remote
git remote -v

# Ver archivos en el último commit
git show --name-only HEAD
```

---

## 🎯 Resumen Ejecutivo

**Para ver los cambios en Streamlit Cloud:**

1. **Push a GitHub** (con token):
   ```bash
   git push https://TU_TOKEN@github.com/alvaretto/resultados-icfes.git main
   ```

2. **En Streamlit Cloud:**
   - Settings → Main file = `app_resultados_icfes_completo.py`
   - Menú → Reboot app
   - Esperar 2 minutos

3. **En la aplicación:**
   - Presionar "C" (limpiar caché)
   - Ctrl+Shift+R (refrescar navegador)

**Resultado esperado:**
- ✅ Ver "Modelo Aula Regular" (36 estudiantes)
- ✅ Ver "Modelo Flexible" (62 estudiantes)
- ✅ Ver comparativas entre modelos
- ✅ Ver 8 pestañas de análisis

---

**Creado:** 2025-10-16  
**Última actualización:** 2025-10-16 15:15

