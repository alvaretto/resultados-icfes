#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo para analizar inconsistencias entre el PDF de La Tebaida
y los PDFs oficiales del ICFES
"""

import pdfplumber
import pandas as pd
import re
from typing import Dict, List, Tuple

def extraer_datos_pdf_tebaida(pdf_path: str) -> Dict:
    """
    Extrae los datos del PDF de análisis de La Tebaida
    
    Returns:
        Dict con estructura:
        {
            '2024': {'PEDACITO DE CIELO REGULAR': 240, 'PEDACITO DE CIELO PENSAR': 203},
            '2025': {'PEDACITO DE CIELO REGULAR': 234, 'PEDACITO DE CIELO PENSAR': 214}
        }
    """
    datos = {'2024': {}, '2025': {}}
    
    try:
        with pdfplumber.open(pdf_path) as pdf:
            # Extraer texto de la primera página
            if pdf.pages:
                text = pdf.pages[0].extract_text()
                
                # Buscar líneas con "PEDACITO DE CIELO"
                lines = text.split('\n')
                for line in lines:
                    if 'PEDACITO DE CIELO' in line.upper():
                        # Extraer año y puntaje
                        # Formato: "PEDACITO DE CIELO REGULAR 240" o "PEDACITO DE CIELO REGULAR 234"
                        match = re.search(r'PEDACITO DE CIELO (REGULAR|PENSAR)\s+(\d+)', line, re.IGNORECASE)
                        if match:
                            modelo = match.group(1).upper()
                            puntaje = int(match.group(2))
                            
                            # Determinar año por contexto (columna)
                            if '2024' in line or line.find('PEDACITO') < len(line) // 2:
                                datos['2024'][f'PEDACITO DE CIELO {modelo}'] = puntaje
                            else:
                                datos['2025'][f'PEDACITO DE CIELO {modelo}'] = puntaje
                
                # Método alternativo: buscar en tabla estructurada
                if not datos['2024'] and not datos['2025']:
                    # Buscar patrón más específico
                    for i, line in enumerate(lines):
                        if 'PEDACITO DE CIELO REGULAR' in line:
                            # Extraer números de la línea
                            numeros = re.findall(r'\d+', line)
                            if len(numeros) >= 2:
                                datos['2024']['PEDACITO DE CIELO REGULAR'] = int(numeros[0])
                                datos['2025']['PEDACITO DE CIELO REGULAR'] = int(numeros[1])
                        
                        if 'PEDACITO DE CIELO PENSAR' in line:
                            numeros = re.findall(r'\d+', line)
                            if len(numeros) >= 2:
                                datos['2024']['PEDACITO DE CIELO PENSAR'] = int(numeros[0])
                                datos['2025']['PEDACITO DE CIELO PENSAR'] = int(numeros[1])
    
    except Exception as e:
        print(f"Error al extraer datos del PDF de La Tebaida: {e}")
    
    return datos


def calcular_promedio_desde_excel(excel_path: str) -> float:
    """
    Calcula el promedio global desde un archivo Excel de resultados
    
    Args:
        excel_path: Ruta al archivo Excel con resultados
        
    Returns:
        Promedio global calculado
    """
    try:
        df = pd.read_excel(excel_path)
        
        # Buscar columna de puntaje global
        columnas_posibles = ['Puntaje Global', 'PUNTAJE GLOBAL', 'Global', 'GLOBAL']
        columna_global = None
        
        for col in columnas_posibles:
            if col in df.columns:
                columna_global = col
                break
        
        if columna_global:
            # Calcular promedio excluyendo NaN
            promedio = df[columna_global].mean()
            return round(promedio, 2)
        else:
            print(f"No se encontró columna de puntaje global en {excel_path}")
            return None
            
    except Exception as e:
        print(f"Error al calcular promedio desde Excel: {e}")
        return None


def comparar_datos(datos_tebaida: Dict, datos_oficiales: Dict) -> List[Dict]:
    """
    Compara los datos del PDF de La Tebaida con los datos oficiales
    
    Args:
        datos_tebaida: Datos extraídos del PDF de La Tebaida
        datos_oficiales: Dict con promedios oficiales por año y modelo
        
    Returns:
        Lista de inconsistencias encontradas
    """
    inconsistencias = []
    
    for año in ['2024', '2025']:
        for modelo in datos_tebaida.get(año, {}).keys():
            puntaje_tebaida = datos_tebaida[año].get(modelo)
            puntaje_oficial = datos_oficiales.get(año, {}).get(modelo)
            
            if puntaje_oficial is not None and puntaje_tebaida is not None:
                diferencia = abs(puntaje_tebaida - puntaje_oficial)
                
                if diferencia > 0:
                    inconsistencias.append({
                        'año': año,
                        'modelo': modelo,
                        'puntaje_tebaida': puntaje_tebaida,
                        'puntaje_oficial': puntaje_oficial,
                        'diferencia': diferencia,
                        'tipo': 'Discrepancia en puntaje'
                    })
    
    return inconsistencias


def generar_reporte_inconsistencias(inconsistencias: List[Dict]) -> pd.DataFrame:
    """
    Genera un DataFrame con el reporte de inconsistencias
    
    Args:
        inconsistencias: Lista de inconsistencias encontradas
        
    Returns:
        DataFrame con el reporte
    """
    if not inconsistencias:
        return pd.DataFrame()
    
    df = pd.DataFrame(inconsistencias)
    return df

