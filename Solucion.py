#vamos a morir

import nltk
from nltk.tokenize import word_tokenize
import queue

class Var:
    def __init__(self, _type, _name):
        self.id = None#para saber que putas es, si una variable, un if/while, o si se pasó de verga
        self.name = _name
        self.type = _type
        self.line = 0
        self.val = None
        self.father = "main"


#insertar variables a la tabla
globalTable = {}
def saveToTable(var):
    globalTable[var.name] = var


def printHasTable():
    for key in globalTable:
        print(key, globalTable[key].type, globalTable[key].val, globalTable[key].line)


"""AQUI EMPIEEZA EL COPY PASTE/TRADUCCION SALVAJE"""

variables = ["void", "int", "float", "string"]
statements = ["if", "while"]
especiales = ["+","-" , ";" ,"*",",", "/","=","==","!=","<",">" ,")","{","}","("]




#"""ARCHIVO"""
word =None
word1 = None
word2 = None
lineCounter = 1#para ir contanto las lineas


st = queue.LifoQueue()#aqui va la pila de variables
stPadre = queue.LifoQueue()#para las funciones

f = open("pruebas.txt")#encoding = "utf8"...ahora funciona sin esto
line = f.readlines()#una lista de lineas
for x in line:#ir linea por linea del archivo
    word = x.split()#hace tokens por espacios...una lista de cada palabra 
    #print()#linea por linea
    for y in word:#ir recorriendo los tokens de word
        #print(y)
        if word == "}":
            stPadre.get()
        if word == "if" or word == "while":
            var = Var(word, "undefined")
            var.id = "statement"
            if len(stPadre)>0:#pila de funciones
                var.father = stPadre.queue[stPadre.qsize -1]#dudas por aqui de si el "top" es asi
            st.put(var)#mete al stack la variale
            stPadre.put(word)#el identificador de la funcion
        if word in variables or word == "(":
            if word == "(":
                if not st.empty():
                    if st.queue[st.qsize-1].id != "statement":
                        st.queue[st.qsize-1].id = "funcion"
                        stPadre.put(st.queue[st.qsize-1].type)
                        #eliminar la funcion del diccionario, mediante la llave "name"
                        del globalTable[st.queue[st.qsize-1].name]
            else: #se supone que la siguiente palabra el el nombre de la variable
                word1 = word[1]#no se si seria asi.......DUDA
                print(word1)
                var = Var(word, word1)
                if st.qsize>0:
                    var.father = stPadre.queue[stPadre.qsize-1]
                    if word == "}":
                        stPadre.get()
                var.id = "variable"
                sr.put(var)
                saveToTable(var)#el guarda en el diccionario
        elif(not word in especiales and not word.isdigit() and not word in statements and ):
            #
                
                    

f.close()


#print(f.read())
#for x in f:
#    linea = word_tokenize(x)
    #print(linea)
#print(linea)
#print(len(linea))
#print(type(linea))
#print("\n")
flag = True

"""
for tokens in file:#recorre las lineas de codigo del archivo fuente
    #i = word_tokenize(tokens)
    i = file.readlines()
    print(i)
#    for x in i:#ir recorriendo "los tokens" de 
#        print(i)
    if(i[2] == "="):#si asigna valores
        if(i[0] != 'void' and i[0] != 'int' and (i[0])!= 'float' and i[0] != 'string' or (i[0] == '=' or i[0]==';')):
            tipo = None
        else: tipo = i[0]
        if(i[1] != 'void' and i[1] != 'int' and (i[1])!= 'float' and i[1] != 'string' or (i[1] == '=' or i[1]==';')):
            nombre = i[1]
        else: nombre = None 
        
        valor = i[3]
        aux = 3#donde esta la posicion atual en el vector
        while(flag is True and aux != len(i)):
           # if ('"' in i[aux]):
                #flag = False
            if(i[0] == 'string'):
                if('"' in i[aux+1]):
                    valor = valor + ' ' + i[aux+1]
                    flag = False
                if(flag is True):
                    valor = valor + ' ' + i[aux+1]
            aux +=1
        #obj = Var(tipo, nombre, valor,None, lineCounter)
        #saveToTable(obj)
    elif(i[2]== ";"):#por si es solo una declaracion
        if(i[0] != "void" or i[0] != "int" or (i[0])!= "float" or i[0] != "string" and i[0] == "=" or i[0]==";"):
            tipo = None
        else: tipo = i[0]
        if(i[1] != "void" or i[1] != "int" or (i[1])!= "float" or i[1] != "string" and i[1]!= "=" or i[1]!=";"):
            nombre = None
        else: nombre = i[1]
        #obj = Var(tipo, nombre, valor,None, lineCounter)
        #saveToTable(obj)
    #lineCounter +=1

##    if(i[3] == '"'):
#        valor = i[4]
#    valor = i[3][:len(i[3])-1]



#    print("tipo:" + tipo)
#    print("nombre:" + nombre)


print("ESPACIO PARA VER VARAS")
#printHasTable()
"""