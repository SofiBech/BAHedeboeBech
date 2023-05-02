# -*- coding: utf-8 -*-

import math

# Parameter values
tau = 0
alpha = 0.3
psi = 1
beta = 0.5
phi = 0.8
gamma = 0.45
theta = 0.25
A = 0.8
delta = 0.1

# Calculating steady state values
if psi == 0:
    k_bar = ((beta / (1 + beta)) * (1 - tau) * (1 - alpha))**(1 / (1 - alpha))
    c1_bar = (1 / (1 + beta)) * (1 - tau) * (1 - alpha) * k_bar**alpha
    c2_bar = (beta / (1 + beta)) * (1 - tau) * (1 - alpha) * k_bar**alpha * (1 + alpha * k_bar**(alpha - 1) - delta)
    m_bar = 0
    Q_bar = (1 / theta) * (phi * tau * (1 - alpha) - gamma) * k_bar**alpha 
    U_bar = math.log(c1_bar) + beta * math.log(c2_bar) - A * (1 + beta) * Q_bar**2
    M_bar = m_bar + tau*(1 - alpha) * k_bar**alpha
    skat = tau*(1 - alpha) * k_bar**alpha
else:
    k_bar = ((beta / (1 + beta + psi)) * (1 - tau) * (1 - alpha))**(1 / (1 - alpha))
    c1_bar = (1 / (1 + beta + psi)) * (1 - tau) * (1 - alpha) * k_bar**alpha
    c2_bar = (beta / (1 + beta + psi)) * (1 - tau) * (1 - alpha) * k_bar**alpha * (1 + alpha * k_bar**(alpha - 1) - delta)
    m_bar = (psi / (1 + beta + psi)) * (1 - tau) * (1 - alpha) * k_bar**alpha
    Q_bar = (1 / theta) * (phi *(tau + (psi / (1 + psi + beta)) * (1 - tau) * (1 - alpha)) - gamma) * k_bar**alpha 
    U_bar = math.log(c1_bar) + beta * math.log(c2_bar) - A * (1 + beta) * Q_bar**2 + psi * math.log(m_bar)
    M_bar = m_bar + tau*(1 - alpha) * k_bar**alpha
    skat = tau*(1 - alpha) * k_bar**alpha

# Printing steady state values
print(f'Steady state values:')
print(f'k_bar = {k_bar:.4f}')
print(f'c1_bar = {c1_bar:.4f}')
print(f'c2_bar = {c2_bar:.4f}')
print(f'm_bar = {m_bar:.4f}')
print(f'Q_bar = {Q_bar:.4f}')
print(f'U_bar = {U_bar:.4f}')
print(f'M_bar = {M_bar:.4f}')
print(f'skat = {skat:.4f}')



# BA-HedeboeBech
