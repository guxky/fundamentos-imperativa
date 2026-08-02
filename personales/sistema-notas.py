"""
Una institución educativa necesita un pequeño programa de consola para que un profesor pueda 
gestionar las notas de su curso sin depender de una hoja de cálculo. El programa debe iniciar 
con una lista de notas ya cargada y mostrarle al profesor un menú que se mantenga activo mientras 
lo necesite, desde donde pueda revisar todas las notas junto con su clasificación correspondiente 
(excelente, aprobado, necesita mejorar o reprobado), consultar un resumen con el promedio del curso,
 la nota más alta, la más baja y cuántos estudiantes aprobaron o reprobaron, buscar si una nota puntual 
 está entre las registradas, y finalmente salir del programa cuando así lo decida; todo esto sin usar 
 funciones integradas como sum(), max(), min() o sorted(), calculando cada cosa manualmente 
 con loops y variables, y manejando con cuidado cualquier opción inválida que el usuario 
 llegue a ingresar en el menú.
 
"""
#CLASIFICACION DE LAS NOTAS:
"""
90-100 → "Excelente"
70-89 → "Aprobado"
50-69 → "Necesita mejorar"
0-49 → "Reprobado"
"""

notas = [85, 92, 45, 78, 100, 33, 67, 90, 55, 72]
indice = 0

while True:
    print("\n1. Ver todas las notas")
    print("2. Ver estadisticas")
    print("3. Salir")
    opc_1 = input("Elige una opcion: ")

    match opc_1:
        case "3":
            print("Hasta luego")
            break
        case "1":
            print("------LISTADO DE NOTAS------")
            for indice, nota in enumerate(notas):
                if 90 <= nota <= 100:
                    print(f" ESRUDIANTE {indice}   {nota} -> Excelente")
                elif 70 <= nota <= 89:
                    print(f" ESRUDIANTE {indice}   {nota} -> Aprobado")
                elif 50 <= nota <= 69:
                    print(f" ESRUDIANTE {indice}   {nota} -> Necesita mejorar")
                elif 0 <= nota <= 49:
                    print(f" ESRUDIANTE {indice}   {nota} -> Reprobado1")

            print("--------------------------")

        case "2":
            acum = 0
            nota_alta = 0
            nota_baja = notas[0]
            aprobados = 0   
            reprobados = 0  
            for nota in notas: 
                            acum += nota
                            if (nota > nota_alta):
                                nota_alta = nota
                            if(nota_baja > nota):
                                nota_baja = nota
                            if(70 <= nota <= 100):
                                aprobados += 1
                            else:
                                reprobados += 1

            promedio = acum/len(notas)
            print("---- RESUMEN DEL CURSO ----")
            print(f"Total de estudiantes: {len(notas)}")
            print(f"Promedio del curso:  {promedio}")
            print(f"Nota mas alta: {nota_alta}")
            print(f"Nota mas baja: {nota_baja}")
            print(f"Estudiantes aprobados: {aprobados}")
            print(f"Estudiantes reprobados: {reprobados}")

        case _:
              print("Opcion no valida intenta de nuevo")