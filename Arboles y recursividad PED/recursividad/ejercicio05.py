# **Ejercicio 5**: Encuentra el número máximo en una lista recursivamente.
# *Solución*: Compara el primer elemento con el máximo del resto de la lista `max(lista[0], recursivo(lista[1:]))`.

def maximo_lista(lista):
  if len(lista) == 1:
    return lista[0]
  return max(lista[0], maximo_lista(lista[1:]))


numeros = [3, 15, 7, 22, 9, 4]
print(maximo_lista(numeros)) 