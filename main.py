
# 1. Definición de funciones con Type Hints y Docstrings
def suma(a: int, b: int) -> int:
    """Retorna la suma de dos enteros."""
    return a + b


def saludo() -> None:
    """Imprime un saludo por consola."""
    print('Hey there!')


def ejecutar(f, p1, p2):
    """
    Recibe una función y sus argumentos, y la ejecuta.
    """
    return f(p1, p2)


def fabrica_multiplicador(y):
    """
    Crea una función que multiplica por un factor (y) dado.
    """

    def producto(x: int) -> int:
        return x * y

    return producto


def decorador(func):
    """

    """
    def envoltorio():

        print('Executes before the function', func.__name__)

        func()

        print('Executes after the function', func.__name__)

    return envoltorio()


def decorador2(func):
    """

    """
    def envoltorio(*args, **kargs):

        print('Before executing.')

        resultado = func(*args, **kargs)

        print('After executing.')

        return resultado
    return  envoltorio

@decorador2
def mult2(a: int, b: int) -> int:
    """Retorna la multiplicacion de dos enteros."""
    return a * b


# 2. Bloque principal de ejecución
if __name__ == '__main__':
    # Asignación de alias (si es estrictamente necesario, hazlo aquí)
    adicion = suma
    bienvenida = saludo
    # s =
    x = mult2(3, 4)
    # Pruebas
    print(f"Ejecución directa: {ejecutar(suma, 2, 2)}")
    print(x)
    bienvenida()

    # Uso de la Clausura
    doble = fabrica_multiplicador(2)  # Creamos una función que multiplica por 2
    triple = fabrica_multiplicador(3)  # Creamos una función que multiplica por 3

    print(f"Doble de 5: {doble(5)}")  # Salida: 10
    print(f"Triple de 5: {triple(5)}")  # Salida: 15