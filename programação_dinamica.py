#Ejs obtenidos de:https://algoritmos-rw.github.io/tda_bg/material/guias/


#esta es una solucion sin prog dinamica

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-2) + fib(n-1)

#ahora, con prog dinamica, la sol es:

#ESta sol esta en la diapo pero anda pal caralho mano

# def fib_dinamico(n):
#     if n<=1:
#         return n
#     anterior=0
#     actual=1
#     for i in range(1,n):
#         nuevo=actual+anterior
#         anterior=actual
#         actual=nuevo
#     return actual

#sol piola
def fibonacci(n):

    if (n == 0 or n == 1):
        return 1
    #lista del tam de n
    M_FIB = [None] * (n+1)
    #valores base
    M_FIB[0] = 1
    M_FIB[1] = 1
    #arrancamos desde el primer valor no cubierto hasta n(n+1 es por el tema del indice)
    for i in range(2, n+1):
        M_FIB[i] = M_FIB[i-1] + M_FIB[i-2]
    return M_FIB[n] 


#2
# (inicio,fin,valor)
#el vector p indica la posicion en la que hay charlas que no se cruzan con el 
#actual, es decir si n=4 tiene p=2, significa que del indice 2 para abajo
#puedo dar cualquiera, esto seria la memorizao paa 

def getP(charlas):
    p=[-1]*len(charlas)
    
    for i in range(len(charlas)):
        for j in range(i-1,-1,-1):
            #lo que hago es ver las charlas anteriores cuyos fines
            #son menores al inicio actual
            #las voy pisando y me quedo con la mas proxima de las validas
            if charlas[j][1]<=charlas[i][0]:
                p[i]=j
                break
    return p

def scheduling(charlas):
    #ordeno las charlas por fin mas proximo
    charlas.sort(key=lambda x: x[1])
    tam=len(charlas)
    p=getP(charlas)
    #busco el optimo para cada  cant de charlas
    optimos=getOptimos(tam,charlas,p)
    #seleccionadas serian aquellas charlas que van a ir a la solucion optima
    #el arreglo almacena los indices a dichas charlas
    seleccionadas=getSeleccionadas(optimos,charlas,p)
    res=[]
    for s in seleccionadas:
        res.append(charlas[s])

    return res

def getOptimos(tam,charlas,p):
    #este arreglo sirve para guardar el valor acumulado para la n-esima charla
    optimos=[0] * (tam+1)

    for i in range(1,tam+1):
        indice= i-1
        #el valor de la charla actual sobre la que estoy iterando
        ganancia_actual=charlas[indice][2]
        #obtengo el optimo actual
        valor_excluido=optimos[indice]

        #si hay una charla que no se solapa con la actual
        #entonces el valor actualizado va a ser el valor de dicha charla valida
        #sumada al valor de la charla actual
        if p[indice]!=-1:
            # explico optimos[p[indice]+1] :
            #p[i] me devuelve el indice de la charla valida para la i-esima charla
            #entonces quiero el valor optimo para la charla anterior que sea valida
            #con la actual
            valor_nuevo=ganancia_actual + optimos[p[indice]+1]
        else:
            #en caso de que no hay una charla anterior valida
            #la charla actual va a tener como acumulado su propio valor
            valor_nuevo=ganancia_actual
        
        
        
        #el valor maximo para la charla i va a ser el max entre
        #su optimo actual o su optimo actualizado 
        optimos[i]=max(valor_nuevo,valor_excluido)

    return optimos

def getSeleccionadas(optimos,charlas,p):
    cont=len(charlas)
    seleccionadas=[]

    while cont>0:
        indice=cont-1
        valor_actual=charlas[indice][2]
        #si existe una charla valida que no se solapa con la actual
        if p[indice]!=-1:
            #el nuevo valor sería el de dicha charla + el acumulado
            #anteriormente
            valor_actualizau=valor_actual+optimos[p[indice]+1]
        else:
            #y si no es asi, solo va a ser el valor de la charla misma
            valor_actualizau=valor_actual
        

        valor_excluir=optimos[indice]

        #en caso que tenga que pisar valores
        #actualizo y cambio el contador para que itere desde la ultima charla modificada
        if valor_actualizau>valor_excluir:
            seleccionadas.append(indice)
            cont=p[indice]+1
        else:
            cont-=1

    #hago el reverse porque en mi while estuve iterando de mayor a menor, quiero devolver las charlas en orden inverso
    seleccionadas.reverse()
    return seleccionadas

#segun entiendo, esta solucion cumpliría con prog dinamica pues:
#1) resuelvo el problema solucionando sub-problemas(busco el optimo para cada i-esima charla)
#2)Uso memorizacion porque voy armando arreglos como optimos o p que me van almacenando soluciones parciales a los subproblemas
#3)Aplico funciones de recurrencia donde optimizo que valores se deben pisar para cada caso


#3 

#ec recurrencia sería: Opt(n)=Opt(n-1)+Opt(n-2)+Opt(n-3)


def escalones(n):
    if n==0 or n==1:
        return 1
    if n==2:
        return 2
    
    optimos=[0]*(n+1)

    optimos[0]=1
    optimos[1]=1
    optimos[2]=2

    for escalon_i in range(3,n+1):
        optimos[escalon_i]=optimos[escalon_i-1]+optimos[escalon_i-2]+optimos[escalon_i-3]

    return optimos[n]

#4
#ec recurrencia= Opt(n)=max(Opt(n-1),Opt(n-2)+arr[n-1])

def get_optimos(trabajos):
    tam=len(trabajos)
    if tam==0:
        return [0]
    if tam==1:
        return [0,trabajos[0]]
    
    optimos=[0]*(tam+1)
    optimos[1]=trabajos[0]
    optimos[2]=max(trabajos[0],trabajos[1])
    for i in range(3,tam+1):
        #esto quiere decir, el optimo de i será el máximo entre trabajar el día anterior
        #o trabajar dos dias anteriores y el actual(lo acumulado hasta anteayer + hoy)
        optimos[i]=max(optimos[i-1],optimos[i-2]+trabajos[i-1])
    
    return optimos

def getRes(optimos,trabajos,contador):
    res=[]
    while contador>0:
        
        #si el optimo entre trabajar hoy o ayer es lo mismo, significa que juan no trabajó el día actual

        if optimos[contador-1]==optimos[contador]:
            contador-=1
        #si son distintos significa que si trabaje el día actual
        else:
            res.append(contador-1)
            contador-=2

    res.reverse()
    return res

def juan_el_vago(trabajos):
    optimos=get_optimos(trabajos)
    res=getRes(optimos,trabajos,len(trabajos))
    return res


#5

#7-mochila

# cada elemento i de la forma (valor, peso)
#ecuacion de recurrencia: Opt(N,W)=max(Opt(N-1,W),Opt(N-1,W-peso)+Valor) ,es decir,
#el valor maximo entre no agregar el elemento o agregarlo(reduciendo peso disponible y sumando el valor del mismo)
def mochila(elementos, W):
    tam_arreglo=len(elementos)
    #hago matriz de dimensiones donde la cantidad de fila es la cant_elementos y la cant de 
    #columnas es el W asignado
    optimos=[[0 for _ in range(W+1)] for _ in range(tam_arreglo+1)]
    

    #recorro la matriz

    for fila in range(1,tam_arreglo+1):
        for columna in range(1,W+1):
            #puede entrar algo mas en el peso
            if elementos[fila-1][1]<=columna:
                #me quedo re largo, pero sería comparar entre no modificar la mochi acttual o agregarlo y con eso restar el espacio
                #disponible, pero sumando el valor que aporta el agregado
                optimos[fila][columna]=max(optimos[fila-1][columna],optimos[fila-1][columna-elementos[fila-1][1]]+elementos[fila-1][0])
            else:
                #si el espacio superaba al peso disponible, entonces el optimo para el objeto actual es omitirlo y quedarse
                #con el valor anterior
                optimos[fila][columna]=optimos[fila-1][columna]

    return getRes(optimos,W,tam_arreglo,elementos)

def getRes(optimos,W,tam_arreglo,elementos):
    res=[]
    for i in range(tam_arreglo,0,-1):
        #comparo el optimo entre incluir al elemento iterado con el optimo anterior a no considerarlo
        #si estos difieren, significa que el i-esimo elemento es tomado encuenta para la solucion optima
        if optimos[i][W]!=optimos[i-1][W]:
            #appendeo el indice-1 pero porque comienza a contar desde cero
            res.append(elementos[i-1])
            #le resto el peso para que quede actualizau
            W-=elementos[i-1][1]

    #devuelvo la lista inversa pq estuve iterando en sentido contrario
    res.reverse()
    return res


#8  
#ec recurrencia: el optimo para el valor i, min(opt[i],opt[i-moneda_actual]+1)
#esto quiere decir que para el valor i, su optimo sería el mínimo entre su optimo actual o
#ese valor-la moneda iterada, el +1 significa que agregarías la moneda que iteras

def cambio(monedas, monto):
    #cada valor de este arreglo sería el valor optimo para el cambio de valor i
    optimos=[10000000]*(monto+1)
    #para 0 pesos necesito 0 monedas
    optimos[0]=0
    for moneda in monedas:
        for i in range(moneda,monto+1):
            #el optimo para el valor i (que se encuentra entre la moneda y el monto)
            #es el minimo entre el optimo actual o el valor i-moneda
            #EJ: si tengo el arreglo  [1, 5, 10], y busco el optimo del valor 2 con la moneda 1
            #inicialmente seria hacer min(10000000,2-1+1) diciendome que para el valor 2
            #necesitaría dos monedas
            optimos[i]=min(optimos[i],optimos[i-moneda]+1)
    
    return getRes(optimos,monedas,monto)
    
def getRes(optimos,monedas,contador):
    res=[]
    while contador>0:
        for moneda in monedas:
            #comparamos para que moneda del arreglo llegamos al optimo del valor contador
            #en caso de que esa moneda cumpla, lo appendeamos
            if optimos[contador]==optimos[contador-moneda]+1 and contador-moneda>=0:
                res.append(moneda)
                contador-=moneda
                #rompo el ciclo porque ya no hace falta seguir buscando para ese valor
                break

    return res

#9
##igual al prob de la mochi.


def subset_sum(elementos,v):
    tam=len(elementos)
    optimos=[[0 for _ in range (v+1)]for _ in range(tam+1)]

    for fila in range(1,tam+1):
        for columna in range(v+1):
            if elementos[fila-1]<=columna:
                optimos[fila][columna]=max(optimos[fila-1][columna],optimos[fila-1][columna-elementos[fila-1]]+elementos[fila-1])
            else:
                optimos[fila][columna]=optimos[fila-1][columna]

    return getRes(elementos,v,optimos,tam)

def getRes(elementos,v,optimos,tam):
    res=[]
    for i in range(tam,0,-1):
        if optimos[i][v]!=optimos[i-1][v]:
            res.append(elementos[i-1])
            v-=elementos[i-1]

            if v<0:
                break
    res.reverse()

    return res




#10

#ec recurrencia, para el mes i, su optimo sería Opt(i)=min(Opt(ciudad_actual i),Opt(cambio_ciudad)+M)
#osea, mi criterio va a ser, elijo trabajar en la otra ciudad solo si sus costos(+ mudanza) son
#menores a los de trabajar en la actual
def plan_operativo(arreglo_L, arreglo_C, costo_M):
    n=len(arreglo_L)
    optimos_C=[0]*(n+1)
    optimos_L=[0]*(n+1)
    
    optimos_C[0]=arreglo_C[0]
    optimos_L[0]=arreglo_L[0]

    for i in range (1,n):

        optimos_C[i]=min(optimos_C[i-1]+arreglo_C[i],optimos_L[i-1]+arreglo_C[i]+costo_M)

        optimos_L[i]=min(optimos_L[i-1]+arreglo_L[i],optimos_C[i-1]+arreglo_L[i]+costo_M)

    

    #reconstruir esta wea
    

    
    return getRes(optimos_L,optimos_C,arreglo_L,arreglo_C,n,costo_M)

def getRes(optimos_L,optimos_C,arreglo_L,arreglo_C,n,costo_M):
    res=[]
     
    #caso para la primer ciudad
    if optimos_C[n - 1] < optimos_L[n - 1]:
        res.append("california")
        ciudad_actual = "california"
    else:
        res.append("londres")
        ciudad_actual = "londres"

    
    for i in range(n - 2, -1, -1):
        if ciudad_actual == "california":
            #si el valor optimo de trabajr en california + costo de otro mes es igual a dicho optimo
            #si fueran distintos, significa que el mes i venía de Londres
            #entonces el optimo para el mes i sería londres
            if optimos_C[i] + arreglo_C[i + 1] == optimos_C[i + 1]:
                res.append("california")
            else:
                res.append("londres")
                ciudad_actual = "londres"
        else:
            if optimos_L[i] + arreglo_L[i + 1] == optimos_L[i + 1]:
                res.append("londres")
            else:
                res.append("california")
                ciudad_actual = "california"

    res.reverse()
    return res


#11

#recurrencia: el optimo de un numero i sería el minimo entre los optimos de (i-1)
#y de (i//2), esto quiere decir, me quedo con el optimo que tenga la cantidad de pasos mas chica
#entre los dos y le sumo el paso extra que doy

def operaciones(K):
    #uno de los arreglos guarda la cantidad de operaciones para un numero i
    #mientras que el otro guarda los strings
    optimos=[10000000000]*(K+1)
    operaciones=[""]*(K+1)
    #no necesito ninguna operacion para el numero 0
    optimos[0]=0

    #entendiendo que trabajo con nums enteros, solo puedo duplicar para 
    #aquellos numeros pares, si mi num es 5 no hay ningun *2 que me ayude a 
    #conseguirlo
    for i in range(1,K+1):
        #evalúo si el optimo actual de i es mayor al optimo del numero
        #anterior + la operacion actual
        if optimos[i-1]+1<optimos[i] :
            optimos[i]=optimos[i-1]+1
            operaciones[i]="mas1"
        if optimos[i//2]+1<optimos[i] and i%2==0:
            #esto significa que si la minima cantidad de operaciones para 
            #llegar al numero i//2 +1 es menor que el optimo actual
            #lo ideal sería duplicar i//2 sumandole esa operacion
            optimos[i]=optimos[i//2]+1
            operaciones[i]="por2"

    return getRes(K,optimos,operaciones)

def getRes(contador,optimos,operaciones):
    res=[]
    while contador>0:
        res.append(operaciones[contador])
        if operaciones[contador]=="por2":
            contador//=2
        else:
            contador-=1

    res.reverse()
    return res


#12-

# cada campaña publicitaria i de la forma (Gi, Ci)
#Me suena a un idem del problema de la mochila
#A priori, intuiría que el optimo para la campaña i es max(Opt(no hago la i_esima campaña),Opt(hago la campaña y resto su coste al presupuesto, pero sumo el valor obtenido))


def carlitos(c_publicitaria, P):
    #separo el arreglo en dos para mas placer
    costos=[c_publicitaria[i][1] for i in range(0,len(c_publicitaria))]
    ganancias=[c_publicitaria[i][0] for i in range(0,len(c_publicitaria))]
    tam_arreglo=len(c_publicitaria)
    #repito lo de la mochi, una matriz donde el tamaño de sus col lo determina el P
    #y las filas por la cantidad de elementos
    optimos=[[0 for _ in range(P+1)] for _ in range(tam_arreglo+1)]

    for fila in range(1,tam_arreglo+1):
        for columna in range(1,P+1):
            #esto vendría a significar, si el costo del item iterado es menor al presupuesto actual
            #entonces puedo ver de calcular un optimo para las dimensiones dadas
            #Aplico, entonces, la ec de recurrencia de la mochi
            if costos[fila-1]<=columna:
                optimos[fila][columna]=max(optimos[fila-1][columna],optimos[fila-1][columna-costos[fila-1]]+ganancias[fila-1])
            else:
                #si entro aca, significa que el costo de la campaña actual es muy grande para el P dado
                #entonces el optimo sería no realizar la campaña y que su optimo sea la sol anterior
                optimos[fila][columna]=optimos[fila-1][columna]

    return getRes(optimos,tam_arreglo,P,c_publicitaria,costos)


def getRes(optimos,tam_arreglo,P,c_publicitaria,costos):
    res=[]
    for i in range(tam_arreglo,0,-1):
        #si los optimos de la actual y el anterior difieren, significa que el optimo de la campaña actual la considera 
        if optimos[i][P]!=optimos[i-1][P]:
            res.append(c_publicitaria[i-1])
            #voy actualizando el presupuesto en base a la campaña que itero
            P-=costos[i-1]

    res.reverse()
    return res

#13

#Bueno, vuelve a ser un ej de mochis :P
#Copiar y pegar, solo que ajustando a que ahora es un arreglo de un único elemento

def bodegon_dinamico(P, W):
    tam_arreglo=len(P)
    #hago matriz de dimensiones donde la cantidad de fila es la cant_elementos y la cant de 
    #columnas es el W asignado
    optimos=[[0 for _ in range(W+1)] for _ in range(tam_arreglo+1)]

    for fila in range(1,tam_arreglo+1):
        for columna in range(1,W+1):
            if P[fila-1]<=columna:
                optimos[fila][columna]=max(optimos[fila-1][columna],optimos[fila-1][columna-P[fila-1]]+P[fila-1])
            else:
                #si el espacio superaba al peso disponible, entonces el optimo para el objeto actual es omitirlo y quedarse
                #con el valor anterior
                optimos[fila][columna]=optimos[fila-1][columna]

    return getRes(P,W,tam_arreglo,optimos)

def getRes(P,W,tam_arreglo,optimos):
    res=[]
    for i in range(tam_arreglo,0,-1):
        if optimos[i][W]!=optimos[i-1][W]:
            res.append(P[i-1])
            W-=P[i-1]

    res.reverse()
    return res


#14

#Me suena mucho a Juan el Vago, cambiando los dias adyacentes por casas adyacentes,
#su ec de recurrencia para la casa i sería Opt(i)=max(Opt(i-1),Opt(i-2)+arr[i-1])
#vendría ser elegir entre no robar la casa i y quedarme con el optimo de la casa anterior, o
#robar la casa actual, almacenar su valor, y sumarle el optimo de la casa no adyacente mas cercana


#Hay que adicionar el caso de que es circular, entonces la casa 0 y n-1 cumplen adyacencias
#lo que hago entonces es obtener el optimo tanto para el caso donde robo la primer casa
#como para el caso donde robo la ultima y devuelvo el maximo entre esos dos
def lunatico_no_circular(ganancias):
    tam_arreglo=len(ganancias)
    if tam_arreglo==0:
        return []
    if tam_arreglo==1:
        return [0]
    optimos=[0]*(tam_arreglo+1)
    optimos[1]=ganancias[0]
    if tam_arreglo>1:
        optimos[2]=max(ganancias[0],ganancias[1])
    for i in range(3,tam_arreglo+1):
        optimos[i]=max(optimos[i-1],optimos[i-2]+ganancias[i-1])
    
    return getRes(optimos,tam_arreglo,ganancias)


def getRes(optimos,tam_arreglo,ganancias):
    res=[]
    while tam_arreglo>0:
        #si los optimos del actual y el anterior son iguales, significa que no entre a robar
        #la casa actual
        if optimos[tam_arreglo]==optimos[tam_arreglo-1]:
            tam_arreglo-=1
        else:
            res.append(tam_arreglo-1)
            #ni voy a tener en cuenta la casa adyacente
            tam_arreglo-=2

    res.reverse()
    return res

def lunatico(ganancias):
    if sum(ganancias)==0:
        return []
    if len(ganancias)==1:
        return [0]
    ganancias_excluyo_primera=ganancias[1:]
    ganancias_excluyo_ultima=ganancias[:-1]

    optimo_excluyo_primera=lunatico_no_circular(ganancias_excluyo_primera)
    optimo_excluyo_ultima=lunatico_no_circular(ganancias_excluyo_ultima)

    #ajusto el indice sumandole 1 porque omito la casa 0
    optimo_excluyo_primera=[i+1 for i in optimo_excluyo_primera]

    #calculo la ganancia total tanto de robar la primera como de robar la ultima
    ganancias_excluyo_primera=sum(ganancias[i] for i in optimo_excluyo_primera)
    ganancias_excluyo_ultima=sum(ganancias[i] for i in optimo_excluyo_ultima)

    if ganancias_excluyo_ultima>ganancias_excluyo_primera:
        return optimo_excluyo_ultima
    return optimo_excluyo_primera


#15

#caso base, la soga mide 2

def problema_soga(n):
    
    if n == 2:
        return 1  
    if n == 3:
        return 2  

    
    optimos = [0] * (n + 1)
    
    
    optimos[1] = 1 
    optimos[2] = 1  
    optimos[3] = 2 

    
    for i in range(4, n + 1):
        #itero en cachitos mayores a la mitad de la soga
        for cachito in range(1, i // 2 + 1):  # j es el tamaño del primer corte
            #los optimos puede ser el del caso base, el cacho de la cuerda * el resto, o el cacho
            #* el optimo del resto
            optimos[i] = max(optimos[i], cachito * (i - cachito), cachito * optimos[i - cachito])

    return optimos[n]






