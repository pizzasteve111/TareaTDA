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
    if not vertices:
        return []
    conjunto=[]
    max_conjunto=[]
    
    return backtracking(0,grafo,[],max_conjunto,vertices)


def es_valido(grafo,conjunto,v):
    #verifico que el vertice que queremos appendear
    #no este unido a ninguno de nuestro conjunto previo
    for u in conjunto:
        if grafo.estan_unidos(u,v):
            return False
    return True

def backtracking(indice,grafo,conjunto,max_conjunto,vertices):
    #si ya recorri todas las iteraciones posibles al grafo
    if indice==len(vertices):
        #comparo si el conjunto acutal es mas grande al que ya tengo armado
        if len(conjunto)>len(max_conjunto):
            max_conjunto.clear()
            max_conjunto.extend(conjunto)
        return max_conjunto
    
    #vertice actual
    v= vertices[indice]
    #si se puede agregar el vertice al conjunto,
    #lo meto y llamo a la funcion recursiva ahora con el indice actualizado
    #en caso de que la funcion falle,
    #se eliminan vertices hasta encontrar el camino correcto
    if es_valido(grafo,conjunto,v):
        conjunto.append(v)
        backtracking(indice+1,grafo,conjunto,max_conjunto,vertices)
        conjunto.pop()
    #en caso de que popeo el vertice, significa que para ninguna combinacion
    #es util, entonces llamo a la funcion y lo omito complemtamente
    backtracking(indice+1,grafo,conjunto,max_conjunto,vertices)
    return max_conjunto



def camino_hamiltoniano(grafo):
    #voy probando para que vertice puedo conseguir el camino
    for v in grafo.obtener_vertices():
        ya_visitados=set()
        ya_visitados.add(v)
        res=[v]
        if  backtracking_hamilton(grafo,ya_visitados,res,0,v,grafo.obtener_vertices()):
            return res
    return None



def backtracking_hamilton(grafo,ya_visitados,res,indice,v,vertices):
    #si ya recorri todos los vertices del grafo, el camino es posible
    if len(ya_visitados)==len(vertices):
        return True
    
    #voy repitiendo los casos para los vertices vecinos a v
    for w in grafo.adyacentes(v):
        if w not in ya_visitados:
            ya_visitados.add(w)
            res.append(w)
            #si el vecino cumple, entonces lo agrego y llamo a la funcion
            #a partir de él
            if backtracking_hamilton(grafo,ya_visitados,res,indice,w,vertices):
                return True
            #caso donde un adyacente no cumple, lo elimino
            ya_visitados.remove(w)
            res.pop()

    return False

def hay_isomorfismo(g1, g2):
    v1=g1.obtener_vertices()
    v2=g2.obtener_vertices()
    #si son grafos dispares ya la corto
    if len(v1)!=len(v2):
        return False
    
    return backtracking_iso(g1,g2,v1,v2,{},set())

def iso_valido(g1,g2,imagen):
    #veo al vertice1 y sus adyacentes, comparo que la imagen de v1
    #en el g2 debe tener la misma relacion con sus respectivos adyacentes
    for v1 in g1.obtener_vertices():
        for w1 in g1.adyacentes(v1):
            #si v1 adyacente de w1, sus imagenes tmb lo son
            v2=imagen[v1]
            w2=imagen[w1]
            if not g2.estan_unidos(v2,w2):
                return False
    return True

def backtracking_iso(g1,g2,vertices1,vertices2,imagen,visitados):

    #si complete todas las imagenes del grafo, veo que se cumpla
    if len(imagen)==len(vertices1):
        return iso_valido(g1,g2,imagen)

    #itero sobre un grafo
    for v1 in vertices1:
        if v1 not in imagen:
            for v2 in vertices2:
                #si v2 no fue visitado y cumple mismas adyacencias
                #es candidato a ser imagen de v1
                if v2 not in visitados and len(g1.adyacentes(v1))==len(g2.adyacentes(v2)):
                    #lo agrego como imagen
                    visitados.add(v2)
                    imagen[v1]=v2
                    #si v1 y v2 son imagenes correctas , sigo de largo
                    if backtracking_iso(g1,g2,vertices1,vertices2,imagen,visitados):
                        return True
                    #si no son imagenes
                    #los libero
                    del imagen[v1]
                    visitados.remove(v2)
            break

    return False


def obtener_combinaciones(materias):
    resul=[]
    combinaciones=[]

    return backtracking_materias(materias,resul,combinaciones,0)



def backtracking_materias(materias,resul,combinaciones,indice):
    if len(materias)==indice:
        combinaciones.append(list(resul))
        return
    materia=materias[indice]
    

    for curso in materia:
        valido=True
        for posible in resul:
            if not son_compatibles(curso,posible):
                valido=False
                break
        
        if valido:
            resul.append(curso)
            backtracking_materias(materias,resul,combinaciones,indice+1)
            resul.pop()

    return combinaciones


def sumatoria_dados(n, s):

    return backtracking_dado(n,s,[],[],0,0)

def backtracking_dado(n,s,resul,combinacion,iteracion,suma):
    if iteracion==n:
        if suma==s:
            combinacion.append(list(resul))
        return

    for cara in range(1,7):
        if suma + cara <=s:
            resul.append(cara)
            backtracking_dado(n,s,resul,combinacion,iteracion+1,suma+cara)
            resul.pop()

    return combinacion

def sumatorias_n(lista, n):
    resultados = []  # Lista para almacenar todas las combinaciones válidas
    backtracking_suma(lista, [], resultados, 0, 0, n)
    return resultados

def backtracking_suma(lista, combinacion, resultados, indice, suma, n):
    # Caso base: si hemos considerado todos los elementos
    if suma == n:
        resultados.append(list(combinacion))
        return
    if indice >= len(lista) or suma > n:
        return

    # Incluir el elemento actual
    combinacion.append(lista[indice])
    backtracking_suma(lista, combinacion, resultados, indice + 1, suma + lista[indice], n)
    
    # Excluir el elemento actual (backtrack)
    combinacion.pop()
    backtracking_suma(lista, combinacion, resultados, indice + 1, suma, n)


def max_sumatoria_n(lista, n):
    return backtracking_sumatoria(lista,n,[],[],0,0)

def backtracking_sumatoria(lista,n,mejor_sol,sol_actual,suma,indice):
    #recorri toda la lista
    if indice==len(lista):
        #si justo llego a igualar n luego de la iteracion, mi mejor_sol va a ser la         actual
        if suma==n:
            mejor_sol.clear()
            mejor_sol.extend(sol_actual)
            return mejor_sol
        #si mi mejor sol no supera a n, devuelvo la sol actual
        if suma > sum(mejor_sol) and suma<n:
            mejor_sol.clear()
            mejor_sol.extend(sol_actual)
        #para el caso donde mi sol actual no es la mejor sol
        return mejor_sol

    numero=lista[indice]
    if suma+numero <=n:
        sol_actual.append(numero)
        backtracking_sumatoria(lista,n,mejor_sol,sol_actual,suma+numero,indice+1)
        sol_actual.pop()
    
    mejor_sol =backtracking_sumatoria(lista,n,mejor_sol,sol_actual,suma,indice+1)
    return mejor_sol


def vertex_cover_min(grafo):
    #inicialmente la mejor solucion son todos los vertices
    return backtracking_vertex(grafo,grafo.obtener_vertices(),[],0)

#osea, todas las aristas del grafo tienen por lo menos una conexion al vertex
def backtracking_vertex(grafo,mejor_res,res_actual,indice):
    vertices=grafo.obtener_vertices()

    #si consigo una sol actual menor a la mejor, la reemplazo
    if vertex_valido(grafo,res_actual,vertices):
        if len(res_actual)<len(mejor_res):
            mejor_res.clear()
            mejor_res.extend(res_actual)
        return mejor_res

    #termine de iterar el grafo
    if indice>=len(vertices):
        return mejor_res
    
    
    actual = vertices[indice]
    res_actual.append(actual)
    backtracking_vertex(grafo,mejor_res,res_actual,indice+1)
    res_actual.pop()
    d=set()
    d.re
    
    mejor_res=backtracking_vertex(grafo,mejor_res,res_actual,indice+1)
    return mejor_res


def vertex_valido(grafo,res_actual,vertices):
    #debe haber una conexion entre todos los vertices del grafo con el vertex
    for v in vertices:
        for w in grafo.adyacentes(v):
            if v not in res_actual and w not in res_actual:
                return False
    return True


def dominating_set_min(grafo):
    return backtracking_dominating_set(grafo,[],grafo.obtener_vertices(),0)

def backtracking_dominating_set(grafo,res_actual,mejor_res,indice):
    vertices=grafo.obtener_vertices()
    if set_valido(grafo,res_actual,vertices):
        if len(res_actual)<len(mejor_res):
            mejor_res.clear()
            mejor_res.extend(res_actual)
        return mejor_res
    
    if indice>=len(vertices):
        return mejor_res

    actual=vertices[indice]
    res_actual.append(actual)
    backtracking_dominating_set(grafo,res_actual,mejor_res,indice+1)
    res_actual.pop()
    
    mejor_res=backtracking_dominating_set(grafo,res_actual,mejor_res,indice+1)
    return mejor_res

def set_valido(grafo,res_actual,vertices):
    es_valido=True
    for v in vertices:
        if v not in res_actual:
            es_valido=False
        for w in grafo.adyacentes(v):
            #si v o uno de sus adyacentes esta en el set, ese v es valido
            # y salto al prox vertice
            if  w   in res_actual:
                es_valido=True
        if not es_valido:
            return False
            

    return True

def max_grupos_bodegon(P, W):
    #cada indice de P te dice la cant de personas de dicho grupo
    #W son los lugares en total
    #devolver los grupos que maximizan los lugares
    
    return backtracking_bodegon(P,W,[],[],0)

def backtracking_bodegon(P,W,res,mejor_res,indice):
    if indice==len(P):
        if sum(res)>=sum(mejor_res):
            mejor_res.clear()
            mejor_res.extend(res)
        return mejor_res
    
    actual=P[indice]

    if sum(res)+actual<=W:
        res.append(actual)
        backtracking_bodegon(P,W,res,mejor_res,indice+1)
        res.pop()
    mejor_res=backtracking_bodegon(P,W,res,mejor_res,indice+1)
    return mejor_res



    



