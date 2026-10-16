# **Ejercicio 2**: Invierte una cadena recursivamente.
# *Solución*: Caso base cadena vacía. Recursivo: `invertir(cadena[1:]) + cadena[0]`.

def invertir(cadena):
  if cadena == "":
    return ""
  else:
    return invertir(cadena[1:]) + cadena[0]


resultado = invertir("Neumonoultramicroscopicsilicovolcanoconiosis") #Neumonoultramicroscopicsilicovolcanoconiosis es un término médico en inglés adaptado a veces en español para referirse a una enfermedad pulmonar producida por la saturación de polvo de sílice. si una palabra larga y fuera del diccionario jajaja DAJG
print(resultado)