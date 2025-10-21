#!/bin/bash
# Script de diagnóstico para problemas con Streamlit
# Institución Educativa Pedacito de Cielo

echo "================================================================================"
echo "  🔍 DIAGNÓSTICO DE STREAMLIT"
echo "  Institución Educativa Pedacito de Cielo"
echo "================================================================================"
echo ""

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para imprimir con color
print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

# 1. VERIFICAR DIRECTORIO
echo "1. VERIFICANDO DIRECTORIO DE TRABAJO"
echo "-----------------------------------"
if [ -f "app_resultados_icfes_completo.py" ]; then
    print_success "Archivo app_resultados_icfes_completo.py encontrado"
    FILE_SIZE=$(ls -lh app_resultados_icfes_completo.py | awk '{print $5}')
    FILE_DATE=$(ls -l app_resultados_icfes_completo.py | awk '{print $6, $7, $8}')
    print_info "Tamaño: $FILE_SIZE"
    print_info "Última modificación: $FILE_DATE"
else
    print_error "Archivo app_resultados_icfes_completo.py NO encontrado"
    print_warning "Asegúrate de estar en el directorio correcto"
    exit 1
fi
echo ""

# 2. VERIFICAR ARCHIVOS APP
echo "2. VERIFICANDO ARCHIVOS DE APLICACIÓN"
echo "--------------------------------------"
APP_FILES=$(ls app*.py 2>/dev/null | wc -l)
if [ $APP_FILES -gt 1 ]; then
    print_warning "Se encontraron $APP_FILES archivos app*.py:"
    ls -lh app*.py | awk '{print "   - " $9 " (" $5 ")"}'
    print_info "Asegúrate de ejecutar el archivo correcto"
else
    print_success "Solo hay 1 archivo app*.py"
fi
echo ""

# 3. VERIFICAR PROCESOS DE STREAMLIT
echo "3. VERIFICANDO PROCESOS DE STREAMLIT"
echo "-------------------------------------"
STREAMLIT_PROCS=$(ps aux | grep -v grep | grep streamlit | wc -l)
if [ $STREAMLIT_PROCS -eq 0 ]; then
    print_warning "No hay procesos de Streamlit activos"
    print_info "Necesitas iniciar la aplicación con: streamlit run app_resultados_icfes_completo.py"
else
    print_success "Hay $STREAMLIT_PROCS proceso(s) de Streamlit activo(s):"
    ps aux | grep -v grep | grep streamlit | awk '{print "   PID: " $2 " - " $11 " " $12 " " $13}'
    
    # Verificar qué archivo está ejecutando
    RUNNING_FILE=$(ps aux | grep -v grep | grep streamlit | grep -o 'app[^ ]*\.py' | head -1)
    if [ "$RUNNING_FILE" == "app_resultados_icfes_completo.py" ]; then
        print_success "Ejecutando el archivo correcto: $RUNNING_FILE"
    else
        print_error "Ejecutando archivo incorrecto: $RUNNING_FILE"
        print_warning "Deberías ejecutar: app_resultados_icfes_completo.py"
    fi
fi
echo ""

# 4. VERIFICAR PUERTO 8501
echo "4. VERIFICANDO PUERTO 8501"
echo "--------------------------"
if command -v lsof &> /dev/null; then
    PORT_CHECK=$(lsof -i :8501 2>/dev/null | grep -v COMMAND | wc -l)
    if [ $PORT_CHECK -eq 0 ]; then
        print_warning "Puerto 8501 está libre"
        print_info "No hay aplicación escuchando en http://localhost:8501"
    else
        print_success "Puerto 8501 está en uso"
        lsof -i :8501 | grep -v COMMAND | awk '{print "   PID: " $2 " - " $1}'
    fi
else
    print_info "Comando lsof no disponible, saltando verificación de puerto"
fi
echo ""

# 5. VERIFICAR ESTADO DE GIT
echo "5. VERIFICANDO ESTADO DE GIT"
echo "-----------------------------"
if [ -d ".git" ]; then
    # Verificar cambios no guardados
    CHANGES=$(git status --porcelain app_resultados_icfes_completo.py | wc -l)
    if [ $CHANGES -eq 0 ]; then
        print_success "No hay cambios sin guardar en app_resultados_icfes_completo.py"
    else
        print_warning "Hay cambios sin guardar en app_resultados_icfes_completo.py"
        git status --porcelain app_resultados_icfes_completo.py
    fi
    
    # Verificar commits pendientes de push
    UNPUSHED=$(git log origin/main..HEAD --oneline 2>/dev/null | wc -l)
    if [ $UNPUSHED -eq 0 ]; then
        print_success "No hay commits pendientes de push"
    else
        print_warning "Hay $UNPUSHED commit(s) pendiente(s) de push"
        print_info "Ejecuta: git push origin main"
    fi
    
    # Mostrar último commit
    LAST_COMMIT=$(git log --oneline -1 2>/dev/null)
    print_info "Último commit: $LAST_COMMIT"
else
    print_warning "No es un repositorio Git"
fi
echo ""

# 6. VERIFICAR ARCHIVOS DE DATOS
echo "6. VERIFICANDO ARCHIVOS DE DATOS"
echo "---------------------------------"
ARCHIVO1="PCIELO-RESULTADOS-ICFES-MODELO-AULA-REGULAR-2025.xlsx"
ARCHIVO2="PCIELO-RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx"

if [ -f "$ARCHIVO1" ]; then
    print_success "$ARCHIVO1 encontrado"
else
    print_error "$ARCHIVO1 NO encontrado"
fi

if [ -f "$ARCHIVO2" ]; then
    print_success "$ARCHIVO2 encontrado"
else
    print_error "$ARCHIVO2 NO encontrado"
fi
echo ""

# 7. VERIFICAR DEPENDENCIAS
echo "7. VERIFICANDO DEPENDENCIAS"
echo "---------------------------"
if python3 -c "import streamlit" 2>/dev/null; then
    STREAMLIT_VERSION=$(python3 -c "import streamlit; print(streamlit.__version__)" 2>/dev/null)
    print_success "Streamlit instalado (versión $STREAMLIT_VERSION)"
else
    print_error "Streamlit NO instalado"
    print_info "Instala con: pip install streamlit"
fi

if python3 -c "import pandas" 2>/dev/null; then
    print_success "Pandas instalado"
else
    print_error "Pandas NO instalado"
fi

if python3 -c "import plotly" 2>/dev/null; then
    print_success "Plotly instalado"
else
    print_error "Plotly NO instalado"
fi
echo ""

# 8. RESUMEN Y RECOMENDACIONES
echo "================================================================================"
echo "  📋 RESUMEN Y RECOMENDACIONES"
echo "================================================================================"
echo ""

# Determinar escenario
if [ $STREAMLIT_PROCS -eq 0 ]; then
    echo "🎯 ESCENARIO DETECTADO: Aplicación NO está corriendo"
    echo ""
    echo "RECOMENDACIONES:"
    echo "1. Limpiar caché de Streamlit:"
    echo "   streamlit cache clear"
    echo ""
    echo "2. Iniciar la aplicación:"
    echo "   streamlit run app_resultados_icfes_completo.py"
    echo ""
    echo "3. Abrir en el navegador:"
    echo "   http://localhost:8501"
    echo ""
    echo "4. Si no ves los cambios, presiona Ctrl+Shift+R en el navegador"
    echo ""
else
    RUNNING_FILE=$(ps aux | grep -v grep | grep streamlit | grep -o 'app[^ ]*\.py' | head -1)
    if [ "$RUNNING_FILE" == "app_resultados_icfes_completo.py" ]; then
        echo "🎯 ESCENARIO DETECTADO: Aplicación corriendo correctamente"
        echo ""
        echo "RECOMENDACIONES para ver cambios:"
        echo "1. En la aplicación web, presiona la tecla 'C' para limpiar caché"
        echo "2. O presiona 'R' para recargar"
        echo "3. O en el navegador: Ctrl+Shift+R (recarga forzada)"
        echo ""
        echo "Si aún no ves cambios:"
        echo "1. Detener la aplicación (Ctrl+C en la terminal)"
        echo "2. Limpiar caché: streamlit cache clear"
        echo "3. Reiniciar: streamlit run app_resultados_icfes_completo.py"
    else
        echo "🎯 ESCENARIO DETECTADO: Aplicación corriendo archivo INCORRECTO"
        echo ""
        echo "PROBLEMA: Estás ejecutando '$RUNNING_FILE' en lugar de 'app_resultados_icfes_completo.py'"
        echo ""
        echo "SOLUCIÓN:"
        echo "1. Detener la aplicación actual (Ctrl+C en la terminal)"
        echo "2. O matar el proceso: pkill -f streamlit"
        echo "3. Ejecutar el archivo correcto:"
        echo "   streamlit run app_resultados_icfes_completo.py"
    fi
fi

# Verificar si hay commits pendientes
if [ $UNPUSHED -gt 0 ]; then
    echo ""
    echo "⚠️  IMPORTANTE: Tienes commits pendientes de push"
    echo "Si usas Streamlit Cloud, ejecuta:"
    echo "   git push origin main"
    echo "Luego en Streamlit Cloud: Reboot app"
fi

echo ""
echo "================================================================================"
echo "Para más información, consulta: DIAGNOSTICO-STREAMLIT.md"
echo "================================================================================"

