# menu.py (actualizado)
from cargarArchivo import CargarArchivo
from procesadorXML import ProcesadorXML
from procesador import Procesador
from escritorXML import EscritorXML
from graficador import Graficador
from lista import ListaEnlazada

class Menu:
    def __init__(self):
        self.procesador_xml = ProcesadorXML()
        self.procesador = None
        self.campos_procesados = ListaEnlazada()
    
    def mostrarmenu(self):
        while True:
            print("\n----------------- MENÚ PRINCIPAL -----------------")
            print("1. Cargar archivo")
            print("2. Procesar archivo")
            print("3. Escribir archivo salida")
            print("4. Datos del Estudiante")
            print("5. Generar gráfica")
            print("6. Salir")
        
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                carga = CargarArchivo()
                ruta_completa = carga.CargarArchivo()
                if ruta_completa:
                    if self.procesador_xml.cargar_archivo(ruta_completa):
                        print("✓ Archivo cargado y procesado correctamente")
            
            elif opcion == "2":
                if len(self.procesador_xml.campos) > 0:
                    self.procesador = Procesador(self.procesador_xml.campos)
                    self.procesador.procesar()
                    self.campos_procesados = self.procesador.campos_procesados
                    print("✓ Archivo procesado correctamente")
                else:
                    print("Error: Primero debe cargar un archivo")
            
            elif opcion == "3":
                if len(self.campos_procesados) > 0:
                    ruta = input("Ingrese la ruta del archivo: ")
                    nombre = input("Ingrese el nombre del archivo: ")
                    ruta_salida = f"{ruta}/{nombre}" if ruta else nombre
                    
                    escritor = EscritorXML()
                    escritor.generar_xml(self.campos_procesados, ruta_salida)
                    print("✓ Archivo de salida generado correctamente")
                else:
                    print("Error: Primero debe procesar un archivo")
            
            elif opcion == "4":
                with open("estudiante.txt", "r", encoding="utf-8") as archivo:
                    contenido = archivo.read()
                    print(contenido)
            
            elif opcion == "5":
                if len(self.campos_procesados) > 0:
                    print("Campos disponibles:")
                    for i, campo_proc in enumerate(self.campos_procesados):
                        print(f"{i+1}. {campo_proc['campo'].nombre}")
                    
                    try:
                        opcion_campo = int(input("Seleccione un campo: ")) - 1
                        if 0 <= opcion_campo < len(self.campos_procesados):
                            print("Tipos de gráfica disponibles:")
                            print("1. Matriz de frecuencias original")
                            print("2. Matriz de patrones")
                            print("3. Matriz reducida")
                            
                            opcion_tipo = input("Seleccione el tipo de gráfica: ")
                            tipos = {"1": "original", "2": "patron", "3": "reducida"}
                            
                            if opcion_tipo in tipos:
                                ruta = input("Ingrese la ruta para guardar la gráfica: ")
                                nombre = input("Ingrese el nombre de la gráfica: ")
                                ruta_salida = f"{ruta}/{nombre}" if ruta else nombre
                                
                                graficador = Graficador()
                                graficador.generar_grafica(
                                    self.campos_procesados.obtener(opcion_campo),
                                    tipos[opcion_tipo],
                                    ruta_salida
                                )
                            else:
                                print("Error: Tipo de gráfica no válido")
                        else:
                            print("Error: Campo no válido")
                    except ValueError:
                        print("Error: Debe ingresar un número válido")
                else:
                    print("Error: Primero debe procesar un archivo")
            
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            
            else:
                print("Opción inválida, ingrese una opción válida.")