"""
Una pequeña tienda necesita un programa de consola para llevar el control 
de su inventario, sin depender de papel ni hojas de cálculo. El programa debe 
iniciar con un inventario ya cargado (usando un diccionario donde cada
producto tenga su nombre, precio, cantidad disponible y categoría), y ofrecer 
un menú interactivo que se mantenga activo mientras el dueño lo necesite, desde 
donde pueda 
1.revisar el listado completo de productos con su información, 
2.buscar un producto puntual y ver si hay stock disponible, 
3.registrar una venta descontando la cantidad vendida del inventario (validando que no se venda más de lo que hay disponible), 
4.consultar cuáles son las categorías únicas de productos que maneja la tienda, 
5.ver un resumen con el valor total del inventario y cuántos productos están por agotarse, y 
6.finalmente salir del programa cuando así lo decida; 
todo esto usando comentarios que expliquen las partes menos obvias del código, convirtiendo tipos de datos cuando 
sea necesario (por ejemplo al leer el input del usuario), y sin usar funciones todavía, 
ya que ese tema lo verás más adelante.       
"""

inventario = {
    "manzana" : {"precio": 2500, "cantidad": 20, "categoria": "frutas"},
    "leche": {"precio": 4200, "cantidad": 30, "categoria": "lacteos"},
    "pan": {"precio": 3000, "cantidad": 5, "categoria": "panaderia"},
    "yogurt": {"precio": 3800, "cantidad": 0, "categoria": "lacteos"},
    "queso": {"precio": 8500, "cantidad": 12, "categoria": "lacteos"},
}


def listar_inventario(inv):
    """
    Recibe un diccionario en representacion al inventario y lo descompone 
    usando un for, guardando los resultados en un acumulador para despues imprimirlo 
    """
    acum = "\n---- INVENTARIO DE LA TIENDA ----"
    for producto, datos in inv.items():
        acum += f"\n {producto:<15} || Precio: {datos["precio"]:<15} || Cantidad disponible: {datos["cantidad"]:<15} Categoria: {datos["categoria"]}"
    acum += f"\n--------------------------------\n"
    return acum


def buscar_producto(busqueda, inv):
    """
    Recibe un producto que se va a buscar y un inventario, se recorre el inventario para ver 
    cuando el producto a buscar es igual a alguno del inventario, cuando se encuentra se descomponen su datos 
    y se almacenan en una variable para despues imprimirla, si no se ceuntra se dice que no se encontro
    """
    acum = "\n--- BUSQUEDA DE PRODUCTO ---"
    for producto, datos in inv.items():
        if busqueda == producto:
            acum += f"\n Producto: {producto}\n Precio: {datos["precio"]}\n Cantidad disponible: {datos["cantidad"]}\n Categoria: {datos["categoria"]}"
            acum += f"\n-----------------------------------\n"
            return acum
    else:
        acum = f"\n El producto '{busqueda}' no se encuentra en el inventario"
        acum += f"\n--------------------------\n"
        return acum


def registrar_venta(producto_v,cantidad, inv):
    """
    Recibe un producto a vender, la cantidad y el inventario
    se verifica primero que el producto exista para pider asignar una cantidad,
    si se puede hacer la venta se registra la diferencia y se descomponen los datos
    si no se puede se guarda un mensaje y si el producto no existe tambien se guarda el mensaje
    """
    acum = ""
    if producto_v in inv:
        cantidad_inv = inv[producto_v]["cantidad"]

        if (cantidad_inv-cantidad) < 0:
                acum += f"\n No hay suficiente stock para completar la venta\n Stock disponible: {cantidad_inv}, cantidad solicitada: {cantidad}\n Venta cancelada"
                acum += f"\n----------------------\n"
                return acum
        else:
            inv[producto_v]["cantidad"] = cantidad_inv - cantidad
            acum += f"\n Venta registrada con exito \n Se vendieron {cantidad} unidades de {producto_v}\n Stock restante: {cantidad_inv-cantidad}"
            acum += f"\n---------------------------\n"
            return acum 
    else:
        acum += f"\nEl producto: '{producto_v}' no se encuentra en el inventario"
        acum += f"\n----------------------------\n"
        return acum    
    
    
def mostrar_categorias(inv):
    """
    se crea un una variable llamada categoria de tipo set para almacenar los tipos de categorias sin repeticion
    luego se descompone los datos del set para imprimirlos despues
    """
    categorias = set()
    acum = "\n--- CATEGORIAS DISPONIBLES ---"
    for producto, datos in inv.items():
        categorias.add(datos["categoria"])

    for categoria in categorias:
        acum += f"\n{categoria}"

    acum += f"\n---------------------------\n"
    return acum


def resumen_inventario(inv):
    """
    Se crea las variables necesarias para el resumen y se calculan con un for que recorre todos 
    los productos descomponiendo sus datos, dentro del for hay un condicional que verifica los productos que tengan
    una cantidad menor a 10 para guardarlos en otra variable e imprimirla despues 
    """
    acum = "\n--- RESUMEN DEL INVENTARIO ---"
    total = 0
    cantidad_p = 0 
    producto_por_agotarse = "Productos por agotarse: "

    for producto, datos in inv.items():
        total += datos["cantidad"] * datos["precio"]
        cantidad_p += 1

        if datos["cantidad"] < 10:
            producto_por_agotarse += f"\n {producto} \t ({datos["cantidad"]} unidades)"        

    acum += f"\nValor total del inventario: {total}\nCantidad total de productos distintos: {cantidad_p} \n{producto_por_agotarse}"
    acum += f"\n------------------------\n"
    return acum        


while True:
    """
    While que se ejecuta hasta que se seleccione la opcion 6, si no se selecciona 
    el caso 6 entonces se llamara la funcion de su respectivo caso
    """
    print(f"1. Listado completo del inventario")
    print(f"2. Buscar producto puntual")
    print(f"3. Registrar venta")
    print(f"4. Categorias de la tienda")    
    print(f"5. Resumen del inventario") 
    print(f"6. Salir")
    opc = input("Seleccione una opcion: ")

    match opc :
        case "6":
            print("\nHasta luego")
            break

        case "1":
            print(listar_inventario(inventario))  

        case "2":
            busqueda = input("¿Que producto desea buscar? ").lower().strip()
            print(buscar_producto(busqueda, inventario))

        case "3":
            print(f"\n--- REGISTRAR VENTA ---")
            producto_v = input("Producto a vender: ").lower().strip()
            
            while True:
                try:
                    cantidad = int(input("Cantidad a vender: "))
                    break
                except ValueError:
                    print("\nDigite solo numeros por favor")

            print(registrar_venta(producto_v, cantidad, inventario))

        case "4":
            print(mostrar_categorias(inventario))

        case "5":
            print(resumen_inventario(inventario))

        case _: 
            print(f"\nSeleccione una opcion correcta")
