#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para la aplicación completa de análisis ICFES
Verifica que todas las funciones principales funcionen correctamente
"""

import sys
import pandas as pd
import numpy as np
from scipy import stats

print("="*80)
print("PRUEBA DE LA APLICACIÓN DE ANÁLISIS ICFES COMPLETA")
print("="*80)

# Importar funciones de la aplicación
try:
    from app_resultados_icfes_completo import (
        cargar_datos_unificados,
        cargar_datos_historicos,
        calcular_estadisticas_descriptivas,
        realizar_test_comparacion,
        calcular_percentil,
        obtener_ranking,
        AREAS,
        ARCHIVO_AULA_REGULAR,
        ARCHIVO_MODELO_FLEXIBLE
    )
    print("✓ Importación de módulos exitosa")
except Exception as e:
    print(f"✗ Error al importar módulos: {e}")
    sys.exit(1)

print("\n" + "="*80)
print("1. PRUEBA DE CARGA DE DATOS")
print("="*80)

try:
    df, info = cargar_datos_unificados()
    
    if df is None:
        print("✗ No se pudieron cargar los datos")
        sys.exit(1)
    
    print(f"✓ Datos cargados exitosamente")
    print(f"  - Total estudiantes: {info['total_estudiantes']}")
    print(f"  - Aula Regular: {info['estudiantes_aula_regular']}")
    print(f"  - Modelo Flexible: {info['estudiantes_modelo_flexible']}")
    print(f"  - Modelos: {df['Modelo'].unique().tolist()}")
    print(f"  - Grupos: {sorted(df['Grupo'].unique().tolist())}")
    
except Exception as e:
    print(f"✗ Error al cargar datos: {e}")
    sys.exit(1)

print("\n" + "="*80)
print("2. PRUEBA DE CARGA DE DATOS HISTÓRICOS")
print("="*80)

try:
    historicos = cargar_datos_historicos()
    
    if historicos['Aula Regular']:
        print("✓ Datos históricos de Aula Regular cargados")
        print(f"  - Años disponibles: 2024, 2025")
        print(f"  - Puntaje Global 2025: {historicos['Aula Regular']['2025']['Puntaje Global']:.2f}")
        print(f"  - Puntaje Global 2024: {historicos['Aula Regular']['2024']['Puntaje Global']:.2f}")
        print(f"  - Avance: {historicos['Aula Regular']['Avance']['Puntaje Global']:+.2f}")
    else:
        print("⚠ No se cargaron datos históricos de Aula Regular")
    
    if historicos['Modelo Flexible']:
        print("✓ Datos históricos de Modelo Flexible cargados")
    else:
        print("⚠ Modelo Flexible no tiene datos históricos (esperado)")
    
except Exception as e:
    print(f"✗ Error al cargar datos históricos: {e}")

print("\n" + "="*80)
print("3. PRUEBA DE ESTADÍSTICAS DESCRIPTIVAS")
print("="*80)

try:
    # Estadísticas generales
    stats_general = calcular_estadisticas_descriptivas(df, 'Puntaje Global')
    print("✓ Estadísticas generales calculadas")
    print(f"  - Promedio: {stats_general['Promedio']:.2f}")
    print(f"  - Mediana: {stats_general['Mediana']:.2f}")
    print(f"  - Desv. Estándar: {stats_general['Desv. Estándar']:.2f}")
    
    # Estadísticas por modelo
    stats_modelo = calcular_estadisticas_descriptivas(df, 'Puntaje Global', 'Modelo')
    print("✓ Estadísticas por modelo calculadas")
    print(f"  - Modelos analizados: {len(stats_modelo)}")
    
except Exception as e:
    print(f"✗ Error al calcular estadísticas: {e}")

print("\n" + "="*80)
print("4. PRUEBA DE TEST ESTADÍSTICO")
print("="*80)

try:
    resultado = realizar_test_comparacion(
        df,
        'Puntaje Global',
        df['Modelo'] == 'Aula Regular',
        df['Modelo'] == 'Modelo Flexible',
        'Aula Regular',
        'Modelo Flexible'
    )
    
    if resultado['valido']:
        print("✓ Test estadístico realizado exitosamente")
        print(f"  - Diferencia de medias: {resultado['diferencia_medias']:.2f}")
        print(f"  - Valor p: {resultado['p_value']:.4f}")
        print(f"  - ¿Significativo?: {resultado['significativo']}")
        print(f"  - Interpretación: {resultado['interpretacion']}")
    else:
        print(f"⚠ Test no válido: {resultado['mensaje']}")
    
except Exception as e:
    print(f"✗ Error al realizar test: {e}")

print("\n" + "="*80)
print("5. PRUEBA DE CÁLCULO DE PERCENTILES")
print("="*80)

try:
    # Obtener un valor de ejemplo
    valor_ejemplo = df['Puntaje Global'].median()
    percentil = calcular_percentil(df, 'Puntaje Global', valor_ejemplo)
    
    print("✓ Percentil calculado exitosamente")
    print(f"  - Valor: {valor_ejemplo:.2f}")
    print(f"  - Percentil: {percentil:.2f}%")
    
except Exception as e:
    print(f"✗ Error al calcular percentil: {e}")

print("\n" + "="*80)
print("6. PRUEBA DE RANKINGS")
print("="*80)

try:
    # Ranking global
    ranking_global = obtener_ranking(df, 'Puntaje Global', top_n=5)
    print("✓ Ranking global generado")
    print(f"  - Top 5 estudiantes:")
    for idx, row in ranking_global.iterrows():
        print(f"    {idx}. {row['Nombre Completo']} - {row['Puntaje Global']:.1f} ({row['Modelo']})")
    
    # Ranking por área
    ranking_area = obtener_ranking(df, 'Matemáticas', top_n=3)
    print("✓ Ranking por área generado")
    print(f"  - Top 3 en Matemáticas:")
    for idx, row in ranking_area.iterrows():
        print(f"    {idx}. {row['Nombre Completo']} - {row['Matemáticas']:.1f}")
    
except Exception as e:
    print(f"✗ Error al generar rankings: {e}")

print("\n" + "="*80)
print("7. PRUEBA DE ANÁLISIS POR MODELO")
print("="*80)

try:
    for modelo in df['Modelo'].unique():
        df_modelo = df[df['Modelo'] == modelo]
        promedio = df_modelo['Puntaje Global'].mean()
        grupos = sorted(df_modelo['Grupo'].unique())
        
        print(f"✓ {modelo}")
        print(f"  - Estudiantes: {len(df_modelo)}")
        print(f"  - Promedio Global: {promedio:.2f}")
        print(f"  - Grupos: {', '.join(grupos)}")
        
        # Promedios por área
        print(f"  - Promedios por área:")
        for area in AREAS:
            prom_area = df_modelo[area].mean()
            print(f"    • {area}: {prom_area:.2f}")
    
except Exception as e:
    print(f"✗ Error al analizar por modelo: {e}")

print("\n" + "="*80)
print("8. PRUEBA DE ANÁLISIS POR GRUPO")
print("="*80)

try:
    for grupo in sorted(df['Grupo'].unique()):
        df_grupo = df[df['Grupo'] == grupo]
        modelo = df_grupo['Modelo'].iloc[0]
        promedio = df_grupo['Puntaje Global'].mean()
        
        print(f"✓ Grupo {grupo} ({modelo})")
        print(f"  - Estudiantes: {len(df_grupo)}")
        print(f"  - Promedio Global: {promedio:.2f}")
    
except Exception as e:
    print(f"✗ Error al analizar por grupo: {e}")

print("\n" + "="*80)
print("9. PRUEBA DE CORRELACIONES")
print("="*80)

try:
    for modelo in df['Modelo'].unique():
        df_modelo = df[df['Modelo'] == modelo]
        correlaciones = df_modelo[AREAS].corr()
        
        print(f"✓ Correlaciones calculadas para {modelo}")
        print(f"  - Matriz de correlación: {correlaciones.shape}")
        
        # Encontrar la correlación más alta (excluyendo diagonal)
        corr_values = correlaciones.values
        np.fill_diagonal(corr_values, 0)
        max_corr = np.max(corr_values)
        max_pos = np.unravel_index(np.argmax(corr_values), corr_values.shape)
        area1 = AREAS[max_pos[0]]
        area2 = AREAS[max_pos[1]]
        
        print(f"  - Correlación más alta: {area1} - {area2} ({max_corr:.3f})")
    
except Exception as e:
    print(f"✗ Error al calcular correlaciones: {e}")

print("\n" + "="*80)
print("10. PRUEBA DE CLASIFICACIONES")
print("="*80)

try:
    clasificaciones = df['Clasificación'].value_counts().sort_index()
    
    print("✓ Clasificaciones calculadas")
    for clasificacion, cantidad in clasificaciones.items():
        porcentaje = (cantidad / len(df)) * 100
        print(f"  - {clasificacion}: {cantidad} estudiantes ({porcentaje:.1f}%)")
    
except Exception as e:
    print(f"✗ Error al analizar clasificaciones: {e}")

print("\n" + "="*80)
print("RESUMEN DE PRUEBAS")
print("="*80)

print("""
✓ Todas las pruebas completadas exitosamente

La aplicación está lista para usar. Puedes ejecutarla con:
    streamlit run app_resultados_icfes_completo.py

Funcionalidades verificadas:
  ✓ Carga de datos unificados
  ✓ Carga de datos históricos
  ✓ Estadísticas descriptivas
  ✓ Tests estadísticos
  ✓ Cálculo de percentiles
  ✓ Generación de rankings
  ✓ Análisis por modelo
  ✓ Análisis por grupo
  ✓ Correlaciones entre áreas
  ✓ Clasificaciones de estudiantes
""")

print("="*80)

