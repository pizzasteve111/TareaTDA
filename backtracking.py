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

#4 
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


#5

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

#8

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

#9


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

#10


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


#11

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

#12


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


#13

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


#14

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

#15

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

#16
#No pueden parar dos colectivos del mismo color en la misma parada
#por eso mismo, habría que crear un grafo nuevo con los mismos vertices(colectivos)
#pero que los adyacentes al colectivo no compartan su color

from grafo import Grafo

def pintar_colectivos(colectivos, paradas):
    #creo el grafo nuevo
    grafo=Grafo(vertices_init=colectivos)
    for parada in paradas:
        #entonces creamos adyacencias entre colectivos basado en sus paradas
        for i in range(len(parada)):
            for j in range(i+1,len(parada)):
                colectivo_1,colectivo_2=parada[i],parada[j]
                if not grafo.estan_unidos(colectivo_1,colectivo_2):

                    grafo.agregar_arista(colectivo_1,colectivo_2)
    
    return coloreo_backtracking(grafo,colectivos,paradas)

def coloreo_backtracking(grafo,colectivos,paradas):
    #originalmente, todos tienen el color 0
    colores={c:0 for c in colectivos}

    #originalmente, el color minimo sería un color especial para cada colectivo
    for cant_color in range(1,len(colectivos)+1):
        #si con esa cantidad de colores la funcion es True, entonces la devuelvo
        if coloreo_valido(grafo,colores,0,cant_color,colectivos):
            #cant minima a colorear
            return cant_color

    return len(colectivos)#en caso de no poder cumplir el objetivo, hay que pintar todos

def coloreo_valido(grafo,colores,v,cant_color,colectivos):
    #caso original donde pinto a cada uno de un color distinto
    if v==len(colectivos):
        return True
    
    #mi vertice actual
    actual=colectivos[v]

    for color in range(1,cant_color+1):
        #si no hay problema con el color, se lo asigno
        #racismo
        if es_valido_colorear(grafo,colores,actual,color):
            colores[actual]=color
            #voy iterando para los vertices siguientes
            if coloreo_valido(grafo,colores,v+1,cant_color,colectivos):
                return True
            #si en algun momento la funcion falla, entonces tengo que retroceder
            #le borro el color que le asigne al colectivo
            colores[actual]=0

    return False

#valida que ninguno de sus adyacentes comparta color
def es_valido_colorear(grafo, colores, v, color):
    
    for adyacente in grafo.adyacentes(v):
        if colores[adyacente] == color:
            return False
    return True

#17-Submarinos
#siento que es parecido al caso de coloreo
from grafo import Grafo
#Es un ejercicio parecido a un  vertex cover donde todo vertice del grafo tiene al menos
#una adyacencia a ese cover. En este caso serían los vertices serían las celdas con submarinos
#donde sus adyacencias seran submarinos que pueden ser iluminados por el mismo faro
#Es decir cada vertice tendrá la posicion del submarino en la grilla


def submarinos(matriz):
    vertices = []

    # Reviso si la matriz tiene submarinos
    for fila in matriz:
        if any(fila):  
            break
    else:
        return []  # Si no hay submarinos, retorno lista vacía

    # Agrego vértices para los submarinos (las posiciones en la matriz que tienen un submarino)
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna]:
                vertices.append((fila, columna))
    
    # Crear el grafo con los vértices (submarinos)
    grafo = Grafo(vertices_init=vertices)

    # Conectar los submarinos en base al área de 2 cuadros de distancia
    for (fila, columna) in vertices:
        area = area_2_cuadros(fila, columna, len(matriz), len(matriz[0]))
        for (x, y) in area:
            if (x, y) in vertices and (x, y) != (fila, columna):
                if not grafo.estan_unidos((fila, columna), (x, y)):
                    grafo.agregar_arista((fila, columna), (x, y))

    # Ordenar vértices por la cantidad de adyacentes (priorizamos vértices que cubren más área)
    vertices_ordenados = sorted(vertices, key=lambda v: len(grafo.adyacentes(v)), reverse=True)

    # Llamo a la función de backtracking para encontrar el mínimo conjunto de faros
    mejor_res = []
    mejor_res = backtracking_vertex_cover_min(grafo, mejor_res, [], 0, vertices_ordenados, set(), len(vertices))

    return mejor_res

def backtracking_vertex_cover_min(grafo, mejor_res, res_act, indice, vertices, iluminados, num_vertices_totales):
    # Si ya cubrimos todos los submarinos o llegamos al final de los vértices
    if len(iluminados) >= num_vertices_totales:
        if not mejor_res or len(res_act) < len(mejor_res):
            mejor_res.clear()
            mejor_res.extend(res_act)
        return mejor_res

    if indice >= len(vertices):
        return mejor_res

    actual = vertices[indice]
    adyacentes_actual = grafo.adyacentes(actual)

    # Opción 1: Incluir el vértice actual en la solución
    res_act.append(actual)
    nuevos_iluminados = iluminados.union({actual}).union(adyacentes_actual)
    mejor_res = backtracking_vertex_cover_min(grafo, mejor_res, res_act, indice + 1, vertices, nuevos_iluminados, num_vertices_totales)

    # Opción 2: No incluir el vértice actual en la solución
    res_act.pop()
    mejor_res = backtracking_vertex_cover_min(grafo, mejor_res, res_act, indice + 1, vertices, iluminados, num_vertices_totales)

    return mejor_res

def vertex_valido(grafo, iluminados, vertices):
    # Verificar si todos los submarinos están cubiertos (iluminados)
    return all(v in iluminados for v in vertices)

def area_2_cuadros(i, j, fila, columna):
    area = []
    # Los max y min están para que no se pase de índice de la matriz
    for x in range(max(0, i - 2), min(fila, i + 3)):
        for y in range(max(0, j - 2), min(columna, j + 3)):
            area.append((x, y))
    return area

#solución con matrices-gpteada

def encontrar_submarinos(matriz):
    submarinos_pos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]:
                submarinos_pos.append((i, j))
    return submarinos_pos

def calcular_celdas_iluminadas(faro, filas, columnas):
    direcciones = [(dx, dy) for dx in range(-2, 3) for dy in range(-2, 3)]
    iluminadas = set()
    x, y = faro
    for dx, dy in direcciones:
        nx, ny = x + dx, y + dy
        if 0 <= nx < filas and 0 <= ny < columnas:
            iluminadas.add((nx, ny))
    return iluminadas

def estan_todos_iluminados(submarinos_pos, iluminadas):
    return all(submarino in iluminadas for submarino in submarinos_pos)

def mejores_posiciones(submarinos_pos, filas, columnas):
    posiciones = []
    cobertura = {}
    for i in range(filas):
        for j in range(columnas):
            celdas_iluminadas = calcular_celdas_iluminadas((i, j), filas, columnas)
            cobertura[(i, j)] = sum(1 for sub in submarinos_pos if sub in celdas_iluminadas)
    
    posiciones = sorted(cobertura.keys(), key=lambda pos: cobertura[pos], reverse=True)
    return posiciones

def backtrack(submarinos_pos, faros, indice, filas, columnas, mejor_solucion, iluminadas, posiciones_candidatas):
    if estan_todos_iluminados(submarinos_pos, iluminadas):
        if len(faros) < len(mejor_solucion[0]):
            mejor_solucion[0] = list(faros)
        return

    if indice >= len(posiciones_candidatas):
        return

    x, y = posiciones_candidatas[indice]
    nuevas_iluminadas = iluminadas | calcular_celdas_iluminadas((x, y), filas, columnas)
    
    faros.append((x, y))
    if len(faros) < len(mejor_solucion[0]):
        backtrack(submarinos_pos, faros, indice + 1, filas, columnas, mejor_solucion, nuevas_iluminadas, posiciones_candidatas)
    faros.pop()
    
    backtrack(submarinos_pos, faros, indice + 1, filas, columnas, mejor_solucion, iluminadas, posiciones_candidatas)

def submarinos(matriz):
    if not matriz or not matriz[0]:
        return [] 
    
    filas = len(matriz)
    columnas = len(matriz[0])
    submarinos_pos = encontrar_submarinos(matriz)
    
    if not submarinos_pos:
        return [] 
    
    posiciones_candidatas = mejores_posiciones(submarinos_pos, filas, columnas)
    
    mejor_solucion = [submarinos_pos] 
    backtrack(submarinos_pos, [], 0, filas, columnas, mejor_solucion, set(), posiciones_candidatas)
    
    return mejor_solucion[0]



#18

def contar_ordenamientos(grafo):
    vertices=grafo.obtener_vertices()

    grados={v:0 for v in vertices}
    for v in vertices:
        for w in grafo.adyacentes(v):
            grados[w]+=1
    
    contador=[0]
    backtracking_topo(grafo,[],contador,grados)

    return contador[0]

def backtracking_topo(grafo,res_actual,contador,grados):
    vertices=grafo.obtener_vertices()

    for v in vertices:
        if grados[v]==0 and v not in res_actual:
            res_actual.append(v)

            for w in grafo.adyacentes(v):
                grados[w]-=1

            backtracking_topo(grafo,res_actual,contador,grados)

            res_actual.pop()
            for w in grafo.adyacentes(v):
                grados[w]+=1

    if len(res_actual)==len(vertices):
        contador[0]+=1

    
    return



    



