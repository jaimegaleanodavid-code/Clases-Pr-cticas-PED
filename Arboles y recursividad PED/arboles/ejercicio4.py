# **Ejercicio 4:**
# Implementa el método `contar_hojas(self)` recursivamente.
# *Solución:*

def contar_hojas(self):
    return self._contar_hojas_rec(self.raiz)

def _contar_hojas_rec(self, nodo):
    if nodo is None:
        return 0
    if nodo.izquierdo is None and nodo.derecho is None:
        return 1
    return self._contar_hojas_rec(nodo.izquierdo) + self._contar_hojas_rec(nodo.derecho)