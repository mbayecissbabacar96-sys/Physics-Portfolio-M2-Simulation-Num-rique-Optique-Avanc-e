# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 17:29:03 2026

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt

# Paramètres physiques
w0 = 1e-3
lambda0 = 633e-9
zR = np.pi * w0**2 / lambda0
I0 = 1

# Grilles
r = np.linspace(-3e-3, 3e-3, 200)
z = np.linspace(-0.05, 0.05, 200)

R, Z = np.meshgrid(r, z)

# Rayon du faisceau
def w(z):
    return w0 * np.sqrt(1 + (z / zR)**2)

# Intensité
def intensity(r, z):
    return I0 * (w0 / w(z))**2 * np.exp(-2 * r**2 / w(z)**2)

# Calcul
I = intensity(R, Z)

# FIGURE 1
plt.figure()
plt.plot(r, intensity(r, 0))
plt.title("Profil du faisceau au waist")
plt.xlabel("r (m)")
plt.ylabel("Intensité")
plt.grid()

# FIGURE 2
plt.figure()
plt.plot(z, w(z))
plt.title("Évolution du rayon w(z)")
plt.xlabel("z (m)")
plt.ylabel("Rayon")

# FIGURE 3
plt.figure()
plt.imshow(I, extent=[r.min(), r.max(), z.min(), z.max()], aspect='auto')
plt.title("Propagation du faisceau")
plt.xlabel("r")
plt.ylabel("z")
plt.colorbar()

# Effet Kerr simplifié
n2 = 1e-20
I_kerr = I * (1 + n2 * I)

# FIGURE 4
plt.figure()
plt.imshow(I_kerr, extent=[r.min(), r.max(), z.min(), z.max()], aspect='auto')
plt.title("Propagation avec effet Kerr")

plt.show()