def create_qubit_config(qubit_type="default", value=0, alpha=1+0j, beta=0+0j, state="uncreated"):
    return {
        "type": qubit_type,
        "value": value,
        "alpha": alpha,
        "beta": beta,
        "state": state,
    }

def set_quantum_config():
    pass

def create_quantum_register_config(qubits_number=10, qubit_config=None):
    if qubit_config is None:
        qubit_config = create_qubit_config()
    return {
        key: {**qubit_config, "qubits_number": qubits_number, "detailed_view": False}
        for key in ["main", "temporary", "other"]
    }

default_qubit_config = {key: create_qubit_config() for key in ["main", "temporary", "other"]}
default_quantum_register_config = create_quantum_register_config(qubit_config=create_qubit_config())

print(default_qubit_config)
print("")
print(default_quantum_register_config)

default_quantum_computer_config = {
    "quantum_registers_type_presence" : {
        "main" : 1,
        "temporary" : 1,
        "other" : 0
    },
    "quantum_computer_state": "idle",
    "quantum_computer_name": "QuantumSimV4",
    "quantum_computer_version": "4.0",
    "quantum_computer_description": "A simulation of a quantum computer with configurable registers and qubits."
}

# Additional configurations for quantum gates
default_quantum_gates_config = {
    "supported_gates": ["X", "Y", "Z", "H", "S", "T", "CNOT", "SWAP"],
    "gate_parameters": {
        "X": {"description": "Pauli-X gate"},
        "Y": {"description": "Pauli-Y gate"},
        "Z": {"description": "Pauli-Z gate"},
        "H": {"description": "Hadamard gate"},
        "S": {"description": "Phase gate"},
        "T": {"description": "T gate"},
        "CNOT": {"description": "Controlled-NOT gate"},
        "SWAP": {"description": "SWAP gate"}
    }
}

# Combine all configurations into a single dictionary
quantum_computer_simulation_config = {
    "qubit_config": default_qubit_config,
    "quantum_register_config": default_quantum_register_config,
    "quantum_computer_config": default_quantum_computer_config,
    "quantum_gates_config": default_quantum_gates_config
}
