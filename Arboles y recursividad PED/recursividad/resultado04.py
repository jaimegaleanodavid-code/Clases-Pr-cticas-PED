# **Ejercicio 4**: Verifica si una palabra es un palíndromo recursivamente.
# *Solución*: Caso base len <= 1 (True). Recursivo: `palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])`.

def es_palindromo(palabra):
  if len(palabra) <= 1:
    return True
  return palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])


print(es_palindromo("Vaquita"))
print(es_palindromo("Rinoceronte"))
print(es_palindromo("Tigre"))
print(es_palindromo("python"))
print(es_palindromo("reconocer"))