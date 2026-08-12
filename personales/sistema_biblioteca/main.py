from catalogo import catalogo_libros, agregar_libro, buscar_libro_isbn, buscar_libros_autor, mostrar_catalogo
from socios import socios, registrar_socio, buscar_socio
from prestamos import prestar_libro, devolver_libro


def mostrar_menu() -> None:
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1. Agregar libro")
    print("2. Registrar socio")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar libro por ISBN")
    print("6. Buscar socio por ID")
    print("7. Libros por autor")
    print("8. Ver catalogo completo")
    print("9. Ver total prestamos")
    print("0. Salir")


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            isbn = input("ISBN (13 digitos): ")
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            print(agregar_libro(catalogo_libros, isbn, titulo, autor))

        elif opcion == "2":
            id_socio = input("ID del socio: ")
            nombre = input("Nombre: ")
            print(registrar_socio(socios, id_socio, nombre))

        elif opcion == "3":
            isbn = input("ISBN del libro a prestar: ")
            id_socio = input("ID del socio: ")
            print(prestar_libro(catalogo_libros, socios, isbn, id_socio))

        elif opcion == "4":
            isbn = input("ISBN del libro a devolver: ")
            print(devolver_libro(catalogo_libros, isbn))

        elif opcion == "5":
            isbn = input("ISBN a buscar: ")
            resultado = buscar_libro_isbn(catalogo_libros, isbn)
            print(resultado)

        elif opcion == "6":
            id_socio = input("ID del socio a buscar: ")
            resultado = buscar_socio(socios, id_socio)
            print(resultado)

        elif opcion == "7":
            autor = input("Autor a buscar: ")
            resultado = buscar_libros_autor(catalogo_libros, autor)
            print(resultado)

        elif opcion == "8":
            print(mostrar_catalogo(catalogo_libros))

        elif opcion == "9":
            print(f'\nEl total del prestamos es: {prestar_libro.contador}')

        elif opcion == "0":
            print("\nCerrando el sistema. Hasta luego.")
            break
        else:
            print("\nOpcion no valida, intenta de nuevo")