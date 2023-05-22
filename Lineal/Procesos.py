from pulp import *
from Lineal.LinealProcess import Lineal_Process

class Minimizar(Lineal_Process):
    def __init__(self, data):
        super().__init__(data, LpMinimize)

class Maximizar(Lineal_Process):
    def __init__(self, data):
        super().__init__(data, LpMaximize)