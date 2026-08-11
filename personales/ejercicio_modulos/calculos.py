def promedio(notas: list) -> float:
    return sum(notas)/len(notas)

def nota_maxima(notas: list) -> float:
    return max(notas)

def nota_minima(notas: list) -> float:
    return min(notas)

def aprobados(notas: list) -> list:
    aprobados = []
    for nota in notas:
        if nota >= 60:
            aprobados.append(nota)
    return aprobados

