from src.constants import TEST_DATA_PATH
from src.constants import TRAIN_DATA_PATH
from src.constants import RAW_DATA_PATH
from src.constants import DIR_ARTIFACTS
import sys
import pandas as pd

from src.exception import ExcepcionPersonalizada
from src.logger import logging

from sklearn.model_selection import train_test_split

from src.constants import (
    ARCHIVO,
    RAW_DATA_PATH,
    TRAIN_DATA_PATH,
    TEST_DATA_PATH,
    DIR_ARTIFACTS
)

class IngestaDatos:
    def iniciar_ingesta_datos(self):
        logging.info("Iniciando ingesta de los datos")

        try:

            logging.info(f"Leyendo archivo desde: {ARCHIVO}")
            df = pd.read_csv(ARCHIVO)

            # Crear carpeta de artefactos si no existe
            DIR_ARTIFACTS.mkdir(parents= True, exist_ok= True)

            # Guardar el archivo complet (raw) en artifacts
            df.to_csv(RAW_DATA_PATH, index= False)
            logging.info(f"Archivo raw guardado en: {RAW_DATA_PATH}")

            # División de datos (80% de entrenamiento, 20% prueba)
            test_set, train_set = train_test_split(df, test_size= 0.2, random_state=42)
            
            # Guardar los splits resultantes
            train_set.to_csv(TRAIN_DATA_PATH, index= False)
            test_set.to_csv(TEST_DATA_PATH, index= False)

            logging.info("Ingesta de datos y división train/test completada exitosamente")

            return TRAIN_DATA_PATH, TEST_DATA_PATH

        
        except Exception as e:
            raise ExcepcionPersonalizada(e, sys)