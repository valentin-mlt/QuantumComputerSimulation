class CreateBit:
    def __init__(self,
                 bit_id: int,
                 bit_register_id: int,
                 value: int,
                 bit_type: str) -> None:
        self.qubit_id = bit_id
        self.register_id = bit_register_id
        self.value = value
        self.qubit_type = bit_type
    
    def __str__(self):
        return f"Qubit ID: {self.qubit_id}, Register ID: {self.register_id}, Value: {self.value}, Qubit Type: {self.qubit_type}"
    
    def __add__(self, other):
        if isinstance(other, CreateBit):
            new_value = (self.value + other.value) % 2
            return CreateBit(self.qubit_id, self.register_id, new_value, self.qubit_type)
        else:
            raise TypeError("Les deux objets à additionner doivent être des instances de CreateBit.")


b_0 = CreateBit(0, 0, 1, "normal")
b_1 = CreateBit(1, 0, 1, "normal")

b_2 = b_0 + b_1
print(b_2)