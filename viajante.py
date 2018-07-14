from TDAgrafo import *
import csv
import math
import heapq




def problema_viajante(grafo, origen):
	visitados = []
	mejor_recorrido = [(math.inf, [])]
	_problema_viajante(grafo, origen, origen, visitados, mejor_recorrido, 0)
	mejor_recorrido[0][1].append(origen)
	return mejor_recorrido[0]


def _problema_viajante(grafo, origen, v, visitados, mejor_recorrido, recorrido_actual):
		visitados.append(v)
		if len(visitados) == grafo.cantidad_vertices():
			return grafo.obtener_peso_arista(v, origen)

		if recorrido_actual > mejor_recorrido[0][0]:
			return 0

		for w in grafo.obtener_adyacentes(v):
			if w not in visitados:
				recorrido_actual += grafo.obtener_peso_arista(v, w)
				siguiente = _problema_viajante(grafo, origen, w, visitados, mejor_recorrido, recorrido_actual)
				recorrido_actual += siguiente
				
				if len(visitados) == grafo.cantidad_vertices() and recorrido_actual < mejor_recorrido[0][0]:
					mejor_recorrido[0] = (recorrido_actual, visitados[:])
				
				visitados.pop()
				
				recorrido_actual -= (grafo.obtener_peso_arista(v,w) + siguiente)
		return recorrido_actual


def main():
	graph = Grafo()

	graph.agregar_vertice('A','sochi')
	graph.agregar_vertice('B','moscu')
	graph.agregar_vertice('C','mondongo')
	graph.agregar_vertice('D','samara')
	graph.agregar_vertice('E','sochi')
	graph.agregar_vertice('F','moscu')
	graph.agregar_vertice('G','mondongo')
	graph.agregar_vertice('H','samara')
	
	graph.agregar_arista('A','B',16)
	graph.agregar_arista('A','C',6)
	graph.agregar_arista('A','D',19)
	graph.agregar_arista('A','E',3)
	graph.agregar_arista('A','F',5)
	graph.agregar_arista('A','G',11)
	graph.agregar_arista('A','H',9)
	
	graph.agregar_arista('B','C',14)
	graph.agregar_arista('B','D',18)
	graph.agregar_arista('B','E',19)
	graph.agregar_arista('B','F',17)
	graph.agregar_arista('B','G',15)
	graph.agregar_arista('B','H',18)

	graph.agregar_arista('C','D',17)
	graph.agregar_arista('C','E',2)
	graph.agregar_arista('C','F',10)
	graph.agregar_arista('C','G',10)
	graph.agregar_arista('C','H',9)

	graph.agregar_arista('D','E',11)
	graph.agregar_arista('D','F',23)
	graph.agregar_arista('D','G',16)
	graph.agregar_arista('D','H',18)	
	
	graph.agregar_arista('E','F',13)
	graph.agregar_arista('E','G',25)
	graph.agregar_arista('E','H',20)

	graph.agregar_arista('F','G',11)
	graph.agregar_arista('F','H',12)

	graph.agregar_arista('G','H',2)

	camino = problema_viajante(graph, 'C')
	
	n = len(camino[1])
	for i in range(n):
		if i == n-1:
			print (camino[1][i])
		else:
			print (camino[1][i], end = " -> ")
	print ("Costo total:", camino[0])
		
main()