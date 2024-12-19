#ej 0

#implementado en rpl
from automata import Automata


#basicamente seguir la estructura del dibujo que nos dan
def automata_al_menos_3_0s():
    a = Automata()
    a.estado("q0",es_inicial=True)
    a.estado("q1")
    a.estado("q2")
    a.estado("q3",es_final=True)
    

    a.transicion_estado("q0","q0","1")
    a.transicion_estado("q0","q1","0")
    a.transicion_estado("q1","q0","1")
    a.transicion_estado("q1","q2","0")
    a.transicion_estado("q2","q0","1")
    a.transicion_estado("q2","q3","0")
    a.transicion_estado("q3","q3","0")
    a.transicion_estado("q3","q0","1")
    return a


#1

#Los números en potencia de 2 tienen una representación binaria muy particular: 
# siempre tienen un solo bit con valor 1, y todos los demás bits son 0. La posición del bit en 1 depende de la potencia 𝑛n en la expresión 2𝑛2 n.

#osea que tiene que aceptar aquellos numeros que tienen solo un 1 y el resto todo 0.
#debería tener un estado final.

#1= 0001 = 2**0 , 2=0010=2**1, 4=0100=2**2 etc...

def automata_potencias_2():
    a = Automata()
    a.estado("q0",es_inicial=True)
    a.estado("q1",es_final=True)

    a.transicion_estado("q0","q0","0")
    a.transicion_estado("q0","q1","1")
    a.transicion_estado("q1","q1","0")

    return a

#2

#cantidad par de 0s y 1s: ejs=> 0011, 1010, 1100...

def automata_pares_1y0():
    a = Automata()
    
    
    a.estado("q0", es_inicial=True, es_final=True)  
    a.estado("q1", es_inicial=False, es_final=False)
    a.estado("q2", es_inicial=False, es_final=False) 
    a.estado("q3", es_inicial=False, es_final=False) 

    a.transicion_estado("q0", "q2", "0")  
    a.transicion_estado("q1", "q3", "0")  
    a.transicion_estado("q2", "q0", "0")  
    a.transicion_estado("q3", "q1", "0")  

    a.transicion_estado("q0", "q1", "1")  
    a.transicion_estado("q1", "q0", "1")  
    a.transicion_estado("q2", "q3", "1")  
    a.transicion_estado("q3", "q2", "1") 

    return a

#3 solo comparar las cadenas que entran al final

def es_parte_lenguaje(cadena):
    
    mini_cadena = "ab"  
    
    if cadena.endswith(mini_cadena):
        return True
    
    if cadena.startswith("ac"):
        return True
    
    return False


#4

def expresion():
    a = Automata()
    
    a.estado("q0", es_inicial=True, es_final=True)  
    a.estado("q1")
    a.estado("q2")
    a.estado("q3")
    a.estado("q4")
    a.estado("q5")
    a.estado("qf", es_final=True)
    
    a.transicion_estado("q0", "q1", "a")
    a.transicion_estado("q1", "q2", "a")
    a.transicion_estado("q2", "q3", "b")
    a.transicion_estado("q3", "q0", "")  
    
    a.transicion_estado("q0", "qf", "a")  
    a.transicion_estado("qf", "qf", "a")  
    a.transicion_estado("q0", "q4", "a")  
    a.transicion_estado("q4", "q5", "b")
    a.transicion_estado("q5", "qf", "a")  
    a.transicion_estado("qf", "q4", "a")  

    return a

#5

def expresion():
    a = Automata()

    a.estado("q0", es_inicial=True, es_final=True) 
    a.estado("q1") 
    a.estado("q2") 
    a.estado("q3") 
    a.estado("q4")  
    a.estado("q5") 
    a.estado("q6", es_final=True)  

    a.transicion_estado("q0", "q1", "a")  
    a.transicion_estado("q1", "q2", "b")  
    a.transicion_estado("q2", "q1", "a")  
    a.transicion_estado("q2", "q3", "b")  
    a.transicion_estado("q3", "q3", "a")  
    a.transicion_estado("q3", "q4", "")   

    a.transicion_estado("q0", "q4", "b")  
    a.transicion_estado("q4", "q4", "b")  

    a.transicion_estado("q0", "q5", "a")  
    a.transicion_estado("q5", "q6", "b")  
    a.transicion_estado("q6", "q5", "a")  

    
    a.transicion_estado("q4", "q6", "") 

    return a