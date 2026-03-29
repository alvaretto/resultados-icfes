"""
Páginas y componentes UI reutilizables de Streamlit:
sidebar, tabs, headers y las páginas principales de la aplicación.
"""

import io
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from .data_loader import AREAS
from .estadisticas import calcular_avance, formatear_avance, calcular_distribucion_niveles
from .visualizaciones import (
    crear_grafico_comparativo_areas,
    crear_grafico_avances,
    crear_grafico_avances_modelo,
    crear_grafico_global_evolucion,
    crear_grafico_grupos,
    crear_grafico_comparacion_modelos_areas,
    crear_grafico_lineas_grupos,
)
from .comparativo import (
    mostrar_ficha_tecnica,
    mostrar_analisis_dispersion,
    mostrar_niveles_desempeno_area,
    mostrar_resumen_niveles_todas_areas,
    mostrar_verificacion_datos,
)

# ============================================================================
# CSS
# ============================================================================

CSS_ESTILOS = """
<style>
    .main-header {
        font-size: 2.8rem;
        font-weight: bold;
        color: #1e3a8a;
        text-align: center;
        padding: 1.5rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 5px solid #667eea;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .avance-positivo {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        color: #155724;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    .avance-negativo {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
        color: #721c24;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    .avance-neutro {
        background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
        color: #856404;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    .subtitle {
        font-size: 1.5rem;
        font-weight: 600;
        color: #4a5568;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 3px solid #667eea;
        padding-bottom: 0.5rem;
    }
    .dataframe { font-size: 0.9rem; }
    .css-1d391kg { background-color: #f8f9fa; }
</style>
"""

# ============================================================================
# SIDEBAR
# ============================================================================

def mostrar_sidebar(datos_2024=None, stats_institucional_2025=None):
    """
    Renderiza el sidebar con logo, toggle de chat y navegación.
    Retorna (pagina, mostrar_chat_ia).
    """
    with st.sidebar:
        try:
            from PIL import Image
            import os
            logo_path = os.path.join(os.path.dirname(__file__), "..", "escudo-114x116-1.png")
            if os.path.exists(logo_path):
                logo = Image.open(logo_path)
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.image(logo, width=100)
            else:
                st.markdown('<h2 style="text-align: center; color: #667eea;">🏫</h2>', unsafe_allow_html=True)
        except Exception:
            st.markdown('<h2 style="text-align: center; color: #667eea;">🏫</h2>', unsafe_allow_html=True)

        st.markdown('<h3 style="text-align: center; color: #667eea;">Institución Educativa<br>Pedacito de Cielo</h3>', unsafe_allow_html=True)
        st.markdown("---")

        st.markdown("### 🤖 Pedazote, asistente de IA")

        if "chat_activado" not in st.session_state:
            st.session_state.chat_activado = False

        mostrar_chat_ia = st.checkbox(
            "Activar chat inteligente",
            value=st.session_state.chat_activado,
            key="toggle_chat",
            help="Pregunta sobre los datos, interpretaciones y recomendaciones pedagógicas"
        )

        st.session_state.chat_activado = mostrar_chat_ia

        if mostrar_chat_ia:
            st.success("✅ Chat Pedazote activado")
            num_mensajes = len(st.session_state.get("chat_messages", []))
            if num_mensajes > 0:
                st.info(f"💬 {num_mensajes} mensajes")
        else:
            st.info("ℹ️ Activa el chat para preguntar")

        st.markdown("---")

        if not mostrar_chat_ia:
            pagina = st.radio(
                "📑 Navegación",
                [
                    "🏠 Inicio - Comparativo General",
                    "📊 Estadísticas por Estudiante",
                    "🎓 Estadísticas por Grado",
                    "📚 Estadísticas por Área",
                    "🏫 Estadísticas por Modelo",
                    "🏆 Rankings y Destacados",
                    "🏫 Comparativo Municipal",
                    "📥 Descargar Datos"
                ]
            )
        else:
            pagina = "Chat de IA"
            st.info("💡 Desactiva el chat para volver a la navegación normal")

        if datos_2024 and stats_institucional_2025 and not mostrar_chat_ia:
            st.markdown("---")
            st.markdown("### 📅 Información")
            st.info(f"""
            **Año de comparación:** 2024 vs 2025

            **Estudiantes 2024:** {datos_2024['Institucional']['estudiantes']}

            **Estudiantes 2025:** {stats_institucional_2025['estudiantes']}
            """)

    return pagina, mostrar_chat_ia


# ============================================================================
# PÁGINA: INICIO - COMPARATIVO GENERAL
# ============================================================================

def mostrar_pagina_inicio(datos_2024, stats_regular_2025, stats_flexible_2025,
                          stats_institucional_2025, stats_grupos_2025, datos_2025_raw):
    """Página principal con comparativo general 2024 vs 2025"""

    st.markdown('<div class="title">📊 Comparativo General 2024 vs 2025</div>', unsafe_allow_html=True)
    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🏫 Avance Institucional Global",
        "📚 Avances por Modelos Educativos",
        "📊 Avances por Áreas de Conocimiento",
        "👥 Resultados por Grupos",
        "🎯 Niveles de Desempeño"
    ])

    # ── TAB 1: AVANCE INSTITUCIONAL GLOBAL ──────────────────────────────────
    with tab1:
        st.markdown('<div class="subtitle">🏫 Avance Institucional Global 2024 vs 2025</div>', unsafe_allow_html=True)
        st.info("📌 Esta sección muestra el comparativo general de toda la institución (todos los estudiantes combinados)")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Puntaje Global 2024", datos_2024['Institucional']['puntaje_global'], delta=None)

        with col2:
            st.metric("Puntaje Global 2025", stats_institucional_2025['puntaje_global'], delta=None)

        with col3:
            avance_global = calcular_avance(
                datos_2024['Institucional']['puntaje_global'],
                stats_institucional_2025['puntaje_global']
            )
            texto_avance, clase_avance = formatear_avance(avance_global)
            st.markdown(f'<div class="{clase_avance}">{texto_avance}</div>', unsafe_allow_html=True)

        st.markdown("---")
        mostrar_analisis_dispersion(datos_2024['Institucional'], stats_institucional_2025,
                                    "Análisis de Dispersión Institucional")

        st.markdown("#### 📈 Evolución del Puntaje Global Institucional")
        st.plotly_chart(
            crear_grafico_global_evolucion(
                datos_2024['Institucional']['puntaje_global'],
                stats_institucional_2025['puntaje_global']
            ),
            width="stretch"
        )

        st.markdown("---")
        mostrar_ficha_tecnica(datos_2024, stats_institucional_2025, datos_2025_raw)
        st.info("💡 Para ver el análisis detallado por áreas de conocimiento, consulta la pestaña '📊 Avances por Áreas de Conocimiento'")

    # ── TAB 2: AVANCES POR MODELOS EDUCATIVOS ───────────────────────────────
    with tab2:
        st.markdown('<div class="subtitle">📚 Avances por Modelos Educativos 2024 vs 2025</div>', unsafe_allow_html=True)
        st.info("📌 Esta sección compara el desempeño de Aula Regular (Jornada 1) y Modelo Flexible (Jornada 0) entre 2024 y 2025")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 📘 Aula Regular (Jornada 1)")
            avance_regular = calcular_avance(
                datos_2024['Aula Regular (Jornada 1)']['puntaje_global'],
                stats_regular_2025['puntaje_global']
            )
            texto_avance_regular, clase_avance_regular = formatear_avance(avance_regular)
            st.metric("Puntaje Global 2024", datos_2024['Aula Regular (Jornada 1)']['puntaje_global'])
            st.metric("Puntaje Global 2025", stats_regular_2025['puntaje_global'])
            st.markdown(f'<div class="{clase_avance_regular}">{texto_avance_regular}</div>', unsafe_allow_html=True)

        with col2:
            st.markdown("#### 📙 Modelo Flexible (Jornada 0)")
            avance_flexible = calcular_avance(
                datos_2024['Modelo Flexible (Jornada 0)']['puntaje_global'],
                stats_flexible_2025['puntaje_global']
            )
            texto_avance_flexible, clase_avance_flexible = formatear_avance(avance_flexible)
            st.metric("Puntaje Global 2024", datos_2024['Modelo Flexible (Jornada 0)']['puntaje_global'])
            st.metric("Puntaje Global 2025", stats_flexible_2025['puntaje_global'])
            st.markdown(f'<div class="{clase_avance_flexible}">{texto_avance_flexible}</div>', unsafe_allow_html=True)

        st.markdown("---")

        for modelo_key, stats_modelo, titulo_modelo in [
            ('Aula Regular (Jornada 1)', stats_regular_2025, "Avances por Área - Aula Regular"),
            ('Modelo Flexible (Jornada 0)', stats_flexible_2025, "Avances por Área - Modelo Flexible"),
        ]:
            st.markdown(f"#### 📊 {titulo_modelo}")
            tabla = []
            for area in AREAS:
                puntaje_2024 = datos_2024[modelo_key]['areas'][area]['promedio']
                puntaje_2025 = stats_modelo['areas'][area]['promedio']
                avance = calcular_avance(puntaje_2024, puntaje_2025)
                texto_avance, _ = formatear_avance(avance)
                tabla.append({'Área': area, '2024': puntaje_2024, '2025': puntaje_2025,
                              'Avance': avance, 'Estado': texto_avance})

            df_tabla = pd.DataFrame(tabla)
            st.dataframe(df_tabla, width="stretch", hide_index=True)
            st.plotly_chart(
                crear_grafico_avances_modelo(df_tabla, f"Avances por Área - {titulo_modelo.split('- ')[1]} (2024 → 2025)"),
                width="stretch"
            )
            st.markdown("---")

        st.markdown("#### 🔄 Comparación de Avances entre Modelos")
        col1, col2 = st.columns(2)

        for col, modelo_key, titulo_col in [
            (col1, 'Aula Regular (Jornada 1)', "📘 Top 3 Áreas - Aula Regular (Jornada 1)"),
            (col2, 'Modelo Flexible (Jornada 0)', "📙 Top 3 Áreas - Modelo Flexible (Jornada 0)"),
        ]:
            stats_modelo = stats_regular_2025 if 'Regular' in modelo_key else stats_flexible_2025
            with col:
                st.markdown(f"**{titulo_col}**")
                avances_col = sorted(
                    [(a, calcular_avance(datos_2024[modelo_key]['areas'][a]['promedio'],
                                        stats_modelo['areas'][a]['promedio']))
                     for a in AREAS],
                    key=lambda x: x[1], reverse=True
                )
                for area, avance in avances_col[:3]:
                    if avance > 0:
                        st.success(f"✅ {area}: +{avance} puntos")
                    elif avance < 0:
                        st.error(f"❌ {area}: {avance} puntos")
                    else:
                        st.info(f"⚪ {area}: Sin cambio")

    # ── TAB 3: AVANCES POR ÁREAS DE CONOCIMIENTO ────────────────────────────
    with tab3:
        st.markdown('<div class="subtitle">📊 Avances por Áreas de Conocimiento</div>', unsafe_allow_html=True)
        st.info("📌 Esta sección analiza el desempeño por área de conocimiento en diferentes niveles")

        st.markdown("#### 🏫 Avances por Área - Nivel Institucional")
        tabla_areas_inst = []
        for area in AREAS:
            puntaje_2024 = datos_2024['Institucional']['areas'][area]['promedio']
            puntaje_2025 = stats_institucional_2025['areas'][area]['promedio']
            avance = calcular_avance(puntaje_2024, puntaje_2025)
            texto_avance, _ = formatear_avance(avance)
            tabla_areas_inst.append({'Área': area, '2024': puntaje_2024, '2025': puntaje_2025,
                                     'Avance': avance, 'Estado': texto_avance})

        df_areas_inst = pd.DataFrame(tabla_areas_inst)
        st.dataframe(df_areas_inst, width="stretch", hide_index=True)
        st.plotly_chart(
            crear_grafico_avances_modelo(df_areas_inst, "Avances por Área - Nivel Institucional (2024 → 2025)"),
            width="stretch"
        )

        st.markdown("---")
        st.markdown("#### 🔄 Avances por Área - Comparación entre Modelos")

        datos_comparacion_modelos = []
        for area in AREAS:
            avance_regular = calcular_avance(
                datos_2024['Aula Regular (Jornada 1)']['areas'][area]['promedio'],
                stats_regular_2025['areas'][area]['promedio']
            )
            avance_flexible = calcular_avance(
                datos_2024['Modelo Flexible (Jornada 0)']['areas'][area]['promedio'],
                stats_flexible_2025['areas'][area]['promedio']
            )
            datos_comparacion_modelos.append({'Área': area, 'Modelo': 'Aula Regular', 'Avance': avance_regular})
            datos_comparacion_modelos.append({'Área': area, 'Modelo': 'Modelo Flexible', 'Avance': avance_flexible})

        df_comp_modelos = pd.DataFrame(datos_comparacion_modelos)
        st.plotly_chart(crear_grafico_comparacion_modelos_areas(df_comp_modelos), width="stretch")

        tabla_comp_modelos = []
        for area in AREAS:
            avance_regular = calcular_avance(
                datos_2024['Aula Regular (Jornada 1)']['areas'][area]['promedio'],
                stats_regular_2025['areas'][area]['promedio']
            )
            avance_flexible = calcular_avance(
                datos_2024['Modelo Flexible (Jornada 0)']['areas'][area]['promedio'],
                stats_flexible_2025['areas'][area]['promedio']
            )
            tabla_comp_modelos.append({
                'Área': area,
                'Avance Aula Regular (Jornada 1)': avance_regular,
                'Avance Modelo Flexible (Jornada 0)': avance_flexible,
                'Diferencia': avance_regular - avance_flexible
            })

        st.dataframe(pd.DataFrame(tabla_comp_modelos), width="stretch", hide_index=True)
        st.markdown("---")
        st.info("💡 Para ver la comparación detallada de puntajes por área entre grupos, consulta la pestaña '👥 Resultados por Grupos'")

    # ── TAB 4: RESULTADOS POR GRUPOS ─────────────────────────────────────────
    with tab4:
        st.markdown('<div class="subtitle">👥 Resultados por Grupos - Año 2025</div>', unsafe_allow_html=True)
        st.warning("⚠️ Los datos de 2024 no están disponibles por grupos individuales, solo por modelo educativo.")

        st.markdown("#### 📋 Tabla Comparativa de Todos los Grupos")

        tabla_grupos = []
        for grupo in sorted(stats_grupos_2025.keys()):
            stats = stats_grupos_2025[grupo]
            tabla_grupos.append({
                'Grupo': grupo,
                'Modelo': stats['modelo'],
                'Estudiantes': stats['estudiantes'],
                'Puntaje Global': stats['puntaje_global'],
                **{area: stats['areas'][area]['promedio'] for area in AREAS}
            })

        df_grupos = pd.DataFrame(tabla_grupos)
        st.dataframe(df_grupos, width="stretch", hide_index=True)
        st.plotly_chart(crear_grafico_grupos(df_grupos), width="stretch")

        st.markdown("---")
        st.markdown("#### 🔄 Comparación entre Grupos del Mismo Modelo")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**📘 Grupos de Aula Regular (Jornada 1) (11A vs 11B)**")
            datos_regular = []
            for grupo in ['11A', '11B']:
                if grupo in stats_grupos_2025:
                    for area in AREAS:
                        datos_regular.append({'Grupo': grupo, 'Área': area,
                                              'Puntaje': stats_grupos_2025[grupo]['areas'][area]['promedio']})

            fig_regular = px.bar(pd.DataFrame(datos_regular), x='Área', y='Puntaje', color='Grupo',
                                 barmode='group', title="Comparación por Áreas - Aula Regular",
                                 color_discrete_sequence=['#667eea', '#4c5fd5'])
            fig_regular.update_xaxes(tickangle=-45)
            fig_regular.update_layout(height=400)
            st.plotly_chart(fig_regular, width="stretch")

            if '11A' in stats_grupos_2025 and '11B' in stats_grupos_2025:
                diff = stats_grupos_2025['11A']['puntaje_global'] - stats_grupos_2025['11B']['puntaje_global']
                if diff > 0:
                    st.success(f"📊 11A supera a 11B por {diff} puntos en puntaje global")
                elif diff < 0:
                    st.success(f"📊 11B supera a 11A por {abs(diff)} puntos en puntaje global")
                else:
                    st.info("📊 11A y 11B tienen el mismo puntaje global")

        with col2:
            st.markdown("**📙 Grupos de Modelo Flexible (Jornada 0) (P3A vs P3B vs P3C)**")
            datos_flexible = []
            for grupo in ['P3A', 'P3B', 'P3C']:
                if grupo in stats_grupos_2025:
                    for area in AREAS:
                        datos_flexible.append({'Grupo': grupo, 'Área': area,
                                               'Puntaje': stats_grupos_2025[grupo]['areas'][area]['promedio']})

            fig_flexible = px.bar(pd.DataFrame(datos_flexible), x='Área', y='Puntaje', color='Grupo',
                                  barmode='group', title="Comparación por Áreas - Modelo Flexible",
                                  color_discrete_sequence=['#764ba2', '#9b59b6', '#8e44ad'])
            fig_flexible.update_xaxes(tickangle=-45)
            fig_flexible.update_layout(height=400)
            st.plotly_chart(fig_flexible, width="stretch")

            grupos_flex_ordenados = sorted(
                [(g, stats_grupos_2025[g]['puntaje_global']) for g in ['P3A', 'P3B', 'P3C']
                 if g in stats_grupos_2025],
                key=lambda x: x[1], reverse=True
            )
            if grupos_flex_ordenados:
                mejor_grupo, mejor_puntaje = grupos_flex_ordenados[0]
                st.success(f"🏆 {mejor_grupo} es el mejor grupo de Modelo Flexible con {mejor_puntaje} puntos")

        st.markdown("---")
        st.markdown("#### 🌐 Comparación Global de Todos los Grupos")

        datos_areas_grupos = [
            {'Grupo': grupo, 'Área': area,
             'Puntaje': stats_grupos_2025[grupo]['areas'][area]['promedio'],
             'Modelo': stats_grupos_2025[grupo]['modelo']}
            for grupo in sorted(stats_grupos_2025.keys())
            for area in AREAS
        ]

        st.plotly_chart(crear_grafico_lineas_grupos(pd.DataFrame(datos_areas_grupos)), width="stretch")

        st.markdown("#### 🏆 Ranking de Grupos por Puntaje Global")
        df_ranking = df_grupos[['Grupo', 'Modelo', 'Estudiantes', 'Puntaje Global']].sort_values('Puntaje Global', ascending=False)
        df_ranking.insert(0, 'Posición', range(1, len(df_ranking) + 1))
        st.dataframe(df_ranking, width="stretch", hide_index=True)

    # ── TAB 5: NIVELES DE DESEMPEÑO ──────────────────────────────────────────
    with tab5:
        st.markdown('<div class="subtitle">🎯 Niveles de Desempeño por Área - Año 2025</div>', unsafe_allow_html=True)
        st.info("📌 Esta sección clasifica a los estudiantes en 4 niveles según estándares ICFES: Insuficiente, Mínimo, Satisfactorio y Avanzado")

        mostrar_resumen_niveles_todas_areas(datos_2025_raw['df_todos'])

        st.markdown("### 📚 Análisis Detallado por Área de Conocimiento")
        area_seleccionada = st.selectbox("Seleccione un área:", AREAS, key="selector_area_niveles")

        mostrar_niveles_desempeno_area(datos_2025_raw['df_todos'], area_seleccionada,
                                      "Distribución Detallada por Niveles")

        st.markdown("### 🏫 Comparación de Niveles por Modelo Educativo")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### 📘 Aula Regular (Jornada 1)")
            mostrar_niveles_desempeno_area(datos_2025_raw['df_regular'], area_seleccionada,
                                          "Niveles - Aula Regular")

        with col2:
            st.markdown("#### 📙 Modelo Flexible (Jornada 0)")
            mostrar_niveles_desempeno_area(datos_2025_raw['df_flexible'], area_seleccionada,
                                          "Niveles - Modelo Flexible")


# ============================================================================
# PÁGINA: ESTADÍSTICAS POR ESTUDIANTE
# ============================================================================

def mostrar_estadisticas_estudiante(datos_2025_raw):
    """Página de estadísticas por estudiante individual"""

    st.markdown('<div class="subtitle">👨‍🎓 Estadísticas por Estudiante</div>', unsafe_allow_html=True)
    st.warning("⚠️ Nota: Los datos a nivel de estudiante provienen de fuentes auxiliares (Excel) y no están disponibles en el reporte oficial agregado del ICFES.")

    df_todos = datos_2025_raw['df_todos']
    df_todos['Nombre Completo'] = (
        df_todos['Primer Nombre'].fillna('') + ' ' +
        df_todos['Segundo Nombre'].fillna('') + ' ' +
        df_todos['Primer Apellido'].fillna('') + ' ' +
        df_todos['Segundo Apellido'].fillna('')
    ).str.strip().str.replace(r'\s+', ' ', regex=True)

    estudiante_seleccionado = st.selectbox("Seleccione un estudiante:",
                                           df_todos['Nombre Completo'].sort_values().unique())
    estudiante_data = df_todos[df_todos['Nombre Completo'] == estudiante_seleccionado].iloc[0]

    col1, col2 = st.columns(2)
    with col1:
        st.info(f"**Grupo:** {estudiante_data['Grupo']}")
        st.info(f"**Modelo:** {estudiante_data['Modelo']}")
    with col2:
        st.metric("Puntaje Global", int(estudiante_data['Puntaje Global']))

    st.markdown("#### 📚 Puntajes por Área")
    df_areas_estudiante = pd.DataFrame([{'Área': a, 'Puntaje': int(estudiante_data[a])} for a in AREAS])

    col1, col2 = st.columns([1, 2])
    with col1:
        st.dataframe(df_areas_estudiante, width="stretch", hide_index=True)
    with col2:
        fig = px.bar(df_areas_estudiante, x='Área', y='Puntaje', color='Puntaje',
                     color_continuous_scale='Viridis', title=f"Puntajes de {estudiante_seleccionado}")
        st.plotly_chart(fig, width="stretch")


# ============================================================================
# PÁGINA: ESTADÍSTICAS POR GRADO
# ============================================================================

def mostrar_estadisticas_grado(datos_2025_raw):
    """Página de estadísticas por grado"""

    st.markdown('<div class="subtitle">🎓 Estadísticas por Grado</div>', unsafe_allow_html=True)

    df_todos = datos_2025_raw['df_todos']
    grado_seleccionado = st.selectbox("Seleccione un grado:", sorted(df_todos['Grupo'].unique()))
    df_grado = df_todos[df_todos['Grupo'] == grado_seleccionado]

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Estudiantes", len(df_grado))
    with col2:
        st.metric("Puntaje Global Promedio", int(round(df_grado['Puntaje Global'].mean())))
    with col3:
        st.metric("Puntaje Máximo", int(df_grado['Puntaje Global'].max()))
    with col4:
        st.metric("Puntaje Mínimo", int(df_grado['Puntaje Global'].min()))

    st.markdown("#### 📚 Promedios por Área")
    df_promedios = pd.DataFrame([{'Área': a, 'Promedio': int(round(df_grado[a].mean())),
                                   'Desv. Estándar': round(df_grado[a].std(), 2)} for a in AREAS])

    col1, col2 = st.columns([1, 2])
    with col1:
        st.dataframe(df_promedios, width="stretch", hide_index=True)
    with col2:
        fig = px.bar(df_promedios, x='Área', y='Promedio', color='Promedio',
                     color_continuous_scale='Blues', title=f"Promedios por Área - {grado_seleccionado}")
        st.plotly_chart(fig, width="stretch")

    st.markdown("#### 👥 Estudiantes del Grado")
    df_grado_display = df_grado[['Primer Nombre', 'Primer Apellido', 'Puntaje Global'] + AREAS].copy()
    st.dataframe(df_grado_display.sort_values('Puntaje Global', ascending=False), width="stretch", hide_index=True)


# ============================================================================
# PÁGINA: ESTADÍSTICAS POR ÁREA
# ============================================================================

def mostrar_estadisticas_area(datos_2024, datos_2025_raw, stats_institucional_2025):
    """Página de estadísticas por área de conocimiento"""

    st.markdown('<div class="subtitle">📚 Estadísticas por Área de Conocimiento</div>', unsafe_allow_html=True)

    area_seleccionada = st.selectbox("Seleccione un área:", AREAS)

    st.markdown(f"#### 📊 Comparativo {area_seleccionada} - 2024 vs 2025")
    col1, col2, col3 = st.columns(3)

    with col1:
        puntaje_2024 = datos_2024['Institucional']['areas'][area_seleccionada]['promedio']
        st.metric("Promedio 2024", puntaje_2024)
    with col2:
        puntaje_2025 = stats_institucional_2025['areas'][area_seleccionada]['promedio']
        st.metric("Promedio 2025", puntaje_2025)
    with col3:
        avance = calcular_avance(puntaje_2024, puntaje_2025)
        texto_avance, clase_avance = formatear_avance(avance)
        st.markdown(f'<div class="{clase_avance}">{texto_avance}</div>', unsafe_allow_html=True)

    st.markdown(f"#### 📈 Distribución de Puntajes - {area_seleccionada} (2025)")
    fig = px.histogram(datos_2025_raw['df_todos'], x=area_seleccionada, nbins=20, color='Modelo',
                       title=f"Distribución de Puntajes - {area_seleccionada}",
                       labels={area_seleccionada: 'Puntaje'},
                       color_discrete_map={'Aula Regular (Jornada 1)': '#667eea',
                                           'Modelo Flexible (Jornada 0)': '#764ba2'})
    st.plotly_chart(fig, width="stretch")

    st.markdown(f"#### 🏫 Comparativo por Modelo Educativo - {area_seleccionada}")
    col1, col2 = st.columns(2)

    for col, df_modelo, label in [
        (col1, datos_2025_raw['df_regular'], "📘 Aula Regular"),
        (col2, datos_2025_raw['df_flexible'], "📙 Modelo Flexible"),
    ]:
        with col:
            st.markdown(f"**{label}**")
            st.metric("Promedio", int(round(df_modelo[area_seleccionada].mean())))
            st.metric("Desviación Estándar", round(df_modelo[area_seleccionada].std(), 2))
            st.metric("Máximo", int(df_modelo[area_seleccionada].max()))
            st.metric("Mínimo", int(df_modelo[area_seleccionada].min()))


# ============================================================================
# PÁGINA: ESTADÍSTICAS POR MODELO
# ============================================================================

def mostrar_estadisticas_modelo(datos_2024, stats_regular_2025, stats_flexible_2025):
    """Página de estadísticas por modelo educativo"""

    st.markdown('<div class="subtitle">🏫 Estadísticas por Modelo Educativo</div>', unsafe_allow_html=True)

    modelo_seleccionado = st.radio("Seleccione un modelo:",
                                   ["Aula Regular (Jornada 1)", "Modelo Flexible (Jornada 0)"],
                                   horizontal=True)

    if modelo_seleccionado == "Aula Regular (Jornada 1)":
        datos_2024_modelo = datos_2024['Aula Regular (Jornada 1)']
        datos_2025_modelo = stats_regular_2025
    else:
        datos_2024_modelo = datos_2024['Modelo Flexible (Jornada 0)']
        datos_2025_modelo = stats_flexible_2025

    st.markdown(f"#### 📊 Métricas Generales - {modelo_seleccionado}")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Estudiantes 2024", datos_2024_modelo['estudiantes'])
    with col2:
        st.metric("Estudiantes 2025", datos_2025_modelo['estudiantes'])
    with col3:
        st.metric("Puntaje Global 2024", datos_2024_modelo['puntaje_global'])
    with col4:
        st.metric("Puntaje Global 2025", datos_2025_modelo['puntaje_global'])

    avance_global = calcular_avance(datos_2024_modelo['puntaje_global'], datos_2025_modelo['puntaje_global'])
    texto_avance, clase_avance = formatear_avance(avance_global)
    st.markdown(f'<div class="{clase_avance}">{texto_avance}</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown(f"#### 📚 Comparativo por Áreas - {modelo_seleccionado}")

    tabla_areas = []
    for area in AREAS:
        puntaje_2024 = datos_2024_modelo['areas'][area]['promedio']
        puntaje_2025 = datos_2025_modelo['areas'][area]['promedio']
        avance = calcular_avance(puntaje_2024, puntaje_2025)
        texto_avance, _ = formatear_avance(avance)
        tabla_areas.append({'Área': area, '2024': puntaje_2024, '2025': puntaje_2025, 'Avance': texto_avance})

    st.dataframe(pd.DataFrame(tabla_areas), width="stretch", hide_index=True)

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(
            crear_grafico_comparativo_areas(datos_2024_modelo, datos_2025_modelo,
                                            f"Comparativo por Áreas - {modelo_seleccionado}"),
            width="stretch"
        )
    with col2:
        st.plotly_chart(crear_grafico_avances(datos_2024_modelo, datos_2025_modelo), width="stretch")


# ============================================================================
# PÁGINA: RANKINGS
# ============================================================================

def mostrar_rankings(datos_2025_raw):
    """Página de rankings y estudiantes destacados"""

    st.markdown('<div class="subtitle">🏆 Rankings y Estudiantes Destacados</div>', unsafe_allow_html=True)

    df_todos = datos_2025_raw['df_todos']
    df_todos['Nombre Completo'] = (
        df_todos['Primer Nombre'].fillna('') + ' ' +
        df_todos['Segundo Nombre'].fillna('') + ' ' +
        df_todos['Primer Apellido'].fillna('') + ' ' +
        df_todos['Segundo Apellido'].fillna('')
    ).str.strip().str.replace(r'\s+', ' ', regex=True)

    st.markdown("#### 🥇 Top 10 - Puntaje Global")
    df_top10 = df_todos.nlargest(10, 'Puntaje Global')[
        ['Nombre Completo', 'Grupo', 'Modelo', 'Puntaje Global'] + AREAS
    ].copy()
    df_top10.insert(0, 'Posición', range(1, len(df_top10) + 1))
    st.dataframe(df_top10, width="stretch", hide_index=True)

    fig = px.bar(df_top10, x='Nombre Completo', y='Puntaje Global', color='Modelo',
                 title="Top 10 Estudiantes - Puntaje Global",
                 color_discrete_map={'Aula Regular (Jornada 1)': '#667eea',
                                     'Modelo Flexible (Jornada 0)': '#764ba2'})
    fig.update_xaxes(tickangle=-45)
    st.plotly_chart(fig, width="stretch")

    st.markdown("---")
    st.markdown("#### 🌟 Mejores Estudiantes por Área")

    tabs = st.tabs(AREAS)
    for i, area in enumerate(AREAS):
        with tabs[i]:
            df_top_area = df_todos.nlargest(5, area)[
                ['Nombre Completo', 'Grupo', 'Modelo', area, 'Puntaje Global']
            ].copy()
            df_top_area.insert(0, 'Posición', range(1, len(df_top_area) + 1))
            st.dataframe(df_top_area, width="stretch", hide_index=True)

    st.markdown("---")
    st.markdown("#### 🏫 Rankings por Modelo Educativo")
    col1, col2 = st.columns(2)

    for col, df_modelo, label in [
        (col1, datos_2025_raw['df_regular'], "📘 Top 5 - Aula Regular"),
        (col2, datos_2025_raw['df_flexible'], "📙 Top 5 - Modelo Flexible"),
    ]:
        with col:
            st.markdown(f"**{label}**")
            df_modelo = df_modelo.copy()
            df_modelo['Nombre Completo'] = (
                df_modelo['Primer Nombre'].fillna('') + ' ' +
                df_modelo['Segundo Nombre'].fillna('') + ' ' +
                df_modelo['Primer Apellido'].fillna('') + ' ' +
                df_modelo['Segundo Apellido'].fillna('')
            ).str.strip().str.replace(r'\s+', ' ', regex=True)

            df_top = df_modelo.nlargest(5, 'Puntaje Global')[
                ['Nombre Completo', 'Grupo', 'Puntaje Global']
            ].copy()
            df_top.insert(0, 'Posición', range(1, len(df_top) + 1))
            st.dataframe(df_top, width="stretch", hide_index=True)

    st.markdown("---")
    st.markdown("#### 🎓 Rankings por Grado")

    grado_seleccionado = st.selectbox("Seleccione un grado:", sorted(df_todos['Grupo'].unique()),
                                      key='ranking_grado')
    df_grado = df_todos[df_todos['Grupo'] == grado_seleccionado].copy()
    df_grado_ranking = df_grado.nlargest(10, 'Puntaje Global')[
        ['Nombre Completo', 'Modelo', 'Puntaje Global'] + AREAS
    ].copy()
    df_grado_ranking.insert(0, 'Posición', range(1, len(df_grado_ranking) + 1))
    st.dataframe(df_grado_ranking, width="stretch", hide_index=True)


# ============================================================================
# PÁGINA: DESCARGAR DATOS
# ============================================================================

def mostrar_descarga_datos(datos_2025_raw):
    """Página para descargar datos en diferentes formatos"""

    st.markdown('<div class="subtitle">📥 Descargar Datos</div>', unsafe_allow_html=True)
    st.info("Descargue los datos en formato CSV o Excel para análisis adicionales.")

    df_todos = datos_2025_raw['df_todos']
    df_regular = datos_2025_raw['df_regular']
    df_flexible = datos_2025_raw['df_flexible']

    for df in [df_todos, df_regular, df_flexible]:
        df['Nombre Completo'] = (
            df['Primer Nombre'].fillna('') + ' ' +
            df['Segundo Nombre'].fillna('') + ' ' +
            df['Primer Apellido'].fillna('') + ' ' +
            df['Segundo Apellido'].fillna('')
        ).str.strip().str.replace(r'\s+', ' ', regex=True)

    conjunto_datos = st.radio(
        "Seleccione el conjunto de datos a descargar:",
        ["Todos los estudiantes", "Aula Regular (Jornada 1)", "Modelo Flexible (Jornada 0)"],
        horizontal=True
    )

    if conjunto_datos == "Todos los estudiantes":
        df_descarga = df_todos.copy()
        nombre_archivo = "resultados_icfes_2025_todos"
    elif conjunto_datos == "Aula Regular (Jornada 1)":
        df_descarga = df_regular.copy()
        nombre_archivo = "resultados_icfes_2025_aula_regular"
    else:
        df_descarga = df_flexible.copy()
        nombre_archivo = "resultados_icfes_2025_modelo_flexible"

    columnas_a_eliminar = ['Número de documento', 'Tipo documento']
    df_descarga = df_descarga.drop(columns=[c for c in columnas_a_eliminar if c in df_descarga.columns])

    st.markdown("#### 👀 Vista Previa de los Datos")
    st.dataframe(df_descarga.head(10), width="stretch")
    st.markdown(f"**Total de registros:** {len(df_descarga)}")

    st.markdown("#### 💾 Descargar")
    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            label="📄 Descargar CSV",
            data=df_descarga.to_csv(index=False, encoding='utf-8-sig'),
            file_name=f"{nombre_archivo}.csv",
            mime="text/csv",
            width="stretch"
        )

    with col2:
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df_descarga.to_excel(writer, index=False, sheet_name='Resultados')
        buffer.seek(0)
        st.download_button(
            label="📊 Descargar Excel",
            data=buffer,
            file_name=f"{nombre_archivo}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            width="stretch"
        )

    st.markdown("---")
    st.markdown("#### 📊 Estadísticas Resumidas")

    estadisticas_resumen = {
        'Métrica': [
            'Total Estudiantes', 'Puntaje Global Promedio', 'Puntaje Global Máximo',
            'Puntaje Global Mínimo', 'Desviación Estándar Global'
        ] + [f'Promedio {area}' for area in AREAS],
        'Valor': [
            len(df_descarga),
            int(round(df_descarga['Puntaje Global'].mean())),
            int(df_descarga['Puntaje Global'].max()),
            int(df_descarga['Puntaje Global'].min()),
            round(df_descarga['Puntaje Global'].std(), 2),
        ] + [int(round(df_descarga[area].mean())) for area in AREAS]
    }

    df_estadisticas = pd.DataFrame(estadisticas_resumen)
    st.dataframe(df_estadisticas, width="stretch", hide_index=True)

    st.download_button(
        label="📄 Descargar Estadísticas (CSV)",
        data=df_estadisticas.to_csv(index=False, encoding='utf-8-sig'),
        file_name=f"{nombre_archivo}_estadisticas.csv",
        mime="text/csv"
    )
