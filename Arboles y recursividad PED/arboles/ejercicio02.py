# **Ejercicio 2:** 
# Implementa el método `altura(self, nodo)` que retorne la altura del árbol.
# *Solución:*

def altura(self, nodo):
    if nodo is None:
        return -1
    return 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho))
