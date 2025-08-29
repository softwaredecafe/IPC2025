# procesadorXML.py
import xml.etree.ElementTree as ET
from modelos import CampoAgricola, EstacionBase, SensorSuelo, SensorCultivo
from lista import ListaEnlazada

class ProcesadorXML:
    def __init__(self):
        self.campos = ListaEnlazada()
    
    def cargar_archivo(self, ruta_archivo):
        try:
            tree = ET.parse(ruta_archivo)
            root = tree.getroot()
            
            for campo_elem in root.findall('campo'):
                campo = CampoAgricola(
                    campo_elem.get('id'),
                    campo_elem.get('nombre')
                )
                
                # Procesar estaciones base
                estaciones_elem = campo_elem.find('estacionesBase')
                if estaciones_elem:
                    for estacion_elem in estaciones_elem.findall('estacion'):
                        estacion = EstacionBase(
                            estacion_elem.get('id'),
                            estacion_elem.get('nombre')
                        )
                        campo.estaciones.agregar(estacion)
                
                # Procesar sensores de suelo
                sensores_suelo_elem = campo_elem.find('sensoresSuelo')
                if sensores_suelo_elem:
                    for sensor_elem in sensores_suelo_elem.findall('sensor'):
                        sensor = SensorSuelo(
                            sensor_elem.get('id'),
                            sensor_elem.get('nombre')
                        )
                        
                        for freq_elem in sensor_elem.findall('frecuencia'):
                            estacion_id = freq_elem.get('idEstacion')
                            frecuencia = int(freq_elem.text.strip())
                            sensor.frecuencias.agregar((estacion_id, frecuencia))
                        
                        campo.sensores_suelo.agregar(sensor)
                
                # Procesar sensores de cultivo
                sensores_cultivo_elem = campo_elem.find('sensoresCultivo')
                if sensores_cultivo_elem:
                    for sensor_elem in sensores_cultivo_elem.findall('sensorT'):
                        sensor = SensorCultivo(
                            sensor_elem.get('id'),
                            sensor_elem.get('nombre')
                        )
                        
                        for freq_elem in sensor_elem.findall('frecuencia'):
                            estacion_id = freq_elem.get('idEstacion')
                            frecuencia = int(freq_elem.text.strip())
                            sensor.frecuencias.agregar((estacion_id, frecuencia))
                        
                        campo.sensores_cultivo.agregar(sensor)
                
                self.campos.agregar(campo)
                print(f"✓ Cargando campo agrícola {campo.id}")
            
            return True
        except Exception as e:
            print(f"Error al procesar el archivo: {e}")
            return False