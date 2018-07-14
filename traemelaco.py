#!/usr/bin/pythonw

#tp con python 2.6

import sys
from TDAgrafo import *
from tejotools import *





def interfaz():
    parametros = sys.argv
    #./traemelaco ciudades.csv mapa.kml
    # if (len(sys.argv)!=3:
    #     print('Error')


    csv = parametros[1]

    #ruta en hold
    ruta_exportar_kml = parametros[2]

    #cargo el grafo en memoria:
    grafo = Grafo()
    parsear_archivo_grafo(csv,grafo)

    #print(grafo.vertices)

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
