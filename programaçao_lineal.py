#ejercicios de la guia:https://algoritmos-rw.github.io/tda_bg/material/guias/pl/
#cabe aclarar que para este caso no hay herramienta de corrección de los ejercicios así que las implementaciones pueden tener errores leves


import pulp
#es una forma de llamar mas bonito a las sumatorias que tiene PuLP
from pulp import LpAffineExpression as Sumatoria
#importarse una implementación de grafo
from Grafo import grafo

#1 (valor,peso)
def mochila(v: list[int],w: list[int],W: int):
    #es res
    y=[]
    #y se appendea variables con el indice de los elementos
    #son de categoria binaria, osea que indican dos estados(True,False)
    #para ver si lo agregamos a la mochi o no
    for i in range(len(v)):
        y.append(pulp.LpVariable("y"+str(i),cat="Binary"))

    #voy a buscar maximizar
    problem=pulp.LpProblem("products",pulp.LpMaximize)
    #la sumatoria de la variable por la constante peso siendo menores al W
    problem+=Sumatoria([y[i],w[i]]for i in range(len(v))) <=W
    #sumatoria de los valores
    problem+=Sumatoria([y[i],v[i]]for i in range(len(v)))

    problem.solve()

    return list(map(lambda yi : pulp.value(yi),y))

#2 Lazy Johnnn

#mi variable es j(i) donde vale 1 si trabajo el dia i, o vale 0 en caso contrario
#buscamos maximizarlo, entonces deberiamos plantear una sumatoria de
# el monto(i)*la variable j => sum(valor(i)*j(i))
#  pero sabemos que los dias no pueden solaparse, entonces deberiamos plantear
#   que la variable actual + variable siguiente se mantengan menor o igual a 1
#con esta restriccion aseguramos que mi variable que valga 1 se solape con variables
#que valen 0
def lazy_john(dias):
    #aca guardo mis variables binarias
    j=[]
    #indicamos que queremos maximizar
    problema=pulp.LpProblem("max_ganancia",pulp.LpMaximize)
    for i in range(len(dias)):
        #seteo variables binarias
        j.append(pulp.LpVariable("x"+i,cat="Binary"))

    #planteo la inecuacion
    problema+=Sumatoria(dias[i]*j[i]for i in range(len(dias)))

    #planteo restriccion
    for c in range(len(dias)-1):
        problema+=j[c]+j[c+1]<=1

    problema.solve()

    return list(map(lambda ji : pulp.value(ji),j))


#3 min Vertex Cover ==> todos los vertices tienen adyacencias con el conjunto del cover
#en papel es un poco parecido a juan el vago pues no puede haber solapamiento entre
#variables vecinas
#en este caso queremos el minimo conjunto de vertices para los cuales todo el grafo tiene adyacencia
#con los vertices del cover. El vertex cover maximo seria el grafo mismo

#La inecuacion tendria una variable j(i) binaria que indica si debe o no debe
#ser asignada, asi mismo las j(k) para k siendo adyacentes de i deben ser menores o iguales a 1

#j[k]+j[i]>=1 pues idealmente solo uno de esas dos debe valer 1, pero las dos juntas
#no pueden sumar 0 porque sino la regla del vertex cover no se cumple

def vertex_cover_min(grafo):
    res=[]
    j={}
    vertices=grafo.obtener_vertices()

    problema=pulp.LpProblem("min_cover",pulp.LpMinimize)
    for v in vertices:
        j[v]=pulp.LpVariable("j",cat="Binary")
    
    problema+=pulp.lpSum(j[v] for v in vertices)

    for v in vertices:
        for w in grafo.adyacentes(v):
            problema+=j[v]+j[w]<=1

    problema.solve()

    for v in vertices:
        if pulp.value(j[v])==1:
            res.append(v)


    return res

#4 Dominating-set minimo = el conjunto mas pequenio posible donde todo v del grafo tiene conexiones con los vertices del set
#Muy parecido al anterior, solo que no hace falta que todas las aristas tengan por lo menos un vertice, sino que con que este el vertice
#o alguno de sus adyacentes ya cumple

def dom_set_min(grafo):
    res=[]
    j=[]
    vertices = grafo.obtener_vertices()

    problema=pulp.LpProblem("min_set",pulp.LpMinimize)

    for v in vertices:
        j[v]=pulp.LpVariable(f"j{v}",cat="Binary")

    for v in  vertices:
        problema+=j[v] 

    for v in vertices:
        ws=grafo.adyacentes(v)
        problema+=j[v] + pulp.Sumatoria(j[w] for w in ws)

    problema.solve()

    res.extend[(v for v in  vertices if pulp.Value(j[v])==1)]

    return res

#5 No idea manito

#6 MST ===> conjunto de aristas que une todos los vertices del grafo y minimiza el peso de sus aristas
# Se ve compliqueti, todos nuestros vertices tienen que estar conectados en un grafo sin ciclos
# habria que minimizar la suma de aristas por su peso
#algo del estilo sum(peso[a]*a) siendo a una arista

def mst_min(grafo):
    j=[]
    aristas=grafo.obtener_aristas()
    vertices=grafo.obtener_vertices()

    problema = pulp.LpProblem("mst_minimize",pulp.LpMinimize)

    #cada arista del grafo es una variable binaria
    for (v,w) in aristas:
        j[(v,w)]=pulp.LpVariable(f"j{(v,w)}",cat="Binary")

    #no me acuerdo si existia el metodo obtener peso :P pero de ultima 
    #la implementation seria la misma solo que hacemos v=>adyacenteW
    #obtener_peso(v,w)
    for (v,w) in aristas:
        problema +=pulp.Sumatoria(grafo.obtener_peso()*j[a])

    #ahora tenemos que asegurar que eun vertice se conecte con una arista
    for v in vertices:
        adyacentes=grafo.adyacentes(v)
        
        problema+=pulp.LpSum()

    #incompleto
    problema.solve()


# 7   Independent Set Maximo => conjunto de vertices donde ninguno es adyacente del otro, quiero la cantidad máxima
#cada vertice es una variable binaria donde indican si debe ser asignada, asi mismo todos los adyacentes w deben valer 0 para el vertice asignado
# sum(J[v]+J[w]<=1) osea que entre el vertice y sus adyacentes puede haber solo una asignación

def max_IndSet(grafo):
    #es bastante mas cómodo asignar las variables binarias con un diccionario que con una lista
    j={}
    res=[]
    vertices=grafo.obtener_vertices()

    problema = pulp.LpProblem("ind_set",pulp.LpMaximize)

    for v in vertices:
        j[v]=(pulp.LpVariable(f"j{v}",cat="Binary"))

    problema+=pulp.lpSum(j[v] for v in vertices)

    #restricción
    for v in vertices:
        for w in grafo.adyacentes(v):
            problema+=j[v]+j[w]<=1

    problema.solve()

    for v in vertices:
        if pulp.value(j[v])==1:
            res.append(v)
    
    return res

#8 min colores de un grafo => el vertice v tiene que tener distinto color a sus adyacentes, creo que para este caso no sería útil usar variables binarias como antes. 
#

def min_color(grafo):
    vertices=grafo.obtener_vertices()
    #en el peor de los casos, cada vertice tiene que tener su propio color
    colores_max=len(vertices)
    j={}
    res={}
    problema= pulp.LpProblem("coloreo",pulp.LpMinimize)

    for v in vertices:
        #variables enteras cuyo valor abarca del 1 al colores_max
        j[v]=pulp.LpVariable(f"j{v}",lowBound=1,upBound=colores_max,cat="Integer")

    for v in vertices:
        for w in grafo.adyacentes(v):
            #restriccion del color
            problema+= abs(j[v]-j[w])>=1

    problema.solve()

    for v in vertices:
        res[v]=pulp.value(j[v])

    return res



    


    




