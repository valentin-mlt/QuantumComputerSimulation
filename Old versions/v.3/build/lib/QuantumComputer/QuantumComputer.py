from Classic.ClassicRegister import CreateClassicRegister
from Quantum.QuantumRegister import CreateQuantumRegister

class QuantumComputer:
    def __init__(self, num_classic, num_quantum):
        self.classic = CreateClassicRegister(num_classic)
        self.quantum = CreateQuantumRegister(num_quantum)

    def run(self):
        print("Quantum Computer running!")

def main():
    qc = QuantumComputer(2, 2)
    qc.run()

if __name__ == "__main__":
    main()
