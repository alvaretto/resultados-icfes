"""
Configuración de logging estructurado para la aplicación ICFES.
Salida a archivo con rotación automática. No usar prints ni st.write para debugging.
"""

import logging
import os
from logging.handlers import RotatingFileHandler

# Directorio de logs relativo a la raíz del proyecto
_LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
_LOG_FILE = os.path.join(_LOG_DIR, "app.log")

# Formato estructurado: timestamp | nivel | módulo | mensaje
_LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def get_logger(name: str) -> logging.Logger:
    """
    Devuelve un logger configurado con salida a archivo y consola.

    Uso:
        from app.logger import get_logger
        logger = get_logger(__name__)
        logger.info("Datos cargados correctamente")
        logger.warning("Columna faltante: %s", nombre_col)
        logger.error("Error al leer Excel: %s", str(e))
    """
    logger = logging.getLogger(name)

    # Evitar duplicar handlers si el logger ya fue configurado
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # Crear directorio de logs si no existe
    os.makedirs(_LOG_DIR, exist_ok=True)

    # Handler a archivo con rotación (5 MB x 3 archivos = 15 MB máximo)
    file_handler = RotatingFileHandler(
        _LOG_FILE,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(_LOG_FORMAT, datefmt=_DATE_FORMAT))

    # Handler a consola (solo WARNING+ para no saturar la terminal de Streamlit)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_handler.setFormatter(logging.Formatter(_LOG_FORMAT, datefmt=_DATE_FORMAT))

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Logger raíz de la aplicación — importar directamente si se necesita
app_logger = get_logger("icfes_app")
