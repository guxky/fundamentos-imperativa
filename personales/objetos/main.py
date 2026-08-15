from catalogo import Catalogo
from socios import Socios
from libro import Libro
from socio import Socio
from biblioteca import Biblioteca


def mostrar_menu() -> None:
    print("\n=== SISTEMA DE BIBLIOTECA (OOP) ===")
    print("1. Agregar libro")
    print("2. Registrar socio")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Buscar libro por ISBN")
    print("6. Buscar socio por ID")
    print("7. Libros por autor")
    print("8. Ver catalogo completo")
    print("0. Salir")


if __name__ == "__main__":
    catalogo = Catalogo()
    socios = Socios()
    biblioteca = Biblioteca(catalogo.catalogo, socios.socios)

    # Datos de prueba, para no tener que cargarlos a mano cada vez
    libro_prueba = Libro("9780307474723", "Cien años de soledad", "Gabriel Garcia Marquez")
    catalogo.agregar_libro(libro_prueba)

    socio_prueba = Socio("1", "Ana")
    socios.registrar_socio(socio_prueba)

    print(f"\nDatos de prueba cargados:")
    print(f"Libro: {libro_prueba}")
    print(f"Socio: {socio_prueba.nombre} (ID: {socio_prueba.id})")

    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            isbn = input("ISBN (13 digitos): ")
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            try:
                libro = Libro(isbn, titulo, autor)
                catalogo.agregar_libro(libro)
                print(f"\nLibro agregado: {libro}")
            except ValueError as e:
                print(e)

        elif opcion == "2":
            id_socio = input("ID del socio: ")
            nombre = input("Nombre: ")
            socio = Socio(id_socio, nombre)
            socios.registrar_socio(socio)
            print(f"\nSocio registrado: {socio.nombre} (ID: {socio.id})")

        elif opcion == "3":
            id_socio = input("ID del socio: ")
            isbn = input("ISBN del libro a prestar: ")
            try:
                print(biblioteca.prestar_libro(id_socio, isbn))
            except ValueError as e:
                print(e)

        elif opcion == "4":
            isbn = input("ISBN del libro a devolver: ")
            try:
                print(biblioteca.devolver_libro(isbn))
            except ValueError as e:
                print(e)

        elif opcion == "5":
            isbn = input("ISBN a buscar: ")
            print(catalogo.buscar_libro_isbn(isbn))

        elif opcion == "6":
            id_socio = input("ID del socio a buscar: ")
            print(socios.buscar_socio(id_socio))

        elif opcion == "7":
            autor = input("Autor a buscar: ")
            print(catalogo.buscar_libro_autor(autor))

        elif opcion == "8":
            print(catalogo)

        elif opcion == "0":
            print("\nCerrando el sistema. Hasta luego.")
            break

        else:
            print("\nOpcion no valida, intenta de nuevo")