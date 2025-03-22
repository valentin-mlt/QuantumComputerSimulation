from Classic.ClassicRegister import CreateClassicRegister
from Quantum.QuantumRegister import CreateQuantumRegister, MainQuantumRegister, TemporaryQuantumRegister
from Config.Quantum_config.load_config import 
import json, math, time


print(qubit_config, quantum_register_config, quantum_computer_config)

class QuantumComputer:
    def __init__(self,quantum_register_number)-> None:
        self.quantum_register_number = quantum_register_number
        self.main_register = MainQuantumRegister(0,10,qubits_view=True)
        self.temporary_register  = TemporaryQuantumRegister(0,10,qubits_view=True)

class Circuit:
    pass

def space(func):
    def wrapper(*args, **kwargs):
        print("")
        result = func(*args, **kwargs)
        print("")
        return result
    return wrapper

@space
def main():
    pass

if __name__ == "__main__":
    main()


