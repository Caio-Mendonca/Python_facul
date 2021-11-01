import networkx as nx
import matplotlib.pyplot as plt

class visualizazaoGrafo:
    def __init__(self):
        self.visual = []


    def adicionaAresta(self, a, b):
        temp = [a, b] #Argamazena as arestas temporárias
        self.visual.append(temp) #Insere na linha visual

    def desenhar(self):
        G = nx.Graph() #Cria um grafo chamado "G"  e adiciona um senão se a lista de arestas G
        G.add_edges_from(self.visual) #Execução da função de desenho
        nx.draw_networkx(G, node_color ="lightgrey") #O grafo é então desenhado na tela
        plt.show()


G = visualizazaoGrafo()
G.adicionaAresta('Pedro', 'CP')
G.adicionaAresta('Pedro', 'Carla')
G.adicionaAresta('Carla', 'CP')
G.adicionaAresta('Pedro', 'CC')
G.adicionaAresta('Joao','CC')
G.desenhar()

