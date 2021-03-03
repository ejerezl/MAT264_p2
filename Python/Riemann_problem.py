import numpy as np
import matplotlib.pyplot as plt
import plotter as plot

X = 0.5
h = 0.01
x_step = int(np.floor(X/h))

T = 50
k = h * 0.5
t_step = int(np.floor(T/k))

U_0 = np.zeros((1, x_step))

'ferry problem'
U_0[0, :int(np.floor(x_step/5))] = 1
U_0[0, 0] = 1
'two step function'
#U_0[0, :int(np.floor(x_step/5))] = 0.99
#U_0[0, x_step - int(np.floor(x_step/5)):] = 1
'police problem'
#U_0[0, int(np.floor(x_step/2))-5:int(np.floor(x_step/2))] = 0.9
#U_0[0, :int(np.floor(x_step/2))-5] = 0.3
#U_0[0, int(np.floor(x_step/2)):] = 0.3
'cos function'
#U_0[0, :16] = np.cos(10 * np.arange(0, 16*h, h))**2

a = 1

'~~~~~ CELECT A METHOD ~~~~~'
#method = 'backward_Euler'
#method = 'one_side'
#method = 'Lax-Friedrichs'
method = 'Lax-Wendsdroff'
#method = 'Beam-Warming'

sol = U_0
t = 0
while t < T:
    t += k
    print(t/T)
    U_n = np.zeros((x_step))
    for j in range(x_step):
        p1 = min(j+1, x_step-1)
        m2 = max(j - 2, 0)
        m1 = max(j - 1, 0)

        #if j != x_step - 1 and j != 0:
        #    p1 = j + 1
        #    m1 = j - 1
        #    m2 = j - 2
        #elif j == 0:
        #    p1 = j + 1
        #    m1 = j
        #    m2 = j
        #else:
        #    p1 = j
        #    m1 = j - 1
        #    m2 = max(j - 2, 0)

        if method == 'backward_Euler':
            U_n[j] = sol[-1, j] - k/(2*h) * a * (sol[-1, p1] - sol[-1, m1])
        elif method == 'one_side':
            U_n[j] = sol[-1, j] - k/2 * a * (sol[-1, j]) - (sol[-1, m1])
        elif method == 'Lax-Friedrichs':
            U_n[j] = 1/2 * (sol[-1, m1] + sol[-1, p1]) - k/(2*h) * a * (sol[-1, p1] - sol[-1, m1])
        elif method == 'Lax-Wendsdroff':
            U_n[j] = sol[-1, j] - k/(2*h) * a * (sol[-1, p1] - sol[-1, m1]) + k**2/(2*h**2) * a**2 * (sol[-1, p1] - 2 * sol[-1, j] + sol[-1, m1])
        elif method == 'Beam-Warming':
            U_n[j] = sol[-1, j] - k/(2*h) * a * (3 * sol[-1, j] - 4 * sol[-1, m1] + sol[-1, m2]) + k**2/(2*h**2) * a**2 * (sol[-1, j] - 2 * sol[-1, m1] + sol[-1, m2])


    sol = np.vstack((sol, U_n))

plot.plot_flow(sol, velocity, X, T, h)
