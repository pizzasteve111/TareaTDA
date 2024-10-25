#Ejercicios sacados de: https://algoritmos-rw.github.io/tda_bg/material/guias/reducciones/
# Clase no grabada: https://www.youtube.com/watch?v=rg1vwVsaJMo
# Video 3-SAT: https://www.youtube.com/watch?v=GCw07nZckps
#Ej 3-SAT:  https://www.youtube.com/watch?v=MV8Z_D1mLMU




#Problema P: Problema cuya solución es polinomial, osea, que debería resolverse en un tiempo lógico acorde al tamaño del imput => debería ser fácil de implementar
#Problema NP: No podemos afirmar que la solución sea polinomial, pero la validación de dicha solución si lo es
#Entonces, para una solución propuesta para un problema NP, podemos verificarla polinomialmente.
# toda solución a un problema P puede ser validada en Polinomial. 
#No se sabe si P=NP pues eso significaría que toda solución que se verifica en tiempo polinomial sería fácil de resolver.
#Problema NP-Completo: si encontras una solución eficiente para este problema, será eficiente para todo NP.
#Teorema de Cook-Levin: Asegura que el problema de SAT es Np-completo
# V:OR, ^:AND, NOT

#Literals: variables booleanas(1-0), True=1,False=0
#Problema 3-SAT: tengo cláusulas(conjunto de 3 literals)
#Algo del estilo => (notX1 v X2 v X3)^(X1 v notX2 v X3)^(X1 v X2 v X3)^(notX1 v notX2 v notX3)
#entonces  se tiene que cumplir que para cierta combinacion de literals, el output tiene que ser true
#por ej X1=1,X2=1,X3=0 ===> (0 or 1 or 0) and (1 or 0 or 0) and (1 or 0 or 0) and (0 or 0 or 1)
#Que si lo seguimos desarrollando ===> (1) and (1) and(1) and (1)
#Se termina llegando a True

#1 Verificador del Indepent Set => No hay conexiones entre los vértices del set
#Imagino que se recibe el Set propuesto y el grafo del que se obtuvo

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



#7 Problema K-Clique: un grafo para el cual podemos hacer un subconjunto
#de K vertices para los cuales todos ellos están conectados entre si

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






