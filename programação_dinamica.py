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