# 🚀 Inicio Rápido - Aplicación Comparativa ICFES

## ⚡ Inicio en 3 Pasos

### 1️⃣ Abre una terminal

```bash
cd /home/proyectos/Escritorio/Resultados-ICFES-2025
```

### 2️⃣ Ejecuta el script de inicio

```bash
./iniciar_aplicacion.sh
```

### 3️⃣ ¡Listo! 🎉

La aplicación se abrirá automáticamente en tu navegador en:
- **Local:** http://localhost:8501
- **Red:** http://192.168.10.13:8501

---

## 🔧 Inicio Manual (Alternativa)

Si prefieres iniciar manualmente:

```bash
cd /home/proyectos/Escritorio/Resultados-ICFES-2025
streamlit run streamlit_app.py
```

---

## 📱 Acceso desde Otros Dispositivos

### Desde la misma red local:

1. Abre un navegador en cualquier dispositivo conectado a la misma red
2. Ingresa la URL: `http://192.168.10.13:8501`
3. ¡Listo!

### Desde internet (si está configurado):

1. Abre un navegador
2. Ingresa la URL: `http://181.53.99.10:8501`
3. ¡Listo!

---

## 🛑 Detener la Aplicación

Presiona `Ctrl + C` en la terminal donde se está ejecutando la aplicación.

---

## 📊 Navegación Rápida

Una vez abierta la aplicación, usa el **sidebar izquierdo** para navegar entre:

1. 🏠 **Inicio** - Comparativo General 2024 vs 2025
2. 📊 **Estadísticas por Estudiante** - Análisis individual
3. 🎓 **Estadísticas por Grado** - Análisis por grado
4. 📚 **Estadísticas por Área** - Análisis por área de conocimiento
5. 🏫 **Estadísticas por Modelo** - Aula Regular vs Modelo Flexible
6. 📈 **Análisis de Avances** - Avances detallados 2024 → 2025
7. 🏆 **Rankings y Destacados** - Top estudiantes
8. 📥 **Descargar Datos** - Exportar en CSV o Excel

---

## 💡 Consejos Rápidos

### Para ver el comparativo general:
- La página de inicio muestra automáticamente el comparativo 2024 vs 2025
- Los avances se muestran con colores:
  - 🟢 Verde = Mejora
  - 🔴 Rojo = Disminución
  - 🟡 Amarillo = Sin cambio

### Para buscar un estudiante:
1. Ve a "📊 Estadísticas por Estudiante"
2. Selecciona el estudiante del menú desplegable
3. Revisa sus puntajes y gráficos

### Para ver rankings:
1. Ve a "🏆 Rankings y Destacados"
2. Revisa el Top 10 general
3. Navega por las pestañas para ver mejores por área

### Para descargar datos:
1. Ve a "📥 Descargar Datos"
2. Selecciona el conjunto de datos (Todos, Aula Regular o Modelo Flexible)
3. Haz clic en "Descargar CSV" o "Descargar Excel"

---

## 🔍 Características Destacadas

### ✨ Gráficos Interactivos
- **Hover:** Pasa el mouse sobre los gráficos para ver valores exactos
- **Zoom:** Usa la rueda del mouse para hacer zoom
- **Pan:** Arrastra para mover el gráfico
- **Descargar:** Usa el botón de cámara para guardar el gráfico

### 📊 Tablas Dinámicas
- Todas las tablas son ordenables
- Puedes hacer scroll horizontal si hay muchas columnas
- Los datos se actualizan automáticamente al cambiar filtros

### 🎨 Formato Condicional
- Los avances se muestran con colores según el tipo:
  - ✅ "Avanzó X puntos" (verde)
  - ❌ "Retrocedió X puntos" (rojo)
  - ⚪ "No subió. No bajó" (amarillo)

---

## 🆘 Solución Rápida de Problemas

### La aplicación no inicia:
```bash
# Verifica que estés en el directorio correcto
pwd

# Debe mostrar: /home/proyectos/Escritorio/Resultados-ICFES-2025
```

### Error de dependencias:
```bash
# Instala las dependencias
pip install -r requirements.txt
```

### Error al cargar datos:
```bash
# Verifica que los archivos existan
ls -la data/RESULTADOS-ICFES-*.xlsx
```

### La página no carga:
- Actualiza el navegador (F5)
- Limpia la caché: presiona "C" en la aplicación
- Reinicia la aplicación (Ctrl+C y vuelve a iniciar)

---

## 📚 Documentación Completa

Para más información, consulta:

- **Guía de uso detallada:** `GUIA-USO-APLICACION-COMPARATIVA.md`
- **README técnico:** `README-APLICACION-COMPARATIVA.md`
- **Resumen ejecutivo:** `RESUMEN-EJECUTIVO-APLICACION.md`

---

## 📞 Información Rápida

**Institución:** Pedacito de Cielo  
**Municipio:** La Tebaida, Quindío  
**Años comparados:** 2024 vs 2025  
**Áreas evaluadas:** 5 (Lectura Crítica, Matemáticas, Sociales, Ciencias, Inglés)  
**Modelos:** Aula Regular y Modelo Flexible

---

## ✅ Checklist de Inicio

- [ ] Abrir terminal
- [ ] Navegar al directorio del proyecto
- [ ] Ejecutar `./iniciar_aplicacion.sh`
- [ ] Esperar a que se abra el navegador
- [ ] Explorar la página de inicio
- [ ] Navegar por las diferentes secciones
- [ ] Probar los gráficos interactivos
- [ ] Descargar datos si es necesario

---

**¡Disfruta analizando los resultados ICFES! 📊🎓**

---

**Última actualización:** 2025-10-21  
**Versión:** 1.0  
**Estado:** ✅ Funcional

