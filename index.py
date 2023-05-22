from JsonReader.JsonReader import JsonReader
from Lineal.Procesos import *

data = JsonReader.read_json('data.json')
i = 0

for exercise in data:
    i+=1

    print()
    print("EJERCICIO #"+str(i))
    print()

    prob = None
    goal = exercise["objetivo"]

    if(goal == "maximizar"):
        prob = Maximizar(exercise)
    elif(goal == "minimizar"):
        prob = Minimizar(exercise)

    prob.Run()

    # Imprimir el estado de la solución
    print("Estado:", LpStatus[prob.problem.status])

    # Imprimir el valor óptimo de las variables de decisión
    for variable in prob.problem.variables():
        print(f"{variable.name} = {variable.varValue}")

    # Imprimir el valor óptimo de la función objetivo
    print("Valor óptimo = ", value(prob.problem.objective))