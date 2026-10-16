# **Ejercicio 3**: Calcula `a` elevado a `b` recursivamente (a^b).
# *Solución*: Caso base b == 0 (return 1). Recursivo: `a * potencia(a, b-1)`.

def potencia(a, b):
  if b == 0:
    return 1
  else:
    return a * potencia(a, b - 1)


resultado = potencia(6, 9)
print(f"el resultado es: {resultado}")