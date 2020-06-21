from Nodo import  Nodo

def imprimirIn(arbol):
    if arbol== None:
        return []
    else:
        return imprimirIn(arbol.izquierda)+[arbol.valor]+imprimirIn(arbol.derecha)
        
def insertar(arbol, valor):
    if arbol == None:
        return Nodo(valor)
    if arbol.valor> valor:
        return Nodo(arbol.valor,insertar(arbol.izquierda,valor),arbol.derecha)
    return Nodo(arbol.valor,arbol.izquierda, insertar(arbol.derecha,valor))

def procesar(entrada):
    return entrada.split()

def estructurar(ao): 
    if(ao[0]=="+" or ao[0]=="-" or ao[0]=="*" or ao[0]=="/" ):  
      if(ao[2]!="+" or ao[2]!="-" or ao[2]!="*" or ao[2]!="/"):
        return Nodo(ao[0], estructurar(ao[1:]),estructurar(ao[ lfo(ao): ]))
         

    return Nodo(ao[0])

def lfo(ao):
    if ((ao[0]!="+" or ao[0]!="-" or ao[0]!="*" or ao[0]!="/") and ((ao[1]!="+" or ao[1]!="-" or ao[1]!="*" or ao[1]!="/"))):
      return 2

    return 1+lfo(ao[1:]) 