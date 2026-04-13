# 🔦 Simulation de Propagation Laser & Effet Kerr Optique

Ce projet explore la dynamique de propagation d'un faisceau gaussien et introduit les phénomènes d'optique non linéaire à travers la simulation de l'effet Kerr.

---

## 🔗 Accès aux documents
* 📄 **Rapport d'étude :** [Simulation_Faisceau_Gaussien_Kerr.pdf](./Simulation_Faisceau_Gaussien_Kerr.pdf)
* 💻 **Code Source (Python) :** [script_propagation_laser.py](./script_propagation_laser.py)

---

## 📝 Description
[cite_start]L'objectif est de modéliser numériquement la propagation d'un laser dans l'approximation paraxiale et d'analyser qualitativement comment un milieu non linéaire modifie ses propriétés (auto-focalisation)[cite: 69, 72].

## 🔬 Concepts Physiques & Modélisation
* [cite_start]**Faisceau Gaussien :** Calcul de l'évolution du rayon $w(z)$ et de la distribution d'intensité $I(r,z)$ en fonction de la longueur de Rayleigh $z_R$[cite: 83, 91].
* [cite_start]**Effet Kerr Optique :** Modélisation de la variation de l'indice de réfraction $n = n_0 + n_2 I$ induite par l'intensité lumineuse[cite: 94].
* [cite_start]**Phénomènes Étudiés :** Diffraction en régime linéaire vs auto-focalisation en régime non linéaire[cite: 95, 139].

## 🛠 Méthodologie Numérique
* **Langage :** Python.
* [cite_start]**Algorithmes :** Utilisation de grilles spatiales 2D (`np.meshgrid`) pour simuler la cartographie d'intensité sur l'axe de propagation[cite: 98, 205].
* [cite_start]**Visualisation :** Génération de profils d'intensité (1D) et de cartes de propagation (2D) avec Matplotlib[cite: 119, 154].

## 📊 Résultats Clés
* [cite_start]Visualisation claire de la divergence naturelle du faisceau due à la diffraction[cite: 155].
* [cite_start]Mise en évidence de la réduction de la divergence sous l'influence de l'effet Kerr, illustrant les prémices de la formation de filaments lumineux[cite: 169, 181].

---
**Babacar NDIAYE** | *Master 2 Physique Appliquée – Nanophysique & Optique Avancée* | *Université du Mans* 
