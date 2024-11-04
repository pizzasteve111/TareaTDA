#Kruskal crea un MST a partir de las aristas de menor peso a mayor
#devuelve un grafo sin ciclos y con el peso mínimo entre aristas
#Es greedy pues en cada paso se elige la arista de menor peso que no provoque ciclos
#es una decision local que eventualmente da una solucion global optima

#Prim itera a partir de un vertice y mediante un heap va intercalando
#dicho vertice a aquellas aristas de menor peso
#es greedy pues el grafo se va a ir expandiendo siempre con la arista de menor peso

#4 SCHEDULING

#Hay que poder dar la mayor cantidad de charlas
#que no se solapen entre si

#Ordenamos las charlas segun horario de finalizacion
#osea van primero las charlas que terminan mas temprano
#e ir agregando charlas que no se solapen entre si

def scheduling(lista_horarios):
    #ordeno la lista, key recibe la funcion de filtro
    #lambda ordena de menor a mayor y especifico que es en el segundo elemento de la tupla

    lista_horarios.sort(key = lambda x: x[1])

    res=[]

    #el ultimo horario, para evitar solapamiento
    ultimo=-1

    for charla in lista_horarios:
        inicio,fin = charla

        if inicio>=ultimo:
            res.append(charla)
            ultimo=fin
    
    return res

#6
#Minimos billetes: devuelvo primero los primeros

def cambio(lista_billetes, precio):
    lista_billetes.sort() #O(n log n)
    lista_billetes.reverse() #O(n)
    res=[]
    
    #O(n)
    for billete in lista_billetes:
        while precio>= billete:
            precio-=billete
            res.append(billete)
    
    return res

#es greedy pues siempre elige la solucion localmente optima, es decir, billete de mayor denominacion
#que no supere el monto total a pagar.

print(cambio([1,3,4],6))
#No es optimoo debería devolver dos monedas de 3

#7
def inflacion(prods):
    j=0
    total=0
    prods.sort()
    prods.reverse()
    for prod in prods:
        total+= prod **(j+1)
        j+=1
    return total

#la solucion es greedy pues localmente va alamcenando los precios mas altos del día cosa de que termin
#emos pagando lo minimo debido a la inflacion, de forma que primero pagamos lo mas caro y luego pagamos
#lo potencialmente mas barato

#Es optimo pues si comprasemos de otra manera siempre terminaríamos gastando mas, lo mejor
#siempre es comprar lo mas caro antes de que la inflacion lo aumente mucho

#Ej deflacion-choreado del repo de luluu

def precios_deflacion(R):
    R_copy = R.copy()
    n = len(R)
    precio_total = 0
    precio_minimo = float('inf')
    for j in range(n):
        elemento_comprado = -1
        for i, price in enumerate(R_copy):
            if price < precio_minimo:
                precio_minimo = price
                elemento_comprado = i
        if elemento_comprado != -1:
            precio_total += (precio_minimo)/(2**j)
            del R_copy[elemento_comprado]
            precio_minimo = float('inf')
    return precio_total

#8
def mochila(elementos,W):
    #valor/peso nos indica el valor por cantidad de peso

    items=[]
    peso_actual=0
    res=[]
    
    for valor,peso in elementos:
        items.append((valor/peso,valor,peso))
    #ordeno esto de menor relacion valor/peso a mayor
    items.sort(key=lambda x: x[0])
    items.reverse()

    for _,valor,peso in items:
        if peso_actual+peso<=W:
            res.append((valor,peso))
            peso_actual+=peso
        else:
            continue
    return res


#realizo aquellas que terminan antes
#9

def minimizar_latencia(L_deadline, T_tareas):
    #Finaliza en F_i= inicio_i+duracion_i
    #latencia es L_i= F_i - Deadline_i si se supera, sino cero
    items=[]
    reloj=0
    res=[]
    for i in range (len(L_deadline)):
        #agrupo el deadline de la tarea con el tiempo que le toma hacerse
        items.append((L_deadline[i],T_tareas[i]))
    #ordeno de menor deadline a mayor deadline
    items.sort(key=lambda x: x[0])
    
    for deadline,tiempo in items:
        
        if reloj+tiempo>deadline:
            latencia=(reloj+tiempo)-deadline
            res.append((tiempo,latencia))
            
        else:
            res.append((tiempo,0))
        
        
        reloj+=tiempo

    
    return res

def medio(arreglo):
    medio= len(arreglo)//2
    return arreglo[medio]

print(medio([156,185,194,242,270]))

def bifurcaciones(ciudades):
    return wrapper_bifu(ciudades.sort(),0,len(ciudades)-1,[])

def wrapper_bifu(ciudades,ini,fin,res):
    if ini==fin:
        return res
    medio=(ini+fin)//2
    medio_bifu=ciudades[medio]
    for bifu in ciudades:
        if bifu<medio_bifu-50:
            return wrapper_bifu(ciudades,ini,medio,res)
        elif bifu>medio_bifu+50:
            return wrapper_bifu(ciudades,medio,fin,res)
        else:
            res.append(bifu)

def bifu(ciudades):
    res=[]
    #ordeno por kilometro
    ciudades.sort(key=lambda x:x[1])

    while ciudades:
        medio=len(ciudades)//2
        km_medio=ciudades[medio][1]
        izq=km_medio-50
        der=km_medio+50

        no_cubierto=[]

        for ciudad,km in ciudades:
            if km<izq or km>der:
                no_cubierto.append((ciudad,km))
            else:
                res.append((ciudad,km))
        ciudades=no_cubierto
    return res

#11
def bolsas(capacidad, productos):
    bolsas=[]
    productos.sort()
    productos.reverse()

    for prod in productos:
        colocado=False
        for bolsa in bolsas:
            if sum(bolsa)+prod<=capacidad:
                bolsa.append(prod)
                colocado=True
                break
        
        if not colocado:
            #nueva bolsa
            bolsas.append([prod])
    return bolsas

#12 Km Mafias
#simil al problema de scheduling
def arnook(kilometros):
    permisos=[]
    #ordeno de fin mas próximo a menos proximo
    kilometros.sort(key=lambda x: x[1])
    
    fin=0
    for ini,fin_ruta in kilometros:
        #el pedido arranca despues de lo ya solicitado, entonces es válido garantizarlo
        if ini>=fin:
            permisos.append((ini,fin_ruta))
            fin=fin_ruta
    return permisos
        

#13 again, choreado de lulu

def cobertura(casas, R, K):
    casas_ordenadas = sorted(casas)

    torres_colocadas = []
    torre = 0

    while casas_ordenadas:
        proxima_torre = casas_ordenadas[0] + R

        # Verificar si la ubicación de la próxima torre excede la longitud de la ruta, si la excede, ponemos la antena justo en la ultima casa antes de que exceda el largo de la ruta
        if proxima_torre > K:
            torres_colocadas.append(casas_ordenadas[0])
            break

        torres_colocadas.append(proxima_torre)
        casas_ordenadas = [casa for casa in casas_ordenadas if casa > proxima_torre + R]

        torre = proxima_torre

    return torres_colocadas

#14 no lo hice, pero se lo robo a lulu
# devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y)
# matriz booleana, indica True en las posiciones con submarinos
def iluminar(matriz, x, y):
    n = len(matriz)
    m = len(matriz[0])
    for i in range(max(0, x-2), min(n, x+3)):
        for j in range(max(0, y-2), min(m, y+3)):
            matriz[i][j] = False

def contar_submarinos(matriz, x, y):
    n = len(matriz)
    m = len(matriz[0])
    cuenta_submarinos = 0
    for i in range(max(0, x-2), min(n, x+3)):
        for j in range(max(0, y-2), min(m, y+3)):
            if matriz[i][j]:
                cuenta_submarinos += 1
    return cuenta_submarinos


def submarinos(matriz):

    n = len(matriz)

    if n == 0:
        return []

    m = len(matriz[0])
    faros = []

    while any(any(row) for row in matriz):
        max_submarinos = 0
        mejor_posicion = None
        for i in range(n):
            for j in range(m):
                cuenta_submarinos = contar_submarinos(matriz, i, j)
                if cuenta_submarinos > max_submarinos:
                    max_submarinos = cuenta_submarinos
                    mejor_posicion = (i, j)
        if mejor_posicion:
            x, y = mejor_posicion
            faros.append((x, y))
            iluminar(matriz, x, y)

    return faros

#15
#idem al ej de las bolsas
def cajas(capacidad, libros):
    libros_ordenados = sorted(libros)
    caja_con_libros = []
    cajas = []

    for espesor in libros_ordenados:
        if espesor > capacidad:
            continue
        elif sum(caja_con_libros) + espesor <= capacidad:
            caja_con_libros.append(espesor)
        else:
            cajas.append(caja_con_libros)
            caja_con_libros = [espesor]

    if caja_con_libros:
        cajas.append(caja_con_libros)

    return cajas

#16
from grafo import Grafo

# conocidos: lista de pares de personas que se conocen, cada elemento es un (a,b)
def obtener_invitados(conocidos):
    
    vertices=set()

    for p1,p2 in conocidos:
        vertices.add(p1)
        vertices.add(p2)

    grafo= Grafo(vertices_init=list(vertices))

    for p1,p2 in conocidos:
        grafo.agregar_arista(p1,p2)
    


    return invitados_grafo(grafo)

def invitados_grafo(grafo):
    invitados=list(grafo.obtener_vertices())
    hay_cambios=True
    
    while hay_cambios:
        hay_cambios=False

        eliminados=[]
        for persona in invitados:
            if len(grafo.adyacentes(persona))<4:
                eliminados.append(persona)
                hay_cambios=True
        
        for persona in eliminados:
            if persona in invitados:
                invitados.remove(persona)
                grafo.borrar_vertice(persona)

    return invitados






            










