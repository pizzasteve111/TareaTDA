#Ejercicios sacados de: https://algoritmos-rw.github.io/tda_bg/material/guias/reducciones/
# Clase no grabada: https://www.youtube.com/watch?v=rg1vwVsaJMo
# Video 3-SAT: https://www.youtube.com/watch?v=GCw07nZckps
#Ej 3-SAT:  https://www.youtube.com/watch?v=MV8Z_D1mLMU
#P-SPACE: https://www.youtube.com/watch?v=a_JXkCBQpX0

# CUANDO TERMINE ESTA GUÍA, SUBO UN PDF MAS BONITO PARA LEER 


#Problema P: Problema cuya solución es polinomial, osea, que debería resolverse en un tiempo lógico acorde al tamaño del imput => debería ser fácil de implementar
#Problema NP: No podemos afirmar que la solución sea polinomial, pero la validación de dicha solución si lo es
#Entonces, para una solución propuesta para un problema NP, podemos verificarla polinomialmente.
# toda solución a un problema P puede ser validada en Polinomial. 
#No se sabe si P=NP pues eso significaría que toda solución que se verifica en tiempo polinomial sería fácil de resolver.
#Problema NP-Completo: si encontras una solución eficiente para este problema, será eficiente para todo NP.
#Teorema de Cook-Levin: Asegura que el problema de SAT es Np-completo
# V:OR, ^:AND, NOT
#Pspace: todos los problemas resolubles en espacio polinomial, NO tiempo polinomial como en P. Mide cuanto espacio toma un algoritmo en ejecutarse, se busca que el crecimiento de la memoria sea poli.
#Literals: variables booleanas(1-0), True=1,False=0
#Problema 3-SAT: tengo cláusulas(conjunto de 3 literals)
#Algo del estilo => (notX1 v X2 v X3)^(X1 v notX2 v X3)^(X1 v X2 v X3)^(notX1 v notX2 v notX3)
#entonces  se tiene que cumplir que para cierta combinacion de literals, el output tiene que ser true
#por ej X1=1,X2=1,X3=0 ===> (0 or 1 or 0) and (1 or 0 or 0) and (1 or 0 or 0) and (0 or 0 or 1)
#Que si lo seguimos desarrollando ===> (1) and (1) and(1) and (1)
#Se termina llegando a True

#1 Verificador del Indepent Set => No hay conexiones entre los vértices del set
#Imagino que se recibe el Set propuesto y el grafo del que se obtuvo

from grafo import Grafo

#Solucion poco eficiente
def validador_IS(grafo,set,tam_pedido):
    #imagino que deberíamos recorrer todos los adyacentes al set y ver si se conectan con el set original
    es_IS=True
    #En este arreglo voy almacenando todos los adyacentes 
    conectados=[]
    for v in set:
        for w in grafo.adyacentes(v):
            conectados.append(w)

    for v in set:
        for vecino in conectados:
            if grafo.estan_unidos(v,vecino):
                return False

    if len(set)!=tam_pedido:
        return False

    return es_IS

#Solución + piola porque solo verifico que dos vertices del set no estén conectaus => menos iteraciones :P
#Con este validador polinomial, aseguro que IS es un problema NP
def validador_IS(grafo,set,tam_pedido):
    
    es_IS=True
    #O (v cuadrático)
    for v1 in set:
        for v2 in set:
            if grafo.estan_unidos(v1,v2) and v1!=v2:
                return False

    #O(1)
    if len(set)!=tam_pedido:
        return False

    return es_IS

#2 Validador Vertex cover => inverso al ej 1, aca en el max vertex cover todas las aristas del grafo tienen una conexión con el mismo 
#Con este validador polinomial, aseguro que IS es un problema NP

def validador_VC(grafo, cover, tam_pedido):
    es_VC=True
    

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if v not in cover and w not in cover:
                es_VC=False

    #esto en realidad es mas eficiente si lo pongo arriba y le mando un return False, pero soy un rebelde

    if len(cover) > tam_pedido:
        es_VC=False

            
    
    return es_VC

#3 Indepent Set y VC son opuestos. Si quiero el Independent Set a partir de un VC, tengo que agregar todos los vértices que no pertenecen al cover. Lo contrario para el otro caso

def obtener_IS(grafo,VC):
    IS=[]
    vertices=grafo.obtener_vertice()
    for vertice in vertices:
        if vertice not in VC:
            IS.append(vertice)
    
    return IS

def obtener_VC(grafo,IS):
    VC=[]
    vertices=grafo.obtener_vertice()
    for vertice in vertices:
        if vertice not in IS:
            VC.append(vertice)
    
    return VC

#4 
#ver explicación 3 sat mas arriba
# Básicamente, yo voy a tener varias cláusulas que servirían como conjuntos separados de 3 vértices
# algo por ejemplo (notX1 or X2 or X3) and (X1 or notX2 or X3) and (notX1 or X2 or X4)

#Por si no se entiende, cada cláusula sería un triangulo de vertices conectados entre si y separados de los otros triángulos.
#Al agarrar uno de cada triángulo, aseguro independencia entre estos.
#Lo que me va a servir es que, para cualquier asignación de booleanos, las variables y sus negados siempre van a
#tener valor opuesto, entonces conecto en cada triángulo los vertices y sus negados, planteando con el 3-SAT de arriba
#nos quedarían libres el X3, X3 y X4 de cada cláusula respectivamente, y estos vertices serían independientes entre si
#Por ultimo, para asegurar que el output es 1, los vertices del IS van a valer siempre 1.

#A partir de 3-SAT llegamos a un IS y, dado a que este ya era NP de antes, ahora demostramos que es NPC
#Como VC es basicamente hacer lo opuesto a IS, estos 2 son equivalentes. Por lo cual, VC es también NP-C.

def crear_Triangulos_3SAT(clausulas):
    grafo=Grafo()
    set_clausulas=set()
    for c in clausulas:
        v1,v2,v3=c
        grafo.agregar_arista(v1,v2)
        grafo.agregar_arista(v3,v2)
        grafo.agregar_arista(v3,v1)
    #creo uniones entre opuestos
    for c in clausulas:
        for literal in c:
            #lo que hago es conectar las variables opuestas
            # abs(X1) y abs(notX1) son lo mismo
            set_clausulas.add(abs(literal))
    
    for literal in set_clausulas:
        grafo.agregar_arista(literal,-literal)
    
    return grafo




#5.a Recibo un numero y tengo que ver si es la solucion a la busqueda del max de un arreglo

#no pero che es re fácil TDA ( ͡° ͜ʖ ͡°)
def validarMax(sol,arr):

    for num in arr:
        if num>sol:
            return False
    return True

#5.b uia estuve toda la tarde para hacerlo uwu, espero que esté bien

def validarArr(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    
    #IMPORTANTE DEFINIR NUESTRA TABLA DE HASH, VITAL PARA EL EJERCICIO NEAA SE HACÍA EL CAPO EL BOT
    class TablaHash:
        def __init__(self, tamano):
            self.tamano = tamano
            self.tabla = [[] for _ in range(tamano)]  

        def _hash(self, clave):
            return hash(clave) % self.tamano

        def insertar(self, clave, valor):
            indice = self._hash(clave)
            for i, (k, v) in enumerate(self.tabla[indice]):
                if k == clave:
                    self.tabla[indice][i] = (clave, valor)
                    return
            self.tabla[indice].append((clave, valor))

        def buscar(self, clave):
            indice = self._hash(clave)
            for k, v in self.tabla[indice]:
                if k == clave:
                    return v  
            return None  

        def __str__(self):
            return str(self.tabla)
        
    return True

#5.c para que hayan N reinas, estas no se deben poder atacar entre sí. No pueden compartir ni fila, ni col y tampoco la diagonal

#Chatgpteadisimo porque me moría de sueño
def Nreinis(reinis):
    for j in range(len(reinis)):
        for w in range(j+1,len(reinis)):
            #verifico que no compartan fila
            if reinis[j] == reinis[w] or abs(reinis[j] - reinis[w]) == abs(j - w):
                return False
            
    return True

#6 Esta bastante mal redactado. Primero tenemos que justificar que N-Reinas es NP-C
#Ya demostramos antes que es NP. Luego tenemos que hacer una reducción de este problema para llegar a IS

#Para llegar que N-Reinas es npc, sabemos que ninguna reyna tiene que poder atacarse. Entonces, podemos armar de nuevo un triángulo
#conectado entre sí y elegir un vertice de cada triangulo (que sería una reina por triángulo).
#Entonces, si tengo c cláusulas de 3 vertices cada una, la dimensión del tablero sería 3c donde cada vértice representaría un casillero,
#Con esto justificaría que N reinas es Np-c. Para llegar a un IS no tendría que hacer mucho pues el set de reinas en el tablero representarían un IS.

# Como N-Reinas es NP-Completo, y cualquier solución de N-Reinas corresponde a un conjunto independiente en el grafo,
# podemos concluir que Independent Set también es NP-Completo, dado que hemos reducido N-Reinas a IS.



#7 Problema K-Clique: un grafo donde podemos hacer un subconjunto
#de K vertices para los cuales todos ellos están conectados entre sí
#Veo si K-clique es npc. Vamos con el famoso cock-levin.
#Ah no, como demostramos que IS es npc, podemos hacer una reducción  y llegar a kc
#IS no puede ser mas dificil que kc, IS<=kc

#video: https://www.youtube.com/watch?v=ST1ozPWvgjs

#se explica que, dado un grafo donde hay K-IS, podemos crear un complemento a ese grafo
#donde agregamos las aristas que no existen en el original y quitamos las existentes
# Entonces en ese grafo se encontrará un K-clique
# Si en el grafo original había un 3-IS con los vertices 3,6 y 8, en el complemento hay un 
#3-clique con esos mismos vértices
#Entonces, si a partir de IS consigo un kc, este weon es npc pues la reducción de un problema a otro es polinómica. 

#esta wea es polinómica, Kc es np como mínimo
def validador_Kclique(tam_pedido,grafo,clique):
    if len(clique)!=tam_pedido:
        return False
    #O(v cuadrático) para todos los Vs del clique
    for v in clique:
        for w in clique:
            #todos los vertices del clique deben estar conectados
            if v!=w and not grafo.estan_unidos(v,w):
                return False
            
    return True

#recibimos un grafo y un K-IS
def getKclique(grafo,ind):
    k=len(ind)
    k_clique=[]
    vertices=grafo.obtener_vertices()
    g_complemento=Grafo(vertices_init=vertices)

    #O(V cuadrau)
    for v in vertices:
        for w in vertices:
            if v!=w and not grafo.estan_unidos(v,w):
                g_complemento.agregar_arista(v,w)

    k_clique.clear()
    k_clique.extend(ind)
    #O(v cuadrático)
    if validador_Kclique(k,g_complemento,k_clique):
        return k_clique
    return None

#8 camino hamiltoniano ==> recorro el grafo en una única iteración sin repetir vértices
#   ciclo hamiltoniano ==> parecido al anterior, pero ahora el camino debe conducir al primer vértice
#   sin repetir los vértices durante el camino. Por enunciado, es npc.

# Entonces, deberíamos poder aplicarle una reducción al camino a partir de un ciclo.
# ¿Cómo? no idea mano, pero se me ocurre que ambos problemas son casi idénticos menos por la parte final.
#  ¿podría conseguir un camino si solo le corto la vuelta al vértice de origen? Sigan viendo

#como obtuvimos el camino a partir de una reducción de un npc, entonces camino
#también es NP-COMPLETO.
def get_CaminoH(grafo,cicloh):
    #grafo? no se yo no lo invité
    camino=[]
    vertice_inicial=cicloh[0]
    camino.append(vertice_inicial)
    for v in cicloh:
        if v!=vertice_inicial:
            camino.append(vertice_inicial)

    return camino

#9 3-Coloring ==> Los vértices del mismo color no pueden tener adyacencias entre si.
#No justifico que es npc porque el enunciado ya dice que lo asumamos.
# Lo que se hace es agregar un vertice del tercer color y unirlo a todo el grafo, de esta manera no puede existir ningun otro vertice de ese color.
#  entonces pasamos de un tri-partito a bi. Lo mismo para cualquier K-partito, creamos k-3 vertices de color único que conecten a todo el grafo y repetimos el proceso.


def verificador_Npartito(grafo,colores,n):
    vertices=grafo.obtener_vertices()
    if len(colores)!=n:
        return False
    for v in vertices:
        for w in grafo.adyacentes(v):
            if colores[v]==colores[w]:
                return False
    return True

#falta hacer el codigo de la reducción

#10 Subset sum ==> dado un conj de numerillos y un valor, ver con que subconjunto de esos nums se puede alcanzar dicho valor. NP-C por enunciau.
# Problema mochi ==>maximizar el valor que se puede acumular dada una limitación del peso. 
# SS es básicamente lo mismo que la mochi, solo que en esta última se puede no alcanzar el valor dado y aún así ser válida(es el valor acumulado mas alto posible, puede no igualar todo el peso disponible)
# Habría que hacer un SS pero sin ser tan tajantes a que el subconjunto iguale el valor, mientras sea el mas aproximau, joya.
# Bueno, en realidad, los dos problemas son iguales XD (ver el archivo con dinámica y literal son lo mismo) entonces no hay que hacer mucho.
#La única diferencia que veo en código es que la mochi trabaja para tuplas y el otro para ints comunes, pero la ec.recurrencia es the same shet
#Si es np-completo, por cambiarle el nombre y meterle mas lore no va a dejar de ser un npc.

# 11 ==> sería un subset sum pero donde quiero todos los subconjuntos posibles.
# No pertenece a Pspace porque su complejidad espacial no es polinómica. Como nos aseguramos que si lo sea? si solo almacena lo mínimo y necesario para 
#acercarnos a la solución, un poco como backtracking donde almacenamos datos parciales pero los descartamos cuando no nos sirven. Lo otro implica una especie de fuerza bruta donde
# guardamos absolutamente todas las soluciones que sirvan.
#La cantidad total de subconjuntos posibles para una lista de largo L sería 2^L. Por qué??
# Es porque cada elemento tiene dos opciones: Agregarse o no al subconjunto. Entonces te queda algo como 2x2x2x2... hasta L.
#Como tendría complejidad espacial O(2^L), esto es exponencial y no polinomial. No es PSpace

# 12 ==> Idem del ej mochila, pero acá solo queremos una solución que cumpla. En este caso, si esta bien implementado con backtracking, sí pertenecería a Pspace pues solo haría falta almacenar datos parciales
# y borrarlos en caso de que no aporten al subconjunto. Su complejidad espacial sería O(N) pues en el peor de los casos almacenaríamos todos los elementos del arreglo.

#13 ==> To-do

#14 ==> Minimizar cantidad de figuritas a dar y que cumpla el monto pedido. Por lo que entendí, sería como un subset-sum minimizando el tamaño del sub-conjunto.
#El detalle de que existan figuritas que valen 1 nos asegura que siempre alcanzamos el monto que piden los proveedores. Esto ayuda para los casos donde el subset sum no podía cubrir todo el valor.
#Entonces yo aplico subset sum al arreglo de figuritas y me puede devolver ya sea un subconjunto que cubre todo el valor, o me puede devolver el que se acerque mas al valor( En esto último le meto figuritas de 1)

#Validador Carlito: tengo un valor k que es la mínima cantidad que pido de figuritas
#Creo que solo me importaría que sea cantidad mínima y que cubra el monto pedido. Complejidad temporal de O(n) y espacial de O(n) tmb



#Carlito´s Problem
#Si con una reducción de un problema NPC logré resolverlo, carlito es un npc.
def carlito_carlito(figuritas,monto,k):
    figuritas.sort(reverse=True)
    #Esta función es como mi caja negra, solo se que Messi me la resuelve
    ss=subset_sum_implementado(figuritas,monto)
    acumulado=sum(ss)
    while acumulado<monto:
        ss.append(1)
        acumulado+=1
    
    if validador_carlito(ss,k,monto):
        return ss
    return None
#En realidad esto es nada que ver porque me piden un problema de decisión y no de optimización. Tengo que devolver si para ciertos parámetros es posible resolver el problema.

def decisión_subset_sum(conjunto,k):
    sub_conjunto=backtrack_subset_sum(conjunto,k)
    return sum(sub_conjunto)==k

#Este es un validador de carlitos, trabaja en la misma complejidad que SS en tiempo polinomial, así que es por lo menos NP
def decision_carlito(figuritas,k,minimo):
    figuritas.sort(reverse=True)
    sub_figuritas=backtrack_subset_sum(figuritas,k)
    #verifico que se cumpla el monto y que como mucho sea del tamaño mínimo
    return sum(sub_figuritas)==k and len(sub_figuritas)<=minimo
#Pude resolver el problema de charly con SS, es NPc también

#15 estos submarinos me tienen reventado es literal el peor problema de la materia.
# Si los vértices de un grafo son las casillas, un vertex cover de ese grafo serían los faros porque cubrirían al submarino con todas sus adyacencias.

#A terminar
def submarinos(matriz):
    vertices=[]
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            vertices.append(matriz[fila][columna])

#16 Hitting set problem ==> tengo un conjunto de N elementos del que puedo obtener M subconjuntos
#Tengo que ver, si para un valor K, existe un conjunto <=K que tenga un elemento de cada uno de los M subconjuntos.
#Primero tendría que ver si este problema es NP, para eso, creo un validador

#Validador con complejidad Polinomial, por ahora es NP
def validador_hitting_set(solucion,subconjuntos,k,m):
    #tomo a los subconjuntos como una lista de listas
    #solución lo tomo como un set de elementos
    #O(n) en caso de que la solucion tenga todos los elementos
    if len(solucion)>k or len(subconjuntos)!=m:
        return False
    #O(M*L) siendo M la cantidad de subconjuntos y L el tamaño(aproximado) de estos
    for conjunto in subconjuntos:
        es_valido=False
        for elemento in conjunto:
            #O(1)
            if elemento in solucion:
                es_valido=True
                break
        if not es_valido:
            return False
    return True

#Creo que si queremos reducir a partir de un NP-C podríamos usar Vertex Cover. Pues el subconjunto C sería aquel conjunto de vértices que tiene
#adyacencias con todo el grafo, osea que para cualquier subconjuntos del grafo tendríamos una o mas conexiones al cover.
#Asumo que el conjunto viene en forma de grafo, los subconjuntos es una lista de listas
def hitting_set(grafo,subconjuntos,k,m):
    solucion=set(vertex_cover(grafo))
    if validador_hitting_set(solucion,subconjuntos,k,m):
        return solucion
    return None

#17 Tenemos que ubicar un guardián en cada esquina(cubriendo todas las que tiene enfrente) y ya nos dicen que este es un NPc. Considero que si queremos
#vigilar todas las calles, habría que pensarlo como un Vertex Cover, teniendo a los vértices como las esquinas(las 4 esquinas por vértice) y las aristas siendo calles.
#Conseguimos el conjunto de vértices que cubran todas las calles y mandamos ahí a los guardianes.

#Copio y pego el validador VC de los primeros ejs
def validador_VC(grafo, cover, tam_pedido):
    es_VC=True
    if len(cover) > tam_pedido:
        es_VC=False

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if v not in cover and w not in cover:
                es_VC=False
    return es_VC

#18 No hice flujo todavía uu

#19 Demostrar que dominating set es NPc.

#Por ahora es NP
def validador_dominating(grafo,set,k):
    vertices=grafo.obtener_vertices()
    if len(set)>k:
        return False
    #O(V^2)
    for v in vertices:
        if v not in set:
            es_valido=False
            for s in set:
                if grafo.estan_unidos(v,s):
                    es_valido=True
        if not es_valido:
            return False
    return True

#Es npc
def getDominating(grafo,cover,k):
    vertices=grafo.obtener_vertices()
    dset=set(cover)
    #solo me tendría que fijar si hay algun vertice que no pertenezca al cover, entonces lo recorro y veo si tiene un adyacente en el cover.
    #En caso negativo, lo agrego
    for v in vertices:
        if v not in dset:
            conectau=False
            for c in cover:
                if grafo.estan_unidos(c,v):
                    conectau=True
                    break
            if not conectau:
                dset.add(v)
    if validador_dominating(grafo,dset,k):
        return dset
    return None

#20 Path Selection ==> dado un conjunto de caminos que recorren el grafo, ¿es posible seleccionar K caminos y que no compartan vértices entre si?
#verifico que sea NP

#Polinomial, es Np
def verificador_path(grafo,caminos,solucion,k):
    #solucion sería una lista de k listas que almacenan un camino c/u
    if len(solucion)>k:
        return False
    #O(K^2 * V) siendo K la cantidad de caminos guardados y V los vertices que hay en cada camino(suponiendo que no hay una grandísima diferencia de tamaño)
    for camino in solucion:
        #habría que verificar que cada vértice del camino no se repita en los otros caminos
        #En realidad, existe una solución con mejor complejidad, pero ya me encariñé de esta que hice
        #Se podría ir recorriendo solo una vez e ir agregando los vértices recorridos a un set y listo te queda k*v con esa
        for v in camino:
            for w in solucion:
                if w!=camino and v in w:
                    return False
    #Entonces, si cada v no se repite en ningún otro camino, tamos bien
    return True

#La semejanza con IS sería que ese te busca conjunto de K vertices independientes, pero este te pide K caminos


    





#22 A veces pido que hubiera entrado la de kolo muani solo para que no vivan repitiendo el chiste de francia segundo. Es 2024 chicos ya está.

    





  


    








