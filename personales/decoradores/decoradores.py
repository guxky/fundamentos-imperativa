from typing import Callable, Any


# ============================================================
# PARTE 1 - CONTADOR DE LLAMADAS
# ============================================================
# Lo que se practico aqui: la diferencia entre la "zona A" (se ejecuta
# una sola vez, cuando se aplica el decorador) y la "zona B" (se ejecuta
# cada vez que se llama a la funcion decorada). El contador vive en la
# zona A para que su valor persista entre llamadas, y se necesita
# "nonlocal" porque "contador += 1" es una asignacion, y sin nonlocal
# Python la trataria como una variable local nueva dentro de envoltura.

def contar_llamadas(funcion: Callable) -> Callable:
    contador: int = 0

    def envoltura(nombre: str) -> None:
        nonlocal contador
        contador += 1
        print(f'Llamada: {contador}')
        return funcion(nombre)

    return envoltura


@contar_llamadas
def saludar(nombre: str) -> None:
    print(f'Hola, {nombre}')


saludar("Marcela")
saludar("Manuela")


# ============================================================
# PARTE 2 - VALIDACION DE POSITIVOS
# ============================================================
# Lo que se practico aqui: un decorador que valida los argumentos ANTES
# de dejar correr la funcion original, lanzando una excepcion si algo
# no cumple la regla. Nota sobre el tipo de retorno: aunque el nombre
# del parametro sea "envoltura", su valor real depende de la funcion
# que decore -- aqui devuelve un float (lo que devuelve "dividir"),
# no None, aunque en el ejercicio de contar_llamadas si era None
# porque "saludar" tampoco devolvia nada.

def solo_positivos(funcion: Callable) -> Callable:
    def envoltura(a: float, b: float) -> float:
        if a < 0 or b < 0:
            raise ValueError("Los numeros no pueden ser negativos")
        return funcion(a, b)

    return envoltura


@solo_positivos
def dividir(a: float, b: float) -> float:
    return a / b


print(dividir(10, 2))


# ============================================================
# PARTE 3 - DECORADOR CON CONFIGURACION (REPETIR)
# ============================================================
# Lo que se practico aqui: un decorador de TRES niveles en vez de dos,
# porque "repetir(veces=3)" necesita ejecutarse primero (recibiendo la
# configuracion) y devolver el decorador real, que despues recibe la
# funcion a decorar. "resultado" vive dentro de "envoltorio" (no en
# "decorador") a proposito: como se explico, el nivel de "decorador"
# solo corre una vez al aplicar el decorador, asi que si "resultado"
# viviera ahi, se compartiria (y acumularia) entre distintas llamadas
# a tirar_dado(). Viviendo dentro de "envoltorio", cada llamada arranca
# con una lista nueva y vacia.

def repetir(veces: int) -> Callable:
    def decorador(funcion: Callable) -> Callable:
        def envoltorio() -> list[int]:
            resultado: list[int] = []
            for _ in range(veces):
                resultado.append(funcion())
            return resultado

        return envoltorio

    return decorador


@repetir(veces=3)
def tirar_dado() -> int:
    import random
    return random.randint(1, 6)


print(tirar_dado())
print(tirar_dado())