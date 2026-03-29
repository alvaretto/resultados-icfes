"""
Lógica de comparación 2024 vs 2025 y análisis institucional/municipal.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from .data_loader import AREAS, DATOS_INSTITUCIONES_TEBAIDA, PROMEDIOS_REFERENCIA
from .estadisticas import calcular_avance, formatear_avance, calcular_distribucion_niveles, obtener_interpretacion_nivel
from .visualizaciones import (
    crear_grafico_ranking_municipal,
    crear_grafico_avances_municipio,
    crear_grafico_posicion_relativa,
    NIVELES_ORDEN,
)


# ============================================================================
# FICHA TÉCNICA
# ============================================================================

def mostrar_ficha_tecnica(datos_2024, stats_2025, datos_2025_raw):
    """
    Muestra la Ficha Técnica según estándares ICFES.
    Incluye: matriculados, inscritos, presentes, con resultados publicados, tasa de participación.
    """
    st.markdown("### 📋 Ficha Técnica")
    st.markdown("*Información sobre la participación de estudiantes en el examen Saber 11°*")

    matriculados_2024 = datos_2024['Institucional']['estudiantes']
    presentes_2024 = datos_2024['Institucional']['estudiantes']
    tasa_2024 = 100.0

    matriculados_2025 = 120
    presentes_2025 = len(datos_2025_raw['df_todos'])
    tasa_2025 = (presentes_2025 / matriculados_2025) * 100

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="📚 Matriculados 2024", value=matriculados_2024,
                  help="Estudiantes registrados en el SIMAT")
        st.metric(label="📚 Matriculados 2025", value=matriculados_2025,
                  delta=matriculados_2025 - matriculados_2024,
                  help="Estudiantes registrados en el SIMAT")

    with col2:
        st.metric(label="✅ Presentes 2024", value=presentes_2024,
                  help="Estudiantes que asistieron a las dos sesiones del examen")
        st.metric(label="✅ Presentes 2025", value=presentes_2025,
                  delta=presentes_2025 - presentes_2024,
                  help="Estudiantes que asistieron a las dos sesiones del examen")

    with col3:
        st.metric(label="📊 Con Resultados 2024", value=presentes_2024,
                  help="Evaluados que obtuvieron resultados publicados")
        st.metric(label="📊 Con Resultados 2025", value=presentes_2025,
                  delta=presentes_2025 - presentes_2024,
                  help="Evaluados que obtuvieron resultados publicados")

    with col4:
        st.metric(label="📈 Tasa Participación 2024", value=f"{tasa_2024:.1f}%",
                  help="Porcentaje de estudiantes matriculados que presentaron el examen")
        st.metric(label="📈 Tasa Participación 2025", value=f"{tasa_2025:.1f}%",
                  delta=f"{tasa_2025 - tasa_2024:.1f}%",
                  help="Porcentaje de estudiantes matriculados que presentaron el examen")

    st.markdown("#### 📊 Participación por Modelo Educativo")

    regular_2024 = datos_2024['Aula Regular (Jornada 1)']['estudiantes']
    flexible_2024 = datos_2024['Modelo Flexible (Jornada 0)']['estudiantes']
    regular_2025 = len(datos_2025_raw['df_regular'])
    flexible_2025 = len(datos_2025_raw['df_flexible'])

    df_participacion = pd.DataFrame({
        'Modelo Educativo': ['Aula Regular (Jornada 1)', 'Modelo Flexible (Jornada 0)', 'Total Institucional'],
        'Estudiantes 2024': [regular_2024, flexible_2024, matriculados_2024],
        'Estudiantes 2025': [regular_2025, flexible_2025, presentes_2025],
        'Variación': [
            regular_2025 - regular_2024,
            flexible_2025 - flexible_2024,
            presentes_2025 - presentes_2024
        ]
    })
    st.dataframe(df_participacion, width="stretch", hide_index=True)

    if tasa_2025 >= 95:
        st.success("✅ **Excelente tasa de participación:** La institución mantiene una alta asistencia al examen Saber 11°")
    elif tasa_2025 >= 85:
        st.info("ℹ️ **Buena tasa de participación:** La mayoría de estudiantes matriculados presentaron el examen")
    else:
        st.warning("⚠️ **Tasa de participación mejorable:** Se recomienda implementar estrategias para aumentar la asistencia al examen")

    st.markdown("---")


# ============================================================================
# ANÁLISIS DE DISPERSIÓN
# ============================================================================

def mostrar_analisis_dispersion(datos_2024, stats_2025, titulo="Análisis de Dispersión"):
    """
    Muestra el análisis de desviación estándar según estándares ICFES.
    Incluye interpretación pedagógica de homogeneidad vs heterogeneidad.
    """
    from .visualizaciones import crear_grafico_dispersion

    st.markdown(f"### 📊 {titulo}")
    st.markdown("*La desviación estándar mide la dispersión de los resultados. Un valor menor indica mayor homogeneidad en el desempeño de los estudiantes.*")

    desv_2024 = datos_2024['desv_global']
    desv_2025 = stats_2025['desv_global']
    diferencia = desv_2025 - desv_2024

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label="📏 Desviación Estándar 2024", value=f"{desv_2024:.1f}",
                  help="Medida de dispersión de los puntajes en 2024")

    with col2:
        st.metric(label="📏 Desviación Estándar 2025", value=f"{desv_2025:.1f}",
                  delta=f"{diferencia:.1f}", delta_color="inverse",
                  help="Medida de dispersión de los puntajes en 2025")

    with col3:
        if abs(diferencia) < 2:
            st.info("• **Dispersión similar**\n\nNo hay cambio significativo en la homogeneidad")
        elif diferencia < 0:
            st.success(f"✅ **Mayor homogeneidad**\n\nLos resultados son {abs(diferencia):.1f} puntos más consistentes")
        else:
            st.warning(f"⚠️ **Mayor heterogeneidad**\n\nLos resultados son {diferencia:.1f} puntos más dispersos")

    st.markdown("#### 📈 Comparación de Dispersión 2024 vs 2025")
    st.plotly_chart(crear_grafico_dispersion(desv_2024, desv_2025), width="stretch")

    st.markdown("#### 📊 Desviación Estándar por Área de Conocimiento")

    areas_data = []
    for area in AREAS:
        desv_area_2024 = datos_2024['areas'][area]['desviacion']
        desv_area_2025 = stats_2025['areas'][area]['desviacion']
        dif_area = desv_area_2025 - desv_area_2024

        if abs(dif_area) < 1:
            estado = "🔵 • Similar"
        elif dif_area < 0:
            estado = "🟢 ▼ Más homogéneo"
        else:
            estado = "🟡 ▲ Más heterogéneo"

        areas_data.append({
            'Área': area,
            'Desv. Est. 2024': f"{desv_area_2024:.1f}",
            'Desv. Est. 2025': f"{desv_area_2025:.1f}",
            'Diferencia': f"{dif_area:+.1f}",
            'Estado': estado
        })

    st.dataframe(pd.DataFrame(areas_data), width="stretch", hide_index=True)

    st.markdown("#### 💡 Interpretación Pedagógica")

    if desv_2025 < desv_2024:
        st.success("""
        **✅ Mejora en la homogeneidad del desempeño:**
        - Los estudiantes muestran resultados más consistentes en 2025
        - Indica que las estrategias pedagógicas están llegando de manera más equitativa a todos los estudiantes
        - Se reduce la brecha entre estudiantes de alto y bajo desempeño
        - **Recomendación:** Mantener y fortalecer las estrategias actuales de enseñanza
        """)
    elif desv_2025 > desv_2024:
        st.warning("""
        **⚠️ Aumento en la heterogeneidad del desempeño:**
        - Los resultados son más dispersos en 2025
        - Puede indicar que algunos estudiantes avanzan más rápido que otros
        - Se amplía la brecha entre estudiantes de alto y bajo desempeño
        - **Recomendación:** Implementar estrategias de nivelación y atención diferenciada
        """)
    else:
        st.info("""
        **ℹ️ Dispersión similar entre 2024 y 2025:**
        - La homogeneidad del desempeño se mantiene estable
        - Los estudiantes continúan con niveles de dispersión similares
        - **Recomendación:** Evaluar si se requieren estrategias para reducir la heterogeneidad
        """)

    st.markdown("---")


# ============================================================================
# NIVELES DE DESEMPEÑO (UI)
# ============================================================================

def mostrar_niveles_desempeno_area(df, area, titulo="Distribución por Niveles de Desempeño"):
    """Muestra la distribución de estudiantes por niveles de desempeño en un área específica"""
    from .visualizaciones import crear_grafico_niveles_area

    st.markdown(f"#### 📊 {titulo} - {area}")

    distribucion, porcentajes, total_estudiantes = calcular_distribucion_niveles(df, area)

    st.plotly_chart(crear_grafico_niveles_area(distribucion, porcentajes, area), width="stretch")

    col1, col2 = st.columns([2, 1])

    with col1:
        df_niveles = pd.DataFrame({
            'Nivel': NIVELES_ORDEN,
            'Estudiantes': [distribucion[n] for n in NIVELES_ORDEN],
            'Porcentaje': [f"{porcentajes[n]:.1f}%" for n in NIVELES_ORDEN]
        })
        st.dataframe(df_niveles, width="stretch", hide_index=True)

    with col2:
        nivel_predominante = distribucion.idxmax()
        info_nivel = obtener_interpretacion_nivel(nivel_predominante)
        st.metric(
            label="Nivel Predominante",
            value=f"{info_nivel['emoji']} {nivel_predominante}",
            help=f"{distribucion[nivel_predominante]} estudiantes ({porcentajes[nivel_predominante]:.1f}%)"
        )

    with st.expander(f"💡 Interpretación Pedagógica - {area}"):
        for nivel in NIVELES_ORDEN:
            if distribucion[nivel] > 0:
                info = obtener_interpretacion_nivel(nivel)
                st.markdown(f"""
                **{info['emoji']} {nivel}** ({distribucion[nivel]} estudiantes - {porcentajes[nivel]:.1f}%)
                - *Descripción:* {info['descripcion']}
                - *Recomendación:* {info['recomendacion']}
                """)

    st.markdown("---")


def mostrar_resumen_niveles_todas_areas(df):
    """Muestra un resumen comparativo de niveles de desempeño para todas las áreas"""
    from .visualizaciones import crear_grafico_niveles_todas_areas

    st.markdown("### 📊 Resumen de Niveles de Desempeño por Área")
    st.markdown("*Distribución de estudiantes en cada nivel de desempeño para todas las áreas evaluadas*")

    datos_resumen = []
    for area in AREAS:
        distribucion, porcentajes, total = calcular_distribucion_niveles(df, area)
        datos_resumen.append({
            'Área': area,
            'Insuficiente': f"{distribucion['Insuficiente']} ({porcentajes['Insuficiente']:.1f}%)",
            'Mínimo': f"{distribucion['Mínimo']} ({porcentajes['Mínimo']:.1f}%)",
            'Satisfactorio': f"{distribucion['Satisfactorio']} ({porcentajes['Satisfactorio']:.1f}%)",
            'Avanzado': f"{distribucion['Avanzado']} ({porcentajes['Avanzado']:.1f}%)"
        })

    st.dataframe(pd.DataFrame(datos_resumen), width="stretch", hide_index=True)

    st.markdown("#### 📈 Comparación Visual de Niveles por Área")
    st.plotly_chart(crear_grafico_niveles_todas_areas(df), width="stretch")

    st.markdown("#### 💪 Fortalezas y Áreas de Mejora por Niveles de Desempeño")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**🟢 Áreas con Mayor Porcentaje en Niveles Satisfactorio/Avanzado:**")
        fortalezas = []
        for area in AREAS:
            distribucion, porcentajes, total = calcular_distribucion_niveles(df, area)
            porcentaje_alto = (distribucion.get('Satisfactorio', 0) + distribucion.get('Avanzado', 0)) / total * 100
            fortalezas.append((area, porcentaje_alto))
        fortalezas.sort(key=lambda x: x[1], reverse=True)
        for i, (area, porcentaje) in enumerate(fortalezas[:3], 1):
            st.success(f"{i}. **{area}**: {porcentaje:.1f}% en niveles altos")

    with col2:
        st.markdown("**🔴 Áreas con Mayor Porcentaje en Niveles Insuficiente/Mínimo:**")
        debilidades = []
        for area in AREAS:
            distribucion, porcentajes, total = calcular_distribucion_niveles(df, area)
            porcentaje_bajo = (distribucion.get('Insuficiente', 0) + distribucion.get('Mínimo', 0)) / total * 100
            debilidades.append((area, porcentaje_bajo))
        debilidades.sort(key=lambda x: x[1], reverse=True)
        for i, (area, porcentaje) in enumerate(debilidades[:3], 1):
            st.warning(f"{i}. **{area}**: {porcentaje:.1f}% en niveles bajos")

    st.markdown("---")


# ============================================================================
# COMPARATIVO MUNICIPAL
# ============================================================================

def mostrar_verificacion_datos(datos_2024, stats_regular_2025, stats_flexible_2025):
    """Página para comparar instituciones educativas de La Tebaida"""

    st.markdown('<div class="subtitle">🏫 Comparativo Instituciones Educativas - La Tebaida</div>', unsafe_allow_html=True)

    st.info("""
    📌 **Fuente:** Análisis de Resultados SABER 11 del Municipio de La Tebaida 2024-2025

    Esta sección permite comparar el desempeño de **Pedacito de Cielo** con las demás
    instituciones educativas del municipio.
    """)

    tab1, tab2, tab3, tab4 = st.tabs([
        "📊 Ranking General",
        "📈 Evolución 2024-2025",
        "🎯 Posición de Pedacito de Cielo",
        "📉 Análisis Detallado"
    ])

    with tab1:
        st.markdown("### 🏆 Ranking de Instituciones Educativas - La Tebaida")

        col_año = st.columns(2)

        with col_año[0]:
            st.markdown("#### 📅 Ranking 2024")
            df_2024 = pd.DataFrame([
                {'Institución': k, 'Puntaje Global': v['2024']}
                for k, v in DATOS_INSTITUCIONES_TEBAIDA.items()
            ]).sort_values('Puntaje Global', ascending=False).reset_index(drop=True)
            df_2024['Posición'] = range(1, len(df_2024) + 1)
            st.dataframe(df_2024[['Posición', 'Institución', 'Puntaje Global']], width="stretch", hide_index=True)

        with col_año[1]:
            st.markdown("#### 📅 Ranking 2025")
            df_2025 = pd.DataFrame([
                {'Institución': k, 'Puntaje Global': v['2025']}
                for k, v in DATOS_INSTITUCIONES_TEBAIDA.items()
            ]).sort_values('Puntaje Global', ascending=False).reset_index(drop=True)
            df_2025['Posición'] = range(1, len(df_2025) + 1)
            st.dataframe(df_2025[['Posición', 'Institución', 'Puntaje Global']], width="stretch", hide_index=True)

        st.markdown("### 📊 Comparativo Visual 2024 vs 2025")

        instituciones = list(DATOS_INSTITUCIONES_TEBAIDA.keys())
        puntajes_2024 = [DATOS_INSTITUCIONES_TEBAIDA[i]['2024'] for i in instituciones]
        puntajes_2025 = [DATOS_INSTITUCIONES_TEBAIDA[i]['2025'] for i in instituciones]

        fig = crear_grafico_ranking_municipal(
            instituciones, puntajes_2024, puntajes_2025,
            PROMEDIOS_REFERENCIA['PROMEDIO TEBAIDA']['2025'],
            PROMEDIOS_REFERENCIA['PROMEDIO COLOMBIA']['2025']
        )
        st.plotly_chart(fig, width="stretch", key="ranking_general")

    with tab2:
        st.markdown("### 📈 Evolución 2024 → 2025")

        datos_avance = []
        for inst, valores in DATOS_INSTITUCIONES_TEBAIDA.items():
            avance = valores['2025'] - valores['2024']
            datos_avance.append({
                'Institución': inst,
                '2024': valores['2024'],
                '2025': valores['2025'],
                'Avance': avance,
                'Estado': '🟢 Mejoró' if avance > 0 else ('🔴 Bajó' if avance < 0 else '🟡 Igual')
            })

        df_avance = pd.DataFrame(datos_avance).sort_values('Avance', ascending=False)
        st.dataframe(df_avance, width="stretch", hide_index=True)

        st.plotly_chart(crear_grafico_avances_municipio(df_avance), width="stretch", key="evolucion_avance")

    with tab3:
        st.markdown("### 🎯 Posición de I.E. Pedacito de Cielo en el Municipio")

        st.info("""
        📌 **Nota:** Para el ranking municipal se considera a **Pedacito de Cielo** como una sola institución
        (fusionando Aula Regular y Modelo Flexible), resultando en **7 instituciones** en total.
        """)

        INSTITUCIONES_RANKING = {
            'ANTONIO NARIÑO': DATOS_INSTITUCIONES_TEBAIDA['ANTONIO NARIÑO'],
            'LUIS ARANGO CARDONA': DATOS_INSTITUCIONES_TEBAIDA['LUIS ARANGO CARDONA'],
            'GABRIELA MISTRAL': DATOS_INSTITUCIONES_TEBAIDA['GABRIELA MISTRAL'],
            'LA POPA': DATOS_INSTITUCIONES_TEBAIDA['LA POPA'],
            'SANTA TERESITA': DATOS_INSTITUCIONES_TEBAIDA['SANTA TERESITA'],
            'INSTITUTO TEBAIDA': DATOS_INSTITUCIONES_TEBAIDA['INSTITUTO TEBAIDA'],
            'PEDACITO DE CIELO': DATOS_INSTITUCIONES_TEBAIDA['PEDACITO DE CIELO (Institucional)'],
        }

        st.markdown("#### 🏫 Posición Institucional (Consolidada)")

        puntaje_inst_2024 = INSTITUCIONES_RANKING['PEDACITO DE CIELO']['2024']
        puntaje_inst_2025 = INSTITUCIONES_RANKING['PEDACITO DE CIELO']['2025']

        pos_inst_2024 = sum(1 for v in INSTITUCIONES_RANKING.values() if v['2024'] > puntaje_inst_2024) + 1
        pos_inst_2025 = sum(1 for v in INSTITUCIONES_RANKING.values() if v['2025'] > puntaje_inst_2025) + 1

        col_inst = st.columns(3)

        with col_inst[0]:
            st.metric("Puntaje 2024", puntaje_inst_2024, f"Posición {pos_inst_2024}/7")

        with col_inst[1]:
            st.metric("Puntaje 2025", puntaje_inst_2025,
                     f"{puntaje_inst_2025 - puntaje_inst_2024:+d} puntos",
                     delta_color="normal" if puntaje_inst_2025 >= puntaje_inst_2024 else "inverse")

        with col_inst[2]:
            cambio_pos = pos_inst_2024 - pos_inst_2025
            if cambio_pos > 0:
                st.metric("Posición 2025", f"{pos_inst_2025}° de 7", f"+{cambio_pos} posiciones")
            elif cambio_pos < 0:
                st.metric("Posición 2025", f"{pos_inst_2025}° de 7", f"{cambio_pos} posiciones", delta_color="inverse")
            else:
                st.metric("Posición 2025", f"{pos_inst_2025}° de 7", "Sin cambio")

        st.success(f"📍 **Posición actual de Pedacito de Cielo: {pos_inst_2025}° de 7 instituciones**")

        st.markdown("---")
        st.markdown("#### 📊 Desglose por Modelo Educativo (Referencia)")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("##### 🏫 Aula Regular")
            puntaje_regular_2024 = DATOS_INSTITUCIONES_TEBAIDA['PEDACITO DE CIELO (Aula Regular - Jornada 1)']['2024']
            puntaje_regular_2025 = DATOS_INSTITUCIONES_TEBAIDA['PEDACITO DE CIELO (Aula Regular - Jornada 1)']['2025']
            st.metric("Puntaje 2024", puntaje_regular_2024)
            st.metric("Puntaje 2025", puntaje_regular_2025,
                     f"{puntaje_regular_2025 - puntaje_regular_2024:+d} puntos",
                     delta_color="inverse" if puntaje_regular_2025 < puntaje_regular_2024 else "normal")

        with col2:
            st.markdown("##### 🎓 Modelo Flexible (Pensar)")
            puntaje_flex_2024 = DATOS_INSTITUCIONES_TEBAIDA['PEDACITO DE CIELO (Modelo Flexible - Jornada 0)']['2024']
            puntaje_flex_2025 = DATOS_INSTITUCIONES_TEBAIDA['PEDACITO DE CIELO (Modelo Flexible - Jornada 0)']['2025']
            st.metric("Puntaje 2024", puntaje_flex_2024)
            st.metric("Puntaje 2025", puntaje_flex_2025,
                     f"{puntaje_flex_2025 - puntaje_flex_2024:+d} puntos")

        st.markdown("---")
        st.markdown("### 📊 Comparación con Promedios de Referencia")

        col_ref = st.columns(3)

        with col_ref[0]:
            prom_tebaida = PROMEDIOS_REFERENCIA['PROMEDIO TEBAIDA']['2025']
            st.metric("Promedio La Tebaida 2025", prom_tebaida)
            st.caption(f"Pedacito de Cielo: {puntaje_inst_2025 - prom_tebaida:+d} pts")

        with col_ref[1]:
            prom_quindio = PROMEDIOS_REFERENCIA['PROMEDIO QUINDÍO']['2025']
            st.metric("Promedio Quindío 2025", prom_quindio)
            st.caption(f"Pedacito de Cielo: {puntaje_inst_2025 - prom_quindio:+d} pts")

        with col_ref[2]:
            prom_col = PROMEDIOS_REFERENCIA['PROMEDIO COLOMBIA']['2025']
            st.metric("Promedio Colombia 2025", prom_col)
            st.caption(f"Pedacito de Cielo: {puntaje_inst_2025 - prom_col:+d} pts")

    with tab4:
        st.markdown("### 📉 Análisis Detallado")
        st.markdown("#### 📋 Datos Completos de Todas las Instituciones")

        datos_completos = []
        for inst, valores in DATOS_INSTITUCIONES_TEBAIDA.items():
            avance = valores['2025'] - valores['2024']
            datos_completos.append({
                'Institución': inst,
                'Puntaje 2024': valores['2024'],
                'Puntaje 2025': valores['2025'],
                'Avance': f"{avance:+d}",
                'vs Tebaida 2025': f"{valores['2025'] - PROMEDIOS_REFERENCIA['PROMEDIO TEBAIDA']['2025']:+d}",
                'vs Colombia 2025': f"{valores['2025'] - PROMEDIOS_REFERENCIA['PROMEDIO COLOMBIA']['2025']:+d}"
            })

        for prom, valores in PROMEDIOS_REFERENCIA.items():
            avance = valores['2025'] - valores['2024']
            datos_completos.append({
                'Institución': f"📌 {prom}",
                'Puntaje 2024': valores['2024'],
                'Puntaje 2025': valores['2025'],
                'Avance': f"{avance:+d}",
                'vs Tebaida 2025': '-',
                'vs Colombia 2025': '-'
            })

        st.dataframe(pd.DataFrame(datos_completos), width="stretch", hide_index=True)

        st.markdown("#### 🎯 Posición Relativa de Pedacito de Cielo (7 Instituciones)")

        instituciones_7 = [
            'ANTONIO NARIÑO', 'LUIS ARANGO CARDONA', 'GABRIELA MISTRAL',
            'LA POPA', 'SANTA TERESITA', 'INSTITUTO TEBAIDA', 'PEDACITO DE CIELO'
        ]
        puntajes_7 = [
            DATOS_INSTITUCIONES_TEBAIDA['ANTONIO NARIÑO']['2025'],
            DATOS_INSTITUCIONES_TEBAIDA['LUIS ARANGO CARDONA']['2025'],
            DATOS_INSTITUCIONES_TEBAIDA['GABRIELA MISTRAL']['2025'],
            DATOS_INSTITUCIONES_TEBAIDA['LA POPA']['2025'],
            DATOS_INSTITUCIONES_TEBAIDA['SANTA TERESITA']['2025'],
            DATOS_INSTITUCIONES_TEBAIDA['INSTITUTO TEBAIDA']['2025'],
            DATOS_INSTITUCIONES_TEBAIDA['PEDACITO DE CIELO (Institucional)']['2025'],
        ]

        fig_pos = crear_grafico_posicion_relativa(
            instituciones_7, puntajes_7,
            PROMEDIOS_REFERENCIA['PROMEDIO TEBAIDA']['2025'],
            PROMEDIOS_REFERENCIA['PROMEDIO COLOMBIA']['2025']
        )
        st.plotly_chart(fig_pos, width="stretch", key="posicion_relativa")

        st.markdown("---")
        st.markdown("### 📝 Conclusiones del Análisis Municipal")

        puntaje_inst_2024_concl = DATOS_INSTITUCIONES_TEBAIDA['PEDACITO DE CIELO (Institucional)']['2024']
        puntaje_inst_2025_concl = DATOS_INSTITUCIONES_TEBAIDA['PEDACITO DE CIELO (Institucional)']['2025']
        avance_inst = puntaje_inst_2025_concl - puntaje_inst_2024_concl

        if avance_inst > 0:
            st.success(f"""
            ✅ **Pedacito de Cielo (Institucional):** Mejora de {avance_inst} puntos respecto a 2024.
            Posición **7° de 7** instituciones en el municipio.
            """)
        elif avance_inst < 0:
            st.warning(f"""
            ⚠️ **Pedacito de Cielo (Institucional):** Disminución de {abs(avance_inst)} puntos respecto a 2024.
            Se requiere análisis de causas y plan de mejoramiento.
            """)
        else:
            st.info("ℹ️ **Pedacito de Cielo (Institucional):** Puntaje estable respecto a 2024.")
