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
    visitados.add(inicio)
    vertices=grafo.obtener_vertices()
    #mientras no haya terminado de recorrer todo el grafo
    while len(visitados)!=len(vertices):
        for v in vertices:
            if v not in visitados:
                camino_min=1
                for w in grafo.adyacentes(v):
                    if camino_min>

#EJ 3 Por lo que entiendo, sería algo de dominant set donde cada vértice tiene que ser una persona
#el tamaño del cover tiene que ser K y con esto nos aseguramos que todos los invitados conocen a alguien con regalo. Re mala onda coty igual
#imaginate caer a un cumple y que le den regalos a tus amigos pero a vos nao.

def validador_coty(grafo,cover,k):
    if len(cover)>k:
        return False
    
                    

