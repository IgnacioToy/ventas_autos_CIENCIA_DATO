import sys
from src.logger import logging


# Función que "rastrea" los detalles tpecnicos del error
def detalle_error_mensaje(error, detalle_error: sys):
    _, _, exc_tb = detalle_error.exc_info()                 # exc_info() devuelve: tipo de error, valor y el 'traceback' (exc_info)
    nombre_archivo = exc_tb.tb_frame.f_code.co_filename     # Extraccion del nombre del archivo donde se produjo el error
    mensaje_error = 'El error ocurrio en src: [{0}]. Número de linea: [{1}]. Mensaje del error: [{2}]'.format(nombre_archivo, exc_tb.tb_lineno, str(error))

    return mensaje_error

class ExcepcionPersonalizada(Exception):
    def __init__(self, mensaje_error, detalle_error):
        super().__init__(mensaje_error)
        self.mensaje_error = detalle_error_mensaje(mensaje_error, detalle_error=detalle_error)

    def __str__(self):
        return self.mensaje_error

        