# map.py
# Programa de prueba para una tabla hash - Implementación básica con diccionarios

import persona



cantidad = 4

array_personas = [persona.Persona("1111", "Jose", 37), persona.Persona("2222", "Karla", 18),
                  persona.Persona("3333", "Monica", 38), persona.Persona("4444", "Arturo", 29)]

# Tabla Hash - Definida como un diccionario
hashtable = {}

# Almacenamos cada persona asociada con la cédula
for per in array_personas:
    hashtable[per.cedula] = per

# Imprimimos la tabla hash
for key in hashtable:
    print(key, hashtable[key].nombre, hashtable[key].edad)