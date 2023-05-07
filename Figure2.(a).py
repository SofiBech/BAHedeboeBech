#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 12:34:56 2023

@author: carolinehedeboe
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"

# Define the parameters
alpha = 0.3
beta = 0.5
phi = 0.8
gamma = 0.45
theta = 0.25
A = 2
delta = 0.025
psi_values = [0, 0.1, 0.5, 1]

# Define the functions for Q and k_bar
def m(tau, psi):
    if psi == 0:
        k_bar = ((beta / (1 + beta) * (1 - tau) * (1 - alpha))**(1 / (1 - alpha)))
        return 0
    else:
        k_bar = ((beta / (1 + beta + psi) * (1 - tau) * (1 - alpha))**(1 / (1 - alpha)))
        return (psi / (1 + beta + psi)) * (1 - tau) * (1 - alpha) * k_bar ** alpha

# Create an array of tau values
tau_values = np.linspace(0, 1, 100)

# Create a figure with a single subplot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot U for each psi value
for psi in psi_values:
    m_values = [m(tau, psi) for tau in tau_values]
    ax.plot(tau_values, m_values, label=r'$\psi$ = {}'.format(psi))

# Add legend and labels
ax.set_xlabel('Tax rate, \u03C4', fontsize=20)
ax.set_ylabel(r'Steady state mitigation, $\mathrm{\bar{m}}$', fontsize=20)
ax.tick_params(axis='both', which='major', labelsize=20)
ax.legend(fontsize=20, frameon=True)

# Add grid lines
ax.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.5)

# Show the figure
plt.show()
