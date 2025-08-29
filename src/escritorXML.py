# escritorXML.py
from lista import ListaEnlazada
import xml.etree.ElementTree as ET

class EscritorXML:
    def generar_xml(self, campos_procesados, ruta_salida):
        root = ET.Element("camposAgricolas")
        
        for campo_proc in campos_procesados:
            campo = campo_proc['campo']
            grupos = campo_proc['grupos']
            matriz_reducida_suelo = campo_proc['matrices_reducidas'][0]
            matriz_reducida_cultivo = campo_proc['matrices_reducidas'][1]
            
            campo_elem = ET.SubElement(root, "campo", id=campo.id, nombre=campo.nombre)
            
            # Estaciones base reducidas
            estaciones_reducidas_elem = ET.SubElement(campo_elem, "estacionesBaseReducidas")
            for i, grupo in enumerate(grupos):
                estacion_id = f"e{i+1:02d}"
                nombres_estaciones = ", ".join([campo.estaciones.obtener(idx).nombre for idx in grupo])
                ET.SubElement(estaciones_reducidas_elem, "estacion", 
                             id=estacion_id, 
                             nombre=nombres_estaciones)
            
            # Sensores de suelo
            sensores_suelo_elem = ET.SubElement(campo_elem, "sensoresSuelo")
            for j, sensor in enumerate(campo.sensores_suelo):
                sensor_elem = ET.SubElement(sensores_suelo_elem, "sensor", 
                                           id=sensor.id, 
                                           nombre=sensor.nombre)
                
                for i, grupo in enumerate(grupos):
                    estacion_id = f"e{i+1:02d}"
                    frecuencia = matriz_reducida_suelo.obtener(i).obtener(j)
                    if frecuencia > 0:
                        freq_elem = ET.SubElement(sensor_elem, "frecuencia", idEstacion=estacion_id)
                        freq_elem.text = str(frecuencia)
            
            # Sensores de cultivo
            sensores_cultivo_elem = ET.SubElement(campo_elem, "sensoresCultivo")
            for j, sensor in enumerate(campo.sensores_cultivo):
                sensor_elem = ET.SubElement(sensores_cultivo_elem, "sensorT", 
                                           id=sensor.id, 
                                           nombre=sensor.nombre)
                
                for i, grupo in enumerate(grupos):
                    estacion_id = f"e{i+1:02d}"
                    frecuencia = matriz_reducida_cultivo.obtener(i).obtener(j)
                    if frecuencia > 0:
                        freq_elem = ET.SubElement(sensor_elem, "frecuencia", idEstacion=estacion_id)
                        freq_elem.text = str(frecuencia)
        
        # Guardar el XML
        tree = ET.ElementTree(root)
        tree.write(ruta_salida, encoding="utf-8", xml_declaration=True)
        print(f"Archivo guardado en: {ruta_salida}")