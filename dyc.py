
def buscar_joya(arreglo):
    return wrapper_joya(arreglo,0,len(arreglo)-1)

def wrapper_joya(arr,ini, fin):
    if ini==fin:
        return arr[ini]
    medio=(ini+fin)//2
    izq=arr[:medio]
    der=arr[medio+1:]
    if balanza(izq,der)<0:
        return wrapper_joya(arr,medio+1,fin)
    elif balanza(izq,der)>0:
        return wrapper_joya(arr,ini,medio)
    else:
        return arr[medio]
    

def parte_entera_raiz(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    mitad = n // 2
    return dividir_y_conquistar(n, mitad, n)

def dividir_y_conquistar(n, raiz, cota_sup, cota_inf = None):
    cuadrado = raiz**2
    cuadrado_del_siguiente = (raiz + 1)**2

    if cuadrado == n or cuadrado_del_siguiente > n and cuadrado < n:
        return raiz

    if cuadrado > n: 
        mitad = raiz // 2
        if cota_inf != None and mitad < cota_inf:
            mitad = (cota_inf + raiz) // 2
            return dividir_y_conquistar(n, mitad, raiz, cota_inf)
        return dividir_y_conquistar(n, mitad, raiz)
     
    else: 
        cota_inf = raiz
        mitad = (cota_inf + cota_sup) // 2
        return dividir_y_conquistar(n, mitad, cota_sup, cota_inf)

    


def KaratsubaOffman(x,y):
    if x<10 or y<10:
        return x*y
    
    n = max(len(str(x)),len(str(y)))
    medio= n//2

    #x1 e y1 son las mitades superiores
   

    x1=x//10**medio
    x0=x%10**medio
    y1=y//10**medio
    y0=y%10**medio

    #se puede evitar una multiplicacion si se hace
    # un z1 que combine dos terminos

    z2=KaratsubaOffman(x1,y1)
    z0=KaratsubaOffman(x0,y0)
    z1=KaratsubaOffman(x1+x0,y1+y0)-z2-z0

    return z2 * 10**(2*medio)+z1*10**medio+z0


def merge_sort(arr):
    if len(arr)<=1:
        return arr
    medio = len(arr)//2
    izq=merge_sort(arr[:medio])
    der= merge_sort(arr[medio:])
    return merge(izq,der)

def merge(izq,der):
    if not izq:
        return der
    if not der:
        return izq
    if izq[0]<der[0]:
        return [izq[0]] + merge(izq[1:], der)
    else:
        return [der[0]]+merge(izq,der[1:])
    
#ej 9

def mas_de_la_mitad(arr):
    if len(arr)==0:
        return False
    if len(arr)==1:
        return True
    
    mitad=[]
    #O(n)
    for i in range(1,len(arr),2):
        if arr[i]==arr[i-1]:
            mitad.append(arr[i])

    
    candidato = mas_de_la_mitad(mitad)

    #si candidato no esta vacio y las apariciones de candidato en el arr
    #son mayores a la mitad, True
    if candidato is not None and arr.count(candidato) > len(arr)//2:
        return True

    #cantidad impar de elementos
    if len(arr)%2==1:
        candidato=arr[-1]
        if candidato is not None and arr.count(candidato) > len(arr)//2:
            return True

    return False

#O(n log n)
def mas_de_la_mitad(arr):
    if wrapper_mitad(arr,0,len(arr)-1) is not None:
        return True
    return False

def wrapper_mitad(arr,ini,fin):
    if ini==fin:
        return arr[ini]
    medio=(ini+fin)//2
    candidato_izq=wrapper_mitad(arr,ini,medio)
    candidato_der=wrapper_mitad(arr,medio+1,fin)

    if candidato_der==candidato_izq:
        return candidato_der
    
    apariciones_candidato_der=0
    apariciones_candidato_izq=0
    for i in range(ini,fin+1):
        if arr[i]==candidato_izq:
            apariciones_candidato_izq+=1
    
    for i in range(ini,fin+1):
        if arr[i]==candidato_der:
            apariciones_candidato_der+=1
    
    if apariciones_candidato_der>(fin-ini +1)//2:
        return candidato_der
    elif apariciones_candidato_izq>(fin - ini +1)//2:
        return candidato_izq
    
    return None


def mas_de_la_mitad_rec(arr):
    if len(arr)==1:
        return arr[0]
    candidatos=[]
    for i in range(0,len(arr)-1,2):
        if arr[i]==arr[i+1]:
            candidatos.append(arr[i])
    
    if candidatos==[]:
        return None
    
    candidato_final=mas_de_la_mitad_rec(candidatos)

    if candidato_final is not None and arr.count(candidato_final)> len(arr)//2:
        return candidato_final
    if len(arr)%2 != 0 and arr.count(arr[-1])>len(arr)//2:
        return candidato_final
    return None

def mas_de_la_mitad(arr):
    if mas_de_la_mitad_rec(arr) is not None:
        return True
    return False


#EJ 11
#Puede time outear porque RPL es una poronga gorda
#Pero anda bem
def mas_de_dos_tercios(arr):
    _,apariciones=wrapper_tercios(arr,0,len(arr)-1)

    if  apariciones > len(arr) * (2/3):
        return True
    return False


def contar_apariciones(arr,candidato,ini,fin):
    cont=0
    for i in range(ini,fin+1):
        if candidato==arr[i]:
            cont+=1
    return cont




def wrapper_tercios(arr,ini,fin):
    if ini==fin:
        return arr[ini],1
    
    medio=(ini+fin)//2
    izq,apariciones_izq=wrapper_tercios(arr,ini,medio)
    der,apariciones_Der=wrapper_tercios(arr,medio+1,fin)

    if izq==der:
        return izq,apariciones_Der+apariciones_izq

    total_izq=contar_apariciones(arr,izq,ini,fin)
    total_Der=contar_apariciones(arr,der,ini,fin)

    if total_Der>total_izq:
        return der,total_Der
    
    return izq,total_izq

#13

def max_subarray(arreglo):
    _,ini,fin= wrapper_massum(arreglo,0,len(arreglo)-1)
    return arreglo[ini,fin+1]

def wrapper_massum(arr,ini,fin):
    if ini==fin:
        return arr[ini],ini,fin
    
    medio=(ini+fin)//2

    suma_izq,izq_ini,izq_fin= wrapper_massum(arr,ini,medio)
    suma_der,der_ini,der_fin=wrapper_massum(arr,medio+1,fin)

    cruce_sum,cruce_ini,cruce_fin = hallar_maxS(arr,ini,medio,fin)

    if suma_izq >= suma_der and cruce_sum<=suma_izq:
        return suma_izq,izq_ini,izq_fin
    elif suma_der>=suma_izq and cruce_sum<=suma_der:
        return suma_der,der_ini,der_fin
    else:
        return cruce_sum, cruce_ini, cruce_fin
    

def hallar_masS(arr,ini,medio,fin):
    suma_izq,suma_der=[-10000],[-10000]
    izq_max,der_max=medio,medio+1

    izq_act,der_act=[0],[0]

    #busco la suma máxima a la izquierda
    #itero desde el medio hasta el final
    #se itera desde el medio hacia los costados
    #para que la suma sea contigua y se pueda tener
    #en cuenta el elemento del medio en las sumas
    for i in range(medio,ini-1,-1):
        izq_act[0]+=arr[i]
        if izq_act[0]>=suma_izq[0]:
            suma_izq.clear()
            suma_izq.extend(izq_act)
    
    for i in range(medio+1,fin+1):
        der_act+=arr[i]
        if der_act[0]>der_max[0]:
            suma_der.clear()
            der_max.extend(der_act)

    return der_max+izq_max, 
    




    



