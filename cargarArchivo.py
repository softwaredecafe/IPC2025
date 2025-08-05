import os

class CargarArchivo:
    
    def CargarArchivo(self):
        ruta = input("Ingrese la ruta del archivo: ")
        nombre = input("Ingrese el nombre del archivo con extension .xml: ")
        ruta_completa = f"{ruta}/{nombre}" if ruta else nombre
        
        if os.path.isfile(ruta_completa):
            print(f"\n Archivo '{nombre}' se a cargado correctamente :D")
        else:
            print(f"\n Error: El archivo '{nombre}' no existe o la ruta es incorrecta :'()")
       
    
    