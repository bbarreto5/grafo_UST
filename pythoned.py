class Vertice:
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}

    def agregarVecino(self,vecino,ponderacion=0):
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self,vecino):
        return self.conectadoA[vecino]

class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def agregarVertice(self,clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        return self.listaVertices.keys()

    def __iter__(self):
        return iter(self.listaVertices.values())


def matriz_adyacencia(grafo):
    n = len(grafo.listaVertices)
    m = [0]* n
    for f in range(0,n,1):
        m[f]=[0]*n
    for v in grafo:
        for vv in [x for x in v.conectadoA]:
            m[v.obtenerId()][vv.id] = v.obtenerPonderacion(vv)
    return m

def lista_adyacencia(grafo):
    n = len(grafo.listaVertices)
    l = [0]* n
    for f in range(0,n,1):
        l[f]={}
    for v in grafo:
        for vv in [x for x in v.conectadoA]:
            l[v.obtenerId()][vv.id] = v.obtenerPonderacion(vv)
    return l

g = Grafo()

for i in range(6):
    g.agregarVertice(i)

g.agregarArista(0,1,5)
g.agregarArista(0,5,2)
g.agregarArista(1,2,4)
g.agregarArista(2,3,9)
g.agregarArista(3,4,7)
g.agregarArista(3,5,3)
g.agregarArista(4,0,1)
g.agregarArista(5,4,8)
g.agregarArista(5,2,1)

print ( g.listaVertices )

for v in g:
    for w in v.obtenerConexiones():
        print("( %s , %s )" % (v.obtenerId(), w.obtenerId()))

m_a = matriz_adyacencia(g)
print ( m_a)

l_a = lista_adyacencia(g)
print( l_a )
