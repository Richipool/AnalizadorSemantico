#vamos a morir

import nltk
from nltk.tokenize import word_tokenize
import tokenize

class Var:
    def __init__(self, _type, _name, _line, _val = None):
        self.name = _name
        self.type = _type
        self.line = _line
        self.val = _val




errors = []#vector de errores
def saveErrors(error, var):
    if(error == 1):#variable no declarada
        errors.append("variable" + var._name+" no declarada")
    elif(error == 2):#valor de retorno no coincide con la declaracion de funcion
        errors.append("valor de retorno no coincide con la declaracion de funcion")
    elif(error == 3):#asignacion de tipo incorrecto
        errors.append("asignacion de tipo incorrecto")


#insertar variables a la tabla
globalTable = {}
def saveToTable(var):
    globalTable[var._name] = var

hashtable = {}

def printHasTable():
    for key in hashtable:
        print(key, globalTable[key].type, globalTable[key].val, globalTable[key].line)





#"""ARCHIVO"""
tipo= None
nombre= None
linea = None 
valor = None #valr 
lineCounter = 1#para ir contanto las lineas
f = open("pruebas.txt", "r")#encoding = "utf8"...ahora funciona sin esto
#print(f.read())
#for x in f:
#    linea = word_tokenize(x)
    #print(linea)
#print(linea)
#print(len(linea))
#print(type(linea))
#print("\n")

for tokens in f:#recorre las lineas de codigo del archivo fuente
    i = word_tokenize(tokens)
    print(i)
#    print(type(i))
#    print(len(i))
    
    #print("espacio")

#    for x in i:
    tipo = i[0]
    nombre = i[1]

    print("tipo:" + tipo)
    print("nombre:" + nombre)
#        if  x[2] == '=':
#            print(i)
#if x== "int" or x == "void" or x == "float" or x == "string":
#tipo = x
#print(tipo)
#elif x[i] is 
f.close()


"""def main():
    #hacer las varas aqui!...solo para que se vea bonito y separar las cosas...pero se puede quitar
    #string textLine#ir extrayendo linea por linea
 
#se llama al main
main()
"""
