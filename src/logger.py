import logging
import os
from datetime import datetime

# Definimos el nombre del archivo
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Creamos la ruta de la CARPETA 'logs'
logs_path = os.path.join(os.getcwd(), "logs")

# Si no existe la carpeta, la creamos
os.makedirs(logs_path, exist_ok=True)

# Definimos la ruta completa del ARCHIVO
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)