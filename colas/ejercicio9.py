import math
from collections import deque

cola = deque([659, 236, 7321, 2278, 321798])

tamano = len(cola)
cola_raiz_cuadrada = deque()

for _ in range(tamano):
    elem = cola.popleft()
    cola_raiz_cuadrada.append(math.sqrt(elem))
    cola.append(elem)

print("Cola original (sin modificaciones):", list(cola))
print("Cola con raices cuadradas:", list(cola_raiz_cuadrada))

"""
Se recorre la cola original respetando sus reglas FIFO
 desencolando los elementos y volviendolos a encolar para que la cola inicial
   mantenga sus valores intactos.
Durante el recorrido se calcula la raiz cuadrada de cada numero mediante
 math.sqrt y se inserta cada resultado en una nueva cola temporal.

 -------------DAJG----------JJLM------------------:)
 ------------------use tantito IA------------------
                        |
                        |
                        ↓

 import math
from collections import deque

cola = deque([4, 9, 16, 25, 36])

def calcular_raiz_aproximada(n, iteraciones=10):
    # Metodo de Newton-Raphson para calcular la raiz cuadrada
    x = n / 2.0 if n > 0 else 0.0
    for _ in range(iteraciones):
        if x == 0:
            break
        x = 0.5 * (x + n / x)
    return x

def procesar_cola_recursivo(cola_original, cola_destino, contador_restante):
    # Condicion de parada de la recursion
    if contador_restante == 0:
        return
    
    # Desencolar elemento de la cola original
    elem = cola_original.popleft()
    
    # Calcular raiz cuadrada mediante algoritmo numerico
    raiz = calcular_raiz_aproximada(elem)
    cola_destino.append(raiz)
    
    # Reencolar para mantener la integridad de la cola original
    cola_original.append(elem)
    
    # Llamada recursiva para el siguiente elemento
    procesar_cola_recursivo(cola_original, cola_destino, contador_restante - 1)

cola_raiz_cuadrada = deque()
procesar_cola_recursivo(cola, cola_raiz_cuadrada, len(cola))

print("Cola original (sin modificaciones):", list(cola))
print("Cola con raices cuadradas:", list(cola_raiz_cuadrada))

"""