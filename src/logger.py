import logging
import os
from datetime import datetime

LOG_FILE = f'{datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}.log'                            # Creacion de la variable que refleja el dia y hora del momento que ocurre el log

log_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)                                      # os.getcwd: Obtiene la carpeta donde estoy parado ahora
os.makedirs(log_path, exist_ok= True)                                                       # Creacion de la carpeta con el nombre del archivo logs

LOG_FILE_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)                                            # Ruta final del archivo

logging.basicConfig(
    filename= LOG_FILE_PATH,                                                                # Le dice en que archivo escrivir
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",           # El formato establecido del .log
    level = logging.INFO                                                                    # Establece el filtro, solo guardara mensajes de nivel INFO o superiores
)