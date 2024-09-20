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




    



