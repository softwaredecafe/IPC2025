from  cargarArchivo import CargarArchivo


class Menu:

    def mostrarmenu(self):
        while True:
         
            print("\n----------------- MENÚ PRINCIPAL -----------------")
            print("1.Cargar archivo")
            print("2.Procesar archivo")
            print("3.Escribir archivo salida")
            print("4.Datos del Estudiante")
            print("5.Generar grafica")
            print("6.Salir")
        
            opcion = input ("Seleccione una opción:")


            if opcion=="1":
                carga= CargarArchivo()
                carga.CargarArchivo()

            elif opcion=="2":
                print("opcion 2")

            elif opcion=="3":
                print("opcion 3")
    
            elif opcion=="4":
                 #Metodo para leer el archivo .txt
                 with open("estudiante.txt", "r" , encoding="utf-8") as archivo:
                    contenido = archivo.read()
                    print(contenido)

            elif opcion=="5":
                print("opcion 5")

            elif opcion=="6":
                print("opcion 6")
                break

            else:
                print("Opcion invalida, ingresa una opcion valida.")


    
    