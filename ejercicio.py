from pulp import *

# Crear el problema de programación lineal
prob = LpProblem("Problema_de_Programación_Lineal", LpMinimize)

x1 = LpVariable("x1", lowBound=0) #Cantidad de kilogramos de alfalfa
x2 = LpVariable("x2", lowBound=0) #Cantidad de kilogramos de maíz
x3 = LpVariable("x3", lowBound=0) #Cantidad de kilogramos de soja

# Función objetivo
prob += 0.5 * x1 + 0.8 * x2 + 1.2* x3

# Restricciones
prob += 20 * x1 + 10 * x2 + 40 * x3 >= 40 #Proteina
prob += 60 * x1 + 70 * x2 + 20 * x3 >= 60 #Carbohidratos
prob += 10 * x1 + 20 * x2 + 40 * x3 >= 20 #Grasas

# Resolver el problema
prob.solve()

# Imprimir el estado de la solución
print("Estado:", LpStatus[prob.status])

# Imprimir el valor óptimo de las variables de decisión
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

# Imprimir el valor óptimo de la función objetivo
print("Valor óptimo = ", value(prob.objective))