#ejercicios de la guia:https://algoritmos-rw.github.io/tda_bg/material/guias/pl/


import pulp
#es una forma de llamar mas bonito a las sumatorias que tiene PuLP
from pulp import LpAffineExpression as Sumatoria
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

