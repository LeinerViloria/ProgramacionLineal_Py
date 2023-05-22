import re

class ecuation_coincidence:
    @staticmethod
    def GetCoincidences(expression):
        pattern = r"([-+]?\s*\d+)\s*\*\s*([a-zA-Z]\w*)"
        coincidences = re.findall(pattern, expression)
        for number, variable in coincidences:
            number = number.replace(" ", "")
            variable = variable.replace(" ", "")
        return coincidences