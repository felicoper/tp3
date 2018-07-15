#!/usr/bin/pythonw
import sys
import heapq
from collections import deque
from TDAgrafo import *
from tejotools import *

""" Devuelve un archivo KML trazando la ruta por lo indicado por parametro. """
def exportar_kml(grafo,comando,ruta,trayecto):
    if (len(trayecto)==0):
        return

    inicio = trayecto[0]
    fin = trayecto[len(trayecto)-1]

    comando[len(comando)-1] = comando[len(comando)-1].rstrip('\n') #saco el \n

    comando = str(' '.join(comando))

    archivo = open(ruta,'w')

    #Header KML
    archivo.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
    archivo.write("<kml xmlns=\"http://earth.google.com/kml/2.1\">\n")
    archivo.write("	<Document>\n")
    archivo.write("		<name>" + comando + "</name>\n\n")

    #Sedes KML
    for sede in range(0,len(trayecto)):
        coordenadas = grafo.obtener_dato_vertice(trayecto[sede])


        archivo.write("		<Placemark>\n")
        archivo.write("			<name>" + str(trayecto[sede]) + "</name>\n")
        archivo.write("			<Point>\n")
        archivo.write("				<coordinates>" + str(coordenadas[0]) + ", " +  str(coordenadas[1]) + "</coordinates>\n")#+ formato_coordenada(grafo,vertice) + "</coordinates>")
        archivo.write("			</Point>\n")
        archivo.write("		</Placemark>\n")

    archivo.write("\n")
    #Traza de rutas en KML.
    for sede in range(0,len(trayecto)):
        try:
            act = trayecto[sede]
            prox = trayecto[sede+1]

            coord_actual = grafo.obtener_dato_vertice(act)
            coord_prox = grafo.obtener_dato_vertice(prox)

            archivo.write("		<Placemark>\n")
            archivo.write("			<LineString>\n")
            archivo.write("				<coordinates>" + str(coord_actual[0]) + ", " + str(coord_actual[1]) + " " + str(coord_prox[0]) + ", " + str(coord_prox[1]) + "</coordinates>\n")
            archivo.write("			</LineString>\n")
            archivo.write("		</Placemark>\n")

        except IndexError:
            break


    #Footer KML
    archivo.write("	</Document>\n")
    archivo.write("</kml>")

    archivo.close()

    return

""" Devuelve un archivo csv similar al original con los caminos reducidos."""
def exportar_csv(grafo,mst,ruta):

    vertices = grafo.obtener_vertices()

    vertices_ordenados = sorted(list(grafo.obtener_vertices()))

    aristas = mst.obtener_aristas(dirigido = True)
    aristas.sort()

    archivo = open(ruta,"w")
    archivo.write(str(grafo.cantidad_vertices()) + "\n")
    for vertice in vertices_ordenados:
        coord = grafo.obtener_dato_vertice(vertice)
        archivo.write(vertice + "," + str(coord[0]) + "," + str(coord[1]) + "\n")

    archivo.write(str(len(aristas)) + "\n")
    for arista in aristas:
        archivo.write(arista[0] + "," + arista[1] + "," + str(arista[2]) + "\n")


    archivo.close()

    return

def parsear_linea(linea,comando):

    if comando=='ir':
        desde = ""
        hasta = ""
        pos_coma = 0

        if len(linea)>3: #va a pasar cuando sea san peterbursgo o rostov del don
            for campo in range(1,len(linea)):
                if linea[campo].endswith(','):
                    desde += linea[campo].rstrip(',')
                    pos_coma +=1
                    break
                pos_coma += 1
                desde += linea[campo] + " "
            for campo in range(pos_coma+1,len(linea)):
                hasta+= linea[campo] + " "
        hasta = hasta[:-1]
        return desde,hasta

    if comando=='viaje':
        origen = ""
        for campo in range(2,len(linea)):
            origen += linea[campo] + " "
        origen = origen[:-1]
        return origen

    return

def interfaz():
    parametros = sys.argv
    csv = parametros[1]
    ruta_kml = parametros[2]

    #cargo el grafo en memoria:
    grafo = Grafo()
    parsear_archivo_grafo(csv,grafo)

    for linea in sys.stdin.readlines():

        linea = linea.split()

        comando = linea[0]
        linea_parseada = parsear_linea(linea,comando)

        if comando=='ir':
            desde = linea_parseada[0]
            hasta = linea_parseada[1]

            recorrido = camino_minimo(grafo,desde,hasta)
            sys.stdout.write(' -> '.join(recorrido[0]) + "\n")
            sys.stdout.write("Costo total: " + str(recorrido[1]) + "\n")
            exportar_kml(grafo,linea,ruta_kml,recorrido[0])

        if comando=='viaje':
            modalidad = linea[1].rstrip(',')
            origen = parsear_linea(linea,comando)
            if modalidad=='optimo':
                recorrido = problema_viajante_bt(grafo,origen)
                sys.stdout.write(' -> '.join(recorrido[1]) + "\n")
                sys.stdout.write("Costo total: " + str(recorrido[0]) + "\n")
                exportar_kml(grafo,linea,ruta_kml,recorrido[1])
            elif modalidad == 'aproximado':
                recorrido = viajante_aproximado(grafo,origen)
                sys.stdout.write(' -> '.join(recorrido[1]) + "\n")
                sys.stdout.write("Costo total: " + str(recorrido[0]) + "\n")
                exportar_kml(grafo,linea,ruta_kml,recorrido[1])

        if comando =='itinerario':
            archivo = linea[1].rstrip(',')
            grafo_dirigido = parsear_recomendaciones(archivo,grafo)
            recorrido = orden_topologico(grafo_dirigido)
            sys.stdout.write(' -> '.join(recorrido[1]) + "\n")
            sys.stdout.write("Costo total: " + str(recorrido[0]) + "\n")
            exportar_kml(grafo,linea,ruta_kml,recorrido[1])

        if comando =='reducir_caminos':
            recorrido,arbol = arbol_tendido_minimo_prim(grafo)
            sys.stdout.write(' -> '.join(recorrido[0]) + "\n")
            sys.stdout.write("Costo total: " + str(recorrido[1]) + "\n")
            exportar_csv(grafo,arbol,archivo)

    return




interfaz()
