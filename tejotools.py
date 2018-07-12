import csv
import math
import heapq
from TDAgrafo import *

"""
arbol_tendido_minimo(grafo),
recibe un grafo (que se puede asumir conexo) y devuelve un nuevo grafo,
que representa un árbol de tendido mínimo del original.

"""

def parsear_archivo_grafo(file,grafo):
    vertices = {}
    with open (file,"r") as f:
        f_reader = csv.reader(f,delimiter=',')
        for row in f_reader:
            if(len(row)==3):
                try:
                    vertice = row[0]
                    coordenadas = (float(row[1]),float(row[2]))
                    grafo.agregar_vertice(vertice,coordenadas)

                except ValueError:
                    vertice = row[0]
                    arista = row[1]
                    peso = int(row[2])
                    grafo.agregar_arista(vertice,arista,peso)

    return grafo

def camino_minimo(grafo,inicio,fin):
    #falta la funcion de reconstruir_ciclo

    #for v in grafo dist[v] = inf
    distancia = dict.fromkeys(grafo.obtener_vertices(),math.inf)
    padre = {}
    heap = []

    distancia[inicio] = 0
    padre[inicio] = None

    #ENCOLO UNA TUPLA DE LA FORMA ('MOSCU',DISTANCIA['MOSCU'])
    heapq.heappush(heap,(inicio,distancia[inicio]))

    while True:
        try:
            v = heapq.heappop(heap)
            for w in grafo.obtener_adyacentes(v[0]):
                print(w)
                if (distancia[v[0]] + grafo.obtener_peso_arista(v[0],w) < distancia[w]):
                    padre[w] = v[0]
                    distancia[w] = distancia[v[0]] + grafo.obtener_peso_arista(v[0],w)
                    heapq.heappush(heap,(w,distancia[w]))
        except IndexError:
            break

    print(padre)
    return

def arbol_tendido_minimo(grafo):
    nuevo_grafo = Grafo()

    inicio = grafo.obtener_vertice_random()
    print(grafo.obtener_nombre_vertice(inicio))
    


    return

def main():
    graph = Grafo()
    parsear_archivo_grafo("sedes.csv",graph)
    #camino_minimo(graph,'Moscu','Saransk')
    arbol_tendido_minimo(graph)

main()
