# ## 6. Tarea
# 1. **Multiplicación Rusa (sin operador `*`)**: Implementa una función recursiva que multiplique dos números `a` y `b` usando únicamente sumas. *Acompaña con análisis Big-O.*
# 2. **Conteo de Vocales**: Cuenta el número de vocales en un string recursivamente.
# 3. **Imprimir Patrón**: Dado un número `n`, imprime usando recursividad un patrón de asteriscos. Ejemplo para n=3:
#    *
#    **
#    ***
# 4. **Caminos en un Tablero**: Escribe una función recursiva que calcule el número de caminos posibles desde la esquina superior izquierda (0,0) hasta la inferior derecha de una matriz NxM, asumiendo que solo puedes moverte hacia abajo o a la derecha. *Acompaña con análisis Big-O.*
# 5. **Flatten List**: Dada una lista que puede contener enteros u otras listas de enteros anidadas a cualquier nivel, retorna una única lista plana. Ej: `[1, [2, [3, 4], 5]] -> [1, 2, 3, 4, 5]`.



def multiplicacion_rusa(a, b):
  if b == 0:
    return 0
  if b % 2 == 0:
    return multiplicacion_rusa(a + a, b // 2)
  else:
    return a + multiplicacion_rusa(a + a, (b - 1) // 2)


print(multiplicacion_rusa(7, 5))  

# Análisis Big-O:Tiempo ($O(\log b)$): En cada paso recursivo, el valor de b se divide a la mitad
#  ($\lfloor b / 2 \rfloor$), lo que reduce el número de llamadas de forma logarítmica respecto a b.Espacio 
# ($O(\log b)$): La profundidad máxima de la pila de llamadas (call stack) es proporcional al número de divisiones
#  necesarias para llegar a cero, es decir, $\log_2(b)$.

#----------------------------------------------------------------------------------------------------------
def contar_vocales(cadena):
  if cadena == "":
    return 0
  es_vocal = 1 if cadena[0].lower() in "aeiouáéíóú" else 0
  
  return es_vocal + contar_vocales(cadena[1:])

print(contar_vocales("Programación"))
#----------------------------------------------------------------------------------------------------------
def imprimir_patron(n):
  if n <= 0:
    return
  imprimir_patron(n - 1)
  print("*" * n)

imprimir_patron(3)

#----------------------------------------------------------------------------------------------------------
def caminos_tablero(n, m):
  if n == 1 or m == 1:
    return 1
  return caminos_tablero(n - 1, m) + caminos_tablero(n, m - 1)
print(caminos_tablero(8, 8)) 

#Análisis Big-O:Tiempo ($O(2^{N+M})$): Sin memorización (memoization),
#  cada llamada genera dos nuevas ramificaciones, lo que provoca un crecimiento 
# de tipo exponencial en el árbol de llamadas.Espacio ($O(N + M)$): La profundidad 
# máxima de la pila de llamadas recursivas corresponde a la longitud máxima del camino 
# desde la esquina superior hasta la inferior, que es $N + M$.

#----------------------------------------------------------------------------------------------------------

def flatten(lista):
  if not lista:
    return []
  primero = lista[0]
  resto = lista[1:]
  if isinstance(primero, list):
    return flatten(primero) + flatten(resto)
  else:
    return [primero] + flatten(resto)
anidada = [1, [2, [3, 4], 5]]
print(flatten(anidada))
