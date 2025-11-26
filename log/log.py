import logging
import os
from datetime import datetime

class Log:
    def __init__(self):
        self.nombre_fichero = f"logs/ErrorCreandoFichero_TasacionesOro.log"

    def log(self,tipo,mensaje):
        self.generarFichero()

        timestamp = datetime.now().strftime("%d%m%Y %H:%M:%S")

        linea_log = f"[{timestamp}] ---- [{tipo}] ---- {mensaje}\n"

        with open(self.nombre_fichero, 'a',
                  encoding='utf-8') as f:  # Para soportar caracteres como la ñ
            f.write(linea_log)
            print(f"Guardado en log:{linea_log}")

    def generarFichero(self):
        fecha = datetime.now().strftime("%Y%m%d").lower()  # Logs ordenados alfabeticamente
        self.nombre_fichero = f"logs/{fecha}_TasacionesOro.log"
        os.makedirs(
            os.path.dirname(self.nombre_fichero) if os.path.dirname(self.nombre_fichero) else '.', exist_ok=True)
        # Comprueba los directorios de la ruta, si no tiene el directorio es esta carpeta, si ya existe no crea nada y no da error