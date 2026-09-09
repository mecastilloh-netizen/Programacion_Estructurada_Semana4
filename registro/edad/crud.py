# Registrar Edades y Clasificarlo
edades = []

def agregarEdad(edad):
    edades.append(edad)

def mostrarEdad():
    return edades

def evaluarEdad():
 for edad in edades:
    if edad < 18:
        print(f"{edad}, Eres menor de edad.")
    elif edad >= 18 and edad < 60:
        print(f"{edad}, Eres adulto.")
    else:
        print(f"{edad}, Eres adulto mayor.")
    return edades

def mostrarMayoryMenor():
   if len(edades) == 0:
      print("No hay edades registradas.")
   else:
      mayor = max(edades)
      menor = min(edades)
      print(f"La edad mayor es: {mayor}")
      print(f"La edad menor es: {menor}")