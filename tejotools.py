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


def arbol_tendido_minimo_prim(grafo):
    inicio = grafo.obtener_vertice_random()

    visitados = set()
    visitados.add(inicio)

    mst = set()

    peso_total = 0

    heap = []

    for w in grafo.obtener_adyacentes(inicio):
        arista = (inicio,w)
        peso = grafo.obtener_peso_arista(inicio,w)
        heapq.heappush(heap,(peso,arista))

    arbol = Grafo()
    for vertice in grafo.obtener_vertices():
        arbol.agregar_vertice(vertice)
    #Tengo un grafo vacio sin aristas.

    while (heap):
        (peso,arista) = heapq.heappop(heap)
        if(arista[1] in visitados):
            continue
        else:
            arbol.agregar_arista(arista[0],arista[1],peso)
            peso_total += peso
            visitados.add(arista[1])
            mst.add((arista[0],arista[1],peso))
            for adyacente in grafo.obtener_adyacentes(arista[1]):
                peso = grafo.obtener_peso_arista(arista[1],adyacente)
                arista = (arista[1],adyacente)
                heapq.heappush(heap,(peso,arista))

    print (mst)

    return visitados,peso_total



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
