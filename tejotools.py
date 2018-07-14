import csv
import heapq
from collections import deque
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

def costo_trayecto(grafo,trayecto):

    costo = 0

    for sede in range (0,len(trayecto)):
        try:
            act = trayecto[sede]
            prox = trayecto[sede+1]

            costo += grafo.obtener_peso_arista(act,prox)
        except IndexError:
            break

    return costo


def reconstruir_ciclo(padre, origen, destino):
    camino = []
    actual = destino
    while actual != origen:
        camino.insert(0,actual)
        actual = padre[actual]
    camino.insert(0,origen)
    return camino

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

    trayecto = reconstruir_ciclo(padre,inicio,fin)
    costo = costo_trayecto(grafo,trayecto)

    return trayecto,costo


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



def problema_viajante_bt(grafo, origen):

	visitados = []
	mejor_recorrido = [(INF, [])]
	_problema_viajante_bt(grafo, origen, origen, visitados, mejor_recorrido, 0)
	mejor_recorrido[0][1].append(origen)
	return mejor_recorrido[0]


def _problema_viajante_bt(grafo, origen, v, visitados, mejor_recorrido, recorrido_actual):
		visitados.append(v)
		if len(visitados) == grafo.cantidad_vertices():
			return grafo.obtener_peso_arista(v, origen)

		if recorrido_actual > mejor_recorrido[0][0]:
			return 0

		for w in grafo.obtener_adyacentes(v):
			if w not in visitados:
				recorrido_actual += grafo.obtener_peso_arista(v, w)
				siguiente = _problema_viajante_bt(grafo, origen, w, visitados, mejor_recorrido, recorrido_actual)
				recorrido_actual += siguiente

				if len(visitados) == grafo.cantidad_vertices() and recorrido_actual < mejor_recorrido[0][0]:
					mejor_recorrido[0] = (recorrido_actual, visitados[:])

				visitados.pop()

				recorrido_actual -= (grafo.obtener_peso_arista(v,w) + siguiente)
		return recorrido_actual

def obtener_arista_minima(grafo, vertice, visitados):
	arista_minima = (INF, None)
	for adyacente in grafo.obtener_adyacentes(vertice):
		if adyacente not in visitados:
			peso = grafo.obtener_peso_arista(vertice, adyacente)
			if arista_minima[0] > peso:
				arista_minima = (peso, adyacente)
	return arista_minima


def viajante_aproximado(grafo, inicio):
	visitados = []
	peso_camino = 0
	camino_eficiente = _viajante_aproximado(grafo, inicio, inicio, visitados, peso_camino)

	return camino_eficiente


def _viajante_aproximado(grafo, origen, inicio, visitados, peso_camino):
	visitados.append(inicio)

	if len(visitados) == grafo.cantidad_vertices():
		peso_camino += grafo.obtener_peso_arista(inicio, origen)
		visitados.append(origen)
		return peso_camino, visitados

	arista_minima = obtener_arista_minima(grafo, inicio, visitados)
	peso_camino += arista_minima[0]
	return _viajante_aproximado(grafo, origen, arista_minima[1], visitados, peso_camino)
