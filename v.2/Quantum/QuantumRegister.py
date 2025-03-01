from Quantum.Qubit import CreateQubit


class CreateQuantumRegister:
    def __init__(self,
                 register_id : int,
                 qubit_number
                 ) -> None:
        self.register_id = register_id
        self.__qubit_number = qubit_number
