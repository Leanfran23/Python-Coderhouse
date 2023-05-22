def registrar_usuario(database):
    nombre = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")

    # Almacenamos la información en un diccionario
    usuario = {
        "nombre": nombre,
        "password": password
    }

    # Agregamos el usuario a la base de datos
    database[nombre] = usuario
    print("Usuario registrado con éxito!")


def mostrar_usuarios(database):
    if len(database) == 0:
        print("No hay usuarios registrados.")
    else:
        print("Usuarios registrados:")
        for nombre, usuario in database.items():
            print(f"Nombre: {nombre}")
            print(f"Contraseña: {usuario['password']}")
            print("-----------")


def login(database):
    nombre = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")

    if nombre in database:
        if password == database[nombre]['password']:
            print("Inicio de sesión exitoso!")
        else:
            print("Contraseña incorrecta.")
    else:
        print("Usuario no encontrado.")


def menu():
    database = {}  # Base de datos vacía

    while True:
        print("***** MENÚ *****")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(database)
        elif opcion == "2":
            mostrar_usuarios(database)
        elif opcion == "3":
            login(database)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutamos el programa
menu()
