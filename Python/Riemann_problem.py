import numpy as np
import matplotlib.pyplot as plt

X = 0.5
h = 0.01
x_step = int(np.floor(X/h))

T = 50
k = h * 0.5
t_step = int(np.floor(T/k))

U_0 = np.zeros((1, x_step))
U_0[0, :int(np.floor(x_step/4))] = 1

a = 1

'~~~~~ CELECT A METHOD ~~~~~'
#method = 'backward_Euler'
#method = 'one_side'
method = 'Lax-Friedrichs'
#method = 'Lax-Wendsdroff'
#method = 'Beam-Warming'

sol = U_0
t = 0
while t < T:
    t += k
    print(t/T)
    U_n = np.zeros((x_step))
    for j in range(x_step-1):
        if j != x_step-1:
            p1 = j + 1
            m1 = j - 1
            m2 = j - 2
        else:
            p1 = 0
            m1 = j - 1
            m2 = j - 2

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

fig = plt.figure(figsize=(15, 5))
ax = plt.subplot()

for datapoint in np.linspace(0, T, 5):
    datapoint = int(np.floor(datapoint))
    data = sol[datapoint, :]
    x_mesh = np.arange(0, X, h)
    ax.plot(x_mesh, data)

plt.tight_layout()
plt.show()