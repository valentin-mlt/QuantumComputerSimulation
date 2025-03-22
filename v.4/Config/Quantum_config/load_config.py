import json

# print("Loading configuration...")
with open("config.json", "r") as file:
    config = json.load(file)

qubit_config = config.get("qubit_config", {})
quantum_register_config = config.get("quantum_register_config", {})
quantum_computer_config = config.get("quantum_computer_config", {})

for qubit_type in ["main_qubit", "temporary_qubit", "other_qubit"]:
    for key in ["alpha_value", "beta_value"]:
        if qubit_type in qubit_config and key in qubit_config[qubit_type]:
            real, imag = qubit_config[qubit_type][key]
            qubit_config[qubit_type][key] = complex(real, imag)

# print("Configuration loaded")

