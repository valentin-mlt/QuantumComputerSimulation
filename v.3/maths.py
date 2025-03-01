import mpmath
import matplotlib.pyplot as plt
import numpy as np

# Définition de la fonction zeta de Riemann avec mpmath
def zeta_function(x, y):
    # Utilisation de mpmath pour gérer les entrées complexes
    return mpmath.zeta(x + 1j * y)

# Définition de la fonction f(x, y) avec gestion du pôle en x = 1
def f(x, y):
    zeta_val = zeta_function(x, y)
    return 1 / (abs(zeta_val) + 1)

# Création du maillage de x et y dans le domaine (0, 1) x (0, 1)
x_vals = np.linspace(0, 1, 100)  # Valeurs de x dans [0, 1]
y_vals = np.linspace(0.001, 25, 100)  # Valeurs de y 
theta_vals = np.linspace(0, 2 * np.pi, 100)  # Ajout d'un point supplémentaire pour garantir la fermeture

# Création de la grille pour le tracé
X, Y = np.meshgrid(x_vals, y_vals)
Theta, Y_theta = np.meshgrid(theta_vals, y_vals)

# Calcul des valeurs de f(x, y) pour le rayon
R = np.zeros_like(X)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        R[i, j] = f(X[i, j], Y[i, j])

# Paramétrisation du cylindre
# x = f(x, y) * cos(theta)
# y = f(x, y) * sin(theta)
# Ici, R définit le rayon à chaque point, donc on utilise f(x, y) pour calculer la coordonnée radiale
X_cylinder = R * np.cos(Theta)  # La partie x est contrôlée par f(x, y)
Y_cylinder = R * np.sin(Theta)  # La partie y est également contrôlée par f(x, y)

# Tracé de la surface 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Affichage de la surface
ax.plot_surface(X_cylinder, Y_cylinder, Y, cmap='viridis')

# Modifier l'angle de vue pour regarder vers le haut
ax.view_init(elev=90, azim=-90)  # Vue verticale de haut (élévation à 90°, azimut à -90°)

# Ajouter des étiquettes et un titre
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title("Cylindre avec rayon défini par f(x, y) et symétrie autour de x=1/2")

plt.show()
