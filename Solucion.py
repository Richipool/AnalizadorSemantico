#vamos a morir

import nltk
from nltk.tokenize import word_tokenize
import vector

class Var:
    def __init__(self, _type, _name, _line, _val = None):
        self.name = _name
        self.type = _type
        self.line = _line
        self.val = _val

errors = []#vector de errores
def saveErrors(error, Var var):
    if(error is 1):#variable no declarada
        errors.append("variable" + var._name+" no declarada")
    elif(error is 2):#valor de retorno no coincide con la declaracion de funcion
        errors.append("valor de retorno no coincide con la declaracion de funcion")
    elif(error is 3):#asignacion de tipo incorrecto
        errors.append("asignacion de tipo incorrecto")


typesArray = ["","","",""]

"""ARCHIVO"""
tipo, nombre, linea, valor#valr
globalTable = {} 
lineCounter = 1#para ir contanto las lineas
f = open("pruebas.txt", encoding = "utf8")
#cadena1 = f.read()....sin el encoding no funca

#print(f.read())
#linea = f.readline()

for tokens in f:
    i = word_tokenize(tokens)
    for x in i:
        if x[i] is "int" or x[i] is "void" or x[i] is "float" or x[i] is "string":
            tipo = x[i]
        else 

    #print(i)



f.close()


"""def main():
    #hacer las varas aqui!...solo para que se vea bonito y separar las cosas...pero se puede quitar
    
  

    #string textLine#ir extrayendo linea por linea
 



#se llama al main
main()
"""