import csv
from collections import deque
from TDAgrafo import *

"""
La biblioteca a implementar debe tener la siguientes funciones implementadas:

camino_minimo(grafo, desde, hasta): (dijkstra)
    que nos devuelva una lista con el camino mínimo entre ese par de sedes.
    Ejemplo: camino_minimo(rusia, 'Moscu', 'Saransk') -> ['Moscu', 'Samara', 'Saransk']

viajante(grafo, origen): *
    que nos devuelva una lista con el recorrido a hacer para resolver de forma óptima el problema del viajante.
    La lista debe tener el mismo formato que camino_minimo.

viajante_aproximado(grafo, origen): **
 idem anterior, pero de forma aproximada, siendo este mucho más rápido.

*** = estos dos son uno greedy y otro con backtracking

orden_topologico(grafo): (ot mdf)
    que nos devuelva una lista con un orden topológico del grafo.
    En caso de no existir, devolver None, NULL, o el equivalente en el lenguaje elegido. Notar que para esta función, el grafo recibido debe ser dirigido.

arbol_tendido_minimo(grafo): (prim o kruskal)
    recibe un grafo (que se puede asumir conexo) y devuelve un nuevo grafo
    que representa un árbol de tendido mínimo del original.

"""


def parsear_archivo(file):
    """
    # Cantidad de ciudades (n)
    Ciudad1,lat1,long1
    Ciudad1,lat1,long1
    #creo el vertice -> el dato es la tupla lat y long.

    ...
    Ciudad_n,lat_n,long_n
    # Cantidad de aristas
    Ciudad_i,Ciudad_j,tiempo
    ...
    """
    vertices = {}

    with open (file,"r") as f:
        f_reader = csv.DictReader(f,delimiter=',')
        for row in f_reader:
            print (row)







def main():
    graph = Grafo()

    graph.agregar_vertice('A','socchi')
    graph.agregar_vertice('B','moscu')
    graph.agregar_vertice('C','mondongo')
    graph.agregar_vertice('D','samara')
    graph.agregar_vertice('E','kazan')

    print(graph.obtener_vertice_random())

    print(graph.obtener_dato_vertice('A'))

    #AGREGO ARISTA
    if (graph.agregar_arista('A','B',8)):
        print ('AGREGAR ARISTA OK ')

    if (not graph.agregar_arista('A','B',8)):
        print ('FALSE DUPLICAR ARISTA OK')

    graph.agregar_arista('A','C',18)
    graph.agregar_arista('A','E',28)
    graph.agregar_arista('B','C',38)
    graph.agregar_arista('B','D',4)
    graph.agregar_arista('C','D',14)
    graph.agregar_arista('D','E',24)

    print("A:", graph.obtener_adyacentes('A'))
    print("B:",graph.obtener_adyacentes('B'))
    print("C:",graph.obtener_adyacentes('C'))
    print("D:",graph.obtener_adyacentes('D'))
    print("E:",graph.obtener_adyacentes('E'))


    graph.borrar_arista('A','B')
    graph.borrar_vertice('D')
    print("debug")
    print("A:", graph.obtener_adyacentes('A'))
    print("B:",graph.obtener_adyacentes('B'))
    print("C:",graph.obtener_adyacentes('C'))
    print("D:",graph.obtener_adyacentes('D'))
    print("E:",graph.obtener_adyacentes('E'))


    parsear_archivo("sedes.csv")


main()
