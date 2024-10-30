from grafo import Grafo
#Juan El vago por prog lineal
#Cada día sería una variable binaria que indica si trabajo o no trabajo
#Maximizar para el caso donde si trabajo dos días seguidos, al siguiente no puedo.
#Función objetivo: dado los días consecutivos x,y,z se tiene como restricción x+y+z<=2 osea que como mucho puedo trabajar dos de esos 3 días consecutivos.
def lazy_john(dias):
    j={}
    res=[]
    problema=pulp.LpProblem("Juan",pulp.LpMaximize)
    for d in dias:
        j[d]=pulp.LpVariable(f"dia{d}",cat="Binary")
    #se multiplica el valor de cada día por 1 o 0(dependiendo de si trabaja)
    problema+=pulp.LpSum(dias[d]*j[d]for d in dias)
    
    for i in range(len(dias)-2):
        problema+=j[i]+j[i+1]+j[i+2]<=2
    
    problema.solve()

    for d in dias:
        if pulp.LpValue(d)==1:
            res.append(d)
    return res,sum(res)

#EJ2 Camino de menor costo. Hay que recorrer todo el grafo pasando por los vértices
#Una única vez y asegurando que minimizamos el costo de las aristas del viaje.
#Supongo que habría que ver si para los adyacentes, estos no están visitados e ir por aquel
#Que tenga menor costo

# **TERMINAR*** va medio mal xd
def min_camino(grafo,inicio):
    visitados=set()
    costo_total=0
    visitados.add(inicio)
    vertices=grafo.obtener_vertices()
    res=[]
    res.append(inicio)
    act=inicio
    #mientras no haya terminado de recorrer todo el grafo
    while len(visitados)!=len(vertices):
        #osea infinito xd
        prox=None
        min_cost_proximo=100000000000
        #Esto va mal porque recorrería varias veces el vertice
        for v in vertices:
            if v not in visitados and grafo.estan_unidos(v,act):
                if grafo.peso_arista(v,act)<min_cost_proximo:
                    min_cost_proximo=grafo.peso_arista(v,act)
                    prox=v
        


        

#EJ 3 Por lo que entiendo, sería algo de Vertex Cover donde cada vértice tiene que ser una persona
#el tamaño del cover tiene que ser K y con esto nos aseguramos que todos los invitados conocen a alguien con regalo. Re mala onda coty igual
#imaginate caer a un cumple y que le den regalos a tus amigos pero a vos nao.

#Podemos armar un grafo donde los vertices sean los invitados y sus adyacencias sean sus conocidos. Una vez armado el grafo, llamaría a un problema Npc conocido como Vertex Cover 
#Y que me devuelva un set donde me aseguro que todos van a poder hablar de sus regalos.

#conocidos es un dic. donde para cada invitado, accedo a sus conocidos
def getCoty(invitados,conocidos,k):
    grafo=Grafo(vertices_init=conocidos)
    for i in invitados:
        for c in conocidos[i]:
            grafo.agregar_arista(i,c)
    #Por ahora, asumo que en el parcial todas las demostraciones que hicimos en la guía se dan como ya justificadas y que no hay que ir hasta cook-levin para justificar todo Np-c
    res=vertex_cover(grafo)
    if validador_coty(grafo,res,k):
        return res
    return None

#Dado que el problema de Coty es Np gracias a su validador polinómico, sabemos que VC es al menos tan difícil como Coty. Demostramos que con una implementación de VC podemos resolver el problema
#de coty si armamos el grafo adecuado.

#Este validador es suficiente
def validador_coty(grafo,cover,k):
    vertices=grafo.obtener_vertices()
    if len(cover)>k:
        return False
    #O(V*K) complejidad temporal polinómica
    for v in vertices:
        es_valido=False
        for w in cover:
            if v!=w and grafo.estan_unidos(v,w):
                es_valido=True
        if not es_valido:
            return False
    return True

#EJ 4 Ni se sumar y me vas a pedir un ej de potencias

#EJ 5 Ni se sumar y me vas a pedir un ej de potencias
                    

