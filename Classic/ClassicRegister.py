from Classic.Bit import CreateBit


class CreateClassicRegister:
    def __init__(self,
                 register_id: int,
                 bits_number: int,
                 register_type: str,
                 default_bit_value: int = 0,
                 bits_view: bool = False):

        self.register_id = register_id
        self.bits_number = bits_number
        self.register_type = register_type
        self.default_bit_value = default_bit_value
        self.bits_view = bits_view

        if register_type == "main":
            pass
        elif register_type == "temporary":
            pass
        elif register_type == "other":
            pass
        
        self.bits = [CreateBit(n, self.register_id, self.default_bit_value, self.register_type) 
                     for n in range(0, self.bits_number)]

    def __str__(self):
        if self.bits_view:
            return "\n".join(str(self.bits[i]) for i in range(0, self.bits_number))
        else:
            return f"Classic Register ID: {self.register_id}, Register Type: {self.register_type}, Bits Number: {self.bits_number}"


class MainClassicRegister(CreateClassicRegister):
    def __init__(self, 
                 register_id: int,
                 bits_number: int,
                 register_type: str = "main",
                 default_bit_value: int = 0,
                 bits_view: bool = False) -> None:
        super().__init__(register_id, bits_number, register_type, default_bit_value, bits_view)


class TemporaryClassicRegister(CreateClassicRegister):
    def __init__(self, 
                 register_id: int,
                 bits_number: int,
                 register_type: str = "temporary",
                 default_bit_value: int = 0,
                 bits_view: bool = False) -> None:
        super().__init__(register_id, bits_number, register_type, default_bit_value, bits_view)


