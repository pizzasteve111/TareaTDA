#EJ1
# Lo podría hacer por programación lineal
from grafo import Grafo
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

#EJ3
#tengo que determinar la minima cantidad de pasos para llegar a K
#comenzando desde el 0, sabiendo que solo podemos aumentar en 1 o duplicar
#para el valor i su optimo debería ser el maximo entre sumarle 1 o duplicarlo sin pasarse de K

def min_pasos(k):
    optimos=[]
    #0 pasos si k=0
    optimos[0]=0
    #1 paso si k=1
    optimos[1]=1
    for i in range(2,k):
        optimos[i]=min(optimos[i-1]+1,optimos[i//2]+1)



    