from pulp import *
code="""
count = 2
x_name = ['x1', 'x2']
x_value = [3, 5]
x = [LpVariable(x_name[i], lowBound = 0) for i in range(count) ]
c = LpAffineExpression([ (x[i],x_value[i]) for i in range(count)])
"""
exec(code)
print(c)

# import re

# cadena = "3 * x1 + 5 * x2 - 8*x3"

# # Patrón de expresión regular para encontrar números con signo y variables
# patron = r"([-+]?\s*\d+)\s*\*\s*([a-zA-Z]\w*)"

# # Buscar todas las coincidencias en la cadena
# coincidencias = re.findall(patron, cadena)
# print("coincidencias", coincidencias)

# # Imprimir los resultados
# for numero, variable in coincidencias:
#     numero = numero.replace(" ", "")
#     variable = variable.replace(" ", "")
#     print("Número:", numero)  # Eliminar espacios en blanco adicionales
#     print("Variable:", variable)
#     print()

