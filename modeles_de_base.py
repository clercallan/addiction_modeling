import numpy as np
import matplotlib.pyplot as plt

# C
def desire(c, a, d=0.1, b=0.2):
    return (1 - d) * c + b * min(1, 1 - c) * a


# S
def self_control(s, c, a, Sm, p=0.1, h=0.2, k=0.3):
    return s - h * c + p*max(0, Sm - s) - k * a

# E
def societal_influence(e, m_e=0.1):
    return e - m_e

# A
def addiction(v, q=0.5):
    return q * v

# V
def vulnerability(c, s, e):
    psi = c - s - e
    return min(1, max(psi, 0))

# Paramètres du modèle
d = 0.2
p = 0.3
q = 0.8
b = 2*d/q
m_E = 0.01
m_S = 0.5
h = p*m_S
k = (p/q)*m_S

# Initial values
c = [0]
s = [0.5]
e = [1]
a = [0]
v = [0]

iterations = 50

results = []

for t in range(iterations):
    c.append(desire(c[-1], a[-1], d, b))
    s.append(self_control(s[-1], c[-1], a[-1], m_S, p, h, k))
    e.append(societal_influence(e[-1], m_E))
    v.append(vulnerability(c[-1], s[-1], e[-1]))
    a.append(addiction(v[-1], q))

    

# Plotting the results
labels = ['C (Désir)', 'S (Self-contrôle)', 'E (Influence sociétale)', 'A (Addiction exercée)', 'V (Vulnérabilité)']
colors = ['b', 'g', 'c', 'm', 'r']
courbes = [c, s, e, a, v]

#plt.plot(range(0, iterations + 1), courbes[1], label=labels[1])
#plt.plot(range(0, iterations + 1), courbes[4], label=labels[4])

for i in range(5):
    plt.plot(range(0, iterations + 1), courbes[i], label=labels[i], color=colors[i])

plt.xlabel('Semaines')
plt.ylabel('Valeurs')
plt.title('Graphiques des fonctions')
plt.legend()
plt.show()
