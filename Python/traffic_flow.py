import numpy as np
import matplotlib.pyplot as plt

X = 0.5
h = 0.01
x_step = int(np.floor(X/h))

T = 30
k = h * 0.5
t_step = int(np.floor(T/k))

U_0 = np.zeros((1, x_step))

'ferry problem'
#U_0[0, :int(np.floor(x_step/5))] = 0.99
'two step function'
#U_0[0, :int(np.floor(x_step/5))] = 0.99
#U_0[0, x_step - int(np.floor(x_step/5)):] = 1
'police problem'
U_0[0, int(np.floor(x_step/2))-5:int(np.floor(x_step/2))] = 0.6
U_0[0, :int(np.floor(x_step/2))-5] = 0.3
U_0[0, int(np.floor(x_step/2)):] = 0.3
'cos function'
#U_0[0, :16] = np.cos(10 * np.arange(0, 16*h, h))**2


'~~~~~ CELECT A METHOD ~~~~~'
#method = 'backward_Euler'
#method = 'one_side'
#method = 'Lax-Friedrichs'
method = 'Lax-Wendsdroff'

def f(x):
    return x * (1 - x**2)

def f_prime(x):
    return 1 - 3 * x**2

#def f(x):
#    return x

#def f_prime(x):
#    return 1

sol = U_0
velocity = np.zeros((1, x_step))
velocity[0, :] = f(U_0)
t = 0
while t < T:
    t += k
    print(t/T)
    U_n = np.zeros((x_step))
    for j in range(x_step):
        if j != x_step-1 and j != 0:
            p1 = j + 1
            m1 = j - 1
        elif j == 0:
            p1 = j + 1
            m1 = j
        else:
            p1 = j
            m1 = j - 1

        if method == 'backward_Euler':
            U_n[j] = sol[-1, j] - k/(2*h) * (f(sol[-1, p1]) - f(sol[-1, m1]))
        elif method == 'one_side':
            U_n[j] = sol[-1, j] - k/2 * (f(sol[-1, j]) - f(sol[-1, m1]))
        elif method == 'Lax-Friedrichs':
            U_n[j] = 1/2 * (sol[-1, m1] + sol[-1, p1]) - k/(2*h) * (f(sol[-1, p1]) - f(sol[-1, m1]))
        elif method == 'Lax-Wendsdroff':
            #U_n[j] = sol[-1, j] + k/(2*h) * ((2 * f(sol[-1, j]) - f(sol[-1, m1]) - f(sol[-1, p1])))
            U_n[j] = sol[-1, j] - k/(2*h) * (f(sol[-1, p1]) - f(sol[-1, m1])) + k**2/(2*h**2) * (
                f_prime((sol[-1, j] + sol[-1, p1])/2) * (f(sol[-1, p1]) - f(sol[-1, j]))
                - f_prime((sol[-1, j] + sol[-1, m1])/2) * (f(sol[-1, j]) - f(sol[-1, m1])))



    sol = np.vstack((sol, U_n))
    velocity = np.vstack((velocity, f(U_n)))

fig = plt.figure(figsize=(15, 5))
ax = plt.subplot()

for datapoint in np.linspace(0, T, 2):
    datapoint = int(np.floor(datapoint))
    data = sol[datapoint, :]
    velo = velocity[datapoint, :]
    x_mesh = np.arange(0, X, h)
    ax.plot(x_mesh, data)
    ax.plot(x_mesh, velo)

ax.set_ylim([0, 1])
plt.tight_layout()
plt.show()