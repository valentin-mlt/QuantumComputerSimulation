import random


class Quantum_Register_Creation_Classic(Qubit):
    def __init__(self, qubits, qubits_number, register_position):
        self.qubits = [Qubit(i,register_position) for i in range(QuantumComputer["main_quantum_register"])]  
        self.qubits_number = qubits_number
        self.register_position = register_position

    def measure(self):

        for qubit in self.qubits:
            qubit.state = "measured"
            qubit.value = 1 if random.random() < abs(qubit.alpha)**2 else 0




class QuantumComputer:
    def __init__(self, 
                 state : str = "initialized", # initialized, running, paused, stopped
                 quantum_registers_number : int = 1,
                 processor = 1,
                 ):
        self.quantum_registers = quantum_registers
        self.processor = QuantumProcessor(quantum_registers)
        self.memory = {}  # Mémoire classique

    quantum_computer_settings = {
        "classic_quantum_registers_number" = 2,
        "main_quantum_register_prescence" = True,
        "processor" = QuantumProcessor(quantum_registers),
        "memory" = {}
    }
    
    def start(self):
        self.state = "running"
        self.run_algorithm()
        self.state = "stopped"
        self.memory = {register.register_position: [qubit.value for qubit in register.qubits] for register in self.quantum_registers}  # Sauvegarder les valeurs des qubits mesurés dans la mémoire classique
    
    def run_algorithm(self, instructions):

        instruction_set = QuantumInstructionSet(self.processor)
        instruction_set.execute(instructions)

        for register in self.quantum_registers: # Mesurer chaque registre quantique
            register.measure()  # Mesurer le registre
        self.memory = {}  # Réinitialiser la mémoire classique
        self.memory = {register.register_position: [qubit.value for qubit in register.qubits] for register in self.quantum_registers}  # Sauvegarder les valeurs des qubits mesurés dans la mémoire classique












class Qubit:
    def __init__(self, 
                 qubit_position: int,        # position of the qubit relative to its register
                 register_position: int,     # position of the register relative to the set of registers
                 state: str = "initialized", # initialized, measured, superimposed, entangled
                 value: int = 0,             # 0, 1, or None
                 alpha: complex = 1 + 0j,    # amplitude of state |0⟩
                 beta: complex = 0 + 0j,     # amplitude of state |1⟩
                 amplitudes_generation_method: str = "attribution"  # attribution, generation
                 ):
        
        self.qubit_position = qubit_position
        self.register_position = register_position
        self.state = state
        self.value = value
        self.alpha = alpha
        self.beta = beta
        self.amplitudes_generation_method = amplitudes_generation_method
        
        self.normalize()

    def __str__(self):
        return (f"Qubit n°{self.qubit_position}/? | Register n°{self.register_position}/? | State: {self.state} | Value: {self.value} | Amplitudes: {self.alpha}|0⟩, ({self.beta})|1⟩")
    
    def normalize(self):
        norm = abs(self.alpha)**2 + abs(self.beta)**2
        if norm != 1:
            self.alpha /= (norm**0.5)
            self.beta /= (norm**0.5)

    def amplitudes_generation(self):
        if self.amplitudes_generation_method == "generation":
            real_alpha = random.uniform(0, 1)
            imag_alpha = random.uniform(0, 1)
            self.alpha = complex(real_alpha, imag_alpha)
            
            real_beta = random.uniform(0, 1)
            imag_beta = random.uniform(0, 1)
            self.beta = complex(real_beta, imag_beta)
            
            self.normalize()
        elif self.amplitudes_generation_method == "attribution":
            self.alpha = 1 + 0j
            self.beta = 0 + 0j
        else:
            raise ValueError("Méthode de génération non reconnue : 'generation' ou 'attribution' attendue.")






















q_0 = Qubit(0,0,"initialized",0,1+0j,0+0j,"attribution")
print(q_0)


class Classic_Register:
    pass

class QuantumInstructionSet:
    def __init__(self, quantum_processor):
        self.processor = quantum_processor

    def execute(self, instructions):
        # instructions est une liste de tuples (qubit, gate_type)
        for qubit, gate in instructions:
            self.processor.apply_gate(qubit, gate)


main_quantum_register = Quantum_Register() # the main quantum register
temporary_quantum_register = Quantum_Register() # a temporary quantum register

main_classic_register = Classic_Register() # the main classic register



class QuantumProcessor:
    def __init__(self, quantum_registers):
        self.quantum_registers = quantum_registers  # Liste des registres quantiques

    def apply_gate(self, qubit, gate_type):
        # Appliquer une porte quantique à un qubit spécifique dans un registre
        if gate_type == 'H':  # Hadamard
            qubit.alpha, qubit.beta = (qubit.alpha + qubit.beta) / 2, (qubit.alpha - qubit.beta) / 2
        elif gate_type == 'X':  # Pauli-X (NOT gate)
            qubit.alpha, qubit.beta = qubit.beta, qubit.alpha
        else:
            raise ValueError(f"Porte quantique {gate_type} non implémentée")


