#EJ 1 
#Tenemos un grafo ordenado donde la arista que sale del Vi siempre apunta a un Vj con i<j.
#Camino mas largo=supongo que sería aquel que abarque mas vertices?
#el optimo del primer vertice V0 sería 0 porque no hay ningun camino largo hacia ese
#Para el V1 su camino mas largo sería la conexión con V0 o 0 en caso de que no lo conecte.
#¿Como calculo la conexión mas larga para cada vértice?
#Podemos setear todas las longitudes de los vertices en un valor estandar, luego recorrer cada vertice y al mismo tiempo todos los anteriores a este
#Preguntando si, dado un vertice actual Vi, hay un vertice anterior Vk que esten conectados y si camino(Vk)+Vi es mayor a camino(Vi)
#Ec recurrencia= opt(Vi)=Max(camino[Vi],Camino[Vk]+Vi)


#Complejidad, en los ciclos voy(primero) a iterar todos los vertices y así mismo sus anteriores. Entonces termina siendo O(V*V)
def camino_mas_largo(grafo):
    #originalmente, dado el caso de que cualquie Vi no tenga un camino precedente, no tiene camino posible(0)
    optimos=[0]*len(grafo.vertices())
    #para la reconstrucción, voy agregandole a cada vertice su anterior
    predecesor=[-1]*len(grafo.vertices())
    for actual in range(1,len(grafo.vertices())):
        for anterior in range(0,actual):
            #si el anterior esta unido con el actual, puedo entrar en comparacion
            if grafo.estan_unidos(anterior,actual)and optimos[anterior]+1 > optimos[actual]:
                #comparo entre si me conviene pisar el valor actual dado a que el anterior tiene un camino + largo(incluyendo al actual) o si no hace falta
                optimos[actual]=optimos[anterior]+1
                predecesor[actual]=anterior
    
    #La lista de optimos tiene para cada indice i el tamaño del camino mas largo del Vi. Entonces, si consigo la longitud maxima, puedo conseguir el vertice 
    #por el que termina este camino y de ahí arrancar mi reconstrucción
    camino_mas_largo=max(optimos)
    ult_vertice=optimos.index(camino_mas_largo)
    res=[]
    
    #voy para atras en los predecesores asignados, cuando llego a -1 significa que no hay predecesor asignado
    while ult_vertice!=-1:
        res.append(ult_vertice)
        ult_vertice=predecesor[ult_vertice]
    #devuelvo el inverso porque fui del final del camino hacia el inicio
    res.reverse()
    return res



#Ej 3 arbol==> estructura mínima de conexión

#necesito la menor cant de vertices
def min_IS(grafo):
    iset=set()
    visitados=set()
    vertices=grafo.obtener_vertices()
    cola=queue()
    cola.encolar(vertices[0])

    #O(V) porque se recorren todos los vértices al menos una vez
    while cola:
        v = cola.desencolar()
        if v not in visitados:
            visitados.add(v)
            iset.add(v)

            for w in grafo.adyacentes(v):
                visitados.add(w)
                cola.encolar(w)

    return iset

#Para resolver este ejercicio globalmente, debemos ir al caso local para el vértice. Si un V pertenece al Independent Set, ninguno de sus adyacentes puede pertenecer. ¿Cómo podemos
#Asegurar una solución local para cada vertice? podemos preguntar a cada vertice si ya fue visitado, en caso negativo signfica que con el recorrido anterior en ningún momento pudimos conectar con este,
#por lo que se convierte en un candidato del IS, luego recorremos todas sus conexiones y las agregamos como ya visitadas para que se descarten como candidatas.
#Entonces, asegurando este caso de optimo local, repitiendolo iterativamente podemos asegurar un optimo local. La solución es optima para cualquier arbol porque aseguramos cubrir todas las conexiones
#del vertice que no pertenecía previamente al set.

#EJ 4 dos grafos son isomorfos si simplemente renombrando los vertices de uno en el otro, se comparten las mismas conexiones.
#Deben tener misma cant de vertices y aristas, teniendo equivalencias en todos el grafo. Básicamente, es como decir que esos dos grafos son iguales
#Pero se llaman distinto. En este caso se habla de que en un Grafo G1 se pueda formar un subgrafo que este incluído a otro grafo G2

#El enunciado nos recuerda K-Clique ==> en este problema conseguimos un conjunto de  vertices donde todos tienen conexiones entre sí.
#Viendo los ejemplos del enunciado, podríamos crear un clique al grafo G1

def validador_clique(g1,g2,sub_g1):
    if len(g1.obtener_vertices())!=len(g2.obtener_vertices()):
        return False
    inicio=sub_g1[0]
    for v in g2.obtener_vertices():
        if len(g1.obtener_adyacentes(inicio))==len(g2.obtener_vertices(v)):
            #si encuentro una similitud de adyacencias, pruebo con los adyacentes al vertice
            




#EJ5 no indican técnica de programación. Será por lineal??
#Los vertices seran variables binarias que indican si pertenecen o no
#función objetivo: Si todos los vertices del clique deben estar conectados entre si,
#entonces podemos decir que para cada v y sus adyacentes, el valor binario de v tiene que ser al menos igual al de sus adyacentes
#Es decir, si v es 1 entonces sus adyacentes deberían ser 1, pero si es 0, sus adyacentes pueden valer o no valer 1.
def getMaxClique(grafo):
    vertices=grafo.obtener_vertices()
    problema=pulp.LpProblems("Clique",pulp.LpMaximize)
    j={}
    clique=[]
    for v in vertices:
        j[v]=pulp.LpVariable(f"v{v}",cat="Binary")
    problema+=pulp.LpSum(j[v] for v in vertices)
    for v in vertices:
        #si conecto a un vertice al clique, tambien todos sus adyacentes deben pertenecer
        for w in grafo.adyacentes(v):
            #Si v pertenece al clique(vale 1) entonces sus adyacentes tmb deben valer 1
            #No hay que imponer con restricción de igual == porque nos obligaría a expandir el clique a todo el grafo y esto no siempre es posible
            #En cambio, con <= se entiende que puede ser que el vertice v sea omitido, pero su adyacente w puede pertenecer a un clique
            problema += j[v]<=j[w]
    problema.solve()

    for v in vertices:
        if pulp.LpValue(j[v])==1:
            clique.append(v)
    return clique


