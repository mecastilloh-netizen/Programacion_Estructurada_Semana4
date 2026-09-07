# Programa para una ferretería

# Pedir Nombre
print("Ingrese su nombre: ")
name = input()

# Función que calcule el subtotal de la venta
def calcular_subtotal(precio, cantidad):
    subtotal = precio * cantidad  # Variable local
    return subtotal

# Función que aplica un 8% de descuento cuando el subtotal es mayor o igual a 3000
def calcular_descuento(subtotal):
    descuento = 0  # Variable local

    if subtotal >= 3000:
        descuento = subtotal * 0.08

    return descuento

# Función que calcula el IVA del 15%
def calcular_iva(monto):
    iva = monto * 0.15  # Variable local
    return iva

# Procedimiento que muestra producto, subtotal, descuento, IVA y total
def mostrar_resumen(producto, subtotal, descuento, iva, total):
    mensaje = "--- RESUMEN DE VENTA ---"  # Variable local

    print(mensaje)
    print("Producto:", producto)
    print("Subtotal: C$", round(subtotal, 2))
    print("Descuento: C$", round(descuento, 2))
    print("IVA: C$", round(iva, 2))
    print("Total: C$", round(total, 2))