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
        print(key, globalTable[key].type, globalTable[key].val, globalTable[key].line, globalTable[key].father)

def esString(w):#recibe 
	#cout << w;
	return(w[0]== -30 and w[w.size()-1] == -99 or w[0] == 34 and w[w.size() - 1] == 34 or w[0] == 39 and w[w.size() - 1] == 39)

def isNumber(s):
    return (s.replace('.','',1).isdigit())

"""AQUI EMPIEEZA EL COPY PASTE/TRADUCCION SALVAJE"""

variables = ["void", "int", "float", "string"]
statements = ["if", "while"]
especiales = ["+","-" , ";" ,"*",",", "/","=","==","!=","<",">" ,")","{","}","("]




#"""ARCHIVO"""
word =None
word1 = None
lineCounter = 1#para ir contanto las lineas


st = queue.LifoQueue()#aqui va la pila de variables
stPadre = queue.LifoQueue()#para las funciones

f = open("pruebas.txt")#encoding = "utf8"...ahora funciona sin esto
line = f.readlines()#una lista de lineas
f.close()

for x in line:#ir linea por linea del archivo
    word = x.split()#hace tokens por espacios...una lista de cada palabra 
    #print()#linea por linea
    for y in word:#ir recorriendo los tokens de word
        #print(y)

        if y == "}":
            stPadre.get()
        if y == "if" or y == "while":
            var = Var(y, "undefined")
            var.id = "statement"
            if stPadre.qsize():#pila de funciones
                var.father = stPadre.queue[stPadre.qsize() -1]#dudas por aqui de si el "top" es asi
            st.put(var)#mete al stack la variale
            stPadre.put(y)#el identificador de la funcion
        if y in variables or y == "(":
            if y == "(":
                if not st.empty():
                    if st.queue[st.qsize()-1].id != "statement":
                        st.queue[st.qsize()-1].id = "funcion"
                        stPadre.put(st.queue[st.qsize()-1].type)
                        #eliminar la funcion del diccionario, mediante la llave "name"
                        del globalTable[st.queue[st.qsize()-1].name]
            else: #se supone que la siguiente palabra el el nombre de la variable
                word1 = word[1]#no se si seria asi.......DUDA
                #print(word1)
                var = Var(y, word1)
                if stPadre.qsize():
                   # print(stPadre.qsize())
                    var.father = stPadre.queue[stPadre.qsize()-1]
                    if y == "}":
                        stPadre.get()
                var.id = "variable"
                st.put(var)
                saveToTable(var)#el guarda en el diccionario
        elif((not y in especiales) and (not isNumber(y)) and (not y in statements) and (not esString(y))):
       # and (not isinstance(y, str))):
            aux = globalTable.get(y)
            if aux is None:
                print("Error -linea " , lineCounter ,": " + y + " no esta declarada\n")
    lineCounter+=1
print("\n\nStack de variables\n\n")
while not st.empty():
    print(st.queue[st.qsize()-1].name + "\n")
    st.get()
print("\n\nHash Table\n\n")
printHasTable()

"""
print("ESPACIO PARA VER VARAS")
#printHasTable()
"""