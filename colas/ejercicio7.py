from collections import deque

cola = deque(["Soundwave", "Shockwave", "Grimlock", "Arcee", "Wheeljack"])


pila = []

# Paso 1: Desencolar todos los elementos y meterlos en la pila
while cola:
    pila.append(cola.popleft())

# Paso 2: Desapilar todos los elementos de la pila y volverlos a encolar
while pila:
    cola.append(pila.pop())

print("Cola invertida:", list(cola))

"""
Para invertir los elementos de una cola respetando
 sus reglas se utiliza una pila auxiliar como estructura temporal.
Al desencolar todos los elementos y meterlos en la
 pila, el orden se invierte debido a la propiedad LIFO
   (Ultimo en entrar, primero en salir), permitiendo
     que al volverlos a encolar en la estructura original 
     la cola quede totalmente invertida.

     -------------DAJG----------JJLM------------------:)
"""