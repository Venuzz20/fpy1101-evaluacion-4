libros = []

def validar_titulo(titulo):
    return len(titulo.strip()) > 0

def validar_copias(copias_str):
    if not copias_str.isdigit():
        return False
    return int(copias_str) >= 0


def validar_prestamo(prestamo_str):
    if not prestamo_str.isdigit():
        return False
    return int(prestamo_str) > 0

def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    opcion = input("Ingrese una opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 6:
        print("Opción inválida. Ingrese un número entre 1 y 6.")
        opcion = input("Ingrese una opción: ")
    return int(opcion)


def agregar_libro(lista):
    titulo = input("Ingrese el título del libro: ")
    if not validar_titulo(titulo):
        print("Error: el título no puede estar vacío.")
        return

    copias_str = input("Ingrese la cantidad de copias: ")
    if not validar_copias(copias_str):
        print("Error: las copias deben ser un número entero mayor o igual a 0.")
        return

    prestamo_str = input("Ingrese el período de préstamo (días): ")
    if not validar_prestamo(prestamo_str):
        print("Error: el período de préstamo debe ser un número entero mayor que 0.")
        return

    libro = {
        "titulo": titulo.strip(),
        "copias": int(copias_str),
        "prestamo": int(prestamo_str),
        "disponible": False
    }

    lista.append(libro)
    print(f"Libro '{titulo.strip()}' agregado exitosamente.")

def buscar_libro(lista, titulo):
    for i in range(len(lista)):
        if lista[i]["titulo"] == titulo:
            return i
    return -1

def eliminar_libro(lista):
    titulo = input("Ingrese el título del libro a eliminar: ")
    posicion = buscar_libro(lista, titulo)
    if posicion != -1:
        lista.pop(posicion)
        print(f"Libro '{titulo}' eliminado exitosamente.")
    else:
        print(f"El libro '{titulo}' no se encuentra registrado.")


def actualizar_disponibilidad(lista):
    for libro in lista:
        libro["disponible"] = libro["copias"] >= 1

def mostrar_libros(lista):
    actualizar_disponibilidad(lista)
    print("\n=== LISTA DE LIBROS ===")

    if len(lista) == 0:
        print("No hay libros registrados.")
        return

    for libro in lista:
        estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado}")
        print("*" * 44)



def main():
    libros = []

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_libro(libros)

        elif opcion == 2:
            titulo = input("Ingrese el título a buscar: ")
            posicion = buscar_libro(libros, titulo)

            if posicion != -1:
                libro = libros[posicion]
                print(f"Libro encontrado en posición {posicion}:")
                print(f"Título: {libro['titulo']}")
                print(f"Copias: {libro['copias']}")
                print(f"Préstamo: {libro['prestamo']}")
                print(f"Disponible: {libro['disponible']}")
            else:
                print(f"El libro '{titulo}' no se encuentra registrado.")

        elif opcion == 3:
            eliminar_libro(libros)

        elif opcion == 4:
            actualizar_disponibilidad(libros)
            print("Disponibilidad actualizada.")

        elif opcion == 5:
            mostrar_libros(libros)

        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva pronto.")
            break

main()