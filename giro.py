from pythoned import Grafo

def giraCaballo(n,ruta,u,limite):
    u.asignarColor('gris')
    ruta.append(u)
    if n < limite - 1:
        listaVecinos = list(u.obtenerConexiones())
        i = 0
        hecho = False
        while i < len(listaVecinos) and not hecho:
            if listaVecinos[i].obtenerColor() == 'blanco':
                hecho = giraCaballo(n+1, ruta, listaVecinos[i], limite)
            i = i + 1
        if not hecho:  # prepararse para retroceder
            ruta.pop()
            u.asignarColor('blanco')
    else:
        hecho = True
    return hecho

g = Grafo()

g.agregarVertice("A")
g.agregarVertice("B")
g.agregarVertice("C")
g.agregarVertice("D")
g.agregarVertice("E")
g.agregarVertice("F")

g.agregarArista("A","B",5)
g.agregarArista("A","D",2)
g.agregarArista("B","C",4)
g.agregarArista("B","D",9)
g.agregarArista("D","E",7)
g.agregarArista("E","B",3)
g.agregarArista("E","F",1)
g.agregarArista("F","C",8)

lista = g.listaVertices

n = 0
ruta = []
u = lista["A"]
limite = 6

giraCaballo(n,ruta,u,limite)

print(  [x.id for x in ruta] )
