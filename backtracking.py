#Ej 1

def no_adyacentes(grafo, n):
    return backtracking(grafo,[],0,n)
    

def es_independiente(grafo,subconjunto):
    #para cada vertice del subconjunto, itero un posible par conectado
    for i in range(len(subconjunto)):
        for j in range(i+1,len(subconjunto)):
            if grafo.estan_unidos(subconjunto[i],subconjunto[j]):
                return False

    return True

def backtracking(grafo,subconjunto,inicio,n):

    if len(subconjunto)==n:
        #si llego al n pedido y todos son ind, devuelvo el conjunto
        if es_independiente(grafo,subconjunto):
            return subconjunto
        else:
            return None
    vertices=grafo.obtener_vertices()
    #itero sobre todos los vertices
    for i in range(inicio,len(vertices)):
        #voy agregando vertices
        subconjunto.append(vertices[i])
        #veo si esto cumple con la condicion
        resultado=backtracking(grafo,subconjunto,i+1,n)
        if resultado !=None:
            return resultado
        #si el vertice agregado rompe la condicion, lo elimino y agrego otro
        #elimino el ultimo pues antes estaba cumpliendo la condicion
        subconjunto.pop()
    return None

#EJ 2

def colorear(grafo, n):
    vertices=grafo.obtener_vertices()
    colores={}
    #seteo todos los colores en -12 un valor neutro
    for v in vertices:
        colores[v]=-12
    if backtracking_coloreo(grafo,vertices,colores,0,n):
        return True
    return False

def es_valido(grafo,v,colores,color):
    
    for w in grafo.adyacentes(v):
        #si el adyacente comparte color, no es npartito
        if colores[w]==color:
            return False
    return True

def backtracking_coloreo(grafo,vertices,colores,indice,n):
    #ya recorri todo el grafo y no me salto el False
    if indice==len(vertices):
        return True

    #vertice del indice actual
    v= vertices[indice]

    #empiezo a colorear a cada vertice
    for color in range(n):
        #si no hay problema con el color
        if es_valido(grafo,v,colores,color):
            #coloreo vertice
            colores[v]=color

            #voy coloreando a todo el grafo
            if backtracking_coloreo(grafo,vertices,colores,indice+1,n):
                return True

            #en caso de que no sea valido, le borro ese color al vertice
            #en la proxima iteracion voy a probar con un color nuevo
            colores[v]= -1

    return False


def independent_set(grafo):
    vertices=grafo.obtener_vertices()
    conjunto=[]
    max_conjunto=[]
    return backtracking(0,grafo,[],[],vertices)


def es_valido(grafo,conjunto,v):
    for u in conjunto:
        if grafo.estan_unidos(u,v):
            return False
    return True

def backtracking(indice,grafo,conjunto,max_conjunto,vertices):
    if indice==len(vertices):
        if len(conjunto)>len(max_conjunto):
            max_conjunto[0]=conjunto.copy()
        return max_conjunto
    
    v= vertices[indice]
    if es_valido(grafo,conjunto,v):
        conjunto.append(v)
        backtracking(indice+1,grafo,conjunto,max_conjunto,vertices)
        conjunto.pop()
    backtracking(indice+1,grafo,conjunto,max_conjunto,vertices)
    return max_conjunto
