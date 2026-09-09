#Registro de estudiantes
"""
Registrar notas de n cantidad de estudiantes
"""

notas = []

def agregarNota(nota):
    notas.append(nota)

def mostrarNotas():
    return notas

def evaluarNotas():
    for nota in notas:
        if nota >= 70:
            print(f"{nota}, es aprobado.")
        else:
            print(f"{nota}, tiene que mejorar.")