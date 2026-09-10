from collections import deque

cola = deque([0, 10, 0, 25, 0, 40, 5])

tamano = len(cola)
cola_sin_ceros = deque()

for _ in range(tamano):
    elem = cola.popleft()
    if elem != 0:
        cola_sin_ceros.append(elem)
    cola.append(elem)

print("Cola original (sin modificaciones):", list(cola))
print("cola sin los elementos ceros:", list(cola_sin_ceros))

"""
Para no modificar la cola original
 se recorren sus elementos desencolandolos y volviendolos
   a encolar en cada iteracion de modo que su estado al final
     sea exactamente el mismo.
Durante este proceso los valores distintos de cero se van insertando
 en una nueva cola secundaria para obtener el resultado deseado respetando las reglas FIFO.

 -------------DAJG----------JJLM------------------:)
"""