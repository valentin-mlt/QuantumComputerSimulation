from Classic.ClassicRegister import CreateClassicRegister
from Quantum.QuantumRegister import CreateQuantumRegister, MainQuantumRegister, TemporaryQuantumRegister

class QuantumComputer:
    def __init__(self,quantum_register_number)-> None:
        self.quantum_register_number = quantum_register_number
        self.main_register = MainQuantumRegister(0,10,qubits_view=True)
        self.temporary_register  = TemporaryQuantumRegister(0,10,qubits_view=True)
        self.attributes = {"quantum_register_number" : self.quantum_register_number,
                           "" : ""
                           }
def space(func):
    def wrapper(*args, **kwargs):
        print("")
        result = func(*args, **kwargs)
        print("")
        return result
    return wrapper

@space
def main():
    qc = QuantumComputer(10)
    R0 = CreateClassicRegister(0, 5, "main", default_bit_value=0, bits_view=True)
    print(R0)

if __name__ == "__main__":
    main()


