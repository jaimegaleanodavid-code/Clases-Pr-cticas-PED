from collections import deque

cola = deque([ "David Jaime","Alan Brito Delgado", "Jeffer Largaespada", "Aitor Tilla"])

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
    
    cola.appendleft(nombre_con_a)

print("Cola resultante:", list(cola))

"""
Se recorre la cola para identificar el primer nombre que inicia con la letra A
 desencolando y reencolando sus elementos para preservar la estructura.
Una vez identificado, se realiza una segunda pasada para remover dicho
 nombre de su posicion original e insertarlo directamente en la cima
   o frente de la cola mediante appendleft.

   -------------DAJG----------JJLM------------------:)
"""