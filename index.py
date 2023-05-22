from JsonReader.JsonReader import JsonReader
from Lineal.Procesos import *

data = JsonReader.read_json('data.json')

prob = None

if(data["objetivo"] == "maximizar"):
    prob = Maximizar(data)
elif(data["objetivo"] == "minimizar"):
    prob = Minimizar(data)

prob.Run()

print(prob.problem)