#EJ 1
#2-Partition: Dado un subconjunto de valores N, es capazr
#de devolver dos subconjuntos donde la suma acumulada es igual. Es Npc

#¿Es subset sum NP?

#Validador en O(N)
def validador_ss(resultado,sub_arr,arr,valor):
    
    for elemento in sub_arr:
        if elemento not in arr:
            return False
    if  valor!=resultado:
        return False
    return True

#Sabemos entonces que 2_partition es al menos tan difícil como Ss

def sub_set(arreglo,valor):
    arreglo_falso=[valor]
    #entonces si yo por ejemplo le paso [1,3,4,7,8] y [5] me va a devolver[1,4] que es lo que resolvería SS
    resultado,_=partition_2(arreglo,arreglo_falso)
    valor_res=sum(resultado)
    if validador_ss(valor_res,resultado,arreglo,valor):
        return resultado
    return None
#Dado a que SS es NP y que se puede resolver a partir de un problema NP-c. Entonces SS es también un problema NP-c.
#EJ 3 ====> Es probable que tenga errores
def get_cicloK(grafo,k):
    vertices=grafo.obtener_vertices()
    #Pruebo con todas las posibilidades 
    for v in vertices:
        res=backtrack_ciclo(grafo,k,[v],0,grafo.obtener_vertices())
        if res:
            return res
    return None

def backtrack_ciclo(grafo,k,res,indice,vertices):
    if len(res)==k:
        if ciclo_valido(grafo,res):
            return res
        return None
    
    actual=vertices[indice]
    res.append(actual)
    backtrack_ciclo(grafo,k,res,indice+1,vertices)
    res.remove(actual)
    return backtrack_ciclo(grafo,k,res,indice+1,vertices)

def ciclo_valido(grafo,res):
    #Para que sea un ciclo valido, se deben poder recorrer todos los vértices y poder volver al primer grafo de origen
    #es decir, todos vertice debe estar unido a su consecutivvo
    primer_ver=res[0]
    ult_ver=res[-1]
    if not grafo.estan_unidos(primer_ver,ult_ver):
        return False
    for i in range(1,len(res)-1):
        if not grafo.estan_unidos(res[i],res[i+1]):
            return False
    return True

#EJ 5 problema de la mochila pero sin cantidades enteras, sino que se pueden particionar
# catalogo = (ml total, valor)
def atraco(catalogo,capacidad):
    items=[]
    res=[]
    #almaceno los fármacos en base a su relacion peso/valor
    for peso,valor in catalogo:
        items.append((valor/peso),valor,peso)
    #la ordeno de mayor a menor en base a la ganancia por ml acumulado
    items.sort(key=lambda x: x[0])
    items.reverse()
    for _,valor,peso in items:
        if peso<=capacidad:
            res.append(valor)
            capacidad-=peso
        else:
            res.append(valor*(capacidad/peso))
            #lleno la mochila todo lo que pueda
            break

    return sum(res)

