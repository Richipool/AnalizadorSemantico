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
flag = True

for tokens in f:#recorre las lineas de codigo del archivo fuente
    #i = word_tokenize(tokens)
    i = tokens.split()
#    print(i)
    if(i[2] == "="):#si asigna valores
        if(i[0] != "void" or i[0] != "int" or (i[0])!= "float" or i[0] != "string" or i[0] == '=' or i[0]==';'):
            tipo = None
        else: tipo = i[0]
        if(i[1] != "void" or i[1] != "int" or (i[1])!= "float" or i[1] != "string" or i[1]!= '=' or i[1]!=';'):
            nombre = None
        else: nombre = i[1]
        
        tipo = i[3]
        aux = 3#donde esta la posicion atual en el vector
        while(flag is True):
            if ('"' in i[aux]):
                flag = False
                if('"' in i[aux+1] or i[aux+1] == ';'):
                    flag = False
                if(flag is True):
                    tipo = tipo + i[aux+1]
                aux +=1
        obj = Var(tipo, nombre, lineCounter, valor)
        saveToTable(obj)
    elif(i[2]== ";"):#por si es solo una declaracion
        if(i[0] != "void" or i[0] != "int" or (i[0])!= "float" or i[0] != "string" and i[0] == "=" or i[0]==";"):
            tipo = None
        else: tipo = i[0]
        if(i[1] != "void" or i[1] != "int" or (i[1])!= "float" or i[1] != "string" and i[1]!= "=" or i[1]!=";"):
            nombre = None
        else: nombre = i[1]
        obj = Var(tipo, nombre, lineCounter)
        saveToTable(obj)
    lineCounter +=1

##    if(i[3] == '"'):
#        valor = i[4]
#    valor = i[3][:len(i[3])-1]



#    print("tipo:" + tipo)
#    print("nombre:" + nombre)

f.close()
print("ESPACIO PARA VER VARAS")
printHasTable()
