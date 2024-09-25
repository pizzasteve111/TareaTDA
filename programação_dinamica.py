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
    #hago matriz de dimensiones tam * W
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

