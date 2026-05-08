import os
import sys
import dill

import statsmodels.api as sm

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import ExcepcionPersonalizada
from src.logger import logging

def guardar_objeto(file_path, obj):
    try:
        logging.info(f"Guardando objeto en: {file_path}")
        
        # Creacion del directorio padre si no existe
        file_path.parent.mkdir(parents= True, exist_ok= True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    
    except Exception as e:
        raise ExcepcionPersonalizada(e, sys)


def analizar_estadisticas_modelo(X_train, y_train):
    # Función inspirada para validar supuestos y ver significancia de variables (p-values)
    try:
        logging.info("Realizando análisis estadístico OLS con statmodels")
        X_train_const = sm.add_constant(X_train)

        # Entrenamiento del modelo OLS (Ordinary Least Squares)
        model = sm.OLS(y_train, X_train_const).fit()
        # Retorno el resumen
        return model.summary()
    
    except Exception as e:
        raise ExcepcionPersonalizada(e, sys)


def evaluar_modelo(X_train, y_train, X_test, y_test, models: dict, param: dict):
    try:
        reporte = {}

        for nombre_modelo, model in models.items():
            # Buscar los parámetros especificos para este modelo en el diccionario param
            para = param.get(nombre_modelo, {})

            logging.info(f"Iniciando GridSearchCv para el modelo: {nombre_modelo}")

            # GridSearchCV para encontrar los mejores parámetros
            gs = GridSearchCV(model, para, cv= 3, n_jobs=1)
            gs.fit(X_train, y_train)

            # Configuracion del modelo con los mejores parámetros encontrados
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # REalizo la predicción y mido presición
            y_test_pred = model.predict(X_test)
            test_model_score = r2_score(y_test, y_test_pred)
        
        #Guardar el resultado en el reporte
        reporte[nombre_modelo] = test_model_score

        logging.info(f"Modelo {nombre_modelo} evaluado. Re: {test_model_score}")

        return reporte
    
    except Exception as e:
        raise ExcepcionPersonalizada(e, sys)