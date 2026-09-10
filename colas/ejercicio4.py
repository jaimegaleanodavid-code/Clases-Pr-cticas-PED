from collections import deque

cola = deque([732, 443, 865, 25, 1012])

tamano = len(cola)
menor = cola[0]


for _ in range(tamano):
    elem = cola.popleft()
    if elem < menor:
        menor = elem
    cola.append(elem)

encontrado = False
for _ in range(tamano):
    elem = cola.popleft()
    if elem == menor and not encontrado:
        encontrado = True
    else:
        cola.append(elem)

cola.appendleft(menor)

print("Cola resultante:", list(cola))

"""
Para respetar la estructura de la cola y las reglas FIFO, se realizan
 dos recorridos sacando y volviendo a meter elementos.
En el primer paso se identifica el valor menor,
 en el segundo paso se filtran los datos manteniendo 
 el orden original sin el numero menor, y al final se 
 inserta este elemento en el frente usando appendleft para colocarlo en la cima.

 -------------DAJG----------JJLM------------------:)
"""