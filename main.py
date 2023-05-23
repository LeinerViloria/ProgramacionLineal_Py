from pulp import *

# Crear el problema de programación lineal
prob = LpProblem("Problema_de_Programación_Lineal", LpMaximize)

# Variables de decisión
x = LpVariable("x", lowBound=0)  # Variable x1 >= 0
y = LpVariable("y", lowBound=0)  # Variable x2 >= 0
k = LpVariable("k", lowBound=0)  # Variable x2 >= 0

# Función objetivo
prob += -1 * x + 2 * y + k  # Maximizar 3x1 + 5x2

# Restricciones
prob += 3 * y + k <= 120  # 2x1 + x2 <= 10
prob += x - y - 4*k <= 80   # x1 + 3x2 <= 12
prob += -3 * x + y + 2*k <= 100   # x1 + 3x2 <= 12

# Resolver el problema
prob.solve()

# Imprimir el estado de la solución
print("Estado:", LpStatus[prob.status])

# Imprimir el valor óptimo de las variables de decisión
for variable in prob.variables():
    print(f"{variable.name} = {variable.varValue}")

# Imprimir el valor óptimo de la función objetivo
print("Valor óptimo = ", value(prob.objective))
