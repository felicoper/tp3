# import itertools
#
# from tejotools import *
# from traemelaco import *
#
# def pairwise(iterable):
#     a, b = itertools.tee(iterable)
#     next(b, None)
#     return itertools.izip(a, b)
#
# """ Devuelve un archivo KML trazando la ruta por lo indicado por parametro. """
# def kmlparser(grafo,comando,ruta,trayecto):
#     if (len(trayecto)==0):
#         return
#
#     print(ruta)
#     print(trayecto)
#
#
#     inicio = trayecto[0]
#     fin = ruta[len(trayecto)-1]
#
#     comando = str(' '.join(comando))
#
#     archivo = open(ruta,'w')
#
#     #Header KML
#     archivo.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
#     archivo.write("<kml xmlns=\"http://earth.google.com/kml/2.1\">\n")
#     archivo.write("	<Document>\n")
#     archivo.write("		<name>" + comando + "</name>")
#
#     #Sedes KML
#     for sede in range(0,len(trayecto)):
#         archivo.write("		<Placemark>")
#         archivo.write("			<name>" + sede + "</name>")
#         archivo.write("			<Point>")
#         archivo.write("<coordinates>"+ formato_coordenada(grafo,vertice) + "</coordinates>")
#         archivo.write("			</Point>")
#         archivo.write("		</Placemark>")
#
#
#     #Traza de rutas en KML.
#     #hay que usar itertools
#     for sede in range(0,len(trayecto)-1):
#         try:
#             print(trayecto[sede+1])
#             #par = trayecto[sede+1]
#             #saco el arista de actual y luego del par
#             print(grafo.obtener_dato_vertice(sede))
#             #grafo.obtener_dato_vertice(par)
#
#         except IndexError:
#             break
#
#
#     #Footer KML
#     archivo.write("	</Document>")
#     archivo.write("</kml>")
#
#     archivo.close()
#
#     return
