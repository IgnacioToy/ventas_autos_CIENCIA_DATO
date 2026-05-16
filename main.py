import sys
from src.logger import logging
from src.exception import ExcepcionPersonalizada
from src.components.data_ingestion import IngestaDatos

# Cuando tengas los otros componentes listos, los importarás así:
# from src.components.data_transformation import DataTransformation
# from src.components.model_trainer import ModelTrainer

def iniciar_pipeline():
    try:
        logging.info("=========================================")
        logging.info("INICIANDO PIPELINE DE MACHINE LEARNING")
        logging.info("=========================================")

        # 1. FASE DE INGESTA DE DATOS
        ingesta = IngestaDatos()
        # Recuerda que tu ingesta actual devuelve el path para el EDA y el Train
        ruta_raw, ruta_train = ingesta.iniciar_ingesta_datos()
        print(f"✅ Ingesta completada con éxito.")

        # 2. FASE DE TRANSFORMACIÓN (Próximo paso en tu proyecto)
        # logging.info("Iniciando transformación de datos...")
        # transformacion = DataTransformation()
        # train_arr, test_arr, _ = transformacion.iniciar_transformacion(ruta_train, ... )

        # 3. FASE DE ENTRENAMIENTO DEL MODELO (Paso final)
        # logging.info("Iniciando entrenamiento del modelo...")
        # entrenador = ModelTrainer()
        # metrica_r2 = entrenador.iniciar_entrenamiento(train_arr, test_arr)
        
        logging.info("=========================================")
        logging.info("PIPELINE EJECUTADO EXITOSAMENTE")
        logging.info("=========================================")

    except Exception as e:
        logging.error("El Pipeline falló de manera crítica")
        raise ExcepcionPersonalizada(e, sys)

if __name__ == "__main__":
    try:
        iniciar_pipeline()
    except Exception as e:
        print(f"❌ Error en la ejecución del pipeline: {e}")