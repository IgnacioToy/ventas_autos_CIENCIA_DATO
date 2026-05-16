import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path

# Importación limpia de constantes
from src.constants import (
    ARCHIVO_OBJETIVO,
    RAW_DATA_PATH,
    TRAIN_DATA_PATH,
    TEST_DATA_PATH,
    DIR_PROCESSED
)
from src.exception import ExcepcionPersonalizada
from src.logger import logging

class IngestaDatos:
    def iniciar_ingesta_datos(self):
        logging.info("Iniciando fase de ingesta de datos")

        try:
            if not ARCHIVO_OBJETIVO.exists():
                raise FileNotFoundError(f"No se encuentra el archivo original en: {ARCHIVO_OBJETIVO}")
            
            logging.info(f"Leyendo archivo fuente: {ARCHIVO_OBJETIVO.name}")
            df = pd.read_csv(ARCHIVO_OBJETIVO)

            DIR_PROCESSED.mkdir(parents= True, exist_ok= True)
            df.to_csv(RAW_DATA_PATH, index= False)
            logging.info(f"Dataset guardado en: {RAW_DATA_PATH}")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(TRAIN_DATA_PATH, index= False)
            test_set.to_csv(TEST_DATA_PATH, index= False)


            logging.info("Ingesta y división de datos finalizada exitosamente")

            return RAW_DATA_PATH, TEST_DATA_PATH



        except Exception as e:
            logging.error("Error detectado en la ingesta de datos")
            raise ExcepcionPersonalizada(e, sys)

# --- BLOQUE PARA PRUEBAS DIRECTAS ---
if __name__ == "__main__":
    try:
        obj = IngestaDatos()
        train_p, test_p = obj.iniciar_ingesta_datos()
        print(f"✅ Ingesta finalizada. Datos en: {train_p}")
    except Exception as e:
        print(f"❌ Error fatal: {e}")