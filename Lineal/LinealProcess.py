from pulp import *

class Lineal_Process:
    def __init__(self, data, problem_type):
        self.data = data
        self.problem_type = problem_type
        self.SetVariables()
        self.SetProblem()
        self.SetGoalFunction()
        # self.SetRestrictions()

    def _get_constrain(self, sense):
        pass
        # result = LpConstraint.from_dict(code)
        # print(result)

    # Crear el problema de programación lineal
    def SetProblem(self):
        self.problem = LpProblem("Problema_de_Programación_Lineal", self.problem_type)

    # Variables de decisión
    def SetVariables(self):
        self.variables_dictionary = {}
        variables = self.data["variables"]
        for variable in variables:
            # Variable X >= 0
            self.variables_dictionary[variable] = LpVariable(variable, lowBound=0)

    # Restricciones
    def SetRestrictions(self):
        print(type(self.problem))
        restrictions = self.data["restricciones"]

        for restriction in restrictions:
            sense = self._get_sense(restriction["condition"])
            name = "Restriccion"
            e = None
            print(sense)
            # equivalent_code = 
            # print(type(equivalent_code))

    def _get_sense(self, condition):
        sense = None
        for item in const.LpConstraintSenses:
            value = const.LpConstraintSenses[item]
            if(value == condition):
                sense = item
                break
        return sense

    def SetGoalFunction(self):
        goalFuncion = self.data["funcionObjetivo"]
        term = goalFuncion.split("+")

        info = []

        for item in term:
            currentInfo = {"name":None, "value": None}
            values = item.split("*")
            first = values[0].strip()
            if(first.isdigit()):
                second = values[1].strip()
                currentInfo["name"] = second
                currentInfo["value"] = first
            else:
                second = values[1].strip()
                currentInfo["name"] = first
                currentInfo["value"] = second

            info.append(currentInfo)
        
        # print(LpAffineExpression.)
