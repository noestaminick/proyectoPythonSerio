import hashlib

libros=None

#Gestión de contraseñas
def leerContraseña():
    contraseñas={}
    with open("Usuaris.txt", "r") as file:
        for line in file:
            usuario, contraseña=line.strip().split("|")
            contraseñas[usuario]=contraseña
    return contraseñas

#Validación de la contraseña
def verificarContraseña():
    counter=3
    contraseñas=leerContraseña()
    while counter>0 and counter<4 :
        usuario=input("Usuario: ")
        contraseña=input("Contraseña: ")
        contraseñaHash=hashlib.md5(contraseña.encode()).hexdigest()
        if contraseñas.get(usuario)==contraseñaHash :
            print("Sesion iniciada correctamente")
            counter=counter+5
        else:
            counter=counter-1
            print("La contraseña es incorrecta")
            print("Numero de intentos restantes: ",counter)
    if counter<=0:
        print("Has superado el limite de intentos")
        exit()
#Leer libros del fichero

def leer():
    global libros
    if libros is None:
        with open("Llibres.txt", "r") as file:
            libros=[line.strip() for line in file]
    return libros

#muestra todos los libros

def muestraTodo():
    libros=leer()
    for libro in libros:
        print(libro)

#muestra un libro

def muestraLibro():
    busca=input("Introduce el nombre del libro: ") 
    libros=leer()
    encuentro=False
    
    for libro in libros:
        if libro.startswith(busca):
            print(libro)
            encuentro=True
            break
    else:
        print("Este libro no se encuentra en nuestra colección.")
        
#añadir libro

def añadir():
    titulo=input("Introduce el nombre del libro: ")
    autor=input("Introduce el nombre del autor/a: ")
    año=input("Introduce el año de publicación del libro: ")
    genero=input("Introduce el genero del libro: ")
    isbn=input("Introduce el ISBN del libro: ")
    libro=f"{titulo}|{autor}|{año}|{genero}|{isbn}"
    
    libros=leer()
    if libro.strip() in libros:
        print("Este libro ya existe")
    
    else:
        with open("Llibres.txt", "a") as file:
            file.write("\n"+libro)
        print("Libro introducido con exito")

#borrar libros

def borrar():
    libro=input("Introduce el nombre del libro que quieres borrar: ")
    libros=leer()
    encuentro=False
    
    if libro in libros:
        libros.remove(libro)
        with open("Llibres.txt", "w") as file:
            for libro in libros:
                file.write(libro+"|")
            print("Libro borrado de la colección")
    else:
        print("Este libro no existe.")

#editar libros
 
def editar():
    libroAnt=input("Introduce el nombre del libro a modificar: ")
    titulo=input("Introduce el nuevo titulo del libro: ")
    autor=input("introduce el nuevo autor del libro: ")
    año=input("Introduce el nuevo año de publicación del libro: ")
    genero=input("introduce el nuevo genero del libro: ")
    isbn=input("introduce el nuevo ISBN del libro: ")
    libroMod=f"{titulo}|{autor}|{año}|{genero}|{isbn}\n"
    
    libros=leer()
    if libroAnt in libros:
        index=libros.index(libroAnt)
        libros[index]=libroMod.strip()
        with open("Llibres.txt", "w") as file:
            for libro in libros:
                file.write(libro+"\n")
        print("Libro modificado con exito.")
    
    else:
        print("Este libro no existe.")