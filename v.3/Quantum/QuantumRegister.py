from Quantum.Qubit import CreateQubit

class CreateQuantumRegister:
    def __init__(self,
                 register_id : int,
                 qubits_number : int,
                 register_type : str,
                 default_qubit_value : int = 0,
                 default_aplha_value : complex = 1+0j,
                 default_beta_value : complex = 0+0j,
                 qubits_view : bool = False
                 ):

        self.register_id = register_id
        self.qubits_number = qubits_number
        self.register_type = register_type
        self.default_qubit_value = default_qubit_value
        self.default_aplha_value = default_aplha_value
        self.default_beta_value = default_beta_value
        self.qubits_view = qubits_view
        
        if register_type == "main" :
            
        elif register_type == "temporary" :
            
        elif register_type == "other" :
            
        
        
        self.qubits = [CreateQubit(n, self.register_id, self.default_qubit_value, self.register_type, self.default_aplha_value, self.default_beta_value) for n in range(0, self.qubits_number)]

        return self.qubits
        
    def __str__(self):
        if self.qubits_view:
            return "\n".join(str(self.qubits[i]) for i in range(0, self.qubits_number))
        else: 
            return f"Quantum Register ID : {self.register_id}, Register type : {self.register_type}, Qubits Number : {self.qubits_number}"

class MainQuantumRegister(CreateQuantumRegister):
    def __init__(self, 
                 register_id: int,
                 qubits_number: int,
                 register_type : str = "main",
                 default_qubit_value: int = 0,
                 default_aplha_value: complex = 1+0j,
                 default_beta_value: complex = 0+0j,
                 qubits_view: bool = False
                 ):
        
        super().__init__(register_id, qubits_number, register_type, default_qubit_value, default_aplha_value, default_beta_value, qubits_view)

class TemporaryQuantumRegister(CreateQuantumRegister):
    def __init__(self, 
             register_id: int,
             qubits_number: int,
             register_type : str = "temporary",
             default_qubit_value: int = 0,
             default_aplha_value: complex = 1+0j,
             default_beta_value: complex = 0+0j,
             qubits_view: bool = False
             ):
    
        super().__init__(register_id, qubits_number, register_type, default_qubit_value, default_aplha_value, default_beta_value, qubits_view)

R0 = CreateQuantumRegister(0,5,"other",qubits_view=False)
print(R0)