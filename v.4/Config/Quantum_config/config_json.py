
# import json
# import os


# config_path = os.path.join(os.path.dirname(__file__), 'config.json')
# with open(config_path, 'r') as f:
#     config = json.load(f)

# # Fonction utilitaire pour reconstruire un nombre complexe depuis sa représentation JSON
# def json_to_complex(comp_dict):
#     # On attend un dictionnaire avec les clés "real" et "imag"
#     try:
#         return complex(comp_dict["real"], comp_dict["imag"])
#     except (KeyError, TypeError):
#         raise ValueError("La représentation du nombre complexe est invalide.")

# class CreateQubit:
#     def __new__(cls, qubit_id, qubit_register_id, value, qubit_type=None,
#                 alpha=None, beta=None, state=None):
#         # Vérifier que qubit_register_id est un entier dans l'intervalle [0, MAX_QUANTUM_REGISTER_ID]
#         if not isinstance(qubit_register_id, int):
#             raise TypeError(f"Le qubit register ID doit être un entier entre 0 et {MAX_QUANTUM_REGISTER_ID}.")
#         if not (0 <= qubit_register_id <= MAX_QUANTUM_REGISTER_ID):
#             raise ValueError(f"Le qubit register ID doit être compris entre 0 et {MAX_QUANTUM_REGISTER_ID}.")
        
#         # Vérifier que value est 0 ou 1
#         if value not in (0, 1):
#             raise ValueError("La valeur du qubit doit être 0 ou 1.")
        
#         # Si aucun qubit_type n'est fourni, utiliser la valeur par défaut
#         if qubit_type is None:
#             qubit_type = DEFAULT_QUBIT_CONFIG.get("qubit_type", "default")
        
#         # Si alpha ou beta ne sont pas fournis, utiliser les valeurs par défaut
#         if alpha is None:
#             alpha = json_to_complex(DEFAULT_QUBIT_CONFIG.get("alpha", {"real":1.0, "imag":0.0}))
#         if beta is None:
#             beta = json_to_complex(DEFAULT_QUBIT_CONFIG.get("beta", {"real":0.0, "imag":0.0}))
        
#         # Vérifier que alpha et beta sont bien des nombres complexes
#         if not isinstance(alpha, complex):
#             raise TypeError("alpha doit être un nombre complexe.")
#         if not isinstance(beta, complex):
#             raise TypeError("beta doit être un nombre complexe.")
        
#         # Si aucun état n'est fourni, utiliser la valeur par défaut
#         if state is None:
#             state = DEFAULT_QUBIT_CONFIG.get("state", "created")
        
#         # Toutes les validations passées, on crée l'instance
#         return super().__new__(cls)

#     def __init__(self, qubit_id, qubit_register_id, value, qubit_type=None,
#                  alpha=None, beta=None, state=None):
#         # Utiliser les mêmes valeurs que dans __new__
#         if qubit_type is None:
#             qubit_type = DEFAULT_QUBIT_CONFIG.get("qubit_type", "default")
#         if alpha is None:
#             alpha = json_to_complex(DEFAULT_QUBIT_CONFIG.get("alpha", {"real":1.0, "imag":0.0}))
#         if beta is None:
#             beta = json_to_complex(DEFAULT_QUBIT_CONFIG.get("beta", {"real":0.0, "imag":0.0}))
#         if state is None:
#             state = DEFAULT_QUBIT_CONFIG.get("state", "created")
        
#         self.qubit_id = qubit_id
#         self.qubit_register_id = qubit_register_id
#         self.value = value
#         self.qubit_type = qubit_type
#         self.alpha = alpha
#         self.beta = beta
#         self.state = state

#     def __repr__(self):
#         return (f"CreateQubit(qubit_id={self.qubit_id}, qubit_register_id={self.qubit_register_id}, "
#                 f"value={self.value}, qubit_type='{self.qubit_type}', alpha={self.alpha}, beta={self.beta}, "
#                 f"state='{self.state}')")


# # Exemple d'utilisation
# if __name__ == "__main__":
#     try:
#         # Cas correct : en utilisant certains paramètres par défaut définis dans le fichier JSON
#         qubit = CreateQubit("q1", 10, 1)
#         print("Qubit créé :", qubit)
        
#         # Cas incorrect : qubit_register_id hors de l'intervalle
#         qubit_err = CreateQubit("q2", 50, 0)
#     except Exception as e:
#         print("Erreur lors de la création du qubit :", e)
