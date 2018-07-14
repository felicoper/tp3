#!/usr/bin/pythonw
import sys
import itertools

from TDAgrafo import *
from tejotools import *

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)

""" Devuelve un archivo KML trazando la ruta por lo indicado por parametro. """
def kmlparser(grafo,comando,ruta,trayecto):
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
    #hay que usar itertools
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
    #./traemelaco ciudades.csv mapa.kml
    # if (len(sys.argv)!=3:
    #     print('Error')


    csv = parametros[1]

    #ruta en hold
    ruta_kml = parametros[2]

    #cargo el grafo en memoria:
    grafo = Grafo()
    parsear_archivo_grafo(csv,grafo)

    #ir desde, hasta (len == 3 )
    #viaje optimo/aproximado, socchi (len == 3)
    #itinerario recomendaciones.csv (len==2)
    #reducir_caminos destino.csv (len==2)

    #pedir_comando = input()
    #while(pedir_comando!='N'):

    pedir_comando = raw_input()

    while (pedir_comando !='Q'):
        comando = pedir_comando.split(' ')
        if (len(comando)==3): #aca puede ir desde o viajero/optimo/aprox.
            if(comando[0]=='ir'):
                desde = comando[1]
                desde = desde[0:len(desde)-1] #saco la coma
                hasta = comando[2]

                #llamo a camino minimo.
                #a camino minimo hay que hacerle devolver una lista del peso de las aristas tambien.
                recorrido = camino_minimo(grafo,desde,hasta)
                print(recorrido)
                kmlparser(grafo,comando,ruta_kml,recorrido)


            elif (comando[0] == 'viaje'):
                pass
                if(comando[1] == 'aproximado'):
                    pass#llamo viaje aproximado
                elif(comando[1]=='optimo'):
                    pass#llamo viaje optimo

        elif (len(comando)==2): #aca puede ser itinerario recomendaciones.csv o reducir_caminos
            pass

        pedir_comando = raw_input()



    return




interfaz()
