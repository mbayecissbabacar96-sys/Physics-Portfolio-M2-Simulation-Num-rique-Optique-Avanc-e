# 🔦 Gaussian Beam Optics & Nonlinear Effects Simulation

[cite_start]This project focuses on the numerical simulation of Gaussian laser beam propagation and the study of nonlinear optical phenomena, specifically the **Kerr effect**[cite: 1, 8].

[cite_start]The objective is to model how a high-intensity laser beam interacts with a medium, leading to **self-focusing**—a fundamental concept for advanced spectroscopy techniques such as CARS[cite: 8, 31, 105, 106].

---

## 🔗 Project Resources
* 📄 **Scientific Report:** [Simulation_Faisceau_Gaussien_Kerr.pdf](./Simulation_de_la_propagation_d_un_faisceau_gaussien_et_introduction_à_l_effet_Kerr_optique.pdf)
* 💻 **Python Code:** [script_propagation_laser.py](./script_propagation_laser.py)

---

## 🔬 Physical Model & Methodology

### 1. Gaussian Beam Propagation
[cite_start]We model the beam intensity distribution $I(r,z)$ and the evolution of the beam radius $w(z)$ using the paraxial approximation[cite: 5, 19, 27]:
* [cite_start]**Rayleigh Length ($z_R$):** Defining the distance over which the beam remains focused[cite: 23, 27].
* **Beam Waist ($w_0$):** Initial focal point parameters[cite: 18, 27].

### 2. Nonlinear Kerr Effect
[cite_start]In high-intensity regimes, the refractive index becomes power-dependent: $n = n_0 + n_2 I$[cite: 6, 26, 30].
This simulation demonstrates:
* [cite_start]**Linear Regime:** Natural beam divergence due to diffraction[cite: 75, 91, 114].
* **Nonlinear Regime:** Self-focusing effect where the medium acts as a converging lens, significantly reducing divergence[cite: 31, 105, 115, 117].

---

## 📊 Numerical Results
The simulation generates 5 key figures to validate the model:
1. **Beam Profile:** Intensity distribution at the waist[cite: 55].
2. **Radius Evolution:** Plot of $w(z)$ showing natural diffraction[cite: 73].
3. **2D Propagation Map:** Visualizing the beam spread in the linear regime[cite: 90].
4. **Kerr Effect Map:** Intensity map showing modified propagation paths[cite: 104].
5. **Direct Comparison:** A side-by-side plot of $w(z)$ with and without the Kerr effect, proving the **auto-focalisation** phenomenon.

---

## 🛠️ Skills Demonstrated
* [cite_start]**Optical Physics:** Laser dynamics and nonlinear optics modeling[cite: 119].
* [cite_start]**Scientific Computing:** Developing numerical simulations with Python (NumPy, Matplotlib)[cite: 120, 128, 129].
* **Data Visualization:** Creating 2D intensity maps and comparative physical plots.
* [cite_start]**Research Readiness:** This work serves as a solid foundation for studying complex systems like fiber optics or ultrafast spectroscopy[cite: 121, 126].

---
**Babacar NDIAYE** | *Master 2 Applied Physics – Nanophysics & Advanced Optics* | *Université du Mans*
