from calculos import promedio, nota_maxima, nota_minima, aprobados
from validaciones import es_nombre_valido

def generar_reporte(nombre: str, notas: list) -> str:
    acum = ""
    
    if es_nombre_valido(nombre):
        acum = f'\nReporte de: {nombre} \nPromedio: {promedio(notas)} \nNota maxima: {nota_maxima(notas)} \nNota minima: {nota_minima(notas)} \nNotas aprobadas: {aprobados(notas)}\n'

    return acum