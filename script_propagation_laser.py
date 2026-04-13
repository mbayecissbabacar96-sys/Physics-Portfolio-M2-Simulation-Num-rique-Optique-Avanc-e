# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 18:38:24 2026

@author: PC
"""

import numpy as np
import matplotlib.pyplot as plt

# =========================
# Paramètres physiques
# =========================
w0 = 1e-3
lambda0 = 633e-9
zR = np.pi * w0**2 / lambda0
I0 = 1

# Effet Kerr
n2 = 1e-20

# =========================
# Grilles
# =========================
r = np.linspace(-3e-3, 3e-3, 300)
z = np.linspace(-0.05, 0.05, 300)
R, Z = np.meshgrid(r, z)

# =========================
# Fonctions
# =========================
def w(z):
    return w0 * np.sqrt(1 + (z / zR)**2)

def intensity(r, z):
    return I0 * (w0 / w(z))**2 * np.exp(-2 * r**2 / w(z)**2)

# =========================
# Calculs
# =========================
I_linear = intensity(R, Z)

# Effet Kerr simplifié
I_kerr = I_linear * (1 + n2 * I_linear)

# =========================
# FIGURE 1
# =========================
plt.figure()
plt.plot(r, intensity(r, 0))
plt.title("Figure 1 : Profil du faisceau au waist")
plt.xlabel("r (m)")
plt.ylabel("Intensité")
plt.grid()
plt.savefig("fig1_profile.png")

# =========================
# FIGURE 2
# =========================
plt.figure()
plt.plot(z, w(z))
plt.title("Figure 2 : Évolution du rayon w(z)")
plt.xlabel("z (m)")
plt.ylabel("Rayon")
plt.savefig("fig2_wz.png")

# =========================
# FIGURE 3
# =========================
plt.figure()
plt.imshow(I_linear, extent=[r.min(), r.max(), z.min(), z.max()], aspect='auto')
plt.title("Figure 3 : Propagation du faisceau")
plt.xlabel("r")
plt.ylabel("z")
plt.colorbar()
plt.savefig("fig3_propagation.png")

# =========================
# FIGURE 4
# =========================
plt.figure()
plt.imshow(I_kerr, extent=[r.min(), r.max(), z.min(), z.max()], aspect='auto')
plt.title("Figure 4 : Propagation avec effet Kerr")
plt.xlabel("r")
plt.ylabel("z")
plt.colorbar()
plt.savefig("fig4_kerr.png")

# =========================
# FIGURE 5 (comparaison)
# =========================
plt.figure()
plt.plot(z, w(z), label="Sans Kerr")
plt.plot(z, w(z)/(1 + 0.1*np.exp(-z**2/zR**2)), label="Avec Kerr")
plt.legend()
plt.title("Figure 5 : Comparaison avec/sans effet Kerr")
plt.xlabel("z")
plt.ylabel("Rayon")
plt.savefig("fig5_comparison.png")

plt.show()
