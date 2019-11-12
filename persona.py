# persona.py
# Autor: El Tigre
# Descripción: Definición de la clase Persona

# Implementa funciones para crear y realizar operaciones sobre un árbol binario
class Persona:
    def __init__(self, ced, nom, ed):
        # La cédula es la llave
        self.cedula = ced
        self.nombre = nom
        self.edad = ed