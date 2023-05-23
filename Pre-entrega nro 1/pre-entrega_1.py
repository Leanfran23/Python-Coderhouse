def registrar_usuario(database_file):
    nombre = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    email = input("Ingrese el email")
    telefono = input("Ingrese el telefono")

    #Abrir el archivo en modo de escritura
    with open(database_file, "a") as file:
        # Escribir nueva linea.
        file.write(f"{nombre},{password},{email},{telefono}\n")

    print("Usuario registrado con éxito!")


def mostrar_usuarios(database_file):
    # Abrir el archivo en modo de lectura
    with open("database/db.txt", "r") as file:
        # Leer todas las líneas del archivo
        lines = file.readlines()

        if len(lines) == 0:
            print("No hay usuarios registrados.")
        else:
            print("Usuarios registrados:")
            for line in lines:
                # Separar el nombre de usuario y la contraseña por coma
                nombre, password, email, telefono = line.strip().split(",")
                print("------------------------------------------------")
                print(f"Nombre: {nombre}")
                print(f"Contraseña: {password}")
                print(f"email: {email}")
                print(f"telefono: {telefono}")
                print("------------------------------------------------")


def login(database_file):
    nombre = input("Ingrese el nombre de usuario: ")
    password = input("Ingrese la contraseña: ")
    email = input("Ingrese el email: ")
    telefono = input("Ingrese el telefono: ")
    # Abrir el archivo en modo de lectura
    with open(database_file, "r") as file:
        # Leer todas las líneas del txt
        lines = file.readlines()

        for line in lines:
            # Separar el nombre de usuario y la contraseña por coma
            usuario, contraseña = line.strip().split(",")

            if nombre == usuario:
                if password == contraseña:
                    print("Inicio de sesión exitoso!")
                    return

        print("Usuario o contraseña incorrectos.")


def menu(database_file):
    while True:
        print("***** MENÚ *****")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Iniciar sesión")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario(database_file)
        elif opcion == "2":
            mostrar_usuarios(database_file)
        elif opcion == "3":
            login(database_file)
        elif opcion == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ruta del archivo de base de datos
database_file = "database/db.txt"
# Ejecutamos el programa
menu(database_file)
