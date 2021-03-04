import sys 
import numpy as np
import matplotlib.pyplot as plt


def v(b):
    return 1 - (b / 250) ** 2


def p(b):
    return b * v(b)


if len(sys.argv) < 3:
    print('You have to introduce the following arguments: 1) Type of traffic flow problem \
    2) Method you will use to solve it')
    exit()

#Time setups
dt = 5e-2
T = np.arange(0, 30, dt)

#Distance setups
dx = 1e-1
X = np.arange(0, 1e2, dx)

B = np.zeros((len(X),len(T)))

#First we choose the scenario
if sys.argv[1] == 'ferry':
    B[:len(X) // 2, 0] = 250
elif sys.argv[1] == 'police1': #Good road
    B[:, 0] = 25 * (0.45 * max(X) < X) * (X < .55 * max(X)) + 50
elif sys.argv[1] == 'police2': #Bad road
    B[:, 0] = 25 * (0.45 * max(X) < X) * (X < .55 * max(X)) + 175
else:
    print('Option not aviable')
    exit()

#Choose the method
if sys.argv[2] == 'left-sided':
    for i in range (1, len(T)):
        B[1:-1, i] = + B[1:-1, i - 1] + dt / dx * (p(B[:-2, i - 1]) - p(B[1:-1, i - 1]))
        #Start and end without changes
    B[0, i] = B[0, i - 1]
    B[-1, i] = B[-1, i - 1]
elif sys.argv[2] == 'right-sided':
    for i in range (1, len(T)):
        B[1:-1, i] = + B[1:-1, i - 1] + dt / dx * (p(B[1:-1, i - 1]) - p(B[2:, i - 1]))
        #Start and end without changes
    B[0, i] = B[0, i - 1]
    B[-1, i] = B[-1, i - 1]
elif sys.argv[2] == 'backward_Euler':
    print('askdn')
elif sys.argv[2] == 'Lax-Friedrich':
    for i in range(1, len(T)):
        B[1:-1, i] = .5 * (B[2:, i - 1] + B[:-2, i - 1]) - \
                    .5 * dt / dx * (p(B[2:, i - 1]) - p(B[:-2, i - 1]))

        #Start and end without changes
        B[0, i] = B[0, i - 1]
        B[-1, i] = B[-1, i - 1]
elif sys.argv[2] == 'Lax-Wendsdroff':
    print('lasd')
else:
    print('Method not implemented')

# Change t to change time
t = 100
plt.plot(X, B[:, t])
plt.xlabel('Distance (km)')
plt.ylabel('Cars per km')
plt.savefig('plot.png')