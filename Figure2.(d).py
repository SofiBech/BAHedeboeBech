# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
alpha = 0.3
beta = 0.5
phi = 0.8
gamma = 0.45 
theta = 0.25
A = 1000000
delta = 0.025
psi_values = [0, 0.1 , 0.5, 1]

# Define the functions for Q and k_bar
def U(tau, psi):
    if psi == 0:
        k_bar = ((beta / (1 + beta) * (1 - tau) * (1 - alpha))**(1 / (1 - alpha)))
        c1_bar = (1 / (1 + beta)) * (1 - tau) * (1 - alpha) * k_bar ** alpha
        c2_bar = (beta / (1 + beta)) * (1 - tau) * (1 - alpha) * k_bar ** alpha * (1 + alpha * k_bar ** (alpha - 1) - delta)
        m_bar = 0
        Q_bar = (phi * tau * (1 - alpha) - gamma) * k_bar ** alpha / theta
        return np.log(c1_bar) + beta * np.log(c2_bar) - A * (1 + beta) * Q_bar ** 2 
    else:
        k_bar = ((beta / (1 + beta + psi) * (1 - tau) * (1 - alpha))**(1 / (1 - alpha)))
        c1_bar = (1 / (1 + beta + psi)) * (1 - tau) * (1 - alpha) * k_bar ** alpha
        c2_bar = (beta / (1 + beta + psi)) * (1 - tau) * (1 - alpha) * k_bar ** alpha * (1 + alpha * k_bar ** (alpha - 1) - delta)
        m_bar = (psi / (1 + beta + psi)) * (1 - tau) * (1 - alpha) * k_bar ** alpha
        Q_bar = ((phi * (tau + (psi / (1 + beta + psi)) * (1 - tau)) )* (1 - alpha) - gamma) * k_bar ** alpha / theta
        return np.log(c1_bar) + beta * np.log(c2_bar) - A * (1 + beta) * Q_bar ** 2 + psi * np.log(m_bar)

# Create an array of tau values
tau_values = np.linspace(0, 1, 100)

# Create a figure with a single subplot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot U for each psi value
for psi in psi_values:
    U_values = [U(tau, psi) for tau in tau_values]
    ax.plot(tau_values, U_values, label=f'psi = {psi}')

# Add legend and labels
ax.legend()
ax.set_xlabel('tau')
ax.set_ylabel('U')
ax.set_title(' ')

# Add grid lines
ax.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.5)

# Show the figure
plt.show()

