# Crear diccionario
informacion_personal = {}

# Sirve para ingresar los datos personales del usuario
informacion_personal["nombre"] = input("Ingrese el nombre: ")
informacion_personal["edad"] = int(input("Ingrese la edad: "))
informacion_personal["ciudad"] = input("Ingrese la ciudad: ")
informacion_personal["profesion"] = input("Ingrese la profesión: ")

# Sirve para modificar la ciudad
nueva_ciudad = input("Ingrese una nueva ciudad para actualizarse: ")
informacion_personal["ciudad"] = nueva_ciudad

# Verificar si el telefono existe, caso contrario se agrega
if "telefono" not in informacion_personal:
    telefono = input("Ingrese un número de teléfono: ")
    informacion_personal["telefono"] = telefono

# Sirve para eliminar la edad ingresada
informacion_personal.pop("edad", None)

# Finalmente se imprime el diccionario con todos los datos ingresados
print("\nDiccionario final con la información ingresada:")
print(informacion_personal)
