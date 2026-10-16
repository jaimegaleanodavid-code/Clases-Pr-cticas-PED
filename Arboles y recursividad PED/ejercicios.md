## 5. Práctica en Clase
**Ejercicio 1**: Implementa una función recursiva que cuente hacia atrás (countdown) desde `n` e imprima "Despegue!" al llegar a cero.
*Solución Guiada*: Caso base: n == 0 (print). Recursivo: print(n), llamada a(n-1).

**Ejercicio 2**: Invierte una cadena recursivamente.
*Solución*: Caso base cadena vacía. Recursivo: `invertir(cadena[1:]) + cadena[0]`.

**Ejercicio 3**: Calcula `a` elevado a `b` recursivamente (a^b).
*Solución*: Caso base b == 0 (return 1). Recursivo: `a * potencia(a, b-1)`.

**Ejercicio 4**: Verifica si una palabra es un palíndromo recursivamente.
*Solución*: Caso base len <= 1 (True). Recursivo: `palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])`.

**Ejercicio 5**: Encuentra el número máximo en una lista recursivamente.
*Solución*: Compara el primer elemento con el máximo del resto de la lista `max(lista[0], recursivo(lista[1:]))`.

## 6. Tarea
1. **Multiplicación Rusa (sin operador `*`)**: Implementa una función recursiva que multiplique dos números `a` y `b` usando únicamente sumas. *Acompaña con análisis Big-O.*
2. **Conteo de Vocales**: Cuenta el número de vocales en un string recursivamente.
3. **Imprimir Patrón**: Dado un número `n`, imprime usando recursividad un patrón de asteriscos. Ejemplo para n=3:
   *
   **
   ***
4. **Caminos en un Tablero**: Escribe una función recursiva que calcule el número de caminos posibles desde la esquina superior izquierda (0,0) hasta la inferior derecha de una matriz NxM, asumiendo que solo puedes moverte hacia abajo o a la derecha. *Acompaña con análisis Big-O.*
5. **Flatten List**: Dada una lista que puede contener enteros u otras listas de enteros anidadas a cualquier nivel, retorna una única lista plana. Ej: `[1, [2, [3, 4], 5]] -> [1, 2, 3, 4, 5]`.

## 7. Mini-Proyecto: Explorador de Directorios
**Enunciado**:
Vas a simular un script que recorre el sistema de archivos (el cual representaremos como un 
diccionario anidado en Python).
Ejemplo de estructura:
```python
sistema_archivos = {
    "Documentos": {
        "apuntes.txt": "10kb",
        "fotos": {
            "vacaciones.png": "2mb",
            "perro.jpg": "1mb"
        }
    },
    "sistema.dll": "500kb"
}
```
Debes implementar una clase `ExploradorRecursivo` que contenga métodos recursivos para:
1. `imprimir_arbol(sistema, nivel)`: Que muestre gráficamente la estructura con indentaciones visuales.
2. `buscar_archivo(sistema, nombre)`: Que busque a qué ruta pertenece un archivo específico.
3. `contar_archivos(sistema)`: Retorna la cantidad total de archivos (las carpetas no cuentan).

**Rúbrica (100 puntos):**
- [30 pts] Implementación correcta de `imprimir_arbol` con indentación según el nivel recursivo.
- [30 pts] Búsqueda profunda correcta, sin crashear al llegar a las "hojas" del árbol.
- [20 pts] Conteo correcto de nodos hoja (archivos).
- [10 pts] Definición clara de los casos base y recursivos en comentarios.
- [10 pts] Código legible, estilo PEP8 y orientación a objetos.

//#---------------------------DAJG-------------------------------------------------
//


## 5. Práctica en Clase

**Ejercicio 1:** 
Dado un árbol binario de búsqueda donde se insertaron secuencialmente los elementos: `1, 2, 3, 4, 5`. Dibuja el árbol y comenta su altura.
*Solución:* 
```text
( 1 )
   \
   ( 2 )
      \
      ( 3 )
         \
         ( 4 )
            \
            ( 5 )
```
Es un árbol degenerado (lista enlazada). Altura = 4. Complejidad = O(n).

**Ejercicio 2:** 
Implementa el método `altura(self, nodo)` que retorne la altura del árbol.
*Solución:*
```python
def altura(self, nodo):
    if nodo is None:
        return -1
    return 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho))
```

**Ejercicio 3:**
Explica qué imprimiría un recorrido Postorden del árbol del Ejemplo 2.
*Solución:* [2, 7, 5, 12, 17, 15, 10]

**Ejercicio 4:**
Implementa el método `contar_hojas(self)` recursivamente.
*Solución:*
```python
def contar_hojas(self):
    return self._contar_hojas_rec(self.raiz)

def _contar_hojas_rec(self, nodo):
    if nodo is None:
        return 0
    if nodo.izquierdo is None and nodo.derecho is None:
        return 1
    return self._contar_hojas_rec(nodo.izquierdo) + self._contar_hojas_rec(nodo.derecho)
```

## 6. Tarea / Homework

1. Implementa el método `eliminar(valor)` en la clase `ArbolBinarioBusqueda`. Asegúrate de manejar los 3 casos descritos en la teoría.
2. Implementa el recorrido por niveles (BFS - Breadth First Search) utilizando una Cola (`queue`).
3. Escribe una función que tome un árbol BST y retorne la suma de todos sus elementos sin modificar el árbol original.
4. Escribe un método `es_completo()` que valide si todos los nodos internos de un BST tienen exactamente dos hijos.
5. Crea una función `balancear_arbol()` que tome un BST potencialmente degenerado, extraiga sus elementos y construya un nuevo BST balanceado de altura mínima.

## 7. Mini-Proyecto

**Enunciado: Diccionario Inteligente**
Desarrolla un sistema de autocompletado y diccionario utilizando un Árbol Binario de Búsqueda. En este caso, el BST almacenará Objetos `Palabra`, los cuales contienen el texto de la palabra y su definición. 
Deberás:
1. Cargar al menos 50 palabras en el BST desde un archivo de texto o lista inicial. El ordenamiento en el árbol debe ser alfabético.
2. Permitir al usuario buscar una palabra exacta para obtener su definición.
3. Crear un método `buscar_por_prefijo(prefijo)` que retorne una lista con todas las palabras en el árbol que comiencen con ese prefijo (ej: "au" -> "auto", "autonomía", "aurora").
4. Generar una pequeña interfaz por consola donde el usuario pueda interactuar con el sistema (buscar, ver diccionario completo en orden, salir).

**Rúbrica (100 pts):**
* Implementación del BST orientada a objetos adaptada a strings (25 pts)
* Funcionalidad de Búsqueda Exacta (15 pts)
* Funcionalidad de Autocompletar / Búsqueda por prefijo (30 pts)
* Interfaz de consola interactiva amigable (20 pts)
* Código limpio, comentado y PEP8 (10 pts)