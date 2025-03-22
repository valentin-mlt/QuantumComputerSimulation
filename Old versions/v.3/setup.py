from setuptools import setup, find_packages

setup(
    name="QuantumComputerSimulation",
    version="1.0",
    packages=find_packages(),
    install_requires=[],  # Ajoute ici des dépendances si nécessaire
    entry_points={
        "console_scripts": [
            "quantum-computer = QuantumComputer.QuantumComputer:main",
        ],
    },
)
