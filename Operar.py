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