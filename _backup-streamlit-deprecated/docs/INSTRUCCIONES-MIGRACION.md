# 📦 Instrucciones de Migración Completada

## ✅ Resumen de la Migración

El proyecto **Resultados-ICFES-2025** ha sido migrado exitosamente desde:

**Ubicación Original:**
```
/home/proyectos/Escritorio/Resultados-ICFES-2025
```

**Nueva Ubicación:**
```
/media/disco1tb/Proyectos/Resultados-ICFES-2025
```

---

## 🎯 Tareas Completadas

### ✅ 1. Copia Completa del Proyecto
- ✅ Todos los archivos del proyecto copiados con `rsync`
- ✅ Archivos ocultos incluidos (`.git`, `.gitignore`, `.augment`, etc.)
- ✅ Estructura de directorios preservada
- ✅ Permisos de archivos mantenidos

### ✅ 2. Repositorio Git Intacto
- ✅ Directorio `.git` copiado completamente
- ✅ Historial de commits preservado (verificado con `git log`)
- ✅ Configuración de remote mantenida
- ✅ Estado del repositorio: limpio y sincronizado con `origin/main`

### ✅ 3. Entorno Virtual Recreado
- ✅ Entorno virtual anterior eliminado
- ✅ Nuevo entorno virtual creado con Python 3.13.7
- ✅ Todas las dependencias instaladas desde `requirements.txt`:
  - streamlit >= 1.32.0 ✅
  - pandas >= 2.2.0 ✅
  - plotly >= 5.18.0 ✅
  - openpyxl >= 3.1.2 ✅
  - numpy >= 1.26.0 ✅
  - scipy >= 1.12.0 ✅

### ✅ 4. Configuraciones Actualizadas
- ✅ Permisos de ejecución establecidos en scripts shell
- ✅ Rutas absolutas actualizadas a rutas relativas
- ✅ Archivo `scripts/04-analizar_excel.py` actualizado

### ✅ 5. Verificación de Funcionalidad
- ✅ Aplicación Streamlit probada y funcionando correctamente
- ✅ Entorno virtual activado sin errores
- ✅ Todas las dependencias verificadas

---

## 🚀 Cómo Usar el Proyecto desde la Nueva Ubicación

### 1. Navegar al Directorio del Proyecto

```bash
cd /media/disco1tb/Proyectos/Resultados-ICFES-2025
```

### 2. Activar el Entorno Virtual

```bash
source venv/bin/activate
```

Deberías ver el prefijo `(venv)` en tu terminal:
```
(venv) proyectos@hostname:/media/disco1tb/Proyectos/Resultados-ICFES-2025$
```

### 3. Ejecutar la Aplicación Streamlit

**Opción A: Usando el script de inicio rápido**
```bash
./iniciar_aplicacion.sh
```

**Opción B: Comando directo**
```bash
streamlit run streamlit_app.py
```

**Opción C: Con puerto específico**
```bash
streamlit run streamlit_app.py --server.port 8501
```

### 4. Acceder a la Aplicación

La aplicación se abrirá automáticamente en tu navegador en:
- **Local:** http://localhost:8501
- **Red:** http://192.168.10.13:8501

### 5. Detener la Aplicación

Presiona `Ctrl+C` en la terminal donde se está ejecutando Streamlit.

### 6. Desactivar el Entorno Virtual

Cuando termines de trabajar:
```bash
deactivate
```

---

## 📋 Verificación del Sistema

### Verificar Versión de Python
```bash
cd /media/disco1tb/Proyectos/Resultados-ICFES-2025
source venv/bin/activate
python --version
```
**Resultado esperado:** `Python 3.13.7`

### Verificar Versión de Streamlit
```bash
streamlit --version
```
**Resultado esperado:** `Streamlit, version 1.50.0`

### Verificar Dependencias Instaladas
```bash
pip list
```

### Verificar Estado de Git
```bash
git status
```

### Verificar Historial de Commits
```bash
git log --oneline -5
```

---

## 🔧 Comandos Útiles

### Actualizar Dependencias
```bash
cd /media/disco1tb/Proyectos/Resultados-ICFES-2025
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

### Sincronizar con GitHub
```bash
cd /media/disco1tb/Proyectos/Resultados-ICFES-2025
git add .
git commit -m "Descripción de los cambios"
git push origin main
```

### Ver Logs de la Aplicación
```bash
cd /media/disco1tb/Proyectos/Resultados-ICFES-2025
ls -la logs/
```

---

## 📁 Estructura del Proyecto

```
/media/disco1tb/Proyectos/Resultados-ICFES-2025/
├── 📄 streamlit_app.py              # Aplicación principal
├── 📄 requirements.txt              # Dependencias Python
├── 📄 runtime.txt                   # Versión de Python
├── 📄 iniciar_aplicacion.sh         # Script de inicio rápido
├── 📁 venv/                         # Entorno virtual (NUEVO)
├── 📁 .git/                         # Repositorio Git
├── 📁 data/                         # Archivos de datos Excel
├── 📁 scripts/                      # Scripts Python
├── 📁 scripts-shell/                # Scripts shell
├── 📁 docs-proyecto/                # Documentación
├── 📁 logs/                         # Logs de ejecución
├── 📁 pdfs_descargados/             # PDFs descargados
└── 📁 config/                       # Archivos de configuración
```

---

## ⚠️ Notas Importantes

### 1. NO Eliminar el Directorio Original Todavía
El directorio original en `/home/proyectos/Escritorio/Resultados-ICFES-2025` **NO ha sido eliminado** como medida de seguridad. 

**Recomendación:** Trabaja con la nueva ubicación durante algunos días para asegurarte de que todo funciona correctamente antes de eliminar el directorio original.

### 2. Actualizar Marcadores y Atajos
Si tienes marcadores o atajos que apuntan al directorio original, actualízalos a:
```
/media/disco1tb/Proyectos/Resultados-ICFES-2025
```

### 3. Variables de Entorno
Si tienes variables de entorno que apuntan al directorio original, actualízalas en tu archivo `~/.bashrc` o `~/.zshrc`:
```bash
export ICFES_PROJECT="/media/disco1tb/Proyectos/Resultados-ICFES-2025"
```

### 4. Configuración de IDE
Si usas un IDE (VS Code, PyCharm, etc.), abre el proyecto desde la nueva ubicación:
```
File > Open Folder > /media/disco1tb/Proyectos/Resultados-ICFES-2025
```

---

## 🔍 Solución de Problemas

### Problema: "No se encuentra el módulo streamlit"
**Solución:**
```bash
cd /media/disco1tb/Proyectos/Resultados-ICFES-2025
source venv/bin/activate
pip install -r requirements.txt
```

### Problema: "Permission denied" al ejecutar scripts
**Solución:**
```bash
chmod +x iniciar_aplicacion.sh
chmod +x scripts-shell/*.sh
```

### Problema: Error al cargar archivos de datos
**Solución:** Verifica que los archivos Excel estén en el directorio `data/`:
```bash
ls -la data/*.xlsx
```

### Problema: Git no reconoce el repositorio
**Solución:** Verifica la configuración de Git:
```bash
cd /media/disco1tb/Proyectos/Resultados-ICFES-2025
git remote -v
git status
```

---

## 📞 Información de Contacto

**Proyecto:** Análisis Comparativo de Resultados ICFES Saber 11°  
**Institución:** Institución Educativa Pedacito de Cielo  
**Comparación:** 2024 vs 2025

---

## 📝 Historial de Migración

- **Fecha de Migración:** 22 de octubre de 2025
- **Ubicación Original:** `/home/proyectos/Escritorio/Resultados-ICFES-2025`
- **Nueva Ubicación:** `/media/disco1tb/Proyectos/Resultados-ICFES-2025`
- **Método de Copia:** `rsync -avh --progress`
- **Python Version:** 3.13.7
- **Streamlit Version:** 1.50.0
- **Estado:** ✅ Migración Completada Exitosamente

---

## ✅ Checklist de Verificación Post-Migración

- [x] Todos los archivos copiados correctamente
- [x] Repositorio Git intacto con historial completo
- [x] Entorno virtual recreado con Python 3.13.7
- [x] Todas las dependencias instaladas
- [x] Permisos de archivos establecidos
- [x] Rutas absolutas actualizadas
- [x] Aplicación Streamlit funciona correctamente
- [x] Documentación de migración creada
- [ ] Trabajar con la nueva ubicación durante varios días
- [ ] Eliminar directorio original (después de verificación completa)

---

**¡La migración se completó exitosamente! El proyecto está listo para usar desde la nueva ubicación.** 🎉
