import csv
import math
import heapq

from TDAgrafo import *

INF = 9999999

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

    distancia = dict.fromkeys(grafo.obtener_vertices(),INF)
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
                if (distancia[v[0]] + grafo.obtener_peso_arista(v[0],w) < distancia[w]):
                    padre[w] = v[0]
                    distancia[w] = distancia[v[0]] + grafo.obtener_peso_arista(v[0],w)
                    heapq.heappush(heap,(w,distancia[w]))
        except IndexError:
            break

    return reconstruir_ciclo(padre, inicio, fin)


def reconstruir_ciclo(padre, origen, destino):
    camino = []
    actual = destino
    while actual != origen:
        camino.insert(0,actual)
        actual = padre[actual]
    camino.insert(0,origen)
    return camino

def arbol_tendido_minimo(grafo):

    #usamos prim.
    inicio = grafo.obtener_vertice_random()
    dato = grafo.obtener_dato_vertice(inicio)

    visitados = set()
    visitados.add(inicio)

    heap = []

    for w in grafo.obtener_adyacentes(inicio):
        heapq.heappush(heap,((inicio,w),grafo.obtener_peso_arista(inicio,w)))

    arbol = Grafo()
    for key in grafo.obtener_vertices():
        arbol.agregar_vertice(key)

    while True:
        try:
            (v,w) = heapq.heappop(heap)
            if(v[1]) in visitados:
                continue
            arbol.agregar_arista(v[0],v[1],w)
            visitados.add(v[1])
            print(v[1])
            for adyacente in grafo.obtener_adyacentes(v[1]):
                heapq.heappush(heap,((v[1],adyacente),grafo.obtener_peso_arista(v[1],adyacente)))
        except IndexError:
            break

    return visitados
