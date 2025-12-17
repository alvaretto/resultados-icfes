# 🔧 ANÁLISIS TÉCNICO DETALLADO

## FASE 1: EXTRACCIÓN DE PDFs

### Archivo: `12-descargar_resultados_icfes.py`

#### Clase: `DescargadorICFES`

**Métodos Principales:**

1. `__init__(modo_headless=False)`
   - Inicializa el descargador
   - Prepara listas para tracking de resultados

2. `iniciar_navegador()`
   - Configura Firefox con opciones de descarga automática
   - Configura carpeta de descargas: `pdfs_descargados/`
   - Deshabilita visor PDF integrado
   - Configura descarga automática sin preguntar

3. `leer_excel()`
   - Lee `INSCRITOS_EXAMEN SABER 11 (36).xls`
   - Salta primeras 3 filas de encabezado
   - Retorna DataFrame con 36 estudiantes

4. `descargar_pdf_estudiante(estudiante)`
   - Navega a URL del ICFES
   - Ingresa datos del estudiante
   - Maneja CAPTCHA (requiere intervención manual)
   - Descarga PDF automáticamente
   - Renombra PDF según patrón: `APELLIDO_APELLIDO_NOMBRE_NOMBRE_DOCUMENTO.pdf`

5. `procesar_estudiantes()`
   - Loop principal que procesa todos los estudiantes
   - Manejo de errores y excepciones
   - Logging de resultados

#### Configuración
```python
EXCEL_PATH = '/home/proyectos/Escritorio/Resultados-ICFES-2025/INSCRITOS_EXAMEN SABER 11 (36).xls'
URL_ICFES = 'http://resultadossaber11.icfes.edu.co/'
CARPETA_PDFS = 'pdfs_descargados'
CARPETA_LOGS = 'logs'
DELAY_ENTRE_ESTUDIANTES = 3  # segundos
```

#### Resultado
- ✅ 36 PDFs descargados
- ✅ Logs en `logs/exitosos_*.txt`
- ✅ Errores en `logs/errores_*.txt`

#### Limitaciones
- ⚠️ Requiere intervención manual para CAPTCHA
- ⚠️ Tiempo: ~35 segundos por estudiante
- ⚠️ Requiere supervisión durante ejecución

---

## FASE 2: PROCESAMIENTO DE PDFs

### Archivo: `extraer_puntajes_de_pdfs.py`

#### Problema Identificado

**Flujo Actual:**
```
PDF (imagen escaneada)
    ↓
pdf2image: Convierte a imagen
    ↓
pytesseract: Aplica OCR
    ↓
Regex: Parsea números
    ↓
❌ FALLA: Números incorrectos o incompletos
```

**Razón de Falla:**
- PDFs son imágenes de baja calidad
- OCR no extrae correctamente números
- Regex no puede parsear texto corrupto

#### Funciones Principales

1. `extraer_texto_pdf(pdf_path)`
   - Convierte PDF a imagen (DPI 300)
   - Aplica OCR con pytesseract
   - Retorna texto extraído

2. `extraer_puntajes(texto)`
   - Busca patrón: `XXX/500` para puntaje global
   - Busca línea con nombres de áreas
   - Busca números en líneas siguientes
   - Intenta parsear números con múltiples formatos
   - ❌ FALLA: Números incorrectos

3. `procesar_pdf(pdf_path, nombre_estudiante)`
   - Extrae texto
   - Extrae puntajes
   - Valida resultados
   - Guarda debug si falla

4. `construir_nombre_pdf(estudiante)`
   - Construye nombre esperado del PDF
   - Formato: `APELLIDO_APELLIDO_NOMBRE_NOMBRE_DOCUMENTO.pdf`

5. `main()`
   - Lee Excel de entrada
   - Modo prueba (1 estudiante) o completo (36)
   - Procesa cada PDF
   - Genera Excel de salida

#### Configuración
```python
ARCHIVO_EXCEL_ENTRADA = 'INSCRITOS_EXAMEN SABER 11 (36).xls'
ARCHIVO_EXCEL_SALIDA = 'RESULTADOS-ICFES-AULA-REGULAR.xlsx'
CARPETA_PDFS = 'pdfs_descargados'
CARPETA_LOGS = 'logs'
```

#### Salida Esperada
```
RESULTADOS-ICFES-AULA-REGULAR.xlsx
Columnas: Primer Apellido, Segundo Apellido, Primer Nombre, Segundo Nombre,
          Tipo documento, Número de documento,
          Lectura Crítica, Matemáticas, Sociales y Ciudadanas,
          Ciencias Naturales, Inglés, Puntaje Global
```

#### Estado
- ❌ NO FUNCIONA
- ❌ NO GENERA ARCHIVO

---

## FASE 3: APLICACIÓN STREAMLIT

### Archivo: `app_resultados_icfes.py`

#### Configuración
```python
ARCHIVO_AULA_REGULAR = 'PCIELO-RESULTADOS-ICFES-MODELO-AULA-REGULAR-2025.xlsx'
ARCHIVO_MODELO_FLEXIBLE = 'PCIELO-RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx'
AREAS = ['Lectura Crítica', 'Matemáticas', 'Sociales y Ciudadanas',
         'Ciencias Naturales', 'Inglés']
```

#### Funciones Clave

1. `cargar_datos_unificados()`
   - Carga ambos archivos Excel
   - Unifica en un DataFrame
   - Agrega columna 'Modelo'
   - Filtra solo estudiantes (excluye estadísticas)

2. `cargar_datos_historicos()`
   - Carga datos 2024-2025
   - Extrae filas 37-39 (estadísticas)
   - Retorna datos históricos por modelo

3. Funciones de Visualización
   - `mostrar_vista_general()`
   - `mostrar_por_estudiante()`
   - `mostrar_por_area()`
   - `mostrar_rankings()`
   - `mostrar_segmentacion()`
   - `mostrar_comparacion_modelos()`
   - `mostrar_comparacion_temporal()`
   - `mostrar_resultados_institucionales()`

#### Pestañas
1. 🏫 Resultados Institucionales
2. 📊 Vista General
3. 🔄 Comparación entre Modelos
4. 👤 Por Estudiante
5. 📚 Por Área
6. 🏆 Rankings
7. 📈 Segmentación
8. 📅 Comparación Temporal

#### Estado
- ✅ FUNCIONA CORRECTAMENTE
- ✅ PUBLICADA EN STREAMLIT CLOUD

---

## 📊 ESTRUCTURA DE DATOS

### Entrada (Fase 1)
```
INSCRITOS_EXAMEN SABER 11 (36).xls
Columnas: Primer Apellido, Segundo Apellido, Primer Nombre, Segundo Nombre,
          Tipo documento, Número de documento
Filas: 36 estudiantes
```

### Salida Esperada (Fase 2)
```
RESULTADOS-ICFES-AULA-REGULAR.xlsx
Columnas: Primer Apellido, Segundo Apellido, Primer Nombre, Segundo Nombre,
          Tipo documento, Número de documento,
          Lectura Crítica, Matemáticas, Sociales y Ciudadanas,
          Ciencias Naturales, Inglés, Puntaje Global
Filas: 36 estudiantes + 4 filas de estadísticas
```

### Entrada (Fase 3)
```
PCIELO-RESULTADOS-ICFES-MODELO-AULA-REGULAR-2025.xlsx
PCIELO-RESULTADOS-ICFES-MODELO-FLEXIBLE-2025.xlsx
(Generados manualmente actualmente)
```

---

## 🔗 DEPENDENCIAS

### Fase 1
- selenium
- pandas
- webdriver-manager
- Firefox

### Fase 2
- pandas
- pdf2image
- pytesseract
- Tesseract OCR (sistema)
- poppler-utils (sistema)

### Fase 3
- streamlit
- pandas
- plotly
- numpy
- scipy
- openpyxl


---

**Última actualización:** 2025-10-23  
**Versión:** 2.0  
**Estado:** ✅ Funcional
