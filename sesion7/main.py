# ESCRIBE ESTA LINEA DE CODIGO 
print("bienvenidos al entrenamiento con python, vamos a disfutar al maximo esta sesion")

"""
    descuento en una compra:
    si compras mas de $1000, optienes un descuento del 20%
    pide el monto de la compra y muesetra el precio final
"""

# pedir datos por teclado al usuario int (entero) float (decimales) str (cadenas de caracteres) bool (boleno unos o ceros)

compra = float(input("por favor digite el valor de su compra: "))
# si compras mas de $1000, obtienes un descuento del 20%.
# siempre que la salida tenga mas de un camino de resolución, debo implementar condicionales
# operadores combinados
# operadores de asignación =, operadores aritmeticos + - * /,operadores logicos and y, or o, not
# operadores de comparación ==,!=,>,<,>=,<=
if compra > 1000:
   descuento = compra * 0.2
   compra -= descuento
   #compra = compra - descuento
   print(f"el descuento es de {descuento}, por lo tanto su valor a pagar es: {compra}")
