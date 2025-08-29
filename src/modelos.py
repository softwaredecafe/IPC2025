# modelos.py
from lista import ListaEnlazada

class EstacionBase:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.sensores_suelo = ListaEnlazada()
        self.sensores_cultivo = ListaEnlazada()
    
    def agregar_frecuencia_suelo(self, sensor_id, frecuencia):
        self.sensores_suelo.agregar((sensor_id, frecuencia))
    
    def agregar_frecuencia_cultivo(self, sensor_id, frecuencia):
        self.sensores_cultivo.agregar((sensor_id, frecuencia))

class SensorSuelo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.frecuencias = ListaEnlazada()  # Lista de (estacion_id, frecuencia)

class SensorCultivo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.frecuencias = ListaEnlazada()  # Lista de (estacion_id, frecuencia)

class CampoAgricola:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.estaciones = ListaEnlazada()
        self.sensores_suelo = ListaEnlazada()
        self.sensores_cultivo = ListaEnlazada()