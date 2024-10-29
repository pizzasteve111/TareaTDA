#EJ 1
#Primero hay que ver que sea NP
def validador_hitting_set(subconjuntos,solucion,m,k):
    if len(solucion)>k or len(subconjuntos)!=m:
        return False
    #itero cada conjunto que me dan
    #O(M*K) siendo m la cantidad de subconjuntos y k el tamaño de la solución
    for conjunto in subconjuntos:
        es_valido=False
        #itero los elementos de mi solucion, al menos uno debe estar en el conjunto iterado
        for elemento in solucion:
            if elemento in conjunto:
                es_valido=True
        if not es_valido:
            return False
    return True
#validador polinómico, por ahora es Np

#yo creo que una solución de dominating set es válido para hitting en cualquier combinación de subconjuntos del grafo que nos den
#esto porque el set que recibimos nos asegura que todos los vértices del grafo se conectan al set, ya sea perteneciendo o mediante adyacencias
#Sin importar como armemos nuestros subconjuntos, mediante dominating set siempre resolvemos hitting set pues las conexiones estan aseguradas(al menos una vez para cada conjunto).
#Entonces hitting set es al menos tan difícil como dominating set. En este caso, son problemas equivalentes y por tanto, es NP-C.

#EJ2 un arbol sería un grafo dirigido y acíclico donde se puede armar un único camino para cada par de vértices.
#Terminar.

#EJ3 minimo Dominating Set por prog lineal

#variables binarias donde valen 1 si se agregan al DS o 0 en caso contrario.
#minimo conjunto donde todos los vertices estan conectados con todo el grafo
#Entonces para el vertice Vi y su adyacente Wi, su sumatioria tiene que ser Vi + sum(Wi)>=1 donde uno de los dos debe pertenecer
def getMinDS(grafo,valores):
    #asumo que valores es un dic que almacena el valor de cada vertice
    vertices=grafo.obtener_vertices()
    j={}
    res=[]
    problema=pulp.LpProblem("DS",pulp.LpMinimize)
    for v in vertices:
        j[v]=pulp.LpVariable(f"j{v}",cat="Binary")
    
    problema+=pulp.LpSum(j[v]*valores[v] for v in vertices)

    for v in vertices:
        #la restricción >=1 se debe a que siempre queremos que para un conjunto de conexiones
        #solo tengamos un vertice, pero puede ser que nos tengamos que obligar a conectar dos vertices del mismo conjunto
        #de conexiones para asegurar el conjunto total.
        problema+=j[v]+ pulp.LpSum(j[w]for w in grafo.adyacentes(v))>=1
    
    problema.solve()

    for v in vertices:
        if pulp.value(j[v])==1:
            res.append(v)
    return res


#EJ 4 Idem del anterior, pero por backtracking

def minDS(grafo):
    suma_total=0
    vertices=grafo.obtener_vertices()
    for v in vertices:
        suma_total+=v.valor()
    
    return backtrack_ds(grafo,vertices,[],[],0,suma_total,0)

def backtrack_ds(grafo,vertices,res_parcial,res_final,indice,suma_total,suma_parcial):
    if ds_valido(grafo,res_parcial,vertices):
        if len(res_parcial)<len(res_final) and suma_parcial<suma_total:
            res_final.clear()
            res_final.extend(res_parcial)
        return res_final
    if indice>=len(vertices):
        return res_final
    if suma_parcial>suma_total:
        return res_final
    actual=vertices[indice]
    suma_parcial+=actual.valor()


    res_parcial.append(actual)
    backtrack_ds(grafo,vertices,res_parcial,res_final,indice+1,suma_total,suma_parcial)
    res_parcial.pop()
    suma_parcial-=actual.valor()

    #esto sería res_final
    return backtrack_ds(grafo,vertices,res_parcial,res_final,indice+1,suma_total,suma_parcial)

def ds_valido(grafo,res_parcial,vertices):
    for v in vertices:
        if v not in res_parcial:
            valido=False
            for w in grafo.obtener_adyacentes(v):
                if w in res_parcial:
                    valido=True
            #si el vertice ni ninguno de sus adyacentes pertenece al set, no es dominante
            if not valido:
                return False
    return True

#EJ 5 Min_suma DS con grafo dirigido, osea que los vertices solo tienen adyacencia con su siguiente y su anterior
#Sabiendo que en un Dominating set no deberían estar el vertice y algunos de sus adyacentes(salvo casos muy fortuitos)
#deberíamos ver si, para un Vi, me compensa agregar el valor de dicho vértice o el de alguno de sus adyacentes
#Algo como comparar el valor de Vi con el min(Wi)
#Opt(i)=min((Valor Vi),(Valor Wi para todo Wi en adyacentes),(Valor Vi+Wi))
#Muy parecido a Juan el Vago
def min_ds_pd(grafo):
    vertices=grafo.obtener_vertices()
    n=len(vertices)
    opt=[("inf")]*(n+1)
    opt[1]=vertices[0].valor()
    opt[2]=min(vertices[0].valor(),vertices[1].valor())
    for i in range(3,n+1):
        opt[i]=min(
            #Para cubrir Vi, me quedo con el valor De Vi-1 + lo acumulado antes
            opt[i-2]+vertices[i-1].valor(),
            #Idem como en el anterior pero con Vi-2 que sería su otra adyacencia
            opt[i-2]+vertices[i-2].valor(),
            #Para cubrir a Vi, aporto el valor de sus dos adyacencias
            opt[i-3]+vertices[i-1].valor()+vertices[i-2].valor(),
            #No tengo en cuenta el valor de los adyacentres, pero si el del vertice actual
            opt[i-2]+vertices[i].valor()
                   )
    
    return opt[n]



    



                




