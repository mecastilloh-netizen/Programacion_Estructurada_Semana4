import crud

def leerDatos():
    print("Dime la edad: ")
    edad = int(input())
    crud.agregarEdad(edad)

def menu():
    print("""
1. Ingresar la edad.
2. Mostrar Edades.
3. Evaluar Edades.
4. Mostrar Edad Mayor y Menor.
0. Salir
Digita una opción valida:
""")
     
    opcion = int(input())
    return opcion

def main():
    while True:
        op = menu()
        if op == 1:
            leerDatos()
        elif op == 2:
            print(crud.mostrarEdad())
        elif op == 3:
            print(crud.evaluarEdad())
        elif op == 4:
            print(crud.mostrarMayoryMenor())
        elif op == 0:
            print("Adios ...")
            break
        else:
            print("Opcion Invalida...")

main()