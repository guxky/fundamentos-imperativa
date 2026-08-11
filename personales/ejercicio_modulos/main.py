from reportes import generar_reporte

print(dir())

if __name__ == "__main__":

    estudiantes = {
        "Ana": [85, 90, 78, 92],
        "Carlos": [55, 60, 45, 70],
        "Beto": [100, 95, 88, 91],
        "Diana": [40, 35, 50, 45]
    }

    for nombre, notas in estudiantes.items():
        print(generar_reporte(nombre, notas))

