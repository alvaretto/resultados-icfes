# Plan de Mejoramiento y Desarrollo 2026

## Institución Educativa Pedacito de Cielo - La Tebaida, Quindío

### Priorización de Ejercicios del Repositorio de Matemáticas ICFES

---

## 1. Diagnóstico: Falencias Históricas Identificadas

### 1.1 Fuentes de la Verdad Consultadas

- Resultados Saber 11° 2024 (Código DANE: 163401000298)
- Resultados Saber 11° 2025
- Análisis comparativo institucional 2024-2025
- Comparación con ETC Quindío

### 1.2 Falencias Críticas en Matemáticas

| Aprendizaje ICFES | % Error EE | Brecha vs ETC | Estado |
|-------------------|------------|---------------|--------|
| Validar procedimientos y estrategias matemáticas | **66%** | +9 pts | CRÍTICO |
| Resolver problemas con info cuantitativa | **59%** | +13 pts | CRÍTICO |
| Comprende y transforma info cuantitativa | **49%** | +16 pts | ALTO |

### 1.3 Distribución por Niveles de Desempeño (2025)

| Nivel | % Estudiantes EE | % Colombia | Observación |
|-------|------------------|------------|-------------|
| Nivel 1 (Bajo) | **30%** | 10% | ALARMA: Aumento desde 23% en 2024 |
| Nivel 2 | 34% | 32% | Vaciamiento del nivel intermedio |
| Nivel 3 | 35% | 50% | Polarización: buenos vs deficientes |
| Nivel 4 | 0% | 9% | Sin estudiantes en nivel superior |

### 1.4 Fenómeno de Polarización

El análisis revela un fenómeno preocupante: mientras el promedio se mantuvo estable (44 puntos), la distribución cambió drásticamente. La clase se "partió" en dos extremos, vaciando el nivel intermedio (Nivel 2). Esto indica que las estrategias actuales no están llegando a los estudiantes de desempeño medio.

---

## 2. Inventario de Ejercicios Disponibles

### 2.1 Repositorio Principal: En-Produccion

Ubicación: `/home/bootcamp/Proyectos-2026/RepositorioMatematicasICFES_R_Exams/A-Produccion/En-Produccion`

#### Categorías disponibles:

- 01-Numeros-Reales/Pensamiento-Numerico
- 02-Funciones/Pensamiento-Variacional-Espacial
- 05-Geometría/Pensamiento-Espacial
- 06-Estadística-Y-Probabilidad/Pensamiento-Aleatorio

### 2.2 Repositorio Complementario: En-Desarrollo

Ubicación: `/home/bootcamp/Proyectos-2026/RepositorioMatematicasICFES_R_Exams/A-Produccion/En-Desarrollo`

Ejercicios con alto potencial pedagógico pendientes de validación final.

---

## 3. Priorización de Ejercicios - En-Produccion

### 3.1 PRIORIDAD MÁXIMA - Validación de Procedimientos (Falencia: 66% error)

Estos ejercicios atacan directamente la falencia principal identificada.

| Ejercicio | Ruta Relativa | Justificación |
|-----------|---------------|---------------|
| `2023-Matematicas-11-2-09-Opc-A.Rmd` | `/02-Funciones/.../Variación-Lineal-Auto-Viajero-09/` | Detectar errores en cálculos de rapidez media |
| `2023-Matematicas-11-2-09-Opc-B.Rmd` | `/02-Funciones/.../Variación-Lineal-Auto-Viajero-09/` | Variante del ejercicio anterior |
| `2023-Matematicas-11-2-09-Opc-C.Rmd` | `/02-Funciones/.../Variación-Lineal-Auto-Viajero-09/` | Variante del ejercicio anterior |
| `2023-Matematicas-11-2-09-Opc-D.Rmd` | `/02-Funciones/.../Variación-Lineal-Auto-Viajero-09/` | Variante del ejercicio anterior |
| `2023-Matematicas-11-2-09-Op-M.Rmd` | `/02-Funciones/.../Variación-Lineal-Auto-Viajero-09/` | Variante del ejercicio anterior |
| `vuelo_acrobatico_A.Rmd` | `/02-Funciones/.../Variacion-Lineal-Vuelo-Acrobatico/` | Validación de pasos en variación lineal |
| `vuelo_acrobatico_B.Rmd` | `/02-Funciones/.../Variacion-Lineal-Vuelo-Acrobatico/` | Variante del ejercicio anterior |
| `vuelo_acrobatico_C.Rmd` | `/02-Funciones/.../Variacion-Lineal-Vuelo-Acrobatico/` | Variante del ejercicio anterior |
| `vuelo_acrobatico_mejorado_*.Rmd` | `/02-Funciones/.../Variacion-Lineal-Vuelo-Acrobatico/` | Versiones mejoradas |

### 3.2 PRIORIDAD MÁXIMA - Comprensión y Transformación de Info Cuantitativa (49-59% error)

| Ejercicio | Ruta Relativa | Justificación |
|-----------|---------------|---------------|
| `p25_SAI_CFA11S123.Rmd` | `/06-Estadística/.../Media/Promedios-Borrados/` | Reconstruir información faltante desde promedios |
| `Media-Mediana-Moda.Rmd` | `/06-Estadística/.../01-MediaMedianaModa/Calificaciones-Universitarias/` | Medidas de tendencia central con interpretación |
| `mediana_salas_cine_formulacion_ejecucion_n2_v1.Rmd` | `/06-Estadística/.../Mediana/` | Formulación y ejecución con mediana |

### 3.3 PRIORIDAD ALTA - Interpretación de Gráficos Estadísticos

| Ejercicio | Ruta Relativa | Justificación |
|-----------|---------------|---------------|
| `Adopcion_Mascotas_Aleatorio_Interpretacion_n3_v1-Opc-A.Rmd` | `/06-Estadística/.../Graficos_Estadisticos_Adopcion_Mascotas/` | Nivel 3 de interpretación gráfica |
| `Adopcion_Mascotas_Aleatorio_Interpretacion_n3_v1-Opc-B2.Rmd` | `/06-Estadística/.../Graficos_Estadisticos_Adopcion_Mascotas/` | Variante |
| `Adopcion_Mascotas_Aleatorio_Interpretacion_n3_v1-Opc-C2.Rmd` | `/06-Estadística/.../Graficos_Estadisticos_Adopcion_Mascotas/` | Variante |
| `Adopcion_Mascotas_Aleatorio_Interpretacion_n3_v1-Opc-D2.Rmd` | `/06-Estadística/.../Graficos_Estadisticos_Adopcion_Mascotas/` | Variante |
| `accidentalidad-vial-genero-01.Rmd` | `/06-Estadística/.../Accidentalidad_Vial_Genero-16/` | Variables cualitativas |
| `accidentalidad-vial-genero-02.Rmd` | `/06-Estadística/.../Accidentalidad_Vial_Genero-16/` | Distribución de frecuencias |
| `consumo_gas_natural_porcentaje_maximo_*.Rmd` | `/06-Estadística/.../Gas_natural_*/` | Porcentajes y lectura de gráficos |

### 3.4 PRIORIDAD MEDIA - Probabilidad y Conteo

| Ejercicio | Ruta Relativa | Justificación |
|-----------|---------------|---------------|
| `DVenn_All_GenMus_01.Rmd` | `/06-Estadística/.../Diagramas de Venn/GénerosMusicales/` | Diagramas de Venn con contexto musical |
| `DVenn_All_GenMus_03.Rmd` | `/06-Estadística/.../Diagramas de Venn/GénerosMusicales/` | Variante avanzada |
| `11_C01_G09_2020_Tipo1.Rmd` | `/06-Estadística/.../Probabilidad-Bolas-Colores/` | Probabilidad básica |
| `probabilidad_intervalos_curva_*.Rmd` | `/06-Estadística/.../Probabilidad-Intervalos-Curva-13-S1-2024B/` | Probabilidad con distribuciones |

### 3.5 PRIORIDAD MEDIA - Medidas de Posición

| Ejercicio | Ruta Relativa | Justificación |
|-----------|---------------|---------------|
| `estadistica_diagramas_caja_interpretacion_representacion_Nivel2_v2.Rmd` | `/06-Estadística/.../06-Medidas-De-Posición/` | Interpretación de boxplots |
| `2023-Matematicas-11-2-04-Op-B.Rmd` | `/06-Estadística/.../Mediana/Baterías-Celulares/` | Mediana con datos |
| `2023-Matematicas-11-2-04-Op-C.Rmd` | `/06-Estadística/.../Mediana/Baterías-Celulares/` | Variante |
| `2023-Matematicas-11-2-04-Op-D.Rmd` | `/06-Estadística/.../Mediana/Baterías-Celulares/` | Variante |

### 3.6 PRIORIDAD COMPLEMENTARIA - Números Reales y Geometría

| Ejercicio | Ruta Relativa | Justificación |
|-----------|---------------|---------------|
| `fracciones_reparto_premio_v1.Rmd` | `/01-Numeros-Reales/.../22-S2-2025-SEDQ-fracciones_reparto_premio/` | Operaciones con fracciones |
| `fracciones_reparto_premio_v2.Rmd` | `/01-Numeros-Reales/.../22-S2-2025-SEDQ-fracciones_reparto_premio/` | Variante |
| `fracciones_reparto_premio_v3.Rmd` | `/01-Numeros-Reales/.../22-S2-2025-SEDQ-fracciones_reparto_premio/` | Variante |
| `conversion_unidades_area_formulacion_ejecucion_n2_v1.Rmd` | `/05-Geometría/.../17-Conversión-de-Unidades/` | Conversión de unidades de área |

---

## 4. Priorización de Ejercicios - En-Desarrollo

### 4.1 PRIORIDAD MÁXIMA - Terminar y Validar Urgentemente

Estos ejercicios tienen alto valor pedagógico y deben completarse para uso en 2026.

| Ejercicio | Competencia ICFES | Nivel | Justificación |
|-----------|-------------------|-------|---------------|
| `piscinas_baldosas_patrones_numerico_variacional_interpretacion_representacion_n2_v1.Rmd` | Interpretación-Representación | 2 | Patrones y secuencias - CRÍTICO para el 30% en Nivel 1 |
| `proceso_recaudacion_sitio_turistico_numerico_variacional_argumentacion_n2_v1.Rmd` | Argumentación | 2 | Contexto laboral/turístico con precios reales colombianos |
| `tablas_frecuencia_argumentacion_n3_v1.Rmd` | Argumentación | 3 | Tablas de frecuencia con argumentación avanzada |
| `consumo_telefonico_adicional_n2_v1.Rmd` | Interpretación-Representación | 2 | Lectura de tablas y cálculos - contexto familiar |

### 4.2 PRIORIDAD ALTA - Completar en Primer Semestre 2026

| Ejercicio | Competencia ICFES | Nivel | Justificación |
|-----------|-------------------|-------|---------------|
| `dispersion_alcance_proyectil_aleatorio_interpretacion_representacion_n2_v1_opc_A.Rmd` | Interpretación-Representación | 2 | Gráficos de dispersión - contexto científico |
| `dispersion_alcance_proyectil_aleatorio_interpretacion_representacion_n2_v1_opc_B.Rmd` | Interpretación-Representación | 2 | Variante |
| `dispersion_alcance_proyectil_aleatorio_interpretacion_representacion_n2_v1_opc_C.Rmd` | Interpretación-Representación | 2 | Variante |
| `dispersion_alcance_proyectil_aleatorio_interpretacion_representacion_n2_v1_opc_D.Rmd` | Interpretación-Representación | 2 | Variante |
| `recta_geometria_analitica_interpretacion_representacion_n2_v1.Rmd` | Interpretación-Representación | 2 | Ecuación de la recta, pendiente, intercepto |

### 4.3 PRIORIDAD MEDIA - Completar en Segundo Semestre 2026

| Ejercicio | Competencia ICFES | Nivel | Justificación |
|-----------|-------------------|-------|---------------|
| `01-probabilidad_condicional_diagrama_arbol_aleatorio_argumentacion_n3_v1.Rmd` | Argumentación | 3 | Probabilidad condicional avanzada |
| `seleccion_canciones_cd_diagrama_arbol_aleatorio_argumentacion_n2_v1.Rmd` | Argumentación | 2 | Diagramas de árbol contextualizados |
| `volumen_cilindro_geometrico_metrico_interpretacion_n2_v1.Rmd` | Interpretación | 2 | Volumen de cilindros |
| `proyeccion_usuarios_parabola_geometrico_interpretacion_n2_v1.Rmd` | Interpretación | 2 | Funciones cuadráticas aplicadas |
| `migracion_atun_representacion_grafica_aleatorio_interpretacion_n2_v1.Rmd` | Interpretación | 2 | Gráficas en contexto biológico |

---

## 5. Plan de Implementación 2026

### 5.1 Fase 1: Semanas 1-4 (Fundamentos Críticos)

#### Semana 1: Validación de Procedimientos

Objetivo: Atacar directamente la falencia del 66% de error en validación.

Ejercicios a aplicar:

- `2023-Matematicas-11-2-09-Opc-A.Rmd`
- `2023-Matematicas-11-2-09-Opc-B.Rmd`
- `vuelo_acrobatico_A.Rmd`

#### Semana 2: Patrones y Secuencias

Objetivo: Reforzar pensamiento numérico-variacional para estudiantes en Nivel 1.

Ejercicios a aplicar:

- `piscinas_baldosas_patrones_*.Rmd` (En-Desarrollo - PRIORIZAR TERMINACIÓN)
- `proceso_recaudacion_sitio_turistico_*.Rmd` (En-Desarrollo)

#### Semana 3: Transformación de Información Cuantitativa

Objetivo: Atacar la falencia del 49% de error en comprensión de datos.

Ejercicios a aplicar:

- `p25_SAI_CFA11S123.Rmd`
- `consumo_telefonico_adicional_n2_v1.Rmd` (En-Desarrollo)
- `Media-Mediana-Moda.Rmd`

#### Semana 4: Consolidación Numérico-Variacional

Objetivo: Reforzar y evaluar avances.

Ejercicios a aplicar:

- Variantes restantes de `vuelo_acrobatico_*.Rmd`
- `fracciones_reparto_premio_*.Rmd`

### 5.2 Fase 2: Semanas 5-8 (Interpretación Gráfica y Estadística)

#### Semana 5: Gráficos Estadísticos

Ejercicios a aplicar:

- `Adopcion_Mascotas_*.Rmd` (todas las variantes)
- `accidentalidad-vial-genero-*.Rmd`

#### Semana 6: Tablas y Argumentación

Ejercicios a aplicar:

- `tablas_frecuencia_argumentacion_n3_v1.Rmd` (En-Desarrollo)
- `consumo_gas_natural_*.Rmd`

#### Semana 7: Medidas de Posición

Ejercicios a aplicar:

- `estadistica_diagramas_caja_*.Rmd`
- `mediana_salas_cine_*.Rmd`
- `2023-Matematicas-11-2-04-*.Rmd` (Baterías)

#### Semana 8: Dispersión y Correlación

Ejercicios a aplicar:

- `dispersion_alcance_proyectil_*.Rmd` (En-Desarrollo)
- `confint2-cloze.Rmd`

### 5.3 Fase 3: Semanas 9-12 (Probabilidad y Geometría)

#### Semana 9: Probabilidad con Conjuntos

Ejercicios a aplicar:

- `DVenn_All_GenMus_*.Rmd`
- `11_C01_G09_2020_Tipo1.Rmd`

#### Semana 10: Probabilidad Avanzada

Ejercicios a aplicar:

- `probabilidad_condicional_diagrama_arbol_*.Rmd` (En-Desarrollo)
- `probabilidad_intervalos_curva_*.Rmd`

#### Semana 11: Geometría Analítica

Ejercicios a aplicar:

- `recta_geometria_analitica_*.Rmd` (En-Desarrollo)
- `conversion_unidades_area_*.Rmd`

#### Semana 12: Geometría Métrica

Ejercicios a aplicar:

- `volumen_cilindro_geometrico_*.Rmd` (En-Desarrollo)
- `proyeccion_usuarios_parabola_*.Rmd`

### 5.4 Ciclo Continuo

A partir de la semana 13, repetir el ciclo con nuevas semillas aleatorias para generar versiones diferentes de los ejercicios.

---

## 6. Top 10 Ejercicios Absolutos

Orden estricto de prioridad para implementación inmediata:

1. **`2023-Matematicas-11-2-09-Opc-A.Rmd`** - Validación de procedimientos (66% error)
2. **`piscinas_baldosas_patrones_*.Rmd`** - Patrones numéricos (30% Nivel 1)
3. **`p25_SAI_CFA11S123.Rmd`** - Promedios y transformación de datos
4. **`proceso_recaudacion_sitio_turistico_*.Rmd`** - Argumentación contextualizada
5. **`tablas_frecuencia_argumentacion_n3_v1.Rmd`** - Argumentación Nivel 3
6. **`consumo_telefonico_adicional_n2_v1.Rmd`** - Interpretación de consumo
7. **`Adopcion_Mascotas_*.Rmd`** - Interpretación gráfica Nivel 3
8. **`estadistica_diagramas_caja_*.Rmd`** - Boxplots
9. **`DVenn_All_GenMus_*.Rmd`** - Probabilidad con conjuntos
10. **`recta_geometria_analitica_*.Rmd`** - Geometría analítica

---

## 7. Brechas Detectadas en el Repositorio

### 7.1 Temas No Cubiertos Adecuadamente

| Tema Faltante | Relevancia ICFES | Acción Recomendada |
|---------------|------------------|-------------------|
| Sistemas de ecuaciones | Alta (validación) | Crear nuevos ejercicios |
| Funciones cuadráticas aplicadas | Alta | Expandir desde `proyeccion_usuarios_parabola` |
| Proporcionalidad directa/inversa | Media-Alta | Crear ejercicios contextualizados |
| Perímetro y área compuestas | Media | Crear ejercicios para En-Produccion |
| Razonamiento proporcional | Alta (transformación) | Crear ejercicios |

### 7.2 Fortalezas del Repositorio

- Excelente cobertura de Estadística y Probabilidad (Pensamiento Aleatorio)
- Buenos ejercicios de validación de procedimientos en variación lineal
- Ejercicios con contextos colombianos relevantes (En-Desarrollo)
- Sistema de aleatorización que permite generar múltiples versiones

---

## 8. Alertas y Recomendaciones

### 8.1 Sobre el Repositorio

- **Archivos duplicados**: Existen muchos archivos "Copia de..." que son redundantes. Usar únicamente los archivos originales.
- **Ejercicios En-Desarrollo**: Deben validarse y moverse a En-Produccion antes de su uso en aula.
- **Metadatos ICFES**: Los ejercicios en En-Desarrollo incluyen metadatos explícitos (competencia, nivel, componente) que facilitan el alineamiento curricular.

### 8.2 Sobre la Implementación

- Priorizar la terminación de ejercicios en En-Desarrollo marcados como URGENTE.
- Usar el sistema de semillas aleatorias para generar versiones diferentes en cada aplicación.
- Monitorear el desempeño por competencia para ajustar el plan según resultados.

---

## 9. Indicadores de Seguimiento

### 9.1 Metas para 2026

| Indicador | Línea Base 2025 | Meta 2026 |
|-----------|-----------------|-----------|
| % Estudiantes Nivel 1 | 30% | < 20% |
| % Estudiantes Nivel 3+4 | 35% | > 45% |
| Error en validación de procedimientos | 66% | < 55% |
| Error en transformación de info cuantitativa | 49% | < 40% |
| Brecha vs ETC Quindío | -11 pts | < -8 pts |

### 9.2 Evaluaciones Intermedias

- **Marzo 2026**: Evaluación diagnóstica post-Fase 1
- **Junio 2026**: Simulacro ICFES interno
- **Agosto 2026**: Evaluación pre-Saber 11
- **Octubre 2026**: Análisis de resultados Saber 11

---

## 10. Anexos

### Anexo A: Rutas Completas del Repositorio

```
Repositorio Principal:
/home/bootcamp/Proyectos-2026/RepositorioMatematicasICFES_R_Exams/A-Produccion/

├── En-Produccion/
│   ├── 01-Numeros-Reales/
│   ├── 02-Funciones/
│   ├── 05-Geometría/
│   └── 06-Estadística-Y-Probabilidad/
│
└── En-Desarrollo/
    ├── piscinas_baldosas_patrones.../
    ├── proceso_recaudacion_sitio_turistico.../
    ├── tablas_frecuencia_argumentacion/
    ├── dispersion_alcance_proyectil.../
    ├── recta_geometria_analitica.../
    ├── consumo_telefonico_adicional/
    ├── probabilidad_condicional_diagrama_arbol.../
    ├── volumen_cilindro_geometrico.../
    └── proyeccion_usuarios_parabola.../
```

### Anexo B: Competencias ICFES Evaluadas

- **Interpretación y Representación**: Comprender y transformar información en distintas representaciones.
- **Formulación y Ejecución**: Formular y ejecutar procedimientos para resolver problemas.
- **Argumentación**: Validar o rechazar procedimientos, estrategias o resultados.

### Anexo C: Componentes del Área de Matemáticas

- Numérico-Variacional
- Geométrico-Métrico
- Aleatorio

---

*Documento generado el 30 de enero de 2026*

*Basado en análisis de resultados ICFES 2024-2025 y repositorio de ejercicios R-Exams*
