from pathlib import Path

DIR_BASE = Path(__file__).resolve().parent.parent.parent

# 1 Estructura de datos 
DIR_DATA = DIR_BASE / "data"
DIR_RAW = DIR_DATA / "raw"
DIR_INTERIM = DIR_DATA / "interim"
DIR_PROCESSED = DIR_DATA / "processed"

ARCHIVO_OBJETIVO = DIR_RAW / "ev_market.csv"

# Archivos resultantes de la ingesta (Van a PROCESSED)
TRAIN_DATA_PATH = DIR_PROCESSED / "train.csv"
TEST_DATA_PATH = DIR_PROCESSED / "test.csv"
RAW_DATA_PATH = DIR_PROCESSED / "data_full.csv"     # El dataframe total para el EDA

# Modelos y preprocesadores
DIR_MODELS = DIR_BASE / "models"
PREPROCESSOR_OBJ_FILE_PATH = DIR_MODELS / "preprocessor.pkl"
MODEL_FILE_PATH = DIR_MODELS / "model.pkl"