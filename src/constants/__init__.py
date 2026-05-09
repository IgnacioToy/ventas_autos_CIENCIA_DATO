from pathlib import Path

# Resolvemos la raíz de forma absoluta
DIR_BASE = Path(__file__).resolve().parent.parent.parent

# Rutas de los archivos (Asegúrate de que la carpeta se llame 'notebook')
DIR_DATA = DIR_BASE / "netbook" / "data"
ARCHIVO = DIR_DATA / "ev_market.csv" # O "ev_market.csv" según tu archivo actual

# Artefactos
DIR_ARTIFACTS = DIR_BASE / "artifacts"
TRAIN_DATA_PATH = DIR_ARTIFACTS / "train.csv"
TEST_DATA_PATH = DIR_ARTIFACTS / "test.csv"
RAW_DATA_PATH = DIR_ARTIFACTS / "data.csv"

# Objetos Serializados (Corregido .pkl)
PREPROCESSOR_OBJ_FILE_PATH = DIR_ARTIFACTS / "preprocessor.pkl"
MODEL_FILE_PATH = DIR_ARTIFACTS / "model.pkl"