from collections import deque

cola = deque([34, 643, 67, 490, 1])

tamano = len(cola)
maximo = cola[0]

for _ in range(tamano):
    elemento = cola.popleft()
    if elemento > maximo:
        maximo = elemento
    cola.append(elemento)

encontrado = False
for _ in range(tamano):
    elemento = cola.popleft()
    if elemento == maximo and not encontrado:
        encontrado = True
    else:
        cola.append(elemento)

cola.append(maximo)

print("Cola resultante:", list(cola))

"""
Se utiliza deque para manipular la cola respetando la regla FIFO
 (Primero en entrar, primero en salir).
Primero se realiza un recorrido desencolando y reencolando elementos
 para encontrar el numero mayor.
Luego se hace un segundo recorrido para reordenar los elementos
 omitiendo el mayor, para finalmente agregarlo al fondo de la cola.

 -------------DAJG----------JJLM------------------:)
"""