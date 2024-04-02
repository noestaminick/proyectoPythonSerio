import hashlib

#Gestión de contraseñas
def leerContraseña():
    contraseñas={}
    with open("Usuaris.txt", "r") as file:
        for line in file:
            usuario, contraseña=line.strip().split("|")
            contraseñas[usuario]=contraseña
    return contraseñas

#Validación de la contraseña
def verificarContraseña(usuario, contraseña):
    contraseñas=leerContraseña()
    contraseñaHash=hashlib.md5(contraseña.encode()).hexdigest()
    return contraseñas.get(usuario)==contraseñaHash

#Leer libros del fichero

def leer():
    with open("Llibres.txt", "r") as file:
        libros=file.readlines()
    return [libro.strip("|") for libro in libros]

#muestra todos los libros

def muestraTodo():
    libros=leer()
    libro=input("Introduce el nombre del libro.")
    for libro in libros:
        print(libros)

#muestra un libro

def muestraLibro(libro):
    libros=leer()
    libro=input("Introduce el nombre del libro.")
    if libro in libros:
        print (libro)
    else:
        print("Este libro no se encuentra en nuestra colección.")
        
#añadir libro

def añadir(libro):
    libros=leer()
    libro=input("Introduce el nombre del libro a añadir")
    if libro in libros:
        print("Este libro ya existe")
    
    else:
        with open("Llibres.txt", "a") as file:
            file.write(libro + "|")
        print("Libro introducido con exito")

#borrar libros

def borrar(libro):
    libros=leer()
    libro=input("Introduce el nombre del libro que quieres borrar: ")
    if libro in libros:
        libros.remove(libro)
        with open("Llibres.txt", "w") as file:
            for libro in libros:
                file.write(libro+"|")
            print("Libro borrado de la colección")
    else:
        print("Este libro no existe.")