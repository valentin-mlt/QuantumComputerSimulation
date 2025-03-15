


class CreateQubit:
    def __new__(cls, quantum_computer_config, qubit_id, qubit_register_id, value, qubit_type="default", alpha=1+0j, beta=0+0j, state="created"):
        
        if config is None or config == {}:
            config = {
                "max_qubit_id": 45
            }
        
        if not isinstance(qubit_register_id, int):
            raise TypeError(f"The qubit register ID must be an integer between 0 and {config['max_qubit_id']}")

        if not isinstance(qubit_register_id, int):
            raise TypeError(f"The qubit register ID must be an integer between 0 and{config['']}")
        
        if not (0 <= qubit_register_id <= 45):
            raise ValueError("qubit_register_id doit être compris entre 0 et 45.")
        
        if value not in (None, 0, 1):
            raise ValueError("value doit être 0 ou 1.")

        if not isinstance(alpha, complex):
            raise TypeError("alpha doit être un nombre complexe.")
        
        if not isinstance(beta, complex):
            raise TypeError("beta doit être un nombre complexe.")

        # Ici, on peut également ajouter d'autres validations si nécessaire

        # instance = super().__new__(cls) | return instance
        return super().__new__(cls)

    def __init__(self, qubit_id, qubit_register_id, value, qubit_type="default",
                 alpha=1+0j, beta=0+0j, state="created") -> None:
        self.qubit_id = qubit_id
        self.qubit_register_id = qubit_register_id
        self.value = value
        self.qubit_type = qubit_type
        self.alpha = alpha
        self.beta = beta
        self.state = state

# Exemple d'utilisation
try:
    # Cas correct
    q1 = CreateQubit("q1", 10, 1)
    print("q1 créé avec succès.")
    
    # Cas incorrect : qubit_register_id hors de l'intervalle
    q2 = CreateQubit("q2", 50, 0)
except Exception as e:
    print(f"Erreur lors de la création du qubit : {e}")













    @classmethod
    def create_qubit(cls, qubit_id, qubit_register_id, value, qubit_type):
        if value not in [0, 1]:
            raise ValueError("Value must be 0 or 1")
        return cls(qubit_id, qubit_register_id, value, qubit_type)

    def __str__(self):
        return f"Qubit ID: {self.qubit_id}, Register ID: {self.qubit_register_id}, Value: {self.value}, Type: {self.qubit_type}"
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

qubit1 = CreateQubit(1, 0, 0, "data")
print(qubit1)



























class Gates:
    def __init__(self, qubit: CreateQubit) -> None:
        self.qubit = qubit
    
    def apply_gate(self):
        print(f"Application de la porte au Qubit {self.qubit.qubit_id}")
        self.qubit.alpha = self.qubit.alpha + 0.5j
        self.qubit.beta = self.qubit.beta - 0.5j

    def __str__(self):
        return f"Porte appliquée au qubit ID: {self.qubit.qubit_id}"


gate = Gates(qubit1)
gate.apply_gate()
print(gate)



























"""
                 alpha : complex = 1+0j,
                 beta : complex = 0+0j,
                 state : str = "created"
"""