from collections import deque

cola = deque(["David Jaime","Alan Brito Delgado", "Jeffer Largaespada", "Aitor Tilla"])

tamano = len(cola)
nombre_con_a = None

for _ in range(tamano):
    elem = cola.popleft()
    if nombre_con_a is None and elem.startswith('A'):
        nombre_con_a = elem
    cola.append(elem)

if nombre_con_a is not None:
    encontrado = False
    for _ in range(tamano):
        elem = cola.popleft()
        if elem == nombre_con_a and not encontrado:
            encontrado = True
        else:
            cola.append(elem)
    
    cola.append(nombre_con_a)

print("Cola resultante:", list(cola))

"""
Se busca el primer nombre que comienza con la letra A 
haciendo un recorrido en el que se desencolan
 y vuelven a encolar los elementos para conservar la estructura FIFO.
Posteriormente se realiza una segunda pasada
 para remover únicamente ese nombre de su lugar
   original y finalmente se encola al final mediante
     append para ubicarlo en el fondo.

      -------------DAJG----------JJLM------------------:)
"""