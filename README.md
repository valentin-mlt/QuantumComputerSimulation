from qc.utils.logging import get_logger
from qc.core.computer import settings

log = get_logger("Qubit creation")


class CreateQubit:
    def __new__(cls, type: str = "main", data_type: str = "preconfigured", data: dict = {}):
        if data_type not in ["preconfigured", "personalized"]:
            raise ValueError(
                f"Invalid mode '{data_type}'. Allowed values are 'preconfigured' or 'personalized'."
            )
        instance = super().__new__(cls)
        return instance

    def __init__(self, type: str = "main", data_type: str = "preconfigured", data: dict = {}):
        self.data_type = data_type
        
        if data_type == "preconfigured":
            qubit_config = settings["qubit_config"]

            if type == "main":
                config = qubit_config["main_qubit"]
            elif type == "temporary":
                config = qubit_config["temporary_qubit"]
            elif type == "other":
                config = qubit_config["other_qubit"]
            else:
                raise ValueError(
                    f"Invalid qubit type '{type}'. Allowed values are 'main', 'temporary', or 'other'."
                )
            
            # Appliquer la configuration par défaut
            self.qubit_type = config["qubit_type"]
            self.qubit_value = config["qubit_value"]
            self.alpha_value = config["alpha_value"]
            self.beta_value = config["beta_value"]
            self.state = config["state"]

            log.info(f"Qubit created in preconfigured mode with type '{self.qubit_type}'.")
        
        elif data_type == "personalized":
            expected_keys = {"qubit_type", "qubit_value", "alpha_value", "beta_value", "state"}
            if not expected_keys.issubset(data.keys()):
                missing = expected_keys - data.keys()
                raise ValueError(f"Missing keys in personalized data: {missing}")
            
            self.qubit_type = data["qubit_type"]
            self.qubit_value = data["qubit_value"]
            self.alpha_value = data["alpha_value"]
            self.beta_value = data["beta_value"]
            self.state = data["state"]

            log.info(f"Qubit created in personalized mode with custom configuration.")

        else:
            raise ValueError(f"Invalid data_type '{data_type}'. Should be 'preconfigured' or 'personalized'.")

    def __str__(self):
        return (f"Qubit(type={self.qubit_type}, value={self.qubit_value}, "
                f"alpha={self.alpha_value}, beta={self.beta_value}, state='{self.state}')")

    def __repr__(self):
        return (f"CreateQubit(qubit_type={self.qubit_type!r}, qubit_value={self.qubit_value!r}, "
                f"alpha_value={self.alpha_value!r}, beta_value={self.beta_value!r}, state={self.state!r})")
