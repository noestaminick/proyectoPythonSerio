import hashlib

# Gestión de contraseñas
def leerContraseña():
    contraseñas = {}
    with open("Usuaris.txt", "r") as file:
        for line in file:
            usuario, contraseña = line.strip().split("|")
            contraseñas[usuario] = contraseña
    return contraseñas

# Validación de la contraseña
def verificarContraseña():
    counter = 3
    contraseñas = leerContraseña()
    while counter > 0 and counter < 4:
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        contraseñaHash = hashlib.md5(contraseña.encode()).hexdigest()
        if contraseñas.get(usuario) == contraseñaHash:
            print("Sesion iniciada correctamente")
            counter = counter + 5
        else:
            counter = counter - 1
            print("La contraseña es incorrecta")
            print("Numero de intentos restantes: ", counter)
    if counter <= 0:
        print("Has superado el limite de intentos")
        exit()

# Leer libros del fichero
def leer():
    try:
        with open("Llibres.txt", "r") as file:
            libros = [line.strip() for line in file]
    except FileNotFoundError:
        print("Error: El fichero Llibres.txt no se ha encontrado.")
        libros = []
    return libros

# Mostrar todos los libros
def muestraTodo():
    libros = leer()
    for libro in libros:
        print(libro)

# Mostrar un libro
def muestraLibro():
    busca = input("Introduce el nombre del libro: ")
    libros = leer()
    encuentro = False
    
    for libro in libros:
        if libro.startswith(busca):
            print(libro)
            encuentro = True
            break
    if not encuentro:
        print("Este libro no se encuentra en nuestra colección.")

# Añadir libro
def añadir():
    flag = True
    while flag:
        titulo = input("Introduce el nombre del libro: ")
        autor = input("Introduce el nombre del autor/a: ")
        año = input("Introduce el año de publicación del libro: ")
        genero = input("Introduce el genero del libro: ")
        isbn = input("Introduce el ISBN del libro: ")
        if titulo and autor and año and genero and isbn:
            flag = False
        else:
            print("Uno de los campos estaba vacío, asegúrate de rellenar todos ellos.")
    
    libro = f"{titulo}|{autor}|{año}|{genero}|{isbn}"
    
    libros = leer()
    if libro.strip() in libros:
        print("Este libro ya existe")
    else:
        with open("Llibres.txt", "a") as file:
            file.write("\n" + libro)
        print("Libro introducido con éxito")

# Borrar libros
def borrar():
    elimina = input("Introduce el nombre del libro que quieres borrar: ")
    libros = leer()
    encuentro = False
    
    for libro in libros:
        if libro.startswith(elimina):
            libros.remove(libro)
            encuentro = True
            break
    
    if encuentro:
        with open("Llibres.txt", "w") as file:
            for i, libro in enumerate(libros):
                if i != 0:
                    file.write("\n")
                file.write(libro)
        print("Libro eliminado con éxito.")
    else:
        print("Este libro no existe.")

# Editar libros
def editar():
    libroAnt = input("Introduce el nombre del libro a modificar: ")
    libros = leer()
    encuentro = False
    for index, libro in enumerate(libros):
        if libro.startswith(libroAnt):
            titulo = input("Introduce el nuevo titulo del libro: ")
            autor = input("Introduce el nuevo autor del libro: ")
            año = input("Introduce el nuevo año de publicación del libro: ")
            genero = input("Introduce el nuevo genero del libro: ")
            isbn = input("Introduce el nuevo ISBN del libro: ")
            libroNuevo = f"{titulo}|{autor}|{año}|{genero}|{isbn}\n"
            libros[index] = libroNuevo.strip()
            encuentro = True
            break
    
    if encuentro:
        with open("Llibres.txt", "w") as file:
            for libro in libros:
                file.write(libro + "\n")
        print("Libro modificado con éxito.")
    else:
        print("Este libro no existe.")
