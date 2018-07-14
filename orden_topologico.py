from TDAgrafo import *
from collections import deque

def orden_topologico(grafo):
	grado_entrada = {}
	
	for v in grafo.obtener_vertices():
		grado_entrada[v] = 0
	for v in grafo.obtener_vertices():
		for w in grafo.obtener_adyacentes(v):
			grado_entrada[w] += 1
	
	cola = deque()
	for v in grafo.obtener_vertices():
		if grado_entrada[v] == 0:
			cola.append(v)
	
	salida = []
	peso = 0

	while len(cola) > 0:
		v = cola.popleft()
		salida.append(v)
		for w in grafo.obtener_adyacentes(v):
			grado_entrada[w] -= 1
			peso += grafo.obtener_peso_arista(v,w)
			if grado_entrada[w] == 0:
				cola.append(w)
	return peso, salida



def main():
	graph = Grafo()
	graph.agregar_vertice('A','sochi')
	graph.agregar_vertice('B','moscu')
	graph.agregar_vertice('C','mondongo')
	graph.agregar_vertice('D','samara')
	graph.agregar_vertice('E','kazan')
	graph.agregar_vertice('F','rostov')

	graph.agregar_arista('A','B',1)
	graph.agregar_arista('A','C',2)
	graph.agregar_arista('B','C',3)
	graph.agregar_arista('C','F',4)
	graph.agregar_arista('D','E',5)
	graph.agregar_arista('D','F',6)
	graph.agregar_arista('F','E',5)

	camino = orden_topologico(graph)

	n = len(camino[1])
	for i in range(n):
		if i == n-1:
			print (camino[1][i])
		else:
			print (camino[1][i], end = " -> ")
	print ("Costo total:", camino[0])

main()