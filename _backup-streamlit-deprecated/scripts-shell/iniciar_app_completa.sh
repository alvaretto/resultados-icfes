#!/bin/bash
# Script de inicio rápido para la aplicación de análisis ICFES completa
# Institución Educativa Pedacito de Cielo

echo "================================================================================"
echo "  📊 APLICACIÓN DE ANÁLISIS ICFES SABER 11 - 2025"
echo "  Institución Educativa Pedacito de Cielo"
echo "================================================================================"
echo ""

# Verificar que estamos en el directorio correcto
if [ ! -f "app_resultados_icfes_completo.py" ]; then
    echo "❌ Error: No se encuentra el archivo app_resultados_icfes_completo.py"
    echo "   Por favor, ejecuta este script desde el directorio del proyecto."
    exit 1
fi

# Verificar archivos de datos
echo "🔍 Verificando archivos de datos..."
ARCHIVO1="PCIELO-RESULTADOS-ICFES-MODELO-AULA-REGULAR-2025.xlsx"
ARCHIVO2="PCIELO-RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx"

if [ -f "$ARCHIVO1" ]; then
    echo "   ✓ $ARCHIVO1 encontrado"
else
    echo "   ✗ $ARCHIVO1 NO encontrado"
    echo "   ⚠️  La aplicación no funcionará sin este archivo"
fi

if [ -f "$ARCHIVO2" ]; then
    echo "   ✓ $ARCHIVO2 encontrado"
else
    echo "   ✗ $ARCHIVO2 NO encontrado"
    echo "   ⚠️  La aplicación no funcionará sin este archivo"
fi

echo ""

# Verificar entorno virtual
if [ -d "venv" ]; then
    echo "🐍 Activando entorno virtual..."
    source venv/bin/activate
    echo "   ✓ Entorno virtual activado"
else
    echo "⚠️  No se encontró entorno virtual (venv)"
    echo "   Continuando con el Python del sistema..."
fi

echo ""

# Verificar dependencias
echo "📦 Verificando dependencias..."
if python3 -c "import streamlit, pandas, plotly, scipy" 2>/dev/null; then
    echo "   ✓ Todas las dependencias están instaladas"
else
    echo "   ✗ Faltan dependencias"
    echo "   Instalando dependencias..."
    pip install -r requirements-webapp.txt
fi

echo ""
echo "================================================================================"
echo "  🚀 INICIANDO APLICACIÓN"
echo "================================================================================"
echo ""
echo "La aplicación se abrirá automáticamente en tu navegador."
echo "Si no se abre, accede manualmente a: http://localhost:8501"
echo ""
echo "Para detener la aplicación, presiona Ctrl+C"
echo ""
echo "================================================================================"
echo ""

# Ejecutar la aplicación
streamlit run app_resultados_icfes_completo.py

