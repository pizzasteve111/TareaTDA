#Ejercicios sacados de: https://algoritmos-rw.github.io/tda_bg/material/guias/reducciones/
from grafo import Grafo

#Problema P: Problema cuya solución es polinomial, osea, que debería resolverse en un tiempo lógico acorde al tamaño del imput => debería ser fácil de implementar
#Problema NP: No podemos afirmar que la solución sea polinomial, pero la validación de dicha solución si lo es
#Entonces, para una solución propuesta para un problema NP, podemos verificarla polinomialmente.
# toda solución a un problema P puede ser validada en Polinomial. 
#No se sabe si P=NP pues eso significaría que toda solución que se verifica en tiempo polinomial sería fácil de resolver.
#Problema NP-Completo: si encontras una solución eficiente para este problema, será eficiente para todo NP.

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


# def validador_VC(grafo,cover,tam_pedido):
#     es_VC=True
#     vertices=grafo.obetner_vertices()
#     conexiones=set()
#     for v in cover:
#         #almaceno todos los vertices del cover + sus adyacentes. 
#         #Esto debería devolver el mismo tam que el grafo original
#         conexiones.add(v)
#         for w in grafo.adyacentes(v):
#             if w not in conexiones:
#                 conexiones.add(w)

#     # pongo el <= porque buscamos siempre la sol mínima
#     if len(conexiones)<=len(vertices) or len(conexiones)<=tam_pedido:
#         es_VC=False
    
#     return es_VC

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

#4 TO-DO

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

def Nreinis(reinis):
    for j in range(len(reinis)):
        for w in range(j+1,len(reinis)):
            #verifico que no compartan fila
            if reinis[j] == reinis[w] or abs(reinis[j] - reinis[w]) == abs(j - w):
                return False
            
    return True


    




