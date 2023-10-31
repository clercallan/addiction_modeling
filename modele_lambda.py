import matplotlib.pyplot as plt
import numpy as np

# Paramètres du modèle
d = 0.2
p = 0.2
q = 0.8
b = (2*d)/q
m_E = 0.2
m_S = 0.5
h = p*m_S
k = (p/q)*m_S
lambda_t0= 0.2
lambda_m=0.001
Rm=7

# Conditions initiales
C_0 = 1
S_0 = m_S
E_0 = 0.5


# Fonctions pour calculer les valeurs au temps t+1
def C_t1(C_t, A_t):
    return (1-d)*C_t + b*min(1, 1-C_t)*A_t

def S_t1(S_t, C_t, A_t):
    return S_t + p*max(0,m_S-S_t) - h*C_t - k*A_t

def E_t1(E_t,t):
    if t%6==0:
        return E_0
    return E_t-m_E

def psi_t1(C_t, S_t, E_t):
    return C_t - S_t - E_t

def V_t(psi):
    return min(1, max(psi, 0))

def A_t(Vt,lambdat,t):
    O_t1 = O_t(Vt, lambdat)
    O[t] = O_t1
    return q*Vt+O_t1

def O_t(Vt, lambdat) :
    return (R(lambdat)/Rm)*q*(1-Vt)

def lambda_t1(lambda_t):
    return lambda_t + lambda_m

def R(lambda_t):
    return np.random.poisson(lambda_t)
# Calcul des valeurs pour T étapes de temps
T = 20
C = np.zeros(T+1)
S = np.zeros(T+1)
E = np.zeros(T+1)
O = np.zeros(T+1)
V = np.zeros(T)
psi = np.zeros(T)
A = np.zeros(T)
lambda_t=np.zeros(T+1)


lambda_t[0] = lambda_t0
# R[0] = R_t1(lambda_t0)
C[0] = C_0
S[0] = S_0
E[0] = E_0
psi[0] = C_0 - S_0 - E_0
V[0] = min(1,max(psi[0],1))
A[0] = A_t(V[0],lambda_t[0], 0)

for t in range(T):
    psi[t] = psi_t1(C[t], S[t], E[t])
    V[t] = V_t(psi[t])
    A[t] = A_t(V[t],lambda_t[t],t)
    C[t+1] = C_t1(C[t], A[t])
    S[t+1] = S_t1(S[t], C[t], A[t])
    E[t+1] = E_t1(E[t],t)
    lambda_t[t+1]=lambda_t1(lambda_t[t])
   
  

# Tracé des graphes
t = np.arange(T+1)
t_1 = np.arange(T)
plt.plot(t_1, V, label='Vulnérabilité', linewidth=1, color='red')
#plt.plot(t, O, label='Occasions sociales')
plt.plot(t, C, label='Désir')
plt.plot(t, S, label='Self-contrôle', color='blue')
plt.plot(t, E, label='Influence sociétale')
plt.plot(t_1, A, label='Addiction exercée', linestyle='dashed', linewidth=1)
# plt.plot(t_1, psi, label='psi')
plt.legend()
plt.xlabel('Temps en semaines')
plt.ylabel('Valeurs')
plt.show()
