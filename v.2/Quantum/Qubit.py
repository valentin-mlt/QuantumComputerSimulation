import math, random

class CreateQubit:
    def __init__(self,
                 qubit_id : int,
                 register_id : int,
                 state : str = "initialized",
                 value : int = 0,
                 alpha : complex = 1 + 0j,
                 beta : complex = 0 + 0j,
                 amplitudes_generation_method = "attribution",
                 **kwargs
                 ) -> None:
        
        self.qubit_id = qubit_id
        self.register_id = register_id
        self.__state = state
        self.value = value
        self.__alpha = alpha
        self.__beta = beta
        self.amplitudes_generation_method = kwargs.get("amplitudes_generation_method", "attribution")

    def __repr__(self): #pour débugage et eval(...)
        return f"Qubit {self.qubit_id} in register {self.register_id} is in state {self.__state}, with value {self.value}, and amplitudes alpha = {self.__alpha}, and beta = {self.__beta}"
    def __str__(self):
        return f"Qubit {self.qubit_id} in register {self.register_id} is in state {self.__state}, with value {self.value}, and amplitudes alpha = {self.__alpha}, and beta = {self.__beta}"
    def __add__(self, other):
        return self.__alpha + other.__alpha, self.__beta + other.__beta
    def __sub__(self, other):
        return self.__alpha - other.__alpha, self.__beta - other.__beta
    def __mul__(self, other):
        return self.__alpha * other.__alpha, self.__beta * other.__beta
    def __truediv__(self, other):
        return self.__alpha / other.__alpha, self.__beta / other.__beta
    def __eq__(self, other):
        return self.__alpha == other.__alpha, self.__beta == other.__beta

qubit_0 = CreateQubit(0,0,"initialized",0,1+0j,0+0j,amplitudes_generation_method="attribution")