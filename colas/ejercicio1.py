from collections import deque

cola = deque(["Optimus Prime", "Megatron", "Bumblebee","Starscream"])

primer_elemento = cola[0]

print("El primer elemento es:", primer_elemento)
print("Estado de la cola:", list(cola))

"""
 En Python representamos una cola usando deque para seguir la regla FIFO
   (Primero en entrar, primero en salir).
 Para ver el primer elemento sin modificar la cola solo accedemos
   a la posicion inicial con el indice 0 sin usar popleft.

   -------------DAJG----------JJLM------------------:)
"""