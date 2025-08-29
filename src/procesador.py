# procesador.py
from lista import ListaEnlazada

class Procesador:
    def __init__(self, campos):
        self.campos = campos
        self.campos_procesados = ListaEnlazada()
    
    def procesar(self):
        for campo in self.campos:
            print(f"Procesando campo {campo.id}...")
            
            # Crear matrices de frecuencia
            matriz_suelo = self.crear_matriz_frecuencia_suelo(campo)
            matriz_cultivo = self.crear_matriz_frecuencia_cultivo(campo)
            
            # Crear matrices de patrones
            matriz_patron_suelo = self.crear_matriz_patron(matriz_suelo)
            matriz_patron_cultivo = self.crear_matriz_patron(matriz_cultivo)
            
            # Agrupar estaciones con mismos patrones
            grupos = self.agrupar_estaciones(matriz_patron_suelo, matriz_patron_cultivo)
            
            # Crear matrices reducidas
            matriz_reducida_suelo = self.crear_matriz_reducida_suelo(campo, grupos)
            matriz_reducida_cultivo = self.crear_matriz_reducida_cultivo(campo, grupos)
            
            campo_procesado = {
                'campo': campo,
                'matrices_originales': (matriz_suelo, matriz_cultivo),
                'matrices_patron': (matriz_patron_suelo, matriz_patron_cultivo),
                'grupos': grupos,
                'matrices_reducidas': (matriz_reducida_suelo, matriz_reducida_cultivo)
            }
            
            self.campos_procesados.agregar(campo_procesado)
            print(f"✓ Campo {campo.id} procesado correctamente")
    
    def crear_matriz_frecuencia_suelo(self, campo):
        # Implementar creación de matriz de frecuencia para sensores de suelo
        matriz = ListaEnlazada()
        
        for estacion in campo.estaciones:
            fila = ListaEnlazada()
            for sensor in campo.sensores_suelo:
                frecuencia = 0
                for freq in sensor.frecuencias:
                    if freq[0] == estacion.id:
                        frecuencia = freq[1]
                        break
                fila.agregar(frecuencia)
            matriz.agregar(fila)
        
        return matriz
    
    def crear_matriz_frecuencia_cultivo(self, campo):
        # Similar a crear_matriz_frecuencia_suelo pero para cultivo
        matriz = ListaEnlazada()
        
        for estacion in campo.estaciones:
            fila = ListaEnlazada()
            for sensor in campo.sensores_cultivo:
                frecuencia = 0
                for freq in sensor.frecuencias:
                    if freq[0] == estacion.id:
                        frecuencia = freq[1]
                        break
                fila.agregar(frecuencia)
            matriz.agregar(fila)
        
        return matriz
    
    def crear_matriz_patron(self, matriz):
        # Convertir matriz de frecuencia a matriz de patrones (0 y 1)
        matriz_patron = ListaEnlazada()
        
        for fila in matriz:
            fila_patron = ListaEnlazada()
            for valor in fila:
                fila_patron.agregar(1 if valor > 0 else 0)
            matriz_patron.agregar(fila_patron)
        
        return matriz_patron
    
    def agrupar_estaciones(self, patron_suelo, patron_cultivo):
        # Agrupar estaciones con mismos patrones en ambas matrices
        grupos = ListaEnlazada()
        estaciones_agrupadas = ListaEnlazada()
        
        for i in range(len(patron_suelo)):
            if i in estaciones_agrupadas:
                continue
                
            grupo = ListaEnlazada()
            grupo.agregar(i)
            estaciones_agrupadas.agregar(i)
            
            for j in range(i + 1, len(patron_suelo)):
                if j in estaciones_agrupadas:
                    continue
                    
                # Comparar patrones de ambas matrices
                patron_igual = True
                for k in range(len(patron_suelo.obtener(i))):
                    if (patron_suelo.obtener(i).obtener(k) != patron_suelo.obtener(j).obtener(k) or
                        patron_cultivo.obtener(i).obtener(k) != patron_cultivo.obtener(j).obtener(k)):
                        patron_igual = False
                        break
                
                if patron_igual:
                    grupo.agregar(j)
                    estaciones_agrupadas.agregar(j)
            
            grupos.agregar(grupo)
        
        return grupos
    
    def crear_matriz_reducida_suelo(self, campo, grupos):
        # Implementar creación de matriz reducida para sensores de suelo
        matriz_reducida = ListaEnlazada()
        
        for grupo in grupos:
            fila = ListaEnlazada()
            for sensor in campo.sensores_suelo:
                suma = 0
                for estacion_idx in grupo:
                    estacion = campo.estaciones.obtener(estacion_idx)
                    for freq in sensor.frecuencias:
                        if freq[0] == estacion.id:
                            suma += freq[1]
                            break
                fila.agregar(suma)
            matriz_reducida.agregar(fila)
        
        return matriz_reducida
    
    def crear_matriz_reducida_cultivo(self, campo, grupos):
        # Similar a crear_matriz_reducida_suelo pero para cultivo
        matriz_reducida = ListaEnlazada()
        
        for grupo in grupos:
            fila = ListaEnlazada()
            for sensor in campo.sensores_cultivo:
                suma = 0
                for estacion_idx in grupo:
                    estacion = campo.estaciones.obtener(estacion_idx)
                    for freq in sensor.frecuencias:
                        if freq[0] == estacion.id:
                            suma += freq[1]
                            break
                fila.agregar(suma)
            matriz_reducida.agregar(fila)
        
        return matriz_reducida