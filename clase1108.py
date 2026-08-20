#----------------------------------------------------
#2. funciones auxiliares (sin retorno y sin parametros)
#----------------------------------------------------
def funcion_mostrar_linea():
    #imprime una linea de separacion, funcion sin parametros y sin retorno
    print("= " * 60)
#imprime un encabezado sin titulo proporcionado, funcion con parametros y sin retorno
def funcion_mostrar_encabezado(titulo):
    funcion_mostrar_linea()
    print(f"{titulo}")
    funcion_mostrar_linea()

def funcion_pausar():
    input("precione una tecla para continuar...")

#---------------------------------------------------------------------------------------------
#3.  funciones con retorno (operaciones y validaciones)
#---------------------------------------------------------------------------------------------
def funcion_leer_texto(mensaje):
    while True:
        texto = input(f"{mensaje}").strip()
        if texto:
            return texto
        print ("ERROR: el texto no puesde estar vacio. intente nuevamente.")

def funcion_leer_numero(mensaje, minimo, maximo):
    """Lee un numero flotante y valida un rango"""
    while True:
        try:
            valor = float(input(f"   {mensaje}"))
            if minimo <= valor <= maximo:
                return valor
            print(f"Advertencia: El numero debe estar entre {minimo} y {maximo}. intente nuevamente")
        except ValueError:
            print("ERROR: entrada invalida. por favor ingrese un numero valido.")

def funcion_calcular_promedio(notas):
    if(len(notas) == 0):
        return 0.0
    return sum (notas) / len(notas)

def funcion_determinar_estado(promedio):
    """Determina el estado del estudiante segun su promedio"""
    if promedio >= 3.0:
        return "aprobada"
    else:
        return "reprobado"

def funcion_determinar_mencion():
    """determina la mencion del estudiante segun su promedio"""
    if promedio >= 4.5:
        return "Exelente"
    elif promedio >= 4.0:
        return "muy bueno"
    elif promedio >= 3.5:
        return "Bueno"
    elif promedio >= NOTA_MINIMA_APROBACION:
        return "regular"
    else:
        return "en recuperacion"

#---------------------------------------------------------------------------------------------
#3.  Clase Estudiante (POO - encapsulamiento, herencia, polimorfismo)
#---------------------------------------------------------------------------------------------
class Estudiante:
    """
    Clase que representa a un estudiante con sus atributos y metodos
    encapsulamiento: Los atributos son privados y se accede a ellos mediante metodos
    """
    _cantidad_estudiante = 0

def __init__(self, nombrecompleto, edad, grado):
    """inicia un objeto estudiante con nombre, apellido y lista de notas
    constructor de la clase
    self hace referencia al objeto actual
    """
    Estudiante._cantidad_estudiante += 1
    self._id = Estudiante._cantidad_estudiante
    self._nombrecompleto = nombrecompleto
    self._edad = edad
    self._grado = grado
    self._notas = [] #declaracion de lista vacia que recibe las notas
    self._promedio = 0.0
    self._estado = ""
    self._mencion = ""
    self._rendimiento = ""

#=====================GETTERS (Encapsulamiento) ======================= 
@property
def id(self):
    """Devuelve el ID del estudiante"""
    return self._id

@property
def nombrecompleto(self):
    """Devuelve el nombre completo del estudiante"""
    return self._nombrecompleto

@property
def edad(self):
    """Devuelve la edad del estudiante"""
    return self._edad

@property
def grado(self):
    """Devuelve el grado del estudiante"""
    return self._grado

@property
def notas(self):
    """Devuelve las notas del estudiante"""
    return self._notas.copy()

@property
def promedio(self):
    """Devuelve el promedio del estudiante"""
    return self._promedio

@property
def estado(self):
    """Devuelve el estado del estudiante"""
    return self._estado

@property
def mencion(self):
    """Devuelve el mencion del estudiante"""
    return self._mencion

@property
def rendimiento(self):
    """Devuelve el rendimiento del estudiante"""
    return self._rendimiento

#----------------SETTERS (modificadores)------------------------
@edad.setter
def edad(self, valor):
    """Establece la edad del estudiante"""
    if 0 < valor < 65:
        self._edad = valor
    else:
        raise ValueError("la edad debe ser un numero positivo")