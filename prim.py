from pythoned import ColaPrioridad, Grafo, Vertice
import sys

def prim(G,inicio):
    cp = ColaPrioridad()
    for v in G:
        v.asignarDistancia(sys.maxsize)
        v.asignarPredecesor(None)
    inicio.asignarDistancia(0)
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in G])
    while not cp.estaVacia():
        aux = cp.eliminarMin()
        verticeActual = aux[1]
        for verticeSiguiente in verticeActual.obtenerConexiones():
            nuevoCosto = verticeActual.obtenerPonderacion(verticeSiguiente)

            t = []
            for x in cp.listaMonticulo:
                if x != 0:
                    t.append(x[1].obtenerId())
                    
            if verticeSiguiente.obtenerId() in t and nuevoCosto < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarPredecesor(verticeActual)
                verticeSiguiente.asignarDistancia(nuevoCosto)
                cp.decrementarClave(verticeSiguiente,nuevoCosto)

g = Grafo()

g.agregarVertice("A")
g.agregarVertice("B")
g.agregarVertice("C")
g.agregarVertice("D")
g.agregarVertice("E")
g.agregarVertice("F")
g.agregarVertice("G")

g.agregarArista("A","B",2)
g.agregarArista("B","A",2)
g.agregarArista("A","C",3)
g.agregarArista("C","A",3)
g.agregarArista("C","B",1)
g.agregarArista("B","C",1)
g.agregarArista("B","E",4)
g.agregarArista("E","B",4)
g.agregarArista("B","D",1)
g.agregarArista("D","B",1)
g.agregarArista("C","F",5)
g.agregarArista("F","C",5)
g.agregarArista("D","E",1)
g.agregarArista("E","D",1)
g.agregarArista("E","F",1)
g.agregarArista("F","E",1)
g.agregarArista("F","G",1)
g.agregarArista("G","F",1)

inicio = g.listaVertices['A']

prim(g,inicio)

print( [ (x.obtenerId(), x.obtenerDistancia()) for x in g ])



