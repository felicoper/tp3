import random

"""
- Tener alguna forma de iterarlo. ???
"""


class Vertice(object):

    def __init__(self,nombre,dato=None):
        self.nombre = nombre
        self.dato = dato
        self.adyacentes = {} #Adyacentes es un diccionario de vertices cercanos

    def obtener_nombre(self):
        return self.nombre

    def obtener_dato(self):
        return self.dato


    def esta_conectado(self,vertice):
        if (vertice in self.adyacentes):
            return True
        else:
            return False

    def agregar_adyacentes(self,vertice,peso):
        self.adyacentes[vertice] = peso

    def obtener_adyacentes(self):
        return (self.adyacentes)

    def cantidad_adyacentes(self):
        return (len(self.adyacentes))


class Grafo(object):
    """grafo no dirigido"""
    def __init__(self):
        self.vertices = {}

    def cantidad_vertices(self):
        return (len(self.vertices))

    def agregar_vertice(self,id,dato=None):
        self.vertices[id] = Vertice(id,dato)

    def existe_vertice(self,id):
        if id not in self.vertices:
            return False
        return True

    #hay que hacer una para nombre ?
    def obtener_dato_vertice(self,id):
        if (self.existe_vertice(id)):
            return self.vertices[id].obtener_dato()
        return False

    def obtener_vertices(self):
        return (self.vertices.keys())

    #PRE: EL GRAFO TIENE VERTICES
    def obtener_vertice_random(self):
        claves = list(self.vertices.keys())
        return random.choice(claves)

    def borrar_vertice(self,id):
        if not self.existe_vertice(id):
            return False
        del self.vertices[id]
        for vertice in self.vertices:
            if id in self.obtener_adyacentes(vertice):
                del self.vertices[vertice].adyacentes[id]
        return True

    #conectar vertices
    def agregar_arista(self, a, b, peso = 1):

        if(self.existe_vertice(a) and self.existe_vertice(b) and not self.vertices[a].esta_conectado(b)):
            self.vertices[a].agregar_adyacentes(b,peso)
            self.vertices[b].agregar_adyacentes(a,peso)
            return True
        return False

    def existe_arista(self, a, b):
    	return b in self.vertices[a].adyacentes

    def obtener_peso_arista(self,a,b):
        if not self.existe_arista(a,b):
   	        raise KeyError("No existe la arista.")
        return self.vertices[a].adyacentes[b]


    def borrar_arista(self, a, b):
    	if not self.existe_arista(a,b):
    		return False
    	del self.vertices[a].adyacentes[b]
    	del self.vertices[b].adyacentes[a]
    	return True

    """
    PRE: Tiene que existir el vertice para que funcione
    POST: Devuelve una lista con los adyacentes de ID
    """
    def obtener_adyacentes(self,id):
        if(self.existe_vertice(id)):
            return list(self.vertices[id].obtener_adyacentes())
        return False

    def obtener_todos_vertices(self):
        return grafo.vertices.keys()

    def agregar_arista_dirigido(self, a, b, peso = 1):

        if(self.existe_vertice(a) and self.existe_vertice(b) and not self.vertices[a].esta_conectado(b)):
            self.vertices[a].agregar_adyacentes(b,peso)
            return True
