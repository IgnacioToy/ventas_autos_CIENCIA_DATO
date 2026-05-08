from pathlib import Path

DIR_BASE = Path(__file__).resolve().parent.parent

# Rutas de los archivos
DIR_DATA = DIR_BASE / "netbooks" / "data"
ARCHIVO = DIR_DATA /  "ev_market.csv"

# Artefactos
DIR_ARTIFACTS = DIR_BASE / "artifacts"
TRAIN_DATA_PATH = DIR_ARTIFACTS / "train.csv"
TEST_DATA_PATH = DIR_ARTIFACTS / "test.csv"
RAW_DATA_PATH = DIR_ARTIFACTS / "data.csv"

# Objetos Serializados
PREPROCESSOR_OBJ_FILE_PATH = DIR_ARTIFACTS / "preprocessor.plk"
MODEL_FILE_PATH = DIR_ARTIFACTS / "data.csv"