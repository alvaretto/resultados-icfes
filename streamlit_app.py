#!/usr/bin/env python3
"""
Aplicación Streamlit para Análisis Comparativo de Resultados ICFES Saber 11°
Institución Educativa Pedacito de Cielo — Comparación 2024 vs 2025

Punto de entrada principal. Toda la lógica está en app/.
"""

import streamlit as st

# ============================================================================
# CONFIGURACIÓN DE PÁGINA (debe ir antes de cualquier otra llamada a st)
# ============================================================================

st.set_page_config(
    page_title="Análisis ICFES - Pedacito de Cielo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# IMPORTS DE MÓDULOS
# ============================================================================

from app.chat_ia_icfes import mostrar_chat, inicializar_chat
from app.data_loader import cargar_datos_2024, cargar_datos_2025
from app.estadisticas import calcular_estadisticas_2025, calcular_estadisticas_por_grupo
from app.ui_components import (
    CSS_ESTILOS,
    mostrar_sidebar,
    mostrar_pagina_inicio,
    mostrar_estadisticas_estudiante,
    mostrar_estadisticas_grado,
    mostrar_estadisticas_area,
    mostrar_estadisticas_modelo,
    mostrar_rankings,
    mostrar_descarga_datos,
)
from app.comparativo import mostrar_verificacion_datos

# ============================================================================
# ESTILOS
# ============================================================================

st.markdown(CSS_ESTILOS, unsafe_allow_html=True)

# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    inicializar_chat()

    # Cargar datos
    datos_2024 = cargar_datos_2024()
    datos_2025_raw = cargar_datos_2025()

    if datos_2025_raw is None:
        st.error("No se pudieron cargar los datos de 2025")
        return

    # Calcular estadísticas 2025
    stats_regular_2025 = calcular_estadisticas_2025(datos_2025_raw['df_regular'], 'Aula Regular (Jornada 1)')
    stats_flexible_2025 = calcular_estadisticas_2025(datos_2025_raw['df_flexible'], 'Modelo Flexible (Jornada 0)')
    stats_institucional_2025 = calcular_estadisticas_2025(datos_2025_raw['df_todos'], 'Todos')
    stats_grupos_2025 = calcular_estadisticas_por_grupo(datos_2025_raw['df_todos'])

    # Sidebar
    pagina, mostrar_chat_ia = mostrar_sidebar(datos_2024, stats_institucional_2025)

    # ── MODO CHAT ────────────────────────────────────────────────────────────
    if mostrar_chat_ia:
        mostrar_chat(df=datos_2025_raw['df_todos'], pagina_actual="Chat de IA", datos_2024=datos_2024)
        return

    # ── MODO NORMAL ──────────────────────────────────────────────────────────
    st.markdown(
        '<div class="main-header">📊 Análisis Comparativo ICFES Saber 11°<br>'
        'Institución Educativa Pedacito de Cielo<br>2024 vs 2025</div>',
        unsafe_allow_html=True
    )

    # Routing de páginas
    if pagina == "🏠 Inicio - Comparativo General":
        mostrar_pagina_inicio(datos_2024, stats_regular_2025, stats_flexible_2025,
                              stats_institucional_2025, stats_grupos_2025, datos_2025_raw)

    elif pagina == "📊 Estadísticas por Estudiante":
        mostrar_estadisticas_estudiante(datos_2025_raw)

    elif pagina == "🎓 Estadísticas por Grado":
        mostrar_estadisticas_grado(datos_2025_raw)

    elif pagina == "📚 Estadísticas por Área":
        mostrar_estadisticas_area(datos_2024, datos_2025_raw, stats_institucional_2025)

    elif pagina == "🏫 Estadísticas por Modelo":
        mostrar_estadisticas_modelo(datos_2024, stats_regular_2025, stats_flexible_2025)

    elif pagina == "🏆 Rankings y Destacados":
        mostrar_rankings(datos_2025_raw)

    elif pagina == "🏫 Comparativo Municipal":
        mostrar_verificacion_datos(datos_2024, stats_regular_2025, stats_flexible_2025)

    elif pagina == "📥 Descargar Datos":
        mostrar_descarga_datos(datos_2025_raw)


if __name__ == "__main__":
    main()
