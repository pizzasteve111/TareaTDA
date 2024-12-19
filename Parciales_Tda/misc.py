from grafo import Grafo
import pulp
#greedy






#obtener el camino minimo dado un vertice de inicio el cual pase por todos los vertices una vez
#pero que minimice el costo de su vertice
#defino optimo local: para todo vertice: debería recorrer el adyacente de menor peso y que no haya visitado

def prob_viajante(grafo,ini):
    visitados=set()
    camino=[ini]
    vertices=grafo.obtener_vertices()
    visitados.add(ini)
    actual=ini
    while len(visitados)<len(vertices):
        minimo=100000000000
        for w in grafo.adyacentes(actual):
            if grafo.obtener_peso_arista(actual,w)<minimo and w not in visitados:
                minimo=grafo.obtener_peso_arista(actual,w)
                visitados.add(w)
                actual=w
                camino.append(w)
    return camino

#complejidad: O(v cuadrático) siendo v la cantidad de vertices pues el primer while corre una cantidad de v veces y luego se recorre el adyacente de ese vertice que, potencialmente, pueden ser
#todos los vertices del grafo. El algoritmo no es optimo porque no se consideran decisiones futuras.

def min_cajas(libros,l):
    n=len(libros)
    libros.sort(reverse=True)
    cajas=[[0]]
    caja_act=0
    #mi optimo local va a ser, si mi libro entra en la caja actual, lo agrego
    #sino, lo agrego a una nueva caja
    for i in range(n):
        libro=libros[i]
        if sum(cajas[caja_act])+libro<=l:
            cajas[caja_act].append(libro)
        else:
            cajas.append[libro]
            caja_act+=1

    return cajas, len(cajas)





#optimo local: para cada vertice, si no existe adyacente alguno que pertenezca al cover,
#lo agrego al cover para cubrir la arista
def min_VC(grafo):
    #tengo que cubrir todas las aristas del grafo con la minima cantidad de vertices
    vertices=grafo.obtener_vertices()
    aristas=grafo.aristas()
    visitados=set()
    cover=set()
    for v,w in aristas:
        if (v,w) in visitados or (w,v) in visitados:
            continue
        visitados.add((v,w))
        if v not in cover and w not in cover:
            if grafo.grado(v)>grafo.grado(w):
                cover.add(w)
            else:
                cover.add(v)
    return cover


def min_camino(grafo,ini):
    vertices=grafo.obtener_vertices()
    visitados=set()
    visitados.add(w)
    camino=[ini]
    actual=ini
    while len(visitados)!=len(vertices):
        peso_min=1000000000
        vertice_min=None
        for w in grafo.adyacentes(actual):
            if grafo.obtener_peso(w,actual)<peso_min:
                peso_min=grafo.obtener_peso(w,actual)
                vertice_min=w
            visitados.add(vertice_min)
            camino.append(vertice_min)
    return camino
        

#Backtracking

def ciclo(grafo,k):
    vertices=grafo.obtener_vertices()
    return backtrack_ciclo(grafo,vertices,[],[],0,k)

def backtrack_ciclo(grafo,vertices,res,res_act,indice,k):
    if ciclo_valido(grafo,res_act,k):
        if len(res)<len(res_act):
            res.clear()
            res.extend

    actual=vertices[indice]

    


def min_VC(grafo):
    return backtrack_vc(grafo,grafo.vertices(),[],grafo.vertices(),0)

def backtrack_vc(grafo,vertices,res,res_act,indice):
    if vc_valido(grafo,res_act,vertices):
        if len(res_act)<len(res):
            res.clear()
            res.extend(res_act)
        return res
    actual=vertices[indice]
    res_act.append(actual)
    backtrack_vc(grafo,vertices,res,res_act,indice+1)
    res_act.pop()
    return  backtrack_vc(grafo,vertices,res,res_act,indice+1)

def vc_valido(grafo,res_act,vertices):
    #tengo que asegurar que todas las aristas del grafo estén cubiertas
    aristas=grafo.aristas()
    a_act=set()

    for r in res_act:
        #agrego todas las aristas que cubre mi cover
        for w in grafo.adyacentes(r):
            a_act.add(r,w)
            a_act.add(w,r)
    #mi cover tiene que poder cubrir todas las aristas del grafo
    if len(aristas)!=a_act:
        return False
    return True



def bodegon_bt(grupos,W):
    return backtrack_bodegon(grupos,W,[],[],0)

def backtrack_bodegon(grupos,W,res,res_act,indice):
    #problema de la mochila, 
    if sum(res_act)<=W:
        if len(res)>len(res_act):
            res.clear()
            res.extend(res_act)
        return res
    if sum(res_act)+grupos[indice]<=W:
        res_act.append(grupos[indice])
        backtrack_bodegon(grupos,W,res_act,res,indice+1)
        res_act.pop()
    return backtrack_bodegon(grupos,W,res,res_act,indice+1)


#Reducciones
#resolver el npc mediante el np, NPC<=NP

#




#2-Partition:obtener dos subconjuntos tales que la suma de ambos sea igual
#Este es NPC, demostrar que Subset Sum lo es
#Osea, 2p<=Subset Sum

#es np
def validador_subset_sum(res,monto):
    return sum(res)==monto

#resolver 2partition mediante subset sum. 
#para obtener dos subconjuntos que sumen lo mismo mediante subset sum
#


#Prob coty
#que todas las n personas hablen de los regalos sabiendo que solo compras K regalos

#Primero valido que el problema de coty es NP:

#Luego, debo justificar que si resuelvo el problema de coty, puedo resolver un problema NPC conocido
#Elijo de ejemplo el problema de vertex cover.
#vertex cover <=p Coty
#Vertex cover implica un conjunto de vertices para los cuales
#se cubren todas las aristas del grafo. Esto es equivalente al problema de coty
#pues, si cubro todas las aristas en un cover de tamaño K, esto implicaría
#también poder cubrir a todas las personas minimizando lo mas posible la cantidad de regalos a dar.

#Es por eso que el problema de coty es NPC.


#Prob Hitting set: tengo n elementos del cual se desprenden m subconjuntos.
#Puedo crear un conjunto C<=K tal que al menos un elemento de cada subconjunto
#pertenezca a C?

#1) valido que es NP

def validador_HS(C,k,subconjuntos):
    if len(C)>k:
        return False
    for conjunto in subconjuntos:
        ok=False
        for elemento in conjunto:
            if elemento in C:
                ok=True
        if not ok:
            return False
    return True

#Ahora, para demostrar que es NPC, tengo que poder resolver un NPC mediante el hitting set
#Propongo el caso de Dominating Set. Dominating Set <=p Hitting problem
#esto es valido pues el dominating set propone un conjunto de vertices que conectan con todo el grafo
#y con hitting tambien se propone un conjunto de elementos que conecte con cada subconjunto.
#Puedo modelar un grafo para que cada vertice del subconjunto se conecte entre sí
#Entonces, si encuentro un hitting set de a lo sumo tamaño k, significa que tengo un conjunto de vertices
#donde por ejemplo hay una conexion con cada subconjunto

#ahora lo quiero resolver al revés, demostrar que dominating set es NPC sabiendo que Hitting set lo es

def validador_DS(grafo,res,k):
    if res>k:
        return False
    visitados=set()
    for elemento in res:
        visitados.add(elemento)
        for w in grafo.adyacentes(elemento):
            if w not in visitados:
                visitados.add(w)
    
    return len(visitados)==len(grafo.obtener_vertices())


#Dominating Set:

#Es NP pues puedo resolver el problema de decisión en tiempo polinomial.
def validador_DS(grafo,res,k):
    if len(res)>k:
        return False
    vertices=grafo.obtener_vertices()
    for v in vertices:
        ok=False
        for r in res:
            if grafo.estan_unidos(v,r):
                ok=True
        if not ok:
            return False
        
    return True

#sabemos que Vertex Cover es NPC. entonces podemos ver si Dominating set es npc si 
#una instancia de Dominating set resuelve vertex cover. Planteando que Vertex C <=p Dom.Set

#resolver el npc mediante el np.
#resolver vertex cover mediante dominating set

#dominating set me devuelve un conjunto de vertices que conectan todo el grafo
#vertex cover el conjunto de vertices que conectan todas las aristas

#puedo crear un grafo donde las aristas son tomadas como vertices y las conexiones entre estas
#aristas se da por las demas conexiones que había entre vertices. Es decir si en el grafo original
#la arista A tenía de extremo al vertice T y este verttice era adyacente a J.
#la arista representada como vertice que tenía en el extremo a A va a tener como vertice adyacente a 
#la arista que tenía de extremo a J. De esa manera, pedirle un dominating set a ese grafo
#arrojaría el conjunto de aristas que conectan a todo el grafo y de esta se desglosan los vértices

#Path selection, se tienen varios caminos sobre un grafo
#se pueden seleccionar k caminos tales que no compartan nodos?
#Path selection es NPC, IS es NP.
#planteo Path selection <=p Independent Set
#osea resolver Path selection mediante IS.

#Como ningun conjunto de los k caminos debe compartir vertice
#se puede plantear un grafo donde los vertices representen a los caminos
#y sus conexiones estén dadas por los vertices que se comparten entre los caminos
#obtener un independent set de k vertices devolvería un path selection de tamaño k.




#cliques:
#Demostrar que R cliques es NPC sabiendo que el problema de coloreo lo es.
#R cliques, se puede subdividir el grafo en r Cliques que no repiten vértices.

def validador_rCliques(grafo,cliques,r):
    if len(cliques)!=r:
        return False
    visitados=set()
    #valido que todos los vertices de cada clique se conectan entre sí
    for clique in cliques:
        for vertice in clique:
            for w in clique:
                if not grafo.estan_unidos(vertice,w) and vertice!=w:
                    return False
    #ahora valido que no se repitan vertices en otros cliques
    for clique in cliques:
        for vertice in clique:
            if vertice in visitados:
                return False
        visitados.add(vertice)

    return True

#planteo que Coloreo <=p R clique
#osea que una instancia de R clique debe ser valida como una instancia de Coloreo
#Resolver coloreo mediante R clique

#Un conjunto de X color son vertices donde ninguno es adyacente entre sí. Es decir, 
#vendría ser lo opuesto a un clique. 
#Si planteo un grafo alternativo donde los vertices son adyacentes a aquellos que no lo son
#en el grafo original, pedirle un R clique nos devolvería una instancia de R set de colores
                
#Demostrar que Dominating Set es Npc sabiendo que Vertex cover lo es
#osea planteo Vertex Cover<=p Dominating Set
#tengo que a partir de una instancia de dominating set, poder resolver Vertex Cover

#Vertex Cover cubre todas las aristas del grafo, dominating set todos los vertices asegurando las conexiones
#puedo  plantear un grafo donde las aristas son vértices y su conexión a otro vértice esta dada si
# esas dos aristas tienen vertice en común. De modo que a obtener un dominating set de ese grafo, obtengo un conjunto de vertices que 
#cubrirán todas las aristas




#Dinamica

#hay que encontrar un DS de suma mínima sobre un grafo de tipo camino
#es decir, cada nodo esta conectado solo a su anterior, queremos encontrar la suma mínima
#es como un juan el vago pero minimizando la ganancia
#camino
def min_ds(grafo):
    vertices=grafo.obtener_vertices()
    opt=[1000000000]*(len(vertices))

    #el mínimo para el primer elemento sería agregarlo
    opt[0]=vertices[0]
    opt[1]=min(vertices[0],vertices[1])

    for i in range(2,len(vertices)):
        #el optimo actual es el mínimo entre agregarlo o quedarse con el caso anterior
        opt[i]=min(opt[i-1],opt[i-2]+vertices[i])

    #de esta manera, primero me aseguro un ds de tamaño mínimo y a su vez que sume 
    #la menor cantidad posible de elementos

    res=[]
    n=len(vertices)

    while n>0:
        if opt[n]!=opt[n-1]:
            res.append(vertices[n])
        n-=1

    return res



#osvaldo
#almacenar para cada día el máximo valor obtenible
#hasta dicho día, y almacenando el día de compra
#algo como opt(i)=max(opt(i-1),dias(i)-dia_compra)
def osvaldo(dias):
    n=len(dias)
    opt=[0]*n
    #originalmente el día de venta es el primer día
    #un caso base como compro el primer día y si encuentro  un día mas bajo,
    #lo actualizo
    dia_compra=dias[0]
    for i in range(1,n):
        opt[i]=max(opt[i-1],dias[i]-dia_compra)
        #si el día actual vale menos que el dia de venta aconsejado, 
        #lo ac
        if dias[i]<dia_compra:
            dia_compra=dias[i]
    
    max_ganancia=max(opt)
    dia_venta=opt.index(max_ganancia)
    dia_compra_final=min(dias[:dia_venta])

    return dia_compra_final,dia_venta

    




#Bodegon:

#maximizar la cantidad de espacios otorgados
#me convendría ordenar de mayor a menor cosa que asegure asignar
#
def bodegon(grupos,w):
    n=len(grupos)
    opt=[[0]*(w+1)]*(n+1)

    for fila in range(n):
        for columna in range(w):
            if opt[fila-1]<=w:
                opt[fila][columna]=max(opt[fila-1][columna],opt[fila-1][columna-grupos[fila-1]]+grupos[fila-1])
            else:
                opt[fila][columna]=opt[fila-1][columna]
    
    return getRes(n,opt,w)

def getRes(n,opt,w,grupos):
    res=[]

    for i in range(n):
        if opt[i-1][w]!=opt[i][w]:
            res.append(grupos[i])
            w-=grupos[i]
    
    res.reverse()
    return res

#camino mas largo





def getNoSolapadas(charlas):

    no_solapada=[0*(len(charlas+1))]
    for i in range(len(charlas)):
        for j in range(0,i-1,1):
            #si el inicio de la charla actual es mayor al de la charla anterior
            #no se solapan
            if charlas[i][0]>=charlas[j][1]:
                #de esta forma, para cada charla i, obtengo su charla anterior que no la solapa
                no_solapada[i]=charlas[j]

    return no_solapada



#Juan el vago:
#Optimizar ganancia pero sin trabajar dos días seguidos. entonces para el i-esimo día,
#la ganancia maxima se decidiría entre el optimo de trabajar anteayer y hoy, o de trabajar ayer y saltearse el día actual

def juan_vago(dias):
    n=len(dias)
    optimos=[0 for _ in range(n)]
    optimos[0]=dias[0]
    optimos[1]=max(dias[0],dias[1])

    for i in range(2,n):
        optimos[i]=max(optimos[i-1],optimos[i-2]+dias[i-1])
    return optimos[n]

#elementos ubicados del tipo (valor,peso)
#para cada columna, almaceno el valor optimo 
def problema_mochila(elementos,W):
    n=len(elementos)
    optimos=[[10000 for _ in range(W+1)] for _ in range(n+1)]

    #para cada valor y capacidad actual, el optimo es si agregar otro elemento mas o no
    for fila in range(len(optimos)):
        for capacidad in range(len(optimos[0])):
            if elementos[fila-1][1]<=capacidad:
                optimos[fila][capacidad]=max(optimos[fila-1][capacidad],optimos[fila][capacidad-elementos[fila-1][1]]+elementos[fila-1][0])
            else:
                optimos[fila][capacidad]=optimos[fila-1][capacidad]
    
    return getRes(optimos,elementos,W,n)

def getRes(optimos,elementos,W,n):
    res=[]
    for i in range(n,0,-1):
        if optimos[i][W]!=optimos[i-1][W]:
            res.append(elementos[i-1])
            W-=elementos[i-1][1]
    return res


def jvago(dias):
    n=len(dias)
    opt=[0]*(n+1)
    opt[0]=dias[0]
    opt[1]=max(dias[0],dias[1])

    for i in range(2,n):
        #maximo entre incluir el día actual o el anterior
        opt[i]=max(opt[i-1],opt[i-2]+dias[i])
    
    res=[]
    #tengo que ir acumulando que días se van a ir incluyendo
    ganancia_max=0

    for i in range(n,1,-1):
        #si son distintos, significa que el i-esimo día es laborable
        if opt[i]!=opt[i-1]:
            res.append(dias[i])
            ganancia_max+=opt[i]

    res.reverse()
    return res,ganancia_max

#K pasos
#quiero la mínima cantidad de pasos para llegar a un valor K
#siendo las opciones aumentar de a 1 o duplicar el valor actual
#para alcanzar la mínima cantidad de pasos para un valor i,
#tengo que almacenar el mínimo entre el valor de los pasos de (i-1) +1 o de i//2 +1

def k_pasos(valor):
    opt=[1000000000 for _ in (valor)]

    opt[0]=0
    opt[1]=1

    for i in range(2,valor):
        opt[i]=min(opt[i-1]+1,opt[i//2]+1)

    return opt[valor]




#minimizar el costo de las operaciones, osea que para el mes i, su optimo tiene que ser el mínimo entre operar
#en la ciudad actual o si asumir los costos de mudanza e irse a otra ciudad
def londres_california(l,c,m):
    n=len(l)
    opt_c=[10000000 for _ in range(n)]
    opt_l=[1000000 for _ in range(n)]
    #estos arreglos indican los valores optimos tanto si empezamos en california como en londres
    opt_c[0]=c[0]
    opt_l[0]=l[0]

    for i in range(n):
        opt_c[i]=min(c[i],l[i]+m)
        opt_l[i]=min(l[i],c[i]+m)
    
    return getRes(opt_c,opt_l,n,m)

#funcion objetivo: sacar la maxima ganancia, es decir para el i-esimo día encontrar su máxima ganancia posible,
#osea un arreglo donde para el dia i se almacene la ganancia maxima posible si vendo ese día
#rastreo para el dia i cual es el precio mínimo al que podría comprar 
#algo como opt(i)=max(opt(i-1),dias[i]-precio_min[i])
def problema_osvaldo(dias):
    n=len(dias)
    precio_min=[100000 for _ in range(n)]
    optimos=[0 for _ in range(n)]
    dias_opt=[(10,10) for _ in range(n)]

    precio_min[0]=dias[0]
    optimos[0]=dias[0]

    for i in range(1,n):
        #actualizo el valor mínimo al que puedo comprar para el i-esimo día
        precio_min[i]=min(precio_min[i-1],dias[i])
        #considero que el valor maximo que puedo sacar para el i-esimo día es el valor para un día anterior
        #entonces voy a guardar el máximo valor que puedo sacar hasta el día i
        optimos[i]=max(optimos[i-1],dias[i]-precio_min[i])
        #almaceno el dia del precio minimo y el dia del precio maximo
        dia_precio_min=dias.index(dias[precio_min[i]])
        dia_precio_max=dias.index(dias[optimos[i]])
        dias_opt[i]=(dia_precio_min,dia_precio_max)

    dia_min,dia_max=0,0
    #ahora agarro el maximo de mi arreglo de optimos y le consigo los días aconsejados para comprar y vender
    dia_max=max(dias_opt).index()
    return


#camino maximo
#voy calculando el camino maximo de cada vertice
#el primer vertice no tiene camino hacia el mismo, 
#el segundo vertice tendría que preguntar si esta conectado al primero, si lo esta
#es el primero +1, sino, es 0
#para el tercero debería ver si ese vertice esta conectado al 
#ultimo vertice del camino mas grande, si lo esta, le sumo 1 y sino
#el optimo para el i-esimo vertice es el maximo entre el optimo del vertice anterior
#(osea el camino maximo hasta ese vertice) y el anterior vertice que lo conecta +1


#puedo encontrar el camino máximo
#Lineal:

#max independent Set
#quiero maximizar la cantidad de vertices que no estén conectados entre ellos
#pero que aseguren total conexión con todo el grafo
#planeto a cada vértice como una variable binaria
#Funcion objetivo: maximizar suma(xi*valor_binario)
#puedo plantear como restricción que si dos vértices están conectados
#solo uno de esos dos pueden pertenecer al IS
#algo como xi + suma(vi) <=1 siendo vi todos los vértices adyacentes

def max_IS(grafo):
    vertices=grafo.obtener_vertices()
    problema=pulp.LpProblem("max IS",pulp.LpMaximize)
    j={}
    for v in vertices:
        j[v]=pulp.LpVariable(f"v{v}",cat="Binary")
    
    for v in vertices:
        problema+=j[v]+pulp.LpSum(j[w] for w in grafo.adyacentes(v))<=1

    i_set=[]

    for v in vertices:
        if pulp.LpValue(j[v])==1:
            i_set.append(v)
    
    return i_set





#busco un dominating set mínimo, por lo tanto
#planteando cada vertice como una variable binaria,
#puedo decir que dados dos vertices conectados, la suma entre estos dos
#debe ser <=1 donde solo uno de los dos debe permanecer en la respuesta 
def dominating_set(grafo):
    vertices=grafo.obtener_vertices()
    problema=pulp.LpProblem("min DS",pulp.LpMinimize)
    j={}
    for v in vertices:
        j[v]=pulp.LpVariable(f"vertice{v}",cat="Binary")
    
    for v in vertices:
        for w in grafo.adyacentes(v):
            problema+=j[v]+j[w]>=1
    
    problema.solve()
    res=[]
    for v in vertices:
        if pulp.Value(j[v])==1:
            res.append(v)
    return res

#maximizar la ganancia obtenida sabiendo
#que no se trabajan en días consecuentes

#(valor,peso)
def mochila(elementos,W):

    j={}
    res=[]
    problema=pulp.LpProblem("maximizar mochila",pulp.LpMaximize)
    for elemento in elementos:
        j[elemento]=pulp.LpVariable(f"e{elemento}",cat="Binary")

    problema+=pulp.LpSum(elementos[elemento][0]*j[i] for i in range(len(elementos)))
    problema+=pulp.LpSum(elementos[elemento][1]*j[elemento] for elemento in elementos))<=W

    problema.solve()

    for elemento in elementos:
        if pulp.LpValue(j[elemento])==1:
            res.append(elemento)
    return res
    



    

    


















    



        
        
        
