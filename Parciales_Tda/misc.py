#Archivo de miscelaneo para hacer ejs de todo tipo

def bolsas(articulos,capacidad):
    #cada bolsa debería recorrer los artículos y appendear lo que pueda?
    bolsas=[]
    articulos.sort()
    articulos.reverse()
    #complejidad=O(A*b)
    for a in articulos:
        colocado=False
        for bolsa in bolsas:
            if sum(bolsa)+a<=capacidad:
                bolsa.append(a)
                colocado=True
        if not colocado and a<=capacidad:
            bolsas.append([a])
    return bolsas

print(bolsas([8,6,4,2],10))

#En que casos no se cumple la condición optima?
#Considero que es optimo porque nuestra búsquedad del optimo local hace comparar a todos los artículos con las bolsas existentes y sino crea una nueva
#Ademas que vamos de mayor a menor así que con esto aseguramos de que los valores pequeños siempre puedan encontrar un lugar en las bolsas mas limitadas

#simil al problema de scheduling
def arnook(kilometros):
    permisos=[]
    #ordeno de fin mas próximo a menos proximo
    kilometros.sort(key=lambda x: x[1])
    
    fin=0
    for ini,fin_ruta in kilometros:
        #el pedido arranca despues de lo ya solicitado, entonces es válido garantizarlo
        if ini>=fin:
            permisos.append((ini,fin_ruta))
            fin=fin_ruta
    return permisos

from grafo import Grafo
def obtener_invitados(conocidos):
    personas=set()
    res=[]
    for p1,p2 in conocidos:
        if p1 not in personas:
            personas.add(p1)
        if p2 not in personas:
            personas.add(p2)

    grafo=Grafo(vertices_init=personas)
    #Los vertices son personas y sus adyacencias sus conocidos
    for p1,p2 in conocidos:
        if not grafo.esta_unidos(p1,p2):
            grafo.agregar_arista(p1,p2)
    
    for v in personas:
        if len(grafo.adyacentes(v))>=4:
            res.append(v)
    return res

#Demostrar que Dominating Set es NP-C
#Vertex Cover es NP-C

def validador_dominating(grafo,res,k):
    if len(res)>k:
        return False
    vertices=grafo.obtener_vertices()
    #O(v*W) en el peor de los casos es V cuadrático
    for v in vertices:
        ok=False
        for w in res:
            if v==w or grafo.estan_unidos(v,w):
                ok=True
        if not ok:
            return False
    return True

def getDS(grafo,k):
    #Yo puedo resolver un vertex cover donde me devuelve el conjunto de vertices que cubren todas las aristas
    #Lo que restaría buscar sería aquellos vertices que se escapan de conexiones establecidas por el cover(por ejemplo, donde el vertice no tiene aristas) y agregarlo
    vertices=grafo.obtener_vertices()
    cover=vertex_cover(grafo)
    res=cover.copy()
    for v in vertices:
        ok=False
        for w in cover:
            if v==w or grafo.estan_unidos(v,w):
                ok=True
        if not ok:
            res.append(v)
    if validador_dominating(grafo,res,k):
        return res
    return None

#De la misma manera puedo obtener un vertex cover a partir de un Dominating Set
#Lo que habría que hacer es recorrer los adyacentes del set y ver si hay aristas entre estos

#Lo podría hacer por programación lineal
def min_VC(grafo):
    j={}
    vertices=grafo.obtener_vertices()
    res=[]
    problema=pulp.LpProblem("minVC",pulp.Minimize)
    for v in vertices:
        j[v]=pulp.LpVariable(f"v{v}",cat="Binary")
    problema+=[j[v] for v in vertices]
    for v in vertices:
        for w in grafo.adyacentes(v):
            #La condición j[v]+j[w]>=1 indica que si ha
            problema+=j[v]+j[w]>=1

    problema.solve()
    for v in vertices:
        if pulp.Value(j[v])==1:
            res.append(v)

    return res
#Para un DS deberíamos asegurar que el valor binario de v*la sumatoria de binarios de sus adyacentes sea por lo menos 1
#Asegurando así la mínima conxeión entre v para todos sus adyacentes
def min_DS(grafo):
    j={}
    vertices=grafo.obtener_vertices()
    res=[]
    problema=pulp.LpProblem("minVC",pulp.Minimize)
    for v in vertices:
        j[v]=pulp.LpVariable(f"v{v}",cat="Binary")
    problema+=[j[v] for v in vertices]
    for v in vertices:
        problema+= j[v]+pulp.LpSum(j[w]for w in grafo.adyacentes(v))>=1
    problema.solve()
    for v in vertices:
        if pulp.Value(j[v])==1:
            res.append(v)

    return res

#Problema mochila
#(costo,ganancia)
#podemos trabajarlo como problema mochi
#si al arreglo lo transformamos en (ganancia-costo) y maximizacmos eso
def carlitos(campañas,P):
    res=[]
    items=[]
    for costo,ganancia in campañas:
        items.append(ganancia/costo,costo,ganancia)
    #ordeno de mayor relación ganancia/costo a menor
    items.sort(key=lambda x:x[0])
    items.reverse()

    for _,costo,ganancia in items:
        if costo<=P:
            res.append(ganancia)
            P-=costo
    return sum(res)

#EJ ruta, Es lo mismo que un scheduling pero con rango de cobertura
#Si tengo la primer casa en el km5 y la ruta tiene rango 3
#Me convendría ubicarla en el km8 y así cubro de 5 a 11km
def ruta(casas,rango):
    #de km + cercano a km + lejano
    casas.sort()#Complejidad O(n log N)
    cobertura_act=(0,0)
    antenas=[]
    res=[]
    #Complejidad es O(N) siendo N el tam del arreglo casas
    for casa in casas:
        if casa < cobertura_act[0] or casa > cobertura_act[1]:
            cobertura_act[0],cobertura_act[1]=casa,casa+rango
        
            antenas.append(cobertura_act)
    for antena in antenas:
        res.append(antena[1]-rango)
    return res

#El algoritmo propuesto es óptimo porque siempre se busca ubicar la antena
#de manera que cubra la casa actual, pero ubicada lo mas lejos posible
#para maximizar el rango de cobertura.
#Cumplimos con la técnica de programación greedy porque siempre nos 
#aseguamos que, para encontrar el optimo global  que sería minimizar las antenas ubicadas,
#siempre buscamos el optimo local que sería ubicar la antena de modo que cubra a la casa iterada
#pero este en el rango mas lejano posible de forma que maximice la cantidad de casas cubiertas.


#Problema mochila

def mochila(items,W):
    optimos=[[0 for _ in range(W+1)]*0 for _ in range(len(items)+1)]

    for fila in range(1,len(optimos)+1):
        for columna in range(1,W+1):
            #Para el item actual, puedo agregar el elemento porque no excede el peso iterado
            if items[fila-1][1]<=columna:
                optimos[fila][columna]=max(optimos[fila-1][columna],optimos[fila-1][columna-items[fila-1][1]]+items[fila-1][0])
            else:
                optimos[fila][columna]=optimos[fila-1][columna]

    return getRes(optimos,W,items)

def getRes(optimos,W,items):
    res=[]
    for i in range(0,len(optimos),-1):
        if optimos[i][W]!=optimos[i-1][W]:
            res.append(items[i-1])
            W-=items[i-1][1]

    res.reverse()
    return res

#por prog dinámica
#del tipo (ganancia,costo)
def carlitos_publicidad(campañas,C):
    optimos=[[0 for _ in range(C+1)]for _ in range(len(campañas)+1)]
    for fila in range(1,len(campañas)+1):
        for columna in range(1,C+1):
            if campañas[fila-1][1]<=C:
                optimos[fila][columna]=max(optimos[fila-1][columna],optimos[fila-1][columna-campañas[fila-1][1]]+campañas[fila-1][0])
            else:
                optimos[fila][columna]=optimos[fila-1][columna]

    return getRes(optimos,campañas,C)

def getRes(optimos,campañas,c):
    res=[]
    for i in range(0,len(optimos),-1):
        if optimos[i][c]!=optimos[i-1][c]:
            res.append(campañas[i-1])
            c-=campañas[i-1][1]

    res.reverse()
    return res

#Es el problema de la mochila, conocido como NPc
#El problema de carlitos es así mismo el problema de SUBSET SUM donde se busca llegar a un determinado valor
#Como puedo resolver el problema de la publicidad a través de Subset Sum? la realidad es que ambos problemas son en realidad equivalentes
#Es decir, son el mismo problema. Ambos tienen un valor objetivo (Capacidad en mochila, valor buscado en ss) y mediante un arreglo de valores
#buscan acercarse lo mas posible a dicho objetivo sin pasarse. Puede ocurrir que no se iguale el objetivo, pero nos aseguran que se maximizan las posibilidades

# Para re definirlos como problema de decisión. Tenemos que preguntarnos si es posible saber si para un determinado conjunto de valores y un valor objetivo, 
#es posible recibir una confirmación de que el problema se puede resolver o no.

#Para realizar una reducción polinomial de uno al otro tenemos que poder resolver un problema con el otro

# Publicidad <=p Figuritas

#Esta reducción es posible pues el problema de figuritas busca minimizar la cantidad de figuritas para alcanzar un valor y la publicidad busca
#maximizar las ganancias posibles dentro del presupuesto. Estos dos problemas son equivalentes pues minimizar cantidad = maximizar ganancias
#pues al minimizar la cantidad aseguramos usar solo las opciones mas valiosas. 

#De la misma manera Figuritas <=p Publicidad pues minimizar la cantidad de figuritas sería usar las mas valiosas lo que se traduce a gastar solo 
#en las campañas que traigan mayor ganancia.

#solo puedo aumentar en 1 o duplicar
#al ser la mínima cantidad de pasos, para el valor i, su optimo sería el mínimo entre opt[i-1]+1(el optimo del valor anterior + la nueva operación)
#y el optimo del valor anterior//2 + la nueva operación
def minimos_pasos(K):
    optimos=[(0)]*len(K)+1
    optimos[0]=0
    optimos[1]=1
    for i in range(1,len(K)):
       
        optimos[i]=min(optimos[i-1]+1,optimos[i//2]+1)
    
    return optimos[K]

#Path Selection ==> dado un número K me devuelve un conjunto de K caminos que no comparten nodos entre sí
#Independent Set ==> dado me devuelve el set de vértices no adyacentes de a lo sumo K vértices.

#Primero habría que re definir IS a problema de decisión y entonces para un un grafo y un valor K
#podemos afirmar o negar que existe un IS de ese tamaño.
#Para que IS sea npc, primero deber pertenecer a la familia de los NP y eso sería crear un validador polinomial

#IS es cuanto menos NP
def validador_IS(grafo,solucion,k):
    #solucion es un set de vertices
    if len(solucion)>k:
        return False
    vertices=grafo.obtener_vertices()
    #O(s cuadrático) siendo s la cantidad de vértices del set
    for v in solucion:
        #tengo que asegurar que ninguno de los vértices del IS esten unidos entre sí
        for w in solucion:
            if v!=w and grafo.estan_unidos(v,w):
                return False
    
    #Si no hay adyacencias en el set, debo verificar que conecten con todo el grafo
    #O(V*S)siendo V la cantidad de vértices totales y S los del set
    for v in vertices:
        ok = False
        for s in solucion:
            if v not in solucion and grafo.estan_unidos(v,s):
                ok=True
        if not ok:
            return False
    return True

#Ahora, para que sea NPC se podría hacer una reducción entre IS y Path Selection (y viceversa).

#Planteamos que IS <=p Path Selection

#Para esto, decimos que podríamos tener un grafo comun con vertices y adyacencias. Los paths podrían ser todos los vértices del grafo
#Entonces, a PathSelection le pasaríamos el grafo común, cada uno de los vértices como un path individual, y eso nos devolvería un conjunto K
# de vértices que no son adyacentes entre sí.


#función objetivo del dominating set que busca como mucho K vértices. Busco entonces minimizarlo
# Vi+sum(Wi)<=1 es decir, la sumatoria de Vi y sus adyacentes
#debe ser por lo menos 1 asegurando que esa adyacencia se cumple
def min_DS(grafo,k):
    j={}
    vertices=grafo.obtener_vertices()
    res=[]
    problema=pulp.LpProblem("a lo sumo k",pulp.Minimize)

    for v in vertices:
        j[v]=pulp.LpVariable(f"v{v}",cat="Binary")
    
    problema+=pulp.LpSum(j[v] for v in vertices)

    for v in vertices:
        #Mínimo se tiene que sumar 1 entre V y sus adyacentes
        problema+=j[v] + pulp.LpSum(j[w]for w in grafo.adyacentes(v))>=1
    problema.solve()

    for v in vertices:
        if pulp.LpValue(j[v])==1:
            res.append(v)
    if len(res)<=k:
        return res
    return None

#Demostrar que Dominating Set es NPC sabiendo que vertex cover es NPC.
#Si dominating Set es NP, entonces para que sea NPC debería poder resolver vertex cover
#Es decir, Vertex Cover <=p Dominating Set.

#Dado que DS es NP, obtener un vertex cover a partir de un dominating set se deberían asegurar que se dominen todas las aristas del grafo
#Podría crear un nuevo grafo donde los vértices son las aristas del grafo original y las conexiones se deben

def cambio_greedy(monedas,monto):
    res=[]
    actual=0
    monedas.sort()
    #ordeno de mayor a menor así trato de minimizar la cantidad
    monedas.reverse()
    for moneda in monedas:
        if moneda+actual<=monto:
            while moneda+actual<=monto:
                actual+=moneda
                res.append(moneda)
        else:
            continue
    
    return res

def minimizar_cajas(libros,l):
    libros.sort()
    libros.reverse()
    actual=0
    cajas=[[]]
    indice=0
    for libro in libros:
        if libro+actual<=l:
            cajas[indice].append(libro)
            actual+=libro
        else:
            cajas.append([libro])
            indice+=1
            actual=libro
    
    return cajas


def problema_viajante(grafo,inicio):
    visitados=set()
    vertices=grafo.obtener_vertices()
    visitados.add(inicio)
    costo=0
    actual=inicio
    camino=[inicio]

    while len(visitados)< len(vertices):
        vecino_mas_prox=None
        costo_min="infinito"
        for w in grafo.adyacentes(actual):
            if grafo.obtener_peso(actual,w)<=costo_min:
                costo_min=grafo.obtener_peso(actual,w)
                vecino_mas_prox=w
        visitados.add(vecino_mas_prox)
        camino.append(vecino_mas_prox)
        costo+=costo_min
        actual=vecino_mas_prox
    
    costo+=grafo.obtener_peso(actual,inicio)
    camino.append(inicio)

    return camino

def ds_min(grafo):
    dominados=set()
    ds_set=set()
    vertices=grafo.obtener_vertices()
    while len(dominados)<len(vertices):
        for v in vertices:
            if v not in dominados:
                ds_set.add(v)
                dominados.add(v)
                for w in grafo.adyacentes(v):
                    dominados.add(w)
    
    return ds_set

def ds_min(grafo):
    hojas=set()
    vertices=grafo.obtener_vertices()
    dominados=set()
    
    ds=set()
    for v in vertices:
        #si no tiene adyacentes mas que su padre
        if grafo.adyacentes(v)==1:
            hojas.add(v)

    while len(dominados)!=len(vertices):
        for hoja in hojas:
            for padre in grafo.adyacentes(hoja):
                if padre not in dominados:
                    ds.add(padre)
                    dominados.add(padre)
                    dominados.add(grafo.adyacentes(padre))
            #el padre debería convertirse en la nueva hoja
            hojas.add(padre)
        hojas.remove(hoja)
    return ds

def ds_suma_min(grafo):
    vertices=grafo.obtener_vertices()
    suma_inicial=sum(v.Valor() for v in vertices)
    return backtrack_ds(grafo,vertices,suma_inicial,[suma_inicial],[],0)

def backtrack_ds(grafo,vertices,suma_min,suma_act,conj,indice):
    if ds_valido(grafo,conj,vertices):
        if suma_act[0]<suma_min:
            suma_act.clear()
            suma_act.extend(suma_min)
        return suma_min

    if indice==len(vertices):
        return suma_min
    actual=vertices[indice]

    conj.add(actual)
    suma_act+=actual.valor()
    backtrack_ds(grafo,vertices,suma_min,suma_act,conj,indice+1)
    conj.remove(actual)
    suma_act-=actual.valor()
    backtrack_ds(grafo,vertices,suma_min,suma_act,conj,indice+1)

def ds_valido(grafo,conj,vertices):
    #el conjunto debe poder cubrir todos los vertices
    for v in vertices:
        ok=False
        for w in conj:
            if v==w or grafo.estan_unidos(v,w):
                ok=True
        if not ok:
            return False
    return True

#Hitting Set: dado un conjunto de elementos A, M subconjuntos y un numero k, ver si es posible crear otro subconjunto C de al menos k elementos
#Tales que al menos un elemento de cada subconjunto pertenezca a C.
#Dominating Set es NPC. Demostrar que Hitting es NPC. Para esto, habría que demostrar que es NP y, si hitting set puede resolver Dominating, entonces lo es.

#Primero defino un problema de decisión y es que dado los elementos A, los subconjuntos y k se puede
#afirmar o negar que existe un subconjunto que intersecte en todos de tamaño a lo sumo k.

#El problema de Hitting se podría modelar usando grafos. Donde los vértices sean los elementos de A y estos tengan como adyacentes a
#los elementos con los que pertenecen en el subconjunto.

def validador_hitting(A,subconj,C,k):
    if C>k:
        return False
    #Complejidad O(E*C) siendo E la cantidad de subconjuntos y c la cantidad de elementos en cada subconjunto
    for conjunto in subconj:
        for elemento in conjunto:
            ok=False
            if elemento not in C:
                ok=True
        if not ok:
            return ok
    return True

#Dado a que hitting set es un problema al menos NP. Si con este podemos resolver Dominant Set, entonces constituye un NPC.
#Planteandolo como DSet <=p Hitting Set.

#La realidad es que con un correcto modelado del grafo, ambos problemas son equivalentes pues buscar el hitting set de ese grafo modelado(teniendo todos los vertices como los elementos de A y las 
#adyacencias aquellos con los que comparte conjuntos), validaría la misma instancia que buscar un Dominating Set en ese grafo y con los mismos parámetros.

#Dominating Set de suma mínima para un  grafo camino
#Se tiene que asegurar que se cubran sus adyacentes y sume lo menos posible
#Al ser un grafo camino, todas los vertices conectan con su siguiente de manera directa y lineal.
#Es un problema de juan el vago pero minimizando la ganancia posible, para minimizar la ganancia y que sea DS, lo mejor sería solo agregar el vertice mínimo entre
# el actual, el anterior y el siguiente 
# Es decir, para un vértice i, su optimo sería opt(i)=min(suma+opt[i-1],suma+i.valor,suma+opt[i-1])

def min_suma_DS(grafo):
    vertices=grafo.obtener_vertices()
    optimos=[1000000000]*len(vertices)+1
    optimos[vertices[0]]=vertices[0].valor()
    optimos[vertices[1]]=min(vertices[0].valor(),vertices[1].valor())
    for i in range(2,len(vertices)-1):
        optimos[i]=min(optimos[i-1],optimos[i-2]+vertices[i].valor(),optimos[i-1])
    
    return optimos[len(vertices)+1]

#Un independent Set máximo sería aquel formado por los padres de cada rama
#Es decir, iría la raiz, luego me salteo sus hijos y agrego a sus "nietos" al set.
def max_IS(grafo):
    vertices=grafo.obtener_vertices()
    raiz=vertices[0]
    i_set=set()
    dominados=set()
    i_set.add(raiz)
    dominados.add(raiz)
    for w in grafo.adyacentes(raiz):
        dominados.add(w)
    
    while len(dominados)!=len(vertices):
        for v in vertices:
            if v not in dominados:
                i_set.add(v)
                dominados.add(v)
                for w in grafo.adyacentes(v):
                    dominados.add(w)
    
    return i_set


def max_clique(grafo):
    return back_track_clique(grafo,grafo.obtener_vertices(),[],[],0)

def back_track_clique(grafo,vertices,res_act,res_final,indice):
    if clique_valido(grafo,vertices,res_act):
        if res_act>res_final:
            res_final.clear()
            res_final.extend(res_act)
        return res_final
    
    if indice>=len(vertices):
        return res_final
    act=vertices[indice]

    res_act.append(act)
    back_track_clique(grafo,vertices,res_act,res_final,indice+1)
    res_act.pop()
    return  back_track_clique(grafo,vertices,res_act,res_final,indice+1)

def clique_valido(grafo,vertices,res):
    for v in res:
        
        for w in res:
            if v!=w and not grafo.estan_unidos(v,w):
                return False
            
    return True


def cambio_pd(monedas,monto):
    optimos=[10000000]*len(monedas)+1
    for moneda in monedas:
        for i in range(moneda+1,monto):
            optimos[i]=min(optimos[moneda],optimos[i-moneda]+1)
    return optimos[monto]

#Demostrar que Dominating Set es NPC sabiendo que Vc lo es.
#Es decir, validar que si se puede resolver DS para cierta instancia,
#Se puede resolver VC para esa misma instancia.

#resolver VC a partir de Dominating Set.




def dominating_set(grafo,k):
    sol=backtrack_ds(grafo,grafo.obtener_vertices(),[],[],0)
    if sol<=k:
        return sol
    return None

#busco maximizar el tamaño de mi set
def backtrack_ds(grafo,vertices,res_act,res_final,indice):
    if ds_valido(grafo,res_act,vertices):
        if len(res_act)<len(res_final):
            res_final.clear()
            res_final.extend(res_act)
        return res_final

    if indice==len(vertices):
        return res_final
    
    act=vertices[indice]

    res_act.append(act)
    backtrack_ds(grafo,vertices,res_act,res_final,indice+1)
    res_act.pop()
    backtrack_ds(grafo,vertices,res_act,res_final,indice+1)


#Variables binarias que indican si pertenecen o no al clique
#Problema de maximización
#Función objetivo: V +sum(todos los adyacentes a V)<=cantidad de adyacentes +1
def max_clique(grafo):
    res=[]
    j={}
    vertices=grafo.obtener_vertices()
    problema=pulp.LpProblem("clique",pulp.Maximize)
    for v in vertices:
        j[v]=pulp.LpVariable(f"v{v}",cat="Binary")
    
    problema+=pulp.LpSum(j[v] for v in vertices)

    for v in vertices:
        problema+= j[v] + pulp.LpSum(j[w] for w in grafo.adyacentes(v))<=grafo.adyacentes(v)+1

    problema.solve()

    for v in vertices:
        if pulp.LpValue(j[v])==1:
            res.append(v)
    return res

#Minimizar los costos de operaciones
#El día inicial arrancamos en aquel que tenga menor costo de los dos
#Para el día siguiente habría que ver si es mas barato mudarse y asumir
#Los costos de la otra ciudad o quedarse en la actual
#Algo como opt(mes_i)=min(ciudad_actual(i),otra_ciudad(i)+costo)
#Tendríamos que estar acutalizando cual es la ciudad actual y cual es 
#la extranjera para cada iteración


















    



        
        
        
