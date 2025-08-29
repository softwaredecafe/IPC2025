# cargarArchivo.py (actualizado)
import os

class CargarArchivo:
    def CargarArchivo(self):
        ruta = input("Ingrese la ruta del archivo: ")
        nombre = input("Ingrese el nombre del archivo con extensión .xml: ")
        ruta_completa = f"{ruta}/{nombre}" if ruta else nombre
        
        if os.path.isfile(ruta_completa):
            print(f"\nArchivo '{nombre}' se ha cargado correctamente :D")
            return ruta_completa
        else:
            print(f"\nError: El archivo '{nombre}' no existe o la ruta es incorrecta :'(")
            return None