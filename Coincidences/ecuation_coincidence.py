import re

class ecuation_coincidence:
    @staticmethod
    def GetCoincidences(expression):
        pattern = r"([-+]?\s*\d+(?:\.\d+)?)\s*\*\s*([a-zA-Z]\w*)"
        coincidences = re.findall(pattern, expression)
        for i in range(len(coincidences)):
            number, variable = coincidences[i]
            number = number.replace(" ", "")
            number = float(number)
            variable = variable.replace(" ", "")
            coincidences[i] = (number, variable)
        return coincidences