import random, math
import time

### ====== CREATION DES QUBITS ====== ###
class Qubit:
    def __init__(self, 
                 qubit_id: int,        # id of the qubit relative to its register
                 register_id: int,     # id of the register relative to the set of registers
                 state: str = "initialized", # initialized, measured, superimposed, entangled
                 value: int = 0,             # 0, 1, or None
                 alpha: complex = 1 + 0j,    # amplitude of state |0⟩
                 beta: complex = 0 + 0j,     # amplitude of state |1⟩
                 amplitudes_generation_method: str = "attribution"  # attribution, generation
                 ):
        
        self.qubit_id = qubit_id
        self.register_id = register_id
        self.state = state
        self.value = value
        self.__alpha = alpha
        self.__beta = beta
        self.amplitudes_generation_method = amplitudes_generation_method
        
        self.normalize()

    def __repr__(self):
            return f"Qubit {self.qubit_id} (Registre {self.register_id}) : α={self.alpha}, β={self.beta}"
    
    def __str__(self):
        return f"Qubit {self.qubit_id} (Registre {self.register_id}) : α={self.alpha}, β={self.beta}"
    
    def __eq__(self, other):
        return self.qubit_id == other.qubit_id and self.register_id == other.register_id

    def normalize(self):
        norm = abs(self.alpha)**2 + abs(self.beta)**2
        if not math.isclose(norm, 1, rel_tol=1e-9) and norm != 0:
            self.alpha /= norm**0.5
            self.beta /= norm**0.5
        else:
            raise ValueError("Cannot normalize a zero vector")
        
    def measure(self):
        self.state = "measured"
        self.value = 1 if random.random() < abs(self.alpha)**2 else 0 

### ====== CREATION DES REGISTRES QUANTIQUES ====== ###
class QuantumRegister:
    def __init__(self, qubits_number, register_id):
        self.qubits = [Qubit(i, register_id) for i in range(qubits_number)]
        self.register_id = register_id

    def measure(self):
        for qubit in self.qubits:
            qubit.measure()

    def initialize(self):
        for qubit in self.qubits:
            qubit.state = "initialized"
            qubit.value = 0
            qubit.alpha = 1 + 0j
            qubit.beta = 0 + 0j
            qubit.normalize()

    def apply_gate(self, qubit, gate_type):
        if gate_type == 'H':  
            qubit.alpha, qubit.beta = (qubit.alpha + qubit.beta) / 2, (qubit.alpha - qubit.beta) / 2
        elif gate_type == 'X':  
            qubit.alpha, qubit.beta = qubit.beta, qubit.alpha
        else:
            raise ValueError(f"Porte quantique {gate_type} non implémentée")


class QuantumProcessor:
    def __init__(self, quantum_registers):
        self.quantum_registers = quantum_registers

    def apply_gate(self, qubit, gate_type):
        if gate_type == 'H':  
            qubit.alpha, qubit.beta = (qubit.alpha + qubit.beta) / 2, (qubit.alpha - qubit.beta) / 2
        elif gate_type == 'X':  
            qubit.alpha, qubit.beta = qubit.beta, qubit.alpha
        else:
            raise ValueError(f"Porte quantique {gate_type} non implémentée")

### ====== PARAMETRES DE L'ORDINATEUR QUANTIQUE ====== ###
class QuantumComputer:
    def __init__(self):
        self.state = "initialized" # initialized, running, paused, stopped
        self.quantum_registers = [QuantumRegister(3, i) for i in range(0,2)]  
        self.processor = QuantumProcessor(self.quantum_registers)
        self.memory = {}  
        self.running = False  
        self.start()

    main_quantum_register = QuantumRegister() # the main quantum register
    temporary_quantum_register = QuantumRegister() # a temporary quantum register


    
    
    #def run_simulation(self):
        #while True:
            #try:
                #command = self.command_queue.get(timeout=1)
                #self.execute_command(command)
            #except queue.Empty:
                #if self.running:
                    #self.run_cycle()



    def send_command(self, command):
        self.command_queue.put(command)


