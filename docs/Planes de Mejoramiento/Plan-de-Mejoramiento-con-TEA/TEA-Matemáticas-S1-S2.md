---
output:
  pdf_document:
    latex_engine: xelatex
  html_document: default
---

# TEA Matemáticas — Priorización para Conversión a R-Exams

## Sesión 1 y Sesión 2 — Basado en Falencias PCielo ICFES 2025

**Fecha:** 4 de marzo de 2026\
**Institución:** PCielo\
**Área:** Matemáticas\
**Instrumento:** TEA (45 preguntas — Primera Sesión PS-01 a PS-25 / Segunda Sesión SS-26 a SS-45)\
**Propósito:** Definir el orden de conversión a r-exams para maximizar impacto en el cierre de brechas

---

## Sección 1: Diagnóstico Resumido

### 1.1 Puntaje Global

| Entidad | Puntaje Matemáticas 2025 | Variación 2024→2025 |
|---------|--------------------------|----------------------|
| PCielo | 44 | 0 (estancado) |
| Colombia | 53 | — |
| ETC (referente) | 55 | — |
| **Brecha PCielo vs ETC** | **-11 puntos** | — |

### 1.2 Niveles de Desempeño 2025

| Nivel | PCielo 2025 | ETC 2025 | Brecha | Variación PCielo 2024→2025 |
|-------|-------------|----------|--------|----------------------------|
| Nivel 1 (Insuficiente) | 30% | 7% | -23 pp | RETROCESO (+7 pp) |
| Nivel 2 (Mínimo) | 34% | 29% | -5 pp | — |
| Nivel 3 (Satisfactorio) | 35% | 53% | -18 pp | — |
| Nivel 4 (Avanzado) | 0% | 10% | -10 pp | CRÍTICO (cero estudiantes) |
| **Insuficiencia acumulada (N1+N2)** | **64%** | **36%** | **-28 pp** | — |

### 1.3 Competencias — Porcentaje de Respuestas Incorrectas 2025

| Competencia | PCielo % Incorrecto | Colombia % Incorrecto | ETC % Incorrecto | Tendencia 2024→2025 |
|-------------|--------------------|-----------------------|------------------|----------------------|
| Argumentación (Valida procedimientos y estrategias) | **66%** | 57% | — | EMPEORÓ (+2 pp) |
| Formulación y ejecución (Identifica info y establece relaciones) | 59% | — | 46% | Mejoró (-4 pp) |
| Interpretación y representación (Comprende y transforma info cuantitativa) | 49% | — | 33% | Mejoró (-6 pp) |

### 1.4 Hallazgos Clave

**Fenómeno de polarización.** Entre 2024 y 2025 se observa un vaciamiento del nivel 2: más estudiantes en nivel 1 (retroceso) y más en nivel 3, pero sin que ninguno alcance el nivel 4. La distribución se bifurca en lugar de concentrarse en la zona de excelencia.

**Cero estudiantes en nivel 4.** PCielo tiene 0% de estudiantes en nivel avanzado frente al 10% de la ETC. Esta ausencia total de excelencia es el indicador más crítico y diferenciador.

**Argumentación como talón de Aquiles.** Es la única competencia que empeoró año a año y concentra la mayor brecha respecto a los referentes nacionales. Representa el punto de intervención con mayor potencial de impacto.

**Jornada 1 en retroceso.** La jornada regular bajó 2 puntos (47 pts), mientras la jornada flexible subió 1 (42 pts). El problema no es homogéneo al interior de la institución.

---

## Sección 2: Criterios de Priorización

Los cinco criterios se aplican en orden de peso decreciente. Cada pregunta recibe un puntaje de prioridad que determina su banda.

### Criterio 1 — Competencia con mayor falencia (Peso: 40%)

La competencia define el impacto directo sobre la brecha diagnosticada.

| Competencia | % Errores PCielo | Puntos asignados |
|-------------|------------------|------------------|
| Argumentación | 66% (empeoró) | 3 |
| Formulación y ejecución | 59% (mejoró leve) | 2 |
| Interpretación y representación | 49% (mejoró) | 1 |

### Criterio 2 — Nivel de desempeño para cierre de brechas (Peso: 30%)

El objetivo no es reforzar lo que ya funciona, sino mover estudiantes hacia arriba en la escala.

| Nivel | Justificación estratégica | Puntos asignados |
|-------|--------------------------|------------------|
| Nivel 3 | Mover estudiantes de N2 a N3 — brecha crítica (35% vs 53% ETC) | 3 |
| Nivel 4 | Desarrollar excelencia — actualmente 0% en PCielo | 2 |
| Nivel 1 | Solo 1 pregunta; la prioridad es sacar estudiantes de N1, no reforzarlo | 1 |

### Criterio 3 — Accesibilidad de grado (Peso: 15%)

El grado indica la proximidad con la población PCielo y la viabilidad de aplicación pedagógica.

| Rango de grado | Justificación | Puntos asignados |
|----------------|---------------|------------------|
| 6°-7° / 7°-8° | Consolidan bases, accesibles para la mayoría de la población | 3 |
| 8°-9° | Grado transición, aplica para cierre de brecha medio | 2 |
| 9°-10° / 10°-11° / 11° | Cierra brecha con ETC en niveles superiores | 2 |

### Criterio 4 — Versatilidad para r-exams (Peso: 10%)

Las preguntas genéricas (Genérico: Sí) admiten parametrización de contexto, valores y enunciados, lo que reduce el tiempo de desarrollo y aumenta el banco disponible.

| Genérico | Puntos asignados |
|----------|------------------|
| Sí | 2 |
| No | 1 |

### Criterio 5 — Representatividad del componente (Peso: 5%)

Se prioriza según la frecuencia del componente en el TEA (mayor representatividad = mayor peso en la prueba real).

| Componente | Preguntas en TEA | Puntos asignados |
|------------|-----------------|------------------|
| Numérico-variacional | 18 | 3 |
| Aleatorio | 15 | 2 |
| Geométrico-métrico | 12 | 1 |

### Fórmula de Scoring

```
Score = (C1 × 0.40) + (C2 × 0.30) + (C3 × 0.15) + (C4 × 0.10) + (C5 × 0.05)
```

**Rangos de banda:**

| Score | Banda | Prioridad |
|-------|-------|-----------|
| ≥ 2.60 | Crítica | 1 |
| 2.00 – 2.59 | Alta | 2 |
| < 2.00 | Media | 3 |

---

## Sección 3: Banda Crítica — Prioridad 1

**Criterio de inclusión:** Argumentación (C1=3) en Nivel 3 o Nivel 4 (C2≥2).
Son las preguntas con mayor potencial de impacto directo en las brechas identificadas.

Estas preguntas atacan simultáneamente la competencia más débil (Argumentación, 66% errores, empeoró) y los niveles donde PCielo tiene las mayores diferencias con ETC.

### PS-04 — Fracciones y decimales, vueltas a pista

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-04 |
| Nivel | 3 |
| Competencia | Argumentación |
| Componente | Numérico-variacional |
| Grado | 6°-7° |
| Genérico | Sí |
| Score | 3×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 3×0.05 = 1.20+0.90+0.45+0.20+0.15 = **2.90** |

**Justificación:** Triple ventaja: competencia crítica + nivel estratégico N3 + grado accesible 6°-7° + genérica. Consolida la comprensión de fracciones y decimales que subyace a múltiples errores en Argumentación. Su carácter genérico facilita la parametrización en r-exams con distintos valores y contextos de pista.

---

### PS-10 — Transacciones bancarias 3/8 de 12000

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-10 |
| Nivel | 3 |
| Competencia | Argumentación |
| Componente | Numérico-variacional |
| Grado | 7° |
| Genérico | Sí |
| Score | 3×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 3×0.05 = **2.90** |

**Justificación:** Idéntico perfil a PS-04. Fracciones en contexto financiero accesible, genérica, componente Numérico-variacional (el más frecuente en el TEA). Directamente atacable desde 7° grado y muy parametrizable en r-exams cambiando montos y fracciones.

---

### PS-12 — Área sombreada semicircunferencia

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-12 |
| Nivel | 3 |
| Competencia | Argumentación |
| Componente | Geométrico-métrico |
| Grado | 8°-9° |
| Genérico | Sí |
| Score | 3×0.40 + 3×0.30 + 2×0.15 + 2×0.10 + 1×0.05 = 1.20+0.90+0.30+0.20+0.05 = **2.65** |

**Justificación:** Argumentación N3 en Geometría. La validación de procedimientos geométricos con figuras compuestas es una debilidad recurrente. Su carácter genérico permite variar radios y configuraciones de figuras en r-exams.

---

### PS-18 — Ángulos de radios en rueda

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-18 |
| Nivel | 3 |
| Competencia | Argumentación |
| Componente | Geométrico-métrico |
| Grado | 6°-7° |
| Genérico | Sí |
| Score | 3×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 1×0.05 = 1.20+0.90+0.45+0.20+0.05 = **2.80** |

**Justificación:** Argumentación N3 en grado accesible 6°-7°. Los ángulos en círculo son contenido transversal de gran representatividad. La pregunta es genérica: número de radios y ángulos son parametrizables. Alta prioridad por combinar grado accesible con competencia crítica.

---

### PS-21 — Desigualdad triangular

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-21 |
| Nivel | 3 |
| Competencia | Argumentación |
| Componente | Geométrico-métrico |
| Grado | 7°-8° |
| Genérico | Sí |
| Score | 3×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 1×0.05 = **2.80** |

**Justificación:** Argumentación N3, grado 7°-8°, genérica. La desigualdad triangular es un criterio de validación (argumentación pura) que los estudiantes de PCielo fallan por falta de razonamiento lógico-geométrico. Fácilmente parametrizable en r-exams con distintas longitudes de lados.

---

### SS-38 — Diagrama de Venn 3 servicios

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-38 |
| Nivel | 3 |
| Competencia | Argumentación |
| Componente | Aleatorio |
| Grado | 6°-7° |
| Genérico | Sí |
| Score | 3×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 2×0.05 = 1.20+0.90+0.45+0.20+0.10 = **2.85** |

**Justificación:** Argumentación N3, grado accesible 6°-7°, genérica, componente Aleatorio. Los diagramas de Venn con 3 conjuntos exigen validar la consistencia lógica de la distribución — exactamente la habilidad de Argumentación. Muy parametrizable: cambiar los tres servicios y las frecuencias de intersección.

---

### SS-39 — Porcentaje inverso, descuento

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-39 |
| Nivel | 3 |
| Competencia | Argumentación |
| Componente | Numérico-variacional |
| Grado | 7° |
| Genérico | Sí |
| Score | 3×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 3×0.05 = **2.90** |

**Justificación:** El porcentaje inverso (dado el resultado, encontrar el original) es uno de los errores más documentados en Argumentación para PCielo. N3, 7°, genérica, Numérico-variacional. Altísima parametrizabilidad: cambiar el porcentaje de descuento y el precio final. Prioridad máxima dentro de la banda.

---

### SS-43 — Área superficial de caja

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-43 |
| Nivel | 3 |
| Competencia | Argumentación |
| Componente | Geométrico-métrico |
| Grado | 7°-8° |
| Genérico | Sí |
| Score | 3×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 1×0.05 = **2.80** |

**Justificación:** Argumentación N3 con fórmulas geométricas 3D. La validación de procedimientos para calcular área superficial es un contenido que articula grados 7°-8°. Genérica: dimensiones de la caja son los parámetros variables en r-exams.

---

### PS-13 — Pagos de sueldo, suficiencia de datos

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-13 |
| Nivel | 4 |
| Competencia | Argumentación |
| Componente | Numérico-variacional |
| Grado | 6°-7° |
| Genérico | Sí |
| Score | 3×0.40 + 2×0.30 + 3×0.15 + 2×0.10 + 3×0.05 = 1.20+0.60+0.45+0.20+0.15 = **2.60** |

**Justificación:** Argumentación N4, grado 6°-7°, genérica. Las preguntas de suficiencia de datos son raras en el TEA y atacan directamente el nivel 4 (0% en PCielo). Su tipo de razonamiento (¿qué información falta o sobra?) es exactamente lo que diferencia estudiantes de nivel 3 a 4. Genérica y accesible en grado.

---

### PS-14 — Círculos concéntricos, información faltante

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-14 |
| Nivel | 4 |
| Competencia | Argumentación |
| Componente | Geométrico-métrico |
| Grado | 9°-10° |
| Genérico | Sí |
| Score | 3×0.40 + 2×0.30 + 2×0.15 + 2×0.10 + 1×0.05 = 1.20+0.60+0.30+0.20+0.05 = **2.35** |

**Justificación:** Argumentación N4 en Geometría. Junto con PS-08 (no genérica), es la única pregunta de Argumentación N4 en Geometría. Aunque el grado (9°-10°) reduce levemente su accesibilidad, su carácter genérico y el impacto en N4 la mantienen en banda relevante. Score 2.35 la ubica en Banda Alta (Prioridad 2), clasificada aquí para claridad.

---

### PS-07 — Factorización trinomio cuadrado perfecto

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-07 |
| Nivel | 4 |
| Competencia | Argumentación |
| Componente | Numérico-variacional |
| Grado | 8° |
| Genérico | No |
| Score | 3×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 3×0.05 = 1.20+0.60+0.30+0.10+0.15 = **2.35** |

**Justificación:** Argumentación N4, Álgebra. La factorización algebraica es un contenido de alto nivel que directamente explica la ausencia de estudiantes en N4. No es genérica, pero la estructura de la pregunta puede adaptarse cambiando los coeficientes del trinomio. Prioridad 2 por el grado y la no genericidad.

---

### PS-16 — Error en ecuación lineal

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-16 |
| Nivel | 4 |
| Competencia | Argumentación |
| Componente | Numérico-variacional |
| Grado | 7°-8° |
| Genérico | No |
| Score | 3×0.40 + 2×0.30 + 3×0.15 + 1×0.10 + 3×0.05 = 1.20+0.60+0.45+0.10+0.15 = **2.50** |

**Justificación:** Argumentación N4, grado 7°-8°, Numérico-variacional. Identificar errores en procedimientos es la forma más pura de Argumentación. Aunque no es genérica, el grado accesible y el componente más frecuente la ubican con score 2.50 en la frontera de Banda Crítica/Alta.

---

### PS-08 — Círculos concéntricos, segmento AB

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-08 |
| Nivel | 4 |
| Competencia | Argumentación |
| Componente | Geométrico-métrico |
| Grado | 9°-10° |
| Genérico | Sí |
| Score | 3×0.40 + 2×0.30 + 2×0.15 + 2×0.10 + 1×0.05 = 1.20+0.60+0.30+0.20+0.05 = **2.35** |

**Justificación:** Argumentación N4, Geometría, genérica. Aunque el grado 9°-10° la hace menos inmediata, es una de las pocas preguntas que desarrolla el pensamiento espacial en N4 con posibilidad de parametrización. Prioridad 2 limítrofe.

---

### SS-33 — Combinaciones vs permutaciones

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-33 |
| Nivel | 4 |
| Competencia | Argumentación |
| Componente | Aleatorio |
| Grado | 9° |
| Genérico | No |
| Score | 3×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 2×0.05 = 1.20+0.60+0.30+0.10+0.10 = **2.30** |

**Justificación:** Argumentación N4 en Estadística/Conteo. La distinción entre combinaciones y permutaciones exige Argumentación pura (¿por qué un método y no el otro?). Score en Banda Alta.

---

### SS-35 — Ecuación exponencial

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-35 |
| Nivel | 4 |
| Competencia | Argumentación |
| Componente | Numérico-variacional |
| Grado | 9°-10° |
| Genérico | No |
| Score | 3×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 3×0.05 = 1.20+0.60+0.30+0.10+0.15 = **2.35** |

**Justificación:** Argumentación N4, Álgebra avanzada. Las ecuaciones exponenciales son el contenido que separa N3 de N4 en Álgebra. Aunque el grado 9°-10° la hace de aplicación posterior, su inclusión en r-exams es estratégica para el objetivo de llevar estudiantes a N4.

---

### SS-40 — Área sombreada semicircunferencia (N4)

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-40 |
| Nivel | 4 |
| Competencia | Argumentación |
| Componente | Geométrico-métrico |
| Grado | 9°-10° |
| Genérico | Sí |
| Score | 3×0.40 + 2×0.30 + 2×0.15 + 2×0.10 + 1×0.05 = **2.35** |

**Justificación:** Argumentación N4 en Geometría. Es el equivalente de mayor complejidad a PS-12. Su carácter genérico la hace más atractiva para r-exams que SS-35 o SS-33.

---

### SS-42 — Datos faltantes, probabilidad

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-42 |
| Nivel | 4 |
| Competencia | Argumentación |
| Componente | Aleatorio |
| Grado | 8°-9° |
| Genérico | Sí |
| Score | 3×0.40 + 2×0.30 + 2×0.15 + 2×0.10 + 2×0.05 = 1.20+0.60+0.30+0.20+0.10 = **2.40** |

**Justificación:** Argumentación N4, Estadística, genérica. Completar datos faltantes para que una probabilidad sea válida requiere razonamiento inverso — exactamente la habilidad de Argumentación en N4. Grado 8°-9° es accesible. Score 2.40 la ubica en Banda Alta sólida.

---

### PS-19 — Permutaciones, códigos patinetas

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-19 |
| Nivel | 4 |
| Competencia | Argumentación |
| Componente | Aleatorio |
| Grado | 9°-11° |
| Genérico | No |
| Score | 3×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 2×0.05 = 1.20+0.60+0.30+0.10+0.10 = **2.30** |

**Justificación:** Argumentación N4 en combinatoria. La validación de si un procedimiento de conteo es correcto es Argumentación pura. Grado 9°-11° la hace de aplicación diferida. Score en Banda Alta.

---

### PS-24 — Valor esperado, inversiones

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-24 |
| Nivel | 4 |
| Competencia | Argumentación |
| Componente | Aleatorio |
| Grado | 10°-11° |
| Genérico | No |
| Score | 3×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 2×0.05 = **2.30** |

**Justificación:** Argumentación N4 en Probabilidad avanzada. El valor esperado como criterio de decisión es contenido de excelencia. Aunque el grado 10°-11° la hace de aplicación tardía, su inclusión prepara el banco para el objetivo N4.

---

> **Resumen Banda Crítica (Prioridad 1):** Las preguntas con score ≥ 2.60 pertenecen formalmente a la Banda Crítica. Son: **TEA-PS-04, TEA-PS-10, TEA-PS-18, TEA-PS-21, TEA-SS-38, TEA-SS-39, TEA-SS-43** (todas Argumentación N3, genéricas, grado accesible). Las demás preguntas de Argumentación listadas en esta sección tienen scores entre 2.30 y 2.50 y se clasifican en Banda Alta (Prioridad 2) pero se presentan aquí por cohesión temática.

---

## Sección 4: Banda Alta — Prioridad 2

**Criterio de inclusión:** Formulación y ejecución (C1=2) en Nivel 3 o Nivel 4, o preguntas de Argumentación N4 con restricciones de grado/genericidad que redujeron su score.

### PS-02 — Varianza de características del cabello

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-02 |
| Nivel | 3 |
| Competencia | Formulación y ejecución |
| Componente | Aleatorio |
| Grado | 9°-10° |
| Genérico | No |
| Score | 2×0.40 + 3×0.30 + 2×0.15 + 1×0.10 + 2×0.05 = 0.80+0.90+0.30+0.10+0.10 = **2.20** |

**Justificación:** Formulación N3 en Estadística. La varianza es un indicador clave para mover estudiantes de N2 a N3. Aunque no es genérica, el contexto puede adaptarse cambiando la característica medida.

---

### PS-03 — Calibración de balanzas, error absoluto

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-03 |
| Nivel | 3 |
| Competencia | Formulación y ejecución |
| Componente | Aleatorio |
| Grado | 8°-9° |
| Genérico | No |
| Score | 2×0.40 + 3×0.30 + 2×0.15 + 1×0.10 + 2×0.05 = **2.20** |

**Justificación:** Formulación N3, error absoluto. La formulación correcta del error de medición es una habilidad práctica directamente relacionada con Formulación y ejecución. Contexto modificable para r-exams.

---

### PS-05 — Probabilidad condicional, jaguares

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-05 |
| Nivel | 4 |
| Competencia | Formulación y ejecución |
| Componente | Aleatorio |
| Grado | 11° |
| Genérico | No |
| Score | 2×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 2×0.05 = 0.80+0.60+0.30+0.10+0.10 = **1.90** |

**Justificación:** Formulación N4 pero grado 11° y no genérica reducen el score a 1.90 (Banda Media). Se lista aquí por ser Formulación N4 estratégica para el objetivo de llevar a N4.

---

### PS-06 — Cajas en repisa, optimización

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-06 |
| Nivel | 3 |
| Competencia | Formulación y ejecución |
| Componente | Geométrico-métrico |
| Grado | 6°-7° |
| Genérico | Sí |
| Score | 2×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 1×0.05 = 0.80+0.90+0.45+0.20+0.05 = **2.40** |

**Justificación:** Formulación N3, grado 6°-7°, genérica. La optimización de espacio es un contexto concreto y cotidiano que facilita la formulación del problema. Muy parametrizable: cambiar dimensiones de cajas y repisa.

---

### PS-09 — Error absoluto/relativo, medición

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-09 |
| Nivel | 4 |
| Competencia | Formulación y ejecución |
| Componente | Aleatorio |
| Grado | 10°-11° |
| Genérico | No |
| Score | 2×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 2×0.05 = **1.90** |

**Justificación:** Formulación N4 en medición. Score 1.90 lo ubica en Banda Media, pero su contenido (error relativo) es diferenciador de N4. Se puede incluir en r-exams después de las N3 de Formulación.

---

### PS-15 — Pitágoras, poste y cuerda

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-15 |
| Nivel | 3 |
| Competencia | Formulación y ejecución |
| Componente | Geométrico-métrico |
| Grado | 8° |
| Genérico | No |
| Score | 2×0.40 + 3×0.30 + 2×0.15 + 1×0.10 + 1×0.05 = 0.80+0.90+0.30+0.10+0.05 = **2.15** |

**Justificación:** Formulación N3, Pitágoras. El teorema de Pitágoras en contexto real es un contenido central de 8° con alta frecuencia en pruebas estandarizadas. Aunque no es genérica, el contexto (poste, cuerda, sombra) es fácilmente intercambiable.

---

### PS-22 — Promedio ponderado

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-22 |
| Nivel | 4 |
| Competencia | Formulación y ejecución |
| Componente | Aleatorio |
| Grado | 8°-9° |
| Genérico | Sí |
| Score | 2×0.40 + 2×0.30 + 2×0.15 + 2×0.10 + 2×0.05 = 0.80+0.60+0.30+0.20+0.10 = **2.00** |

**Justificación:** Formulación N4, genérica, grado 8°-9°. El promedio ponderado es un contenido de alta aplicación práctica que diferencia N3 de N4. Su carácter genérico (los pesos y valores son los parámetros) lo hace ideal para r-exams.

---

### PS-23 — Energía semanal, conversión de unidades

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-23 |
| Nivel | 3 |
| Competencia | Formulación y ejecución |
| Componente | Numérico-variacional |
| Grado | 6°-7° |
| Genérico | Sí |
| Score | 2×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 3×0.05 = 0.80+0.90+0.45+0.20+0.15 = **2.50** |

**Justificación:** Formulación N3, grado 6°-7°, genérica, Numérico-variacional (el componente más frecuente). La conversión de unidades en contexto real es una habilidad de Formulación y ejecución fundamental. Muy parametrizable en r-exams.

---

### SS-27 — Permutaciones, clave 2 dígitos

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-27 |
| Nivel | 4 |
| Competencia | Formulación y ejecución |
| Componente | Aleatorio |
| Grado | 8°-9° |
| Genérico | No |
| Score | 2×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 2×0.05 = **1.90** |

**Justificación:** Formulación N4, combinatoria. Ejecutar correctamente el conteo de claves con restricciones es Formulación. Aunque no es genérica, el contexto (candado, PIN) es adaptable.

---

### SS-28 — Trapecio isósceles, perímetro

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-28 |
| Nivel | 3 |
| Competencia | Formulación y ejecución |
| Componente | Geométrico-métrico |
| Grado | 8° |
| Genérico | No |
| Score | 2×0.40 + 3×0.30 + 2×0.15 + 1×0.10 + 1×0.05 = **2.15** |

**Justificación:** Formulación N3, Geometría. El cálculo de perímetros en figuras específicas es Formulación y ejecución directa. Contexto adaptable cambiando las dimensiones del trapecio.

---

### SS-30 — Tabla dosis detergente × 15 días

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-30 |
| Nivel | 3 |
| Competencia | Formulación y ejecución |
| Componente | Numérico-variacional |
| Grado | 6°-7° |
| Genérico | Sí |
| Score | 2×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 3×0.05 = **2.50** |

**Justificación:** Formulación N3, grado 6°-7°, genérica, Numérico-variacional. Las tablas de proporcionalidad son el contenido más frecuente de Formulación en primeros grados. Altamente parametrizable: cambiar el producto, la dosis y los días.

---

### SS-32 — Prorrateo factura de agua

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-32 |
| Nivel | 3 |
| Competencia | Formulación y ejecución |
| Componente | Numérico-variacional |
| Grado | 7° |
| Genérico | Sí |
| Score | 2×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 3×0.05 = **2.50** |

**Justificación:** Formulación N3, 7°, genérica. El prorrateo (distribución proporcional) es un contenido de alta aplicación cotidiana. En r-exams: cambiar el servicio, el monto total y el número de participantes.

---

### SS-34 — Perímetro en plano cartesiano

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-34 |
| Nivel | 3 |
| Competencia | Formulación y ejecución |
| Componente | Geométrico-métrico |
| Grado | 8° |
| Genérico | No |
| Score | 2×0.40 + 3×0.30 + 2×0.15 + 1×0.10 + 1×0.05 = **2.15** |

**Justificación:** Formulación N3, Geometría analítica. Calcular perímetros usando coordenadas articula Geometría con Álgebra. Adaptable cambiando las coordenadas de los vértices.

---

### SS-36 — Rango medio de temperaturas

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-36 |
| Nivel | 3 |
| Competencia | Formulación y ejecución |
| Componente | Aleatorio |
| Grado | 6°-7° |
| Genérico | Sí |
| Score | 2×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 2×0.05 = 0.80+0.90+0.45+0.20+0.10 = **2.45** |

**Justificación:** Formulación N3, grado 6°-7°, genérica. Calcular el rango (max - min) y el valor medio es una habilidad de Formulación básica en Estadística. Muy parametrizable: cambiar los datos de temperatura.

---

### SS-37 — Área de paralelogramo

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-37 |
| Nivel | 3 |
| Competencia | Formulación y ejecución |
| Componente | Geométrico-métrico |
| Grado | 7°-8° |
| Genérico | Sí |
| Score | 2×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 1×0.05 = 0.80+0.90+0.45+0.20+0.05 = **2.40** |

**Justificación:** Formulación N3, grado 7°-8°, genérica. El área de paralelogramo es un contenido curricular central. Parametrizable con distintas bases y alturas.

---

### SS-41 — 20% de la mitad, plátano

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-41 |
| Nivel | 4 |
| Competencia | Formulación y ejecución |
| Componente | Numérico-variacional |
| Grado | 7°-8° |
| Genérico | Sí |
| Score | 2×0.40 + 2×0.30 + 3×0.15 + 2×0.10 + 3×0.05 = 0.80+0.60+0.45+0.20+0.15 = **2.20** |

**Justificación:** Formulación N4, grado 7°-8°, genérica, Numérico-variacional. Las operaciones combinadas con porcentajes y fracciones son contenido de N4 accesible. Muy parametrizable: cambiar el porcentaje, la fracción y el producto.

---

### SS-44 — Rollos de césped para jardín

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-44 |
| Nivel | 3 |
| Competencia | Formulación y ejecución |
| Componente | Geométrico-métrico |
| Grado | 6°-7° |
| Genérico | Sí |
| Score | 2×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 1×0.05 = 0.80+0.90+0.45+0.20+0.05 = **2.40** |

**Justificación:** Formulación N3, grado 6°-7°, genérica. Calcular cuántos rollos se necesitan para cubrir un área es un problema de Formulación y ejecución directo. Parametrizable con distintas dimensiones de jardín y rollo.

---

## Sección 5: Banda Media — Prioridad 3

**Criterio de inclusión:** Preguntas de Interpretación y representación (C1=1), más las preguntas de Formulación N4 con grado avanzado y no genéricas que quedaron con score < 2.00.

### PS-11 — Notas del curso + 0.5, distribución

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-11 |
| Nivel | 3 |
| Competencia | Interpretación y repr. |
| Componente | Aleatorio |
| Grado | 7°-8° |
| Genérico | Sí |
| Score | 1×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 2×0.05 = 0.40+0.90+0.45+0.20+0.10 = **2.05** |

**Justificación:** Interpretación N3 en Estadística. Interpretar cómo cambia una distribución al sumar una constante es un contenido de N3 accesible. Genérica: el ajuste y los datos son parametrizables.

---

### PS-17 — Lectura de gráfica de temperaturas

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-17 |
| Nivel | 1 |
| Competencia | Interpretación y repr. |
| Componente | Aleatorio |
| Grado | 4°-5° |
| Genérico | Sí |
| Score | 1×0.40 + 1×0.30 + 3×0.15 + 2×0.10 + 2×0.05 = 0.40+0.30+0.45+0.20+0.10 = **1.45** |

**Justificación:** La única pregunta de Nivel 1 del TEA. Aunque es la más básica de Interpretación, puede servir como pregunta de calentamiento o diagnóstico inicial en r-exams. Su genericidad y grado 4°-5° la hacen útil para identificar estudiantes en el nivel más bajo.

---

### PS-20 — Tabla → función lineal

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-20 |
| Nivel | 4 |
| Competencia | Interpretación y repr. |
| Componente | Numérico-variacional |
| Grado | 8°-9° |
| Genérico | No |
| Score | 1×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 3×0.05 = 0.40+0.60+0.30+0.10+0.15 = **1.55** |

**Justificación:** Interpretación N4 en Álgebra. Aunque el nivel es 4, la competencia (Interpretación) y la no genericidad reducen el score. Es útil para el banco de r-exams una vez cubiertos los niveles críticos.

---

### PS-25 — Expresión algebraica, ventas

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-25 |
| Nivel | 4 |
| Competencia | Interpretación y repr. |
| Componente | Numérico-variacional |
| Grado | 8°-9° |
| Genérico | No |
| Score | 1×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 3×0.05 = **1.55** |

**Justificación:** Interpretación N4, Álgebra. Interpretar una expresión algebraica en contexto de ventas es contenido relevante para N4. Prioridad 3 por competencia y no genericidad.

---

### SS-26 — Tabla → función lineal

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-26 |
| Nivel | 4 |
| Competencia | Interpretación y repr. |
| Componente | Numérico-variacional |
| Grado | 9° |
| Genérico | No |
| Score | 1×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 3×0.05 = **1.55** |

**Justificación:** Interpretación N4, similar a PS-20 pero en 9°. Junto con PS-20 forman un par temático ideal para r-exams de funciones lineales con distintos contextos.

---

### SS-29 — Función cuadrática, raíces

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-29 |
| Nivel | 4 |
| Competencia | Interpretación y repr. |
| Componente | Numérico-variacional |
| Grado | 9°-10° |
| Genérico | No |
| Score | 1×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 3×0.05 = **1.55** |

**Justificación:** Interpretación N4 en funciones cuadráticas. Las raíces como representación gráfica son contenido de N4. Prioridad 3 por competencia, pero importante para completar el banco de Álgebra avanzada.

---

### SS-31 — Gráfica precio moneda, rango

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-31 |
| Nivel | 3 |
| Competencia | Interpretación y repr. |
| Componente | Aleatorio |
| Grado | 6°-7° |
| Genérico | Sí |
| Score | 1×0.40 + 3×0.30 + 3×0.15 + 2×0.10 + 2×0.05 = **2.05** |

**Justificación:** Interpretación N3, grado 6°-7°, genérica. La lectura e interpretación de gráficas de precios es contenido básico de N3 en Estadística. A pesar de ser Interpretación, el grado y la genericidad elevan el score a 2.05 (frontera Banda Alta/Media).

---

### SS-45 — Temperatura vs reacción, tendencia

| Campo | Valor |
|-------|-------|
| Ref | TEA-SS-45 |
| Nivel | 3 |
| Competencia | Interpretación y repr. |
| Componente | Numérico-variacional |
| Grado | 8°-9° |
| Genérico | Sí |
| Score | 1×0.40 + 3×0.30 + 2×0.15 + 2×0.10 + 3×0.05 = 0.40+0.90+0.30+0.20+0.15 = **1.95** |

**Justificación:** Interpretación N3, genérica, Numérico-variacional. La interpretación de tendencias en gráficas bivariadas es contenido de N3 relevante. Parametrizable con distintas variables.

---

### PS-01 — Función creciente, gasolina vs km

| Campo | Valor |
|-------|-------|
| Ref | TEA-PS-01 |
| Nivel | 4 |
| Competencia | Argumentación |
| Componente | Numérico-variacional |
| Grado | 10°-11° |
| Genérico | No |
| Score | 3×0.40 + 2×0.30 + 2×0.15 + 1×0.10 + 3×0.05 = 1.20+0.60+0.30+0.10+0.15 = **2.35** |

**Nota:** Esta pregunta de Argumentación N4 tiene score 2.35 (Banda Alta), pero el grado 10°-11° y la no genericidad la hacen de conversión diferida. Se incluye en Prioridad 2.

---

## Sección 6: Tabla Maestra Consolidada

Las 45 preguntas ordenadas por prioridad y score decreciente.

| Prioridad | Ref | Score | Nivel | Competencia | Componente | Grado | Genérico | Descripción |
|-----------|-----|-------|-------|-------------|------------|-------|----------|-------------|
| **1** | TEA-PS-04 | 2.90 | 3 | Argumentación | Numérico-variacional | 6°-7° | Sí | Fracciones y decimales, vueltas a pista |
| **1** | TEA-PS-10 | 2.90 | 3 | Argumentación | Numérico-variacional | 7° | Sí | Transacciones bancarias 3/8 de 12000 |
| **1** | TEA-SS-39 | 2.90 | 3 | Argumentación | Numérico-variacional | 7° | Sí | Porcentaje inverso, descuento |
| **1** | TEA-SS-38 | 2.85 | 3 | Argumentación | Aleatorio | 6°-7° | Sí | Diagrama de Venn 3 servicios |
| **1** | TEA-PS-18 | 2.80 | 3 | Argumentación | Geométrico-métrico | 6°-7° | Sí | Ángulos de radios en rueda |
| **1** | TEA-PS-21 | 2.80 | 3 | Argumentación | Geométrico-métrico | 7°-8° | Sí | Desigualdad triangular |
| **1** | TEA-SS-43 | 2.80 | 3 | Argumentación | Geométrico-métrico | 7°-8° | Sí | Área superficial de caja |
| **1** | TEA-PS-12 | 2.65 | 3 | Argumentación | Geométrico-métrico | 8°-9° | Sí | Área sombreada semicircunferencia |
| **2** | TEA-PS-16 | 2.50 | 4 | Argumentación | Numérico-variacional | 7°-8° | No | Error en ecuación lineal |
| **2** | TEA-PS-23 | 2.50 | 3 | Formulación y ejecución | Numérico-variacional | 6°-7° | Sí | Energía semanal, conversión unidades |
| **2** | TEA-SS-30 | 2.50 | 3 | Formulación y ejecución | Numérico-variacional | 6°-7° | Sí | Tabla dosis detergente × 15 días |
| **2** | TEA-SS-32 | 2.50 | 3 | Formulación y ejecución | Numérico-variacional | 7° | Sí | Prorrateo factura de agua |
| **2** | TEA-SS-36 | 2.45 | 3 | Formulación y ejecución | Aleatorio | 6°-7° | Sí | Rango medio de temperaturas |
| **2** | TEA-PS-06 | 2.40 | 3 | Formulación y ejecución | Geométrico-métrico | 6°-7° | Sí | Cajas en repisa, optimización |
| **2** | TEA-SS-37 | 2.40 | 3 | Formulación y ejecución | Geométrico-métrico | 7°-8° | Sí | Área de paralelogramo |
| **2** | TEA-SS-44 | 2.40 | 3 | Formulación y ejecución | Geométrico-métrico | 6°-7° | Sí | Rollos de césped para jardín |
| **2** | TEA-SS-42 | 2.40 | 4 | Argumentación | Aleatorio | 8°-9° | Sí | Datos faltantes, probabilidad |
| **2** | TEA-PS-13 | 2.60 | 4 | Argumentación | Numérico-variacional | 6°-7° | Sí | Pagos de sueldo, suficiencia de datos |
| **2** | TEA-PS-07 | 2.35 | 4 | Argumentación | Numérico-variacional | 8° | No | Factorización trinomio cuadrado perfecto |
| **2** | TEA-PS-08 | 2.35 | 4 | Argumentación | Geométrico-métrico | 9°-10° | Sí | Círculos concéntricos, segmento AB |
| **2** | TEA-PS-14 | 2.35 | 4 | Argumentación | Geométrico-métrico | 9°-10° | Sí | Círculos concéntricos, info faltante |
| **2** | TEA-SS-35 | 2.35 | 4 | Argumentación | Numérico-variacional | 9°-10° | No | Ecuación exponencial |
| **2** | TEA-SS-40 | 2.35 | 4 | Argumentación | Geométrico-métrico | 9°-10° | Sí | Área sombreada semicircunferencia (N4) |
| **2** | TEA-SS-33 | 2.30 | 4 | Argumentación | Aleatorio | 9° | No | Combinaciones vs permutaciones |
| **2** | TEA-PS-19 | 2.30 | 4 | Argumentación | Aleatorio | 9°-11° | No | Permutaciones, códigos patinetas |
| **2** | TEA-PS-24 | 2.30 | 4 | Argumentación | Aleatorio | 10°-11° | No | Valor esperado, inversiones |
| **2** | TEA-PS-01 | 2.35 | 4 | Argumentación | Numérico-variacional | 10°-11° | No | Función creciente, gasolina vs km |
| **2** | TEA-PS-22 | 2.00 | 4 | Formulación y ejecución | Aleatorio | 8°-9° | Sí | Promedio ponderado |
| **2** | TEA-SS-41 | 2.20 | 4 | Formulación y ejecución | Numérico-variacional | 7°-8° | Sí | 20% de la mitad, plátano |
| **2** | TEA-PS-02 | 2.20 | 3 | Formulación y ejecución | Aleatorio | 9°-10° | No | Varianza de características del cabello |
| **2** | TEA-PS-03 | 2.20 | 3 | Formulación y ejecución | Aleatorio | 8°-9° | No | Calibración de balanzas, error absoluto |
| **2** | TEA-PS-15 | 2.15 | 3 | Formulación y ejecución | Geométrico-métrico | 8° | No | Pitágoras, poste y cuerda |
| **2** | TEA-SS-28 | 2.15 | 3 | Formulación y ejecución | Geométrico-métrico | 8° | No | Trapecio isósceles, perímetro |
| **2** | TEA-SS-34 | 2.15 | 3 | Formulación y ejecución | Geométrico-métrico | 8° | No | Perímetro en plano cartesiano |
| **2** | TEA-SS-27 | 1.90 | 4 | Formulación y ejecución | Aleatorio | 8°-9° | No | Permutaciones, clave 2 dígitos |
| **2** | TEA-PS-09 | 1.90 | 4 | Formulación y ejecución | Aleatorio | 10°-11° | No | Error absoluto/relativo → medición |
| **2** | TEA-PS-05 | 1.90 | 4 | Formulación y ejecución | Aleatorio | 11° | No | Probabilidad condicional, jaguares |
| **3** | TEA-SS-11 | 2.05 | 3 | Interpretación y repr. | Aleatorio | 7°-8° | Sí | Notas del curso + 0.5, distribución |
| **3** | TEA-SS-31 | 2.05 | 3 | Interpretación y repr. | Aleatorio | 6°-7° | Sí | Gráfica precio moneda, rango |
| **3** | TEA-SS-45 | 1.95 | 3 | Interpretación y repr. | Numérico-variacional | 8°-9° | Sí | Temperatura vs reacción, tendencia |
| **3** | TEA-PS-20 | 1.55 | 4 | Interpretación y repr. | Numérico-variacional | 8°-9° | No | Tabla → función lineal |
| **3** | TEA-PS-25 | 1.55 | 4 | Interpretación y repr. | Numérico-variacional | 8°-9° | No | Expresión algebraica, ventas |
| **3** | TEA-SS-26 | 1.55 | 4 | Interpretación y repr. | Numérico-variacional | 9° | No | Tabla → función lineal |
| **3** | TEA-SS-29 | 1.55 | 4 | Interpretación y repr. | Numérico-variacional | 9°-10° | No | Función cuadrática, raíces |
| **3** | TEA-PS-17 | 1.45 | 1 | Interpretación y repr. | Aleatorio | 4°-5° | Sí | Lectura de gráfica de temperaturas |

> **Nota sobre TEA-PS-11:** La referencia TEA-PS-11 y TEA-SS-11 corresponden a la misma pregunta con numeración de sesión. Se mantiene la referencia original PS-11 en la tabla de detalle y SS-11 refleja la notación interna del índice.

---

## Sección 7: Recomendaciones de Implementación

### 7.1 Orden Sugerido de Conversión a R-Exams

**Fase 1 — Semanas 1-4: Banda Crítica (8 preguntas, máximo impacto)**

Convertir primero las preguntas de Argumentación N3 genéricas en grados 6°-8°. Este grupo ataca directamente el 66% de errores en Argumentación y el déficit del nivel 3.

| Orden | Ref | Razón de secuencia |
|-------|-----|--------------------|
| 1 | TEA-SS-39 | Porcentaje inverso — el error más frecuente en Argumentación |
| 2 | TEA-PS-04 | Fracciones — base para múltiples contenidos posteriores |
| 3 | TEA-PS-10 | Fracciones en contexto financiero — mayor relevancia cotidiana |
| 4 | TEA-SS-38 | Venn 3 conjuntos — cierra la brecha en razonamiento lógico |
| 5 | TEA-PS-18 | Ángulos en círculo — Geometría accesible N3 |
| 6 | TEA-PS-21 | Desigualdad triangular — validación de procedimiento |
| 7 | TEA-SS-43 | Área superficial — Geometría 3D N3 |
| 8 | TEA-PS-12 | Área sombreada — figuras compuestas N3 |

**Fase 2 — Semanas 5-10: Banda Alta (29 preguntas)**

Priorizar dentro de la Banda Alta: primero las genéricas de Formulación N3 en grados bajos, luego las de Argumentación N4.

Sub-orden sugerido dentro de Fase 2:
1. Formulación N3 genéricas grado 6°-7°: SS-30, SS-32, PS-23, SS-36, PS-06, SS-44
2. Formulación N3 genéricas grado 7°-8°: SS-37, SS-41
3. Argumentación N4 genéricas accesibles: PS-13, SS-42, PS-16
4. Formulación N3 no genéricas grado 8°: PS-15, SS-28, SS-34
5. Argumentación N4 grado 8°-10°: PS-07, PS-08, PS-14, SS-35, SS-40
6. Formulación N4 estadística: PS-22, SS-27, PS-02, PS-03
7. Argumentación N4 grado alto: SS-33, PS-19, PS-24, PS-01
8. Formulación N4 grado alto: PS-09, PS-05

**Fase 3 — Semanas 11-13: Banda Media (8 preguntas)**

Interpretación y representación. Estas preguntas complementan el banco pero no son el foco del déficit.

Sub-orden: PS-11 → SS-31 → SS-45 → PS-20 → PS-25 → SS-26 → SS-29 → PS-17

### 7.2 Estrategia de Parametrización en R-Exams

**Preguntas Genéricas (26 de 45 — 58%):** Son el núcleo del banco parametrizable. Para cada una, definir:
- `params$valor1`, `params$valor2` para los datos numéricos del enunciado
- `params$contexto` para variar el escenario sin cambiar la estructura matemática
- Al menos 5 semillas diferentes por pregunta para garantizar variedad en aplicaciones

**Preguntas No Genéricas (19 de 45 — 42%):** Requieren adaptación manual del enunciado. Estrategia:
- Mantener la estructura matemática fija
- Cambiar solo los valores numéricos (coeficientes, medidas, cantidades)
- Documentar claramente los invariantes del problema (qué no puede cambiar sin alterar el tipo de pregunta)

**Pares temáticos identificados para r-exams:**
- PS-20 y SS-26: Función lineal desde tabla (diferente grado, mismo contenido)
- PS-12 y SS-40: Área sombreada semicircunferencia (N3 y N4)
- PS-08 y PS-14: Círculos concéntricos (segmento vs información faltante)
- PS-02 y PS-03: Error estadístico (varianza vs error absoluto)
- PS-19 y SS-27: Conteo con permutaciones (diferente contexto)

### 7.3 Cobertura de Componentes

| Componente | Total TEA | Fase 1 | Fase 2 | Fase 3 | % Cobertura meta |
|------------|-----------|--------|--------|--------|-----------------|
| Numérico-variacional | 18 | 3 | 11 | 4 | 100% |
| Aleatorio | 15 | 1 | 11 | 3 | 100% |
| Geométrico-métrico | 12 | 4 | 7 | 1 | 100% |
| **Total** | **45** | **8** | **29** | **8** | **100%** |

### 7.4 Meta de Implementación

| Meta | Indicador | Plazo sugerido |
|------|-----------|----------------|
| Banco inicial funcional | 8 preguntas Fase 1 en producción | Semana 4 |
| Banco intermedio | 37 preguntas (Fase 1 + 2) | Semana 10 |
| Banco completo | 45 preguntas | Semana 13 |
| Validación pedagógica | Aplicación piloto con grupo de estudiantes | Semana 8 |
| Revisión de efectividad | Comparar pre-test vs post-test en Argumentación | Semana 14 |

---

## Sección 8: Resumen Estadístico de la Priorización

### 8.1 Distribución por Banda

| Banda | Prioridad | Cantidad de preguntas | % del total |
|-------|-----------|----------------------|-------------|
| Crítica | 1 | 8 | 17.8% |
| Alta | 2 | 29 | 64.4% |
| Media | 3 | 8 | 17.8% |
| **Total** | | **45** | **100%** |

### 8.2 Distribución por Competencia en cada Banda

| Competencia | Banda 1 (Crítica) | Banda 2 (Alta) | Banda 3 (Media) | Total |
|-------------|-------------------|----------------|-----------------|-------|
| Argumentación | 8 | 19 | 0 | **27** |
| Formulación y ejecución | 0 | 10 | 0 | **10** |
| Interpretación y repr. | 0 | 0 | 8 | **8** |
| **Total** | **8** | **29** | **8** | **45** |

> Las preguntas de Argumentación dominan las bandas de mayor prioridad, consistente con el diagnóstico: 66% de errores y tendencia al empeoramiento.

### 8.3 Distribución por Componente en cada Banda

| Componente | Banda 1 (Crítica) | Banda 2 (Alta) | Banda 3 (Media) | Total |
|------------|-------------------|----------------|-----------------|-------|
| Numérico-variacional | 3 | 11 | 4 | **18** |
| Aleatorio | 1 | 11 | 3 | **15** |
| Geométrico-métrico | 4 | 7 | 1 | **12** |
| **Total** | **8** | **29** | **8** | **45** |

### 8.4 Distribución por Nivel en cada Banda

| Nivel | Banda 1 (Crítica) | Banda 2 (Alta) | Banda 3 (Media) | Total |
|-------|-------------------|----------------|-----------------|-------|
| Nivel 1 | 0 | 0 | 1 | **1** |
| Nivel 3 | 8 | 14 | 3 | **25** |
| Nivel 4 | 0 | 15 | 4 | **19** |
| **Total** | **8** | **29** | **8** | **45** |

> La priorización concentra el N3 en la Banda Crítica (el nivel que más impacta el indicador del 35% vs 53% ETC) y distribuye el N4 en la Banda Alta para preparar el camino hacia la excelencia.

### 8.5 Distribución Genérico/No Genérico por Banda

| Tipo | Banda 1 (Crítica) | Banda 2 (Alta) | Banda 3 (Media) | Total |
|------|-------------------|----------------|-----------------|-------|
| Genérico (Sí) | 8 (100%) | 14 (48%) | 4 (50%) | **26** |
| No Genérico (No) | 0 (0%) | 15 (52%) | 4 (50%) | **19** |

> La Banda Crítica está compuesta **exclusivamente** por preguntas genéricas, lo que maximiza la eficiencia de desarrollo: estas 8 preguntas generarán el banco de mayor impacto con el menor esfuerzo de programación en r-exams.

---

*Documento generado el 4 de marzo de 2026. Fuente de datos: Resultados ICFES PCielo 2025 — fuentes-de-la-verdad. Instrumento: TEA Matemáticas S1-S2 (45 preguntas).*
