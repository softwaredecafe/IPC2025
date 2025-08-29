# graficador.py
from graphviz import Digraph
from lista import ListaEnlazada

class Graficador:
    def generar_grafica(self, campo_procesado, tipo_grafica, ruta_salida):
        campo = campo_procesado['campo']
        matrices = campo_procesado['matrices_originales']
        matrices_patron = campo_procesado['matrices_patron']
        matrices_reducidas = campo_procesado['matrices_reducidas']
        grupos = campo_procesado['grupos']
        
        dot = Digraph(comment=f'Campo {campo.id} - {tipo_grafica}')
        dot.attr(rankdir='LR')
        
        if tipo_grafica == "original":
            self._graficar_matrices_originales(dot, campo, matrices)
        elif tipo_grafica == "patron":
            self._graficar_matrices_patron(dot, campo, matrices_patron)
        elif tipo_grafica == "reducida":
            self._graficar_matrices_reducidas(dot, campo, matrices_reducidas, grupos)
        
        dot.render(ruta_salida, format='png', cleanup=True)
        print(f"Gráfica generada en: {ruta_salida}.png")
    
    def _graficar_matrices_originales(self, dot, campo, matrices):
        matriz_suelo, matriz_cultivo = matrices
        
        with dot.subgraph(name='cluster_suelo') as c:
            c.attr(label='Sensores de Suelo', style='filled', color='lightgrey')
            for j, sensor in enumerate(campo.sensores_suelo):
                c.node(f'S_s{j}', sensor.nombre, shape='box')
        
        with dot.subgraph(name='cluster_cultivo') as c:
            c.attr(label='Sensores de Cultivo', style='filled', color='lightblue')
            for j, sensor in enumerate(campo.sensores_cultivo):
                c.node(f'T_s{j}', sensor.nombre, shape='box')
        
        with dot.subgraph(name='cluster_estaciones') as c:
            c.attr(label='Estaciones Base', style='filled', color='lightgreen')
            for i, estacion in enumerate(campo.estaciones):
                c.node(f'E_{i}', estacion.nombre, shape='ellipse')
                
                # Conectar con sensores de suelo
                for j in range(len(matriz_suelo.obtener(i))):
                    frecuencia = matriz_suelo.obtener(i).obtener(j)
                    if frecuencia > 0:
                        dot.edge(f'E_{i}', f'S_s{j}', label=str(frecuencia))
                
                # Conectar con sensores de cultivo
                for j in range(len(matriz_cultivo.obtener(i))):
                    frecuencia = matriz_cultivo.obtener(i).obtener(j)
                    if frecuencia > 0:
                        dot.edge(f'E_{i}', f'T_s{j}', label=str(frecuencia))
    
    def _graficar_matrices_patron(self, dot, campo, matrices_patron):
        # Implementación similar pero mostrando patrones (0/1)
        pass
    
    def _graficar_matrices_reducidas(self, dot, campo, matrices_reducidas, grupos):
        # Implementación para matrices reducidas
        pass