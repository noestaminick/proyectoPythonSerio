from repositorio import *
import hashlib
import os
def main():
    Flag=True
    os.system('cls')
    print("Bienvenido al programa de la libreria CAN CASACOVERTA")
    print("Profavor, inicia sesion para utilizar el programa")
    print(" ")
    verificarContraseña()
    while Flag==True:
        print("Que deseas hacer? ")
        print("-----------------------------------")
        print("1. Mostrar un libro")
        print("2. Mostrar todos los libros")
        print("3. Añadir un libro")
        print("4. Eliminar un libro")
        print("5. Editar un libro")
        print("6. Salir del programa")
        print(" ")
        try:
            eleccion=int(input("Eleccion: "))
            if eleccion==1:
                muestraLibro()
            if eleccion==2:
                muestraTodo()
            if eleccion==3:
                añadir()
                os.system('cls')
            if eleccion==4:
                borrar()
                os.system('cls')
            if eleccion==5:
                editar()
                os.system('cls')
            if eleccion==6:
                Flag=False
                os.system('cls')
            if eleccion>6 or eleccion==str:
                print("No es una opcion valida")   
        except ValueError as e:
            print("No es una opcion valida")


if __name__=="__main__":
    main()