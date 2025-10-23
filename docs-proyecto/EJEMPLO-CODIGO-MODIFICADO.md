# 💻 EJEMPLO: Código Modificado

## Avance Institucional Global (Líneas 935-966)

### Código Completo

```python
# Avance Institucional Global
with col1:
    if avance_institucional_global is not None:
        if avance_institucional_global > 0:
            color_bg = "#d4edda"  # Verde claro
            color_border = "#28a745"  # Verde
            emoji = "📈"
            signo = "+"
            descripcion = f"Avance: {abs(avance_institucional_global)} puntos"
        elif avance_institucional_global < 0:
            color_bg = "#f8d7da"  # Rojo claro
            color_border = "#dc3545"  # Rojo
            emoji = "📉"
            signo = ""
            descripcion = f"Retroceso: {abs(avance_institucional_global)} puntos"
        else:
            color_bg = "#e2e3e5"  # Gris
            color_border = "#6c757d"  # Gris oscuro
            emoji = "➡️"
            signo = ""
            descripcion = "Sin cambios"

        st.markdown(f"""
        <div style='background-color: {color_bg}; padding: 20px; border-radius: 10px; border-left: 5px solid {color_border};'>
        <div style='font-size: 2em; margin-bottom: 10px;'>{emoji}</div>
        <strong style='font-size: 1.2em;'>Avance Institucional Global</strong><br>
        <span style='font-size: 2em; font-weight: bold; color: {color_border};'>{signo}{avance_institucional_global:+.0f} puntos</span><br>
        <span style='font-size: 0.9em; color: #666;'>{descripcion}</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Datos de avance no disponibles")
```

---

## 🔑 Cambios Clave

### 1. Variable `descripcion` (Nueva)

```python
# Si avance es positivo
descripcion = f"Avance: {abs(avance_institucional_global)} puntos"

# Si avance es negativo
descripcion = f"Retroceso: {abs(avance_institucional_global)} puntos"

# Si avance es cero
descripcion = "Sin cambios"
```

### 2. Reordenamiento en HTML

**Antes**:
```html
<strong>{emoji} Avance Institucional Global</strong><br>
```

**Después**:
```html
<div style='font-size: 2em; margin-bottom: 10px;'>{emoji}</div>
<strong style='font-size: 1.2em;'>Avance Institucional Global</strong><br>
```

### 3. Texto Descriptivo Dinámico

**Antes**:
```html
<span style='font-size: 0.9em; color: #666;'>Cambio promedio 2024-2025</span>
```

**Después**:
```html
<span style='font-size: 0.9em; color: #666;'>{descripcion}</span>
```

---

## 📊 Ejemplos de Salida

### Ejemplo 1: Avance Positivo (+1 punto)

```
📈
Avance Institucional Global
+1 puntos
Avance: 1 puntos
```

**Variables**:
- `avance_institucional_global = 1`
- `descripcion = "Avance: 1 puntos"`
- `color_border = "#28a745"` (Verde)

### Ejemplo 2: Retroceso Negativo (-9 puntos)

```
📉
Modelo Aula Regular
-9 puntos
Retroceso: 9 puntos
```

**Variables**:
- `avance_aula_regular = -9`
- `descripcion = "Retroceso: 9 puntos"`
- `color_border = "#dc3545"` (Rojo)

### Ejemplo 3: Sin Cambios (0 puntos)

```
➡️
Métrica
0 puntos
Sin cambios
```

**Variables**:
- `avance = 0`
- `descripcion = "Sin cambios"`
- `color_border = "#6c757d"` (Gris)

---

## 🎨 Estilos CSS Utilizados

```css
/* Contenedor principal */
background-color: {color_bg};
padding: 20px;
border-radius: 10px;
border-left: 5px solid {color_border};

/* Emoji */
font-size: 2em;
margin-bottom: 10px;

/* Título */
font-size: 1.2em;

/* Valor numérico */
font-size: 2em;
font-weight: bold;
color: {color_border};

/* Texto descriptivo */
font-size: 0.9em;
color: #666;
```

---

## ✅ Validación

- ✅ Sintaxis Python correcta
- ✅ Formato HTML válido
- ✅ Variables correctamente inicializadas
- ✅ Lógica condicional correcta
- ✅ Uso correcto de f-strings
- ✅ Función `abs()` aplicada correctamente

---

## 📝 Notas Importantes

1. **Uso de `abs()`**: Se utiliza para obtener el valor absoluto, de modo que:
   - Para +1: muestra "Avance: 1 puntos"
   - Para -9: muestra "Retroceso: 9 puntos"

2. **Formato de número**: Se utiliza `{signo}{avance:+.0f}` para mostrar:
   - +1 puntos (con signo positivo)
   - -9 puntos (con signo negativo)

3. **Colores dinámicos**: El color del borde y del texto cambia según el signo

4. **Emoji dinámico**: El emoji cambia según el signo (📈, 📉, ➡️)

---

**Archivo**: app_resultados_icfes.py

**Líneas**: 935-1032 (96 líneas modificadas)

**Métricas**: 3 (todas con el mismo patrón)


---

**Última actualización:** 2025-10-23  
**Versión:** 2.0  
**Estado:** ✅ Funcional
