#!/usr/bin/pythonw
import sys

from TDAgrafo import *
from tejotools import *

""" Devuelve un archivo KML trazando la ruta por lo indicado por parametro. """
def exportar_kml(grafo,comando,ruta,trayecto):
    if (len(trayecto)==0):
        return

    inicio = trayecto[0]
    fin = trayecto[len(trayecto)-1]

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


def interfaz():
    parametros = sys.argv

    csv = parametros[1]
    ruta_kml = parametros[2]

    #cargo el grafo en memoria:
    grafo = Grafo()
    parsear_archivo_grafo(csv,grafo)

    for comando in sys.stdin.readlines():
        comando = comando.split(' ')
        if (len(comando)==3):
            if(comando[0]=='ir'):
                desde = comando[1].rstrip(',')
                hasta = comando[2].rstrip('\n')

                #llamo a camino minimo.
                #a camino minimo hay que hacerle devolver una lista del peso de las aristas tambien.
                recorrido = camino_minimo(grafo,desde,hasta)

                sys.stdout.write(' -> '.join(recorrido[0]) + "\n")
                sys.stdout.write("Costo total: " + str(recorrido[1]) + "\n")
                exportar_kml(grafo,comando,ruta_kml,recorrido[0])


            elif (comando[0] == 'viaje'):
                pass
                if(comando[1] == 'aproximado'):
                    pass#llamo viaje aproximado
                elif(comando[1]=='optimo'):
                    pass#llamo viaje optimo

        elif (len(comando)==2): #aca puede ser itinerario recomendaciones.csv o reducir_caminos
            pass



    return




interfaz()
