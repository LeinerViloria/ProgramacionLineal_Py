from pulp import *
from Coincidences.ecuation_coincidence import *

class Lineal_Process:
    def __init__(self, data, problem_type):
        self.data = data
        self.problem_type = problem_type

    def Run(self):
        self.SetProblem()
        self.SetVariables()
        self.SetGoalFunction()
        self.SetRestrictions()

        self.problem.solve()

    # Crear el problema de programación lineal
    def SetProblem(self):
        self.problem = LpProblem("Problema_de_Programación_Lineal", self.problem_type)

    # Variables de decisión
    def SetVariables(self):
        variables = self.data["variables"]
        for variable in variables:
            # Variable X >= 0
            newVariable = LpVariable(variable, lowBound=0)
            globals()[variable] = newVariable

    # Restricciones
    def SetRestrictions(self):
        self.problem.checkDuplicateVars()
        restrictions = self.data["restricciones"]
        i = 0
        count = len(self.data["variables"])

        for restriction in restrictions:
            i+=1
            expression = restriction["left"]
            sense = self._get_sense(restriction["condition"])
            name = "R"+str(i)
            e = self.GetExpression(expression, count)
            constant = float(restriction["right"])

            newRestriction = LpConstraint(e, sense, name, constant)
            self.problem.addConstraint(newRestriction, name)

    def _get_sense(self, condition):
        sense = None
        for item in const.LpConstraintSenses:
            value = const.LpConstraintSenses[item]
            if(value == condition):
                sense = item
                break
        return sense

    # Funcion objetivo
    def SetGoalFunction(self):
        goalFunction = self.data["funcionObjetivo"]
        count = len(self.data["variables"])
        z = self.GetExpression(goalFunction, count)

        # Se setea la funcion objetivo
        self.problem.objective = z

    def GetExpression(self, string, total):
        coincidences = ecuation_coincidence.GetCoincidences(string)

        names = []
        values = []

        for coincidence in coincidences:
            number = coincidence[0]
            variableName = coincidence[1]
            names.append(variableName)
            values.append(number)

        x = None

        if(self.problem.numVariables() <= 0):
            x = [LpVariable(names[i], lowBound = 0) for i in range(total) ]
        else:
            x = self.problem.variables()

        z = LpAffineExpression([ (x[i],values[i]) for i in range(total)])
        return z