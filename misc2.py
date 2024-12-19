from grafo import Grafo

#Greedy

def min_VC(grafo)




#(valor,peso)
def farmacos(elementos,w):
    items=[]
    res=[]
    for valor,peso in elementos:
        items.append((valor/peso),valor,peso)
    items.sort(reverse=True, key=lambda x:x[0])
    cap=0
    for _,valor,peso in items:
        if cap+peso<=w:
            res.append((valor,peso))
            cap+=peso
        else:
            #debería solo agregar la porcion que entra en el peso
            #debería dividir el producto total por el espacio que tengo libre
            libre=w-cap
            proporcion=libre/peso
            res.append((valor*proporcion,peso*proporcion))
    
    return res






#minimo vertex cover

def VC(grafo):
    #tengo que incluir todas las aristas con la menor cantidad de vertices posibles
    aristas=grafo.aristas()
    #set que va a asegurar que no repitamos aristas
    visitados=set()
    cover=set()

    while len(visitados)<len(aristas)*2:
        for u,v in aristas:
            #debería comparar si el extremo de una arista no esta en el cover
            if (u,v) not in visitados or (v,u) not in visitados:
                #agrego solo un extremo
                if len(grafo.adyacentes(u))>len(grafo.adyacentes(v)):
                    mejor_opcion=u
                else:
                    mejor_opcion=v
                cover.add(mejor_opcion)
                visitados.add((u,v))
                visitados.add((v,u))
    
    return cover







#obtener minimo problema del viajante

def min_camino(grafo,ini):
    res=[ini]
    vertices=grafo.vertices()
    visitados=set()
    actual=ini

    while len(visitados)<len(vertices):
        peso_min=10000000

        for w in grafo.adyacentes(actual):
            if grafo.peso_arista(actual,w)<peso_min and w not in visitados:
                peso_min=grafo.peso_arista(ini,w)
                actual=w
        res.append(actual)
        visitados.add(actual)
    
    res.append(ini)
    return res





def kcore(grafo,k):
    vertices=grafo.obtener_vertices()
    #tengo que eliminar aquellos vértices que tienen cantidad de adyacentes menor a k
    #pero mantener actualizado el grafo pues estas eliminaciones afectan a otras tmb

    eliminados=[]
    hay_cambios=True
    while hay_cambios:
        hay_cambios=False
        for v in vertices:
            #tengo que borrar el vértice, actualizando tmb las adyacencias de los demas
            if len(grafo.adyacentes(v))<k:
                eliminados.append(v)
                grafo.borrar_vertice(v)
                hay_cambios=True
                
    
    return grafo.vertices()


def min_DS(grafo):
    #minimo conjunto de vertices que cubren todo el grafo
    visitados=set()
    res=[]
    vertices=grafo.vertices()


    for v in vertices:
        if v not in visitados:
            res.append(v)
            visitados.add(v)
            for u in grafo.adyacentes(v):
                visitados.add(u)
    
    #es optimo pues siempre aseguro la mínima cantidad para cubrir un vertice y sus adyacencias(solo 1)
    #y con el set aseguro que no voy a repetir vertices ya dominados
    return res


def min_suma_DS(grafo):
    visitados=set()
    res=[]
    vertices=grafo.vertices()
    vertices.sort(key=lambda x:grafo.valor(v) for v in vertices)

    suma=0
    for v in vertices:
        if v not in visitados:
            res.append(v)
            visitados.add(v)
            suma+=grafo.valor(v)
            ady_min=1000000000
            for u in grafo.adyacentes(v):
                visitados.add(u)
                valor_min=grafo.valor(u)
                if valor_min<ady_min:
                    ady_min=valor_min
            suma+=ady_min
    
    #es optimo pues siempre aseguro la mínima cantidad para cubrir un vertice y sus adyacencias(solo 1)
    #y con el set aseguro que no voy a repetir vertices ya dominados
    return res

def max_IS(grafo):
    #encontrar el maximo conjunto de vertices que no están conectados entre sí
    visitados=set()
    res=[]
    vertices=grafo.vertices()

    for v in vertices:





#minimizar la cantidad de patrullas en las bifurcaciones sabiendo que cubren un rango de 50 km

def bifurcaciones(rutas):
    res=[]
    cubiertos=set()
    rutas.sort()
    rango=0
    for i in range(0,len(rutas)):
        if rutas[i] not in cubiertos and rutas[i]>rango:
            rango=rutas[i]+50
            maximo=rutas[i]
            for j in range(i,len(rutas)):
                if rutas[j]<=rango:
                    maximo=rutas[j]
                    cubiertos.add(rutas[j])
                else: 
                    break
            res.append(maximo)
        else:
            continue
    return res

def bifu(ciudades):
    ciudades.sort()
    i=0
    res=[]
    n=len(ciudades)

    while i<n:
        ubi=ciudades[i]+50
        while i<n and ciudades[i]<=ubi:
            i+=1
        patrulla=ciudades[i-1]
        res.append(patrulla)
        ubi=patrulla+50

        while i<n and ciudades[i]<=ubi:
            i+=1
    
    return res

print(bifu([20,70,120]))
        
def bolsas(elementos,w):
    bolsas=[[]]
    peso_act=0
    bolsa_act=0
    elementos.sort(reverse=True)
    for elemento in elementos:
        if elemento<=w:
            if peso_act+elemento<=w:
                bolsas[bolsa_act].append(elemento)
                peso_act+=elemento
            else:
                bolsas.append([elemento])
                bolsa_act+=1
                peso_act=0
        else:
            continue
    
    return bolsas

def club(amigos):
    conocidos={}
    total=set()
    for p1,p2 in amigos:
        if p1 not in conocidos:
            conocidos[p1]=[]
        if p2 not in conocidos:
            conocidos[p2]=[]
        total.add(p1)
        total.add(p2)
        conocidos[p1].append(p2)
        conocidos[p2].append(p1)
    eliminados=[]
    for invitado in total:
        if len(conocidos[invitado])<4:
            for p in total:
                if invitado in conocidos[p]:
                    conocidos[p].remove(invitado)
            total.remove(invitado)
            eliminados.append(invitado)
        else:
            continue
    

#Backtracking

def ordenamiento_topo(grafo,inicio):
    orden={}
    vertices=grafo.vertices()
    for v in vertices:
        orden[v]=0
    
    for v in vertices:
        for w in grafo.adyacentes(v):
            orden[w]=orden[v]+1

    res=[]

    for v in vertices:
        res_act=backtrack_topo(grafo,v,[],orden)
        res.append(res_act)

    return res

def backtrack_topo(grafo,ini,res,orden):
    if 
    


def ciclo(grafo,k):
    vertices=grafo.vertices()

    for v in vertices:
        res,valido=backtrack_ciclo(grafo,k,vertices,[v],v)
        if valido:
            return res
    return None

def backtrack_ciclo(grafo,k,vertices,res,act):
    if ciclo_valido(grafo,res) and len(res)==k:
        return res,True
    
    for w in grafo.adyacentes(act):
        res.append(w)
        backtrack_ciclo(grafo,k,vertices,res,w)
        res.pop()
    
    #si llego hasta acá es porque no hay ningún ciclo valido a partir del actual
    return res,False

def ciclo_valido(grafo,res):
    if res[0]!=res[-1]:
        return False
    
    #si dos vertices juntos no estan unidos entonces se rompe el camino
    for i in range(1,len(res)):
        if not grafo.estan_unidos(res[i-1],res[i]):
            return False
    
    return True



#mochila a lo sumo k elementos, (peso,valor)

def mochila(elementos,w,k):
    return backtrack_mochila(elementos,w,k,[],[],0,0,0,0)

def backtrack_mochila(elementos,w,k,res_act,res,peso_act,valor_act,valor_final,indice):
    if peso_act<=w and len(res_act)>=k:
        if valor_act>valor_final:
            res.clear()
            res.extend(res_act)
            valor_final=valor_act
        return res
    if indice>=len(elementos):
        return elementos
    
    actual=elementos[indice]
    res_act.append(actual)
    peso_act+=actual[0]
    valor_act+=actual[1]

    backtrack_mochila(elementos,w,k,res_act,res,peso_act,valor_act,valor_final,indice+1)
    res_act.pop()
    peso_act-=actual[0]
    valor_act-=actual[1]

    return backtrack_mochila(elementos,w,k,res_act,res,peso_act,valor_act,valor_final,indice+1)




#maximizar cantidad de cliques disjuntos en un grafo

def encontrar_clique(grafo):
    return backtrack_clique(grafo,grafo.vertices(),[],[],0)

#dado mi grafo, encontrar clique de tamaño máximo
def backtrack_clique(grafo,vertices,res_act,res,indice):
    if clique_valido(grafo,res_act):
        if len(res_act)>len(res):
            res.clear()
            res.extend(res_act)
        return res
    if indice>=len(vertices):
        return res
    actual=vertices[indice]

    res_act.append(actual)
    backtrack_clique(grafo,vertices,res_act,res,indice+1)
    res_act.pop()
    return backtrack_clique(grafo,vertices,res_act,res,indice+1)

def clique_valido(grafo,res):
    for v in res:
        for w in res:
            if not grafo.estan_unidos(v,w) and v!=w:
                return False
    return True

def encontrar_max_cant_cliques(grafo):

    res=[]
    hay_clique=True
    while hay_clique:
        hay_clique=False
        
        clique=encontrar_clique(grafo)
        if clique:
            res.append(clique)
            for v in clique:
                grafo.eliminar_vertice(v)
            hay_clique=True
    
    return res









def flavio(dias):
    return wrapper_flavio(dias,0,1,0,0,0,0)

#(peso,valor)
def prob_mochilaK(elementos,w,k):
    return backtrack_mochila(elementos,w,k,[],[],0,0)

def backtrack_mochila(elementos,w,k,res_act,res,indice,peso_act):
    if mochila_valida(w,peso_act):
        if len(res_act)>len(res) and len(res_act)>=k:
            res.clear()
            res.extend(res_act)
        
        return res
    if indice>=len(elementos):
        return res
    actual=elementos[indice]
    peso_act+=elementos[indice][0]
    res_act.append(actual)
    backtrack_mochila(elementos,w,k,res_act,res,indice+1,peso_act)
    res_act.pop()
    peso_act-=elementos[indice][0]
    return backtrack_mochila(elementos,w,k,res_act,res,indice+1,peso_act)

def mochila_valida(w,p_act):
    return p_act<=w
    



def wrapper_flavio(dias,compra,venta,mejor_compra,mejor_venta,ganancia_act,mejor_ganancia):
    if dias_validos(dias,compra,venta):
        if ganancia_act>mejor_ganancia:
            mejor_compra=compra
            mejor_venta=venta
            mejor_ganancia=ganancia_act
        return mejor_ganancia,mejor_compra,mejor_venta
    
    if venta>=len(dias):
        return mejor_ganancia,mejor_compra,mejor_venta
    
    wrapper_flavio(dias,compra,venta+1,mejor_compra,mejor_venta,dias[compra]-dias[venta],mejor_ganancia)
    return wrapper_flavio(dias,compra,venta+1,mejor_compra,mejor_venta,ganancia_act,mejor_ganancia)

def dias_validos(dias,compra,venta):
    return compra<=venta
def hamilton(g):
    vertices=g.vertices()

    for v in vertices:
        visitados=set()
        visitados.add(v)
        res,valor=backtrack_hamilton(g,vertices,[v],visitados,v)
        if valor:
            return res
    return None

def backtrack_hamilton(g,vertices,res,visitados,act):
    if camino_valido(g,vertices,res):
        return res,True
    
    for w in g.adyacentes(act):
        if w not in visitados:
            visitados.add(w)
            res.append(w)
            backtrack_hamilton(g,vertices,res,visitados,w)
            visitados.remove(w)
            res.pop()
        else:
            continue
    return res,False

def camino_valido(g,vertices,res):
    if len(res)!=len(vertices):
        return False
    act=res[0]
    veces_visitado={}
    for v in vertices:
        if v not in veces_visitado:
            veces_visitado[v]=0
        if v in res:
            veces_visitado[v]+=1
    
    for v in vertices:
        if veces_visitado[v]!=1:
            return False
    return True

def min_DS(g):
    return backtrack_ds(g,g.vertices(),[],g.vertices(),0)

def ds_valido(g,vertices,res_act):
    for v in vertices:
        ok=False
        for r in res_act:
            if g.estan_unidos(v,r) or r==v:
                ok=True
        if not ok:
            return False
    
    return True

def backtrack_ds(g,vertices,res_act,res,indice):
    if ds_valido(g,vertices,res_act):
        if len(res_act)<len(res):
            res.clear()
            res.extend(res_act)
        return res
    
    if indice>=len(res_act):
        return res
    act=vertices[indice]
    res_act.append(act)
    backtrack_ds(g,vertices,res_act,res,indice+1)
    res_act.pop()
    return  backtrack_ds(g,vertices,res_act,res,indice+1)


def mochila(elementos,w):
    return backtrack_mochi(elementos,w,[],[],0)

def mochi_valida(elementos,w,res_act):
    peso=0
    for _,p in res_act:
        peso+=p
    return peso<=w

def sumatoria_valor(res):
    valor=0
    for v,_ in res:
        valor+=v
    return v

def backtrack_mochi(elementos,w,res_act,res,indice):
    if mochi_valida(elementos,w,res_act):
        if sumatoria_valor(res_act)>sumatoria_valor(res):
            res.clear()
            res.extend(res_act)
        return res
    if indice>=len(elementos):
        return res
    
    act=elementos[indice]
    res_act.append(act)
    backtrack_mochi(elementos,w,res_act,res,indice+1)
    res_act.pop()
    return backtrack_mochi(elementos,w,res_act,res,indice+1)


#Dinamica

def camino(grafo,vertices):
    

    

    









#min operaciones para llegar de 0 a K sabiendo que se puede aumentar de a 1 o duplicar el valor

#para el i-esimo valor, su optimo sería el minimo entre el valor de (i-1) y el valor (i/2) y luego sumarle 1 que es la acción actual

def min_pasos(k):
    opt=[]*(k+1)

    opt[0]=0
    opt[1]=1

    for i in range(1,k):
        opt[i]=min(opt[i-1],opt[i//2])+1
    
    return getRes(k,opt)

def getRes(k,opt):
    res=[]

    for i in range(k,1,-1):
        if opt[i]==opt[i-1]+1:
            res.append("sumar uno")
            i-=1
        else:
            res.append("duplicar")
            i=i//2
    
    res.reverse()
    return res



#para el i-esimo dia la ganancia maxima sería el maximo entre el optimo del día anterior
#o la diferencia entre vender hoy con el mejor día de compra.
#[10,2,5,7,6]
#para mantener seguimiento del día de compra podría ir agregando el día minimo que puedo encontrar para cada i-esimo
#y así ir viendo que día me conviene

def osvaldo(dias):
    opt=[-1000000]*(len(dias)+1)
    #este arreglo almacena que día se compra/vende para cada i-esimo día
    acciones=[]
    acciones.append(0,0)
    opt[0]=0
    #originalmente, compro el primer día
    dia_minimo=dias[0]
    dia_max=dias[0]

    for i in range(1,len(dias)+1):
        ganancia_hoy=dias[i]-dia_minimo
        if dias[i]<dias[dia_minimo]:
            dia_minimo=i
        if ganancia_hoy>opt[i-1]:
            opt[i]=ganancia_hoy
            dia_max=dias[i]
        else:
            opt[i]=opt[i-1]
        
        acciones.append((dia_minimo,dia_max))
    
    ganancia_max=max(opt)
    compra,venta=acciones.index(ganancia_max)
    return compra,venta






#suma minima en dominating set de grafo camino v1=>v2=>v3=>v4

def suma_minDS(grafo):
    vertices=grafo.obtener_vertices()
    opt=[100000]*(len(vertices)-1)

    opt[0]=vertices[0]
    opt[1]=min(vertices[0],vertices[1])

    for i in range(2,len(vertices)):
        opt[i]=min(opt[i-1],opt[i-2]+vertices[i])
    
    #ahora debo reconstruir la solución
    ds=[]

    for i in range(len(vertices),1,-1):
        #si hubo un cambio entre el optimo del vertice actual y el anterior,
        #significa que el actual aporta al dominating set de suma mínima
        if opt[i]!=opt[i-1]and i>1:
            ds.append(vertices[i])
            i-=2
        else:
            i-=1
    
    ds.reverse()

    return ds




#osvaldo

#quiero maximizar la ganancia posible y para eso devuelvo los días donde conviene comprar y vender
#el optimo para el día i sería vender ese día - valor mínimo anterior
#osea que el indice i almacena (ganancia,valor minimo de compra) para ese día
def osvaldo(dias):
    ganancias=[]
    minimos=[]
    
    
    ganancias[0]=dias[0]
    minimos[0]=dias[0]
    
    for i in range(1,len(dias)):
        minimos[i]=min(minimos[i-1],dias[i])

        ganancias[i]=max(ganancias[i-1],dias[i]-minimos[i])

    max_ganancia=ganancias[-1]


    #reconstruyo la solución







def juan_vago(dias,n):
    opt=[0]*(n+1)

    opt[0]=dias[0]
    opt[1]=max(dias[0],dias[1])

    for i in range(2,n):
        opt[i]=max(opt[i-1],opt[i-1]+dias[i-1])
    
    return opt[n]



#maximizar ganancia total obtenida 
#(ini,fin,valor) para la i-esima charla, su valor optimo
#sería el de no dar la charla(me quedo con el anterior) o el de dar la charla y sumarle el valor de la charla mas grande que no se solape con ella
#el optimo para la primer charla es darla
#el optimo para dos charlas sería el máximo entre no darla y quedarme con el valor anterior o darla+ el opt de la charla anterior que no se solapa
#algo como opt[i]=max(opt[i-1],opt[no solapada]+charlas[i])


#tengo que buscar aquella charla cuyo fin sea menor a mi inicio
#O(log n)

def no_solapada(charlas,ini,fin,inicio_charla,anterior_valido):
    if ini==fin:
        return anterior_valido
    medio=(ini+fin)//2
    #si el fin de la charla actual es mayor al inicio de mi charla,acoto
    if charlas[medio][1]<=inicio_charla:
        anterior_valido=medio
        return no_solapada(charlas,medio+1,fin,inicio_charla,anterior_valido)
    else:
        return no_solapada(charlas,ini,medio-1,inicio_charla,anterior_valido)

#O (n log n)
def pd_charlas(charlas,n):
    #ordeno por fin mas próximo
    charlas.sort(key=lambda x:x[1])
    opt=[0]*(n+1)
    opt[0]=charlas[0]
    for i in range(1,n):

        indice_no_solapada=no_solapada(charlas,0,i,charlas[i][0],i)

        if indice_no_solapada != -1:
            opt[i] = max(opt[i - 1], charlas[i][2] + opt[indice_no_solapada])
        else:
            opt[i] = max(opt[i - 1], charlas[i][2])
    #entonces tengo almacenado el valor máximo que puedo obtener para cada instancia de charlas
    return getRes(charlas,opt,n)

def getRes(charlas,opt,n):
    #arranco de atrás para adelante si hay discrepancia entre la charla actual y la anterior
    #significa que tengo en cuenta la charla actual sabiendo
    res=[]
    for i in range(n,1,-1):
        #hay discrepancia, agrego la charla actual
        if opt[i]!=opt[i-1]:
            res.append(charlas[i])

    res.reverse()
    return res

#lo que puedo hacer es encontrar el valor mínimo de operacion para cada mes tomando en cuenta 
#si estoy en londres o california
#después reconstruyo la respuesta viendo si el minimo es igual a trabajar en londres o califronia
def londres_california(l,c,m):
    #estos optimos son para el valor mínimo que puedo tener en el mes i sabiendo que estoy en
    #california o londres

    opt_c=[1000000]*(len(l)+1)
    opt_l=[1000000]*(len(c)+1)
    opt_c[0]=c[0]
    opt_l[0]=l[0]
    for i in range(1,len(c)):
        #estando en california
        opt_c[i]=min(c[i]+opt_c[i-1],opt_c[i-1]+l[i]+m)
        #estando en londres
        opt_l[i]=min(l[i]+opt_l[i-1],opt_l[i-1]+c[i]+m)

    return getRes(opt_l,opt_c,m,l,c)



#(valor,peso)
def mochila(elementos,w):
    opt=[[0 for _ in range(w+1)] for _ in range(len(elementos)+1)]

    for fila in len(opt):
        for columna in len(opt[0]):
            #ese elemento puede llegar a entrar en la mochila actual
            if elementos[fila-1][1]<=columna:
                opt[fila][columna]=max(opt[fila-1][columna],opt[fila-1][columna-elementos[fila-1][1]]+elementos[fila-1][0])
            else:
                opt[fila][columna]=opt[fila-1][columna]
    
    return getRes(elementos,opt,w)

def getRes(elementos,opt,w):
    res=[]

    for i in range(len(elementos),1,-1):
        if opt[i][w]!=opt[i-1][w]:
            res.append(elementos[i-1])
            w-=elementos[i-1][1]
    
    return res

#puedo repetir el elemento


def mochila_parcial(elementos,w):
    opt=[[0 for _ in range(w+1)] for _ in range(len(elementos)+1)]

    for fila in len(opt):
        for columna in len(opt[0]):
            #mientras no supere la capcacidad, puedo agregar el elemento cuantas veces quiera
            if elementos[fila-1][1]<=columna:
                #se puede repetir el elemento actual cuantas veces sea necesario
                opt[fila][columna]=max(opt[fila-1][columna],opt[fila-1][columna-elementos[fila][1]]+elementos[fila-1][0])
            else:
                opt[fila][columna]=opt[fila-1][columna]

    return opt


#Dyc




def suma_contigua(arr):
    _,ini,fin= wrapper_suma(arr,0,len(arr)-1)
    return ini,fin

def wrapper_suma(arr,ini,fin):
    if ini==fin:
        return ini,fin
    medio=(ini+fin)//2

    cant_izq,ini_izq,fin_izq=wrapper_suma(arr,ini,medio)
    cant_der,ini_der,fin_der=wrapper_suma(arr,medio+1,fin)

    cant_centro,ini_centro,fin_centro=suma_cruzada(arr,ini,medio,fin)

    if cant_izq>cant_der and cant_izq>cant_centro:
        return ini_izq,fin_izq
    elif cant_der>cant_izq and cant_der>cant_centro:
        return ini_der,fin_der
    








#[c1,c2,c3,c4,d1,d2,d3,d4]
#ini=0,fin=8,medio=4
#for i in range(1,5,2)
# [c2],[d2]=[d2],[c2]
#[c1,d2,c3,c4,d1,c2]


def alternar(arr):
    return wrapper_alternar(arr,0,len(arr)-1)

def wrapper_alternar(arr,ini,fin):
    if fin-ini<2:
        return arr
    
    medio=(ini+fin)//2

    izq=wrapper_alternar(arr,ini,medio)
    der=wrapper_alternar(arr,medio+1,fin)
    
    for i in range(1,medio-ini+1,2):
        arr[ini+i],arr[medio+i]=arr[medio+1],arr[]






#
#Tn= A*T(n/b)+O(n**c) siendo A la cant de llamados recursivos, b las porciones en las que dividimos
# y c el costo de las otras operaciones

#log2(2)=1  ===> O(n log2(n))
#logb(A)<C ==> O(n**c)
#logb(A)==c ==> O(N ** c logb(n))
#logb(A)>c ==> O(N**logb(A))

def mas_mitad(arreglo):
    return wrapper_mitad(arreglo,0,len(arreglo)-1)

def wrapper_mitad(arreglo,ini,fin):
    if ini==fin:
        return arreglo[ini]
    
    medio=(ini+fin)//2
    #A=2
    izq=wrapper_mitad(arreglo,ini,medio)
    der=wrapper_mitad(arreglo,medio+1,fin)

    ap_izq,ap_der=0,0

    #O(N),c=1,b=2
    for i in range(ini,fin+1):
        if arreglo[i]==izq:
            ap_izq+=1
        elif arreglo[i]==der:
            ap_der+=1
        else:
            continue
    
    if ap_izq>ap_der:
        return izq
    else:
        return der







def mitad_rapido(arreglo):
    candidato=wrapper_mitad(arreglo)
    return None if candidato is None or arreglo.count(candidato)<=len(arreglo)//2 else candidato

def wrapper_mitad(arreglo):
    if len(arreglo)==1:
        return arreglo[0]
    
    res=[]

    for i in range(0,len(arreglo)-1,2):
        if arreglo[i]==arreglo[i+1]:
            res.append(arreglo[i])
    if res==[]:
        return None
    candidato=wrapper_mitad(res)
    

def mas_mitad(arreglo):
    return wrapper_mitad(arreglo,0,len(arreglo)-1)

def wrapper_mitad(arreglo,ini,fin):
    if ini==fin:
        return arreglo[ini]
    
    medio=(ini+fin)//2

    izq=wrapper_mitad(arreglo,ini,medio)
    der=wrapper_mitad(arreglo,medio+1,fin)

    cont1,cont2=0,0
    for i in range(ini,fin+1):
        if izq==arreglo[i]:
            cont1+=1
        if der==arreglo[i]:
            cont2+=1
    if cont1>=medio:
        return izq
    if cont2>=medio:
        return der
    return None





def maxima_suma(arreglo):
    _,ini,fin=wrapper_suma(arreglo,0,len(arreglo)-1)
    return ini,fin


#A=2,B=2,C=1
#log2(3)>0 ==> O(n**log2(3))
def wrapper_suma(arreglo,ini,fin):
    if ini==fin:
        return arreglo,ini,fin
    
    medio=(ini+fin)//2

    suma_izq,ini_izq,fin_izq=wrapper_suma(arreglo,ini,medio)
    suma_der,ini_der,fin_der=wrapper_suma(arreglo,medio+1,fin)

    suma_centro,ini_centro,fin_centro=suma_cruzada(arreglo,ini,medio,fin)

    if suma_izq>=suma_der and suma_izq>=suma_centro:
        return suma_izq,ini_izq,fin_izq
    elif suma_der>suma_izq and suma_der>=suma_centro:
        return suma_der,ini_der,fin_der
    else:
        return suma_centro,ini_centro,fin_centro
    
def suma_cruzada(arreglo,ini,medio,fin):
    #almacena la maxima suma que puedo conseguir de cada lado
    suma_izq,suma_der=float("-inf"),float("-inf")

    
    indice_inicio_izq=medio
    indice_final_der=medio+1

    #suma acumulativa temporal
    total_izq,total_der=0,0

    for i in range(medio,ini-1,-1):
        total_izq+=arreglo[i]
        if total_izq>suma_izq:
            suma_izq=total_izq
            indice_inicio_izq=i
    
    for i in range(medio+1,fin+1):
        total_der+=arreglo[i]
        if total_der>suma_der:
            suma_der=total_der
            indice_final_der=i
    
    return suma_izq+suma_der,indice_inicio_izq,indice_final_der


def osvaldo(dias):
    _,compra,venta=wrapper_osvaldo(dias,0,len(dias)-1)
    return compra,venta

def wrapper_osvaldo(dias,ini,fin):
    if ini==fin:
        return ini,fin
    
    medio=(ini+fin)//2

    max_izq,compra_izq,venta_izq=wrapper_osvaldo(dias,ini,medio)
    max_der,compra_der,venta_der=wrapper_osvaldo(dias,medio+1,fin)

    max_centro,compra_centro,venta_centro=compra_cruzada(dias,ini,medio,fin)

    if max_izq>max_der and max_izq>max_centro:
        return max_izq,compra_izq,venta_izq
    elif max_der>max_izq and max_der>max_centro:
        return max_der,compra_der,venta_der
    else:
        return max_centro,compra_centro,venta_centro
    

def compra_cruzada(dias,ini,medio,fin):
    indice_inicio_izq=medio
    indice_fin_der=medio+1

    max_izq,max_der=-100000,-1000000

    suma_izq=0
    suma_der=0

    for i in range(medio,0,-1):
        suma_izq+=dias[i]
        if suma_izq>max_izq:
            max_izq=suma_izq
            indice_inicio_izq=i
    for i in range(medio+1,fin+1,1):
        suma_der+=dias[i]


#Reducciones


#isomorfico: dados dos grafos, se puede decir que uno de ellos es isomorfo del otro si sus vertices
#comparten estructura en el grafo.

#K_Clique: se puede crear un clique de tamaño k

def validador_isomorfo(g1,g2,res):
    #en este caso sería decir que g2 es isomorfo de g1

    for vertice in res:
        for w in res:
            if not g1.estan_unidos(vertice,w):
                return False
    
    return True

#planteo que kclique<=p isomorfismo

#osea que debo poder resolver kclique mediante isomorfismo





#path selection: dado un grafo dirigido y P caminos
#se puede seleccionar al menos k caminos tal que no compartan vertices

#demostrar que es npc sabiendo que independent set lo es.
#IS<=p Path selection

#resolver independent set mediante path selection

#is: conjunto de vertices que no comparten conexiones entre si

#podría hacer que cada path sea el conjunto de cada vertice + sus adyacentes, si consigo aquellos paths
#de los cuales no comparten conexiones entre si, con agarrar un vertice de cada uno ya me aseguraría tener un independent set








#demostrar dominating set es npc sabiendo que vertex cover lo es
#dominating set: conjunto de k vertices que conectan con todo el grafo
#vertex cover: conjunto de k vertices que conectan todas las aristas

#vertex cover<=p dominating set

#tengo que poder resolver vertex cover mediante dominating

#quiero dominar todas las aristas: puedo plantear un grafo donde cada arista original ahora
#esta representada como un vertice(el vertice representa la pareja de vertices conectados originalmente)
#y las conexiones entre esos vertices se da por las conexiones de los vertices en el grafo original
#es decir, en el grafo original tenemos el vertice V que conecta con u y con w. En nuestro
#nuevo grafo tendríamos un vertice que representa la pareja (u,v) y (w,v) conectadas entre sí al compartir un extremo
#pedirle un dominating set  a este nuevo grafo nos devolvería el conjunto de aristas que conectan con todo el grafo.
#solo necesitaríamos agregar uno de esos extremos por cada arista y ya tendríamos un vertex cover

#mediante esto, podríamos resolver vertex cover mediante una resolución de dominating set








#2-Partition: tengo un conjunto de n elementos, se los separa en dos subconjuntos tal que
# la suma de los mismos es igual. Es NP-C

#Subset sum: dado un arreglo de elementos y un valor n, devolver el conjunto de elementos 
#que suma n

def validador_subset(res,valor):
    return sum(res)==valor

#Demostrar que Subset es npc sabiendo que 2-partition lo es
#2P<=p Subset
#es decir, que subset sum permita resolver 2-partition

#Si queremos dos subconjuntos que sumen exactamente lo mismo
#sabemos que la suma de ambos subconjuntos es la suma total de todos los elementos
#lo que podemos pedirle a subset sum es que nos encuentre un subconjunto que sume la mitad del total
#de todos los elementos y una vez nos devuelva un subconjunto también tendríamos el otro por descarte




#hitting set problem: de un conjunto A con n elementos, formo m subconjuntos de A
#dado un numero k, puedo generar un conjunto C de tamaño <=k tal que al menos haya un elemento de cada subconjunto

#demostrar que es np-completo dado que Dominating Set lo es.


#validador polinómico O(M*V*K) siendo M la cantidad de subconjuntos, V la cantidad total de vertices de A y
# K el tamaño del subconjunto de respuesta
def validador_hitting_set(grafo,m_subconjuntos,res,k):
    if len(res)>k:
        return False
    
    for conjunto in m_subconjuntos:
        ok=False
        for elemento in conjunto:
            for w in res:
                if w==elemento:
                    ok=True
        
        if not ok:
            return False

    return True

#ahora que demostre que es NP, 
#planteo Dominating set<=p Hitting set

#para poder resolver dominating set mediante hitting set puedo agarrar mi grafo y crear un conjunto
#A que contiene todos los vertices, cada subconjunto estaría dado por los vertices y sus adyacencias correspondientes
#si obtenemos un hitting set de estos sub conjuntos tendríamos al menos un vertice de cada uno, lo que sería un dominating set
#es por eso que podemos resolver dominating set mediante hitting set





#resuelvo el npc mediante el np
#npc<=p np

#demostrar que separación en R cliques es NP-C sabiendo que R-coloreo es NP-C

#validador en tiempo polinómico O(R*V(cuadrático)) siendo r la cantidad de cliques y v la cantidad de vertices de los cliques
def validador_r_cliques(grafo,res,r):
    if len(res)<r:
        return False
    
    visitados=set()

    for clique in res:
        for v in clique:
            
            #veo que sean cliques
            for w in clique:
                if not grafo.estan_unidos(v,w):
                    return False
                
    #veo ahora que sean cliques disjuntos

    for clique in res:
        for v in clique:
            if v not in visitados:
                visitados.add(v)
            else:
                return False
    
    return True

#demostré que separación en R cliques es NP, ahora planteo una reducción con R-Coloreo.
#Rcoloreo<=p Rcliques

#en mi reducción debería demostrar que a partir de rcliques podría resolver el problema de rcoloreo
#lo que puedo hacer es crear un grafo inverso que tiene conexiones que no se conectan con los vertices originales en el grafo
#al pedirle un clique a ese grafo, obtendría el conjunto de vertices que no se conectan en el grafo original.



#ahora de nuevo, demostrear que r cliques es npc sabiendo que independent set lo es.

#IS<=p K_clique

#resolver independent set mediante r cliques.
#obtener un conjunto de vertices independientes entre sí de tamaño k


#Lineal

#Juan el vago==> maximizar ganancias sabiendo que no va a trabajar 3 días seguidos
#podemos plantear variables binarias que indican si ese día trabajó
#definimos el problema de maximización
# Maximizar Sumatoria (dias[i]*binarias[i])
#Ponemos como condición que la sumatoria de las binarias
#adyacentes puede ser a lo mucho 2
#Sumatoria (binarias[i-1]+binarias[i]+binarias[i+1])<=2


#Osvaldo==> maximizar la ganancia posible y devolver el dia de venta y compra
#Planteo variables binarias tanto para los días de venta como de compra
#Planteo que el indice de la variable de compra es menor al de venta
#indice_venta<indice_compra
#Planteo que:
#Maximizar Sumatoria (dias[i]*dia_venta[i]-dias[j]*dia_compra[j])
#Ahora planteo que solo puede haber un único día de compra y venta
#Sumatoria dia_venta <=1
#Sumatoria dia_compra<=1
    

