import matplotlib.pyplot as plt
import numpy as np

# Paramètres du modèle
d = 0.2
p = 0.5
q = 0.8
b = (2*d)/q
m_E = 0.1
m_S = 0.5
h = p*m_S
k = (p/q)*m_S


# Conditions initiales
C_0 = 0
S_0 = m_S
E_0 = 1


# Fonctions pour calculer les valeurs au temps t+1
def C_t1(C_t, A_t):
    return (1-d)*C_t + b*min(1, 1-C_t)*A_t

def S_t1(S_t, C_t, A_t):
    return S_t + p*max(0,m_S-S_t) - h*C_t - k*A_t

def E_t1(E_t):
    return E_t-m_E

def psi_t1(C_t, S_t, E_t):
    return C_t - S_t - E_t

def V_t(psi):
    return min(1, max(psi, 0))

def A_t(V_t):
    return q*V_t

# Calcul des valeurs pour T étapes de temps
T = 100
C = np.zeros(T+1)
S = np.zeros(T+1)
E = np.zeros(T+1)
V = np.zeros(T)
psi = np.zeros(T)
A = np.zeros(T)

C[0] = C_0
S[0] = S_0
E[0] = E_0
psi[0] = C_0 - S_0 - E_0
V[0] = min(1,max(psi[0],1))
A[0] = A_t(V[0])

for t in range(T):
    psi[t] = psi_t1(C[t], S[t], E[t])
    V[t] = V_t(psi[t])
    A[t] = A_t(V[t])
    C[t+1] = C_t1(C[t], A[t])
    S[t+1] = S_t1(S[t], C[t], A[t])
    E[t+1] = E_t1(E[t])
  

# Tracé des graphes
t = np.arange(T+1)
t_1 = np.arange(T)

# Désir et self-controle
plt.plot(t, C, label='Désir')
plt.plot(t, S, label='Self-contrôle')
plt.legend()
plt.xlabel('Temps en semaines')
plt.ylabel('Valeurs')
plt.show()

# Influence sociétale et vulnérabilité
plt.plot(t, E, label='Influence sociétale')
plt.plot(t_1, V, label='Vulnérabilité')
plt.legend()
plt.xlabel('Temps en semaines')
plt.ylabel('Valeurs')
plt.show()


#plt.plot(t_1, A, label='Addiction exercée')

plt.plot(t_1, psi, label='psi')
plt.legend()
plt.xlabel('Temps en semaines')
plt.ylabel('Valeurs')
plt.show()
print(psi)
print(psi.size)
print(S.size)
print(E.size)
