from pythoned import Grafo

def grafoDelCaballo(tamanoTablero):
    grafoCbllo = Grafo()
    for fil in range(tamanoTablero):
        for col in range(tamanoTablero):
            idNodo = pos_A_Id_Nodo(fil,col,tamanoTablero)
            posicionesNuevas = generarMovLegales(fil,col,tamanoTablero)
            for e in posicionesNuevas:
                nid = pos_A_Id_Nodo(e[0],e[1],tamanoTablero)
                grafoCbllo.agregarArista(idNodo,nid)
    return grafoCbllo

def pos_A_Id_Nodo(fila, columna, tamano_del_tablero):
    return (fila * tamano_del_tablero) + columna

def generarMovLegales(x,y,tamanoTablero):
    nuevosMovimientos = []
    desplazamientosEnL = [(-1,-2),(-1,2),(-2,-1),(-2,1),( 1,-2),( 1,2),( 2,-1),( 2,1)]
    for i in desplazamientosEnL:
        nuevoX = x + i[0]
        nuevoY = y + i[1]
        if coordLegal(nuevoX,tamanoTablero) and coordLegal(nuevoY,tamanoTablero):
            nuevosMovimientos.append((nuevoX,nuevoY))
    return nuevosMovimientos

def coordLegal(x,tamanoTablero):
    if x >= 0 and x < tamanoTablero:
        return True
    else:
        return False


def giraCaballo(n,ruta,u,limite):
    u.asignarColor('gris')
    ruta.append(u)
    if n < (limite -1) :
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

g = grafoDelCaballo(8)




"""
print("-------------------------------")
print( g.listaVertices )
for v in g:
    for w in v.obtenerConexiones():
        print("( %s , %s )" % (v.obtenerId(), w.obtenerId()))

print("")
print("-------------------------------")
"""
lista = g.listaVertices
n = 0
ruta = []
u = lista[4]
limite = 64

giraCaballo(n,ruta,u,limite)

print(  [x.id for x in ruta] )