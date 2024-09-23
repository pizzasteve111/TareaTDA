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