import crud

def leerDatos():
    print("Dime la nota: ")
    nota = int(input())
    crud.agregarNota(nota)

def menu():
    print("""
1. Ingresar Nota.
2. Mostrar Notas.
3. Evaluar Notas.
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
            print(crud.mostrarNotas())
        elif op == 3:
            crud.evaluarNotas()
        elif op == 0:
            print("Adios ...")
            break
        else:
            print("Opcion Invalida...")

main()