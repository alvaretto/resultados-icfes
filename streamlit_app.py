#!/usr/bin/env python3
"""
Punto de entrada para Streamlit Cloud
Carga la aplicación desde app/app.py
"""

import sys
import os

# Agregar el directorio app al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

# Importar y ejecutar la aplicación
from app import *

