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
    globalTable[var.name] = var


def printHasTable():
    for key in globalTable:
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
#bool flag = true

for tokens in f:#recorre las lineas de codigo del archivo fuente
    #i = word_tokenize(tokens)
    i = tokens.split()
#    print(i)
    if(i[2] == "="):#si asigna valores
        if(i[0] != "void" or i[0] != "int" or (i[0])!= "float" or i[0] != "string"):
            tipo = None
        else: tipo = i[0]
        nombre = i[1]
    elif(i[2]== ";"):#por si es solo una declaracion
        if(i[0] != "void" or i[0] != "int" or (i[0])!= "float" or i[0] != "string"):
            tipo = None
        else: tipo = i[0]
        nombre = i[1]

##    if(i[3] == '"'):
#        valor = i[4]
    valor = i[3][:len(i[3])-1]
    obj = Var(tipo, nombre, lineCounter, valor)
    saveToTable(obj)
    lineCounter +=1


#    print("tipo:" + tipo)
#    print("nombre:" + nombre)

f.close()
print("ESPACIO PARA VER VARAS")
printHasTable()
