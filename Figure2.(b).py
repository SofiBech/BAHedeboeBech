import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
alpha = 0.3
beta = 0.5
phi = 0.8
gamma = 0.45
theta = 0.25
A = 2
delta = 0.025
psi_values = [0, 0.5, 1, 1.5]

# Define the functions for Q and k_bar
def Q(tau, psi):
    if psi == 0:
        k_bar = ((beta / (1 + beta)) * (1 - tau) * (1 - alpha))**(1 / (1 - alpha))
        return (1 / theta) * (phi * tau * (1 - alpha) - gamma) * k_bar**alpha
    else:
        k_bar = ((beta / (1 + beta + psi) * (1 - tau) * (1 - alpha))**(1 / (1 - alpha)))
        return (1 / theta) * (phi *(tau + (psi / (1 + psi + beta)) * (1 - tau) * (1 - alpha)) - gamma) * k_bar**alpha 

# Create an array of tau values
tau_values = np.linspace(0, 1, 100)

# Create a figure with a single subplot
fig, ax = plt.subplots(figsize=(10, 8))

# Plot Q for each psi value
for psi in psi_values:
    Q_values = [Q(tau, psi) for tau in tau_values]
    ax.plot(tau_values, Q_values, label=f'psi = {psi}')

# Add legend and labels
ax.legend()
ax.set_xlabel('tau')
ax.set_ylabel('Q')
ax.set_title(' ')

# Show the figure
plt.show()
