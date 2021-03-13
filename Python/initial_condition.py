import numpy as np

def get_initial(name, U=0, X=20, T=100, h=0.01):
    X = X
    h = h
    x_step = int(np.floor(X / h))

    T = T
    k = h * 0.5
    t_step = int(np.floor(T / k))

    U_0 = np.zeros((1, x_step))

    if name == 'ferry problem':
        U_0[0, :int(np.floor(x_step/4))] = 1
        U_0[0, 0] = 1
    elif name == 'traffic jam':
        U_0[0, int(np.floor(x_step/2)):] = 0.95
        U_0[0, :int(np.floor(x_step/2))] = 0.4
    elif name == 'two step function':
        U_0[0, :int(np.floor(x_step/5))] = 0.9
        U_0[0, x_step - int(np.floor(x_step/5)):] = 0.9
    elif name == 'police problem':
        U_0[0, int(np.floor(x_step/5)):int(np.floor(x_step/3))] = 0.5
        U_0[0, :int(np.floor(x_step/5))] = 0.15
        U_0[0, int(np.floor(x_step/3)):] = 0.15
    elif name == 'police problem 2':
        U_0[0, int(np.floor(x_step*4/5)):int(np.floor(x_step*20/21))] = 0.85
        U_0[0, :int(np.floor(x_step*4/5))] = 0.7
        U_0[0, int(np.floor(x_step*20/21)):] = 0.7
    elif name == 'police problem 3':
        police_length = int(np.floor(x_step)) - int(np.floor(x_step*1/4))
        U_0[0, int(np.floor(x_step*1/4)):int(np.floor(x_step))] = 0.7 + np.sin(np.linspace(0., np.pi, police_length))**1.5 * 0.125
        U_0[0, :int(np.floor(x_step*1/4))] = 0.7
        U_0[0, int(np.floor(x_step)):] = 0.7
    elif name == 'cos function':
        U_0[0, :160] = np.cos(1 * np.arange(0, 160*h, h))**2
    elif name == 'cos function 2':
        U_0[0, :] = 1 * np.cos(0.25 * np.arange(0, X, h)[0:x_step])**2
    elif name == 'selfmade':
        U_0[0, :] = U

    return X, h, x_step, T, k, t_step, U_0


def get_problemfunction(name, c=1):
    if name == 'traffic':
        def f(x):
            return x * (1 - x**2)
        def f_prime(x):
            return 1 - 3 * x**2
        def speed(x):
            return 1 - x ** 2
    elif name == 'linear':
        def f(x):
            return c * x
        def f_prime(x):
            return c
        speed = 0
    elif name=='Burger':
        def f(x):
            return x**2
        def f_prime(x):
            return 2 * x
        speed = 0
    elif name == 'Buckley-Leverett':
        def f(x):
            return x**2 / (x**2 + c * (1 - x**2))
        def f_prime(x):
            return 2 * c * x / ((c-1) * x**2 - c)**2
        speed = 0

    return f, f_prime, speed



















