from pulp import *

# Crear el problema de programación lineal
prob = LpProblem("Problema_de_Programación_Lineal", LpMaximize)

# Variables de decisión
x1 = LpVariable("x1", lowBound=0)  # Variable x1 >= 0
x2 = LpVariable("x2", lowBound=0)  # Variable x2 >= 0

# Función objetivo
prob += 3 * x1 + 5 * x2  # Maximizar 3x1 + 5x2

# Restricciones
prob += 2 * x1 + x2 <= 10  # 2x1 + x2 <= 10
prob += x1 + 3 * x2 <= 12   # x1 + 3x2 <= 12

# Resolver el problema
prob.solve()

# Imprimir el estado de la solución
print("Estado:", LpStatus[prob.status])

# Imprimir el valor óptimo de las variables de decisión
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

# Imprimir el valor óptimo de la función objetivo
print("Valor óptimo = ", value(prob.objective))
