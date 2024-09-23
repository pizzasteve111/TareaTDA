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
#actual, es decir si n=4 tiene p=2, significa que de la charla 2 para abajo
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

# def scheduling(charlas):
#     #ordeno las charlas por fin mas proximo
#     charlas.sort(key=lambda x: x[1])
#     tam=len(charlas)
#     p=getP(charlas)
#     optimos=getOptimos(tam,charlas,p)
#     seleccionadas=getSeleccionadas(optimos,charlas,p)
#     res=[]
#     for s in seleccionadas:
#         res.append[s]

#     return res

# def getOptimos(tam,charlas,p):
#     optimos=[0] * (tam+1)

#     for i in range(1,tam+1):
#         indice= i-1
#             valor_incluir = charlas[charla_index][2] + (optimo_scheduling[p[charla_index] + 1] if p[charla_index] != -1 else 0)
#         valor_agregar=charlas[indice][2]+
