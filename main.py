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
  if (len(ao)>0):
    if(ao[0]=="+" or ao[0]=="-" or ao[0]=="*" or ao[0]=="/" ):
      if identificar(ao,0,0,len(ao))==True:
       return Nodo(ao[0], estructurar(ao[1:(len(ao)//2)+1]),estructurar(ao[(len(ao)//2)+1:]))
      else:
        if(ao[(len(ao)//2)-1]== "+" or ao[(len(ao)//2)-1]== "-" or ao[(len(ao)//2)-1]== "*" or ao[(len(ao)//2)-1]== "/" ):
          return Nodo(ao[0], estructurar(ao[1:(len(ao)//2)+2]),estructurar(ao[(len(ao)//2)+2:]))
        else :
          print (ao[(len(ao)//2)])
          #Para la parte derecha mayor
          return Nodo(ao[0], estructurar(ao[1:(len(ao)//2)]),estructurar(ao[(len(ao)//2):])) 

    return Nodo(ao[0])


def identificar(ao,cn,co,t):
   if(len(ao)>0): 
    if (ao[0]=="+" or ao[0]=="-" or ao[0]=="*" or ao[0]=="/"):
      return identificar(ao[1:],cn,co+1,t)
    return identificar(ao[1:],cn+1,co,t)
   if(t<=3):
     return True
   return simetria(cn,co)

def simetria(cn,co):
    if(((co-1)*2)==cn):    
      return True
    return False
 

def operar(arbol):
  if  (not arbol.valor == '+') and  (not arbol.valor == '-' ) and ( not arbol.valor == '*') and (not arbol.valor == '/' ):
    return int(arbol.valor) 
  elif arbol.valor == '+' :
    return ( operar(arbol.izquierda) + operar(arbol.derecha))
  elif arbol.valor == '-' :
    return ( operar(arbol.izquierda) - operar(arbol.derecha))
  elif arbol.valor == '*' :
    return ( operar(arbol.izquierda) * operar(arbol.derecha))
  elif arbol.valor == '/' :
    return ( operar(arbol.izquierda) / operar(arbol.derecha))

def imprimir(arbol) :
   print("Esta es la impresion")
   print (imprimirIn(arbol))
   print("Imprimir operación")
   print(operar(arbol))

imprimir(estructurar(procesar(input("Ingresa algo pls "))))
