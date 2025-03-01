class CreateQubit:
    def __init__(self,
                 qubit_id : int,
                 register_id : int,
                 value : int,
                 qubit_type : str,
                 alpha : complex = 1+0j,
                 beta : complex = 0+0j,
                 state : str = "created"
                 ):
        
        self.qubit_id = qubit_id
        self.register_id = register_id
        self.state = state
        self.value = value
        self.qubit_type = qubit_type
        self.alpha = alpha
        self.beta = beta
    
    def __str__(self):
        return f"Qubit ID: {self.qubit_id}, Register ID: {self.register_id}, State: {self.state}, Value: {self.value}, Qubit Type :{self.qubit_type}, Alpha: {self.alpha}, Beta: {self.beta}"





