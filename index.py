from JsonReader.JsonReader import JsonReader
from Lineal.Procesos import *

json_reader = JsonReader('data.json')
data = json_reader.read_json()

prob = None

if(data["objetivo"] == "maximizar"):
    prob = Maximizar(data)
elif(data["objetivo"] == "minimizar"):
    prob = Minimizar(data)

# print(prob.variables_dictionary)