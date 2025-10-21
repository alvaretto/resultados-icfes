#!/bin/bash

# Script de inicio rápido para la aplicación ICFES
# Institución Educativa Pedacito de Cielo

echo "=================================================="
echo "  Aplicación Comparativa ICFES 2024 vs 2025"
echo "  Institución Educativa Pedacito de Cielo"
echo "=================================================="
echo ""

# Verificar que estamos en el directorio correcto
if [ ! -f "streamlit_app.py" ]; then
    echo "❌ Error: No se encuentra streamlit_app.py"
    echo "   Por favor, ejecuta este script desde el directorio del proyecto"
    exit 1
fi

# Verificar que los archivos de datos existen
echo "🔍 Verificando archivos de datos..."

if [ ! -f "data/RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx" ]; then
    echo "❌ Error: No se encuentra data/RESULTADOS-ICFES-AULA-REGULAR-2025.xlsx"
    exit 1
fi

if [ ! -f "data/RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx" ]; then
    echo "❌ Error: No se encuentra data/RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx"
    exit 1
fi

echo "✅ Archivos de datos encontrados"
echo ""

# Verificar dependencias
echo "🔍 Verificando dependencias..."

if ! command -v streamlit &> /dev/null; then
    echo "❌ Error: Streamlit no está instalado"
    echo "   Instala las dependencias con: pip install -r requirements.txt"
    exit 1
fi

echo "✅ Dependencias verificadas"
echo ""

# Iniciar la aplicación
echo "🚀 Iniciando aplicación..."
echo ""
echo "La aplicación se abrirá en tu navegador en:"
echo "  - Local: http://localhost:8501"
echo "  - Red: http://192.168.10.13:8501"
echo ""
echo "Presiona Ctrl+C para detener la aplicación"
echo ""

streamlit run streamlit_app.py

