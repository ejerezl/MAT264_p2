import numpy as np

def solve_problem(method, U_0, X, T, h, k, x_step, t_step, f, f_prime):
    sol = np.zeros((t_step, x_step))
    sol[0, :] = U_0
    t = 0
    for n in range(1, t_step):
        t += k
        #print(t / T)

        if method == 'Lax-Friedrichs':
            sol = Lax_Friedrich_update(sol, k, h, n, f)
        elif method == 'Lax-Wendsdroff':
            sol = Lax_Wendrof_update(sol, k, h, n, f, f_prime)
        elif method == 'Lax-Wendsdroff from lecture':
            sol = Lax_Wendrof_lecture_update(sol, k, h, n, f)
        elif method == 'left sided':
            sol = left_sided(sol, k, h, n, f)
        elif method == 'right sided':
            sol = right_sided(sol, k, h, n, f)
        elif method == 'Godunov':
            sol = Godunov(sol, k, h, n, f, f_prime, U_0)

    return sol

def get_true_linear_sol(U_0, datapoint, h, k, c):
    '''
    gives the true solution to a specific time
    :param U_0: initial condition
    :param datapoint: timestep to which you want to know the real solution (current time / k)
    :param h: step size in location
    :param k: step size in time
    :param c: constant
    :return: true solution of the linear problem
    '''
    datapoint_raw = datapoint * k
    n = len(U_0[0, :])

    shift = int(np.floor(c * datapoint_raw / h))
    left_bound = min(max(0 + shift, 0), n)
    right_bound = max(min(n + shift, n), 0)

    velo = np.copy(U_0)
    velo[0, :left_bound] = U_0[0, 0]
    velo[0, right_bound:] = U_0[0, n - 1]
    velo[0, left_bound:right_bound] = U_0[0, left_bound - shift:right_bound - shift]
    return velo

def Lax_Friedrich_update(sol, k, h, n, f):
    sol[n, 1:-1] = 1 / 2 * (sol[n - 1, :-2] + sol[n - 1, 2:]) - k / (2 * h) * (f(sol[n - 1, 2:]) - f(sol[n - 1, :-2]))
    sol[n, 0] = 1 / 2 * (sol[n - 1, 0] + sol[n - 1, 1]) - k / (2 * h) * (
            f(sol[n - 1, 1]) - f(sol[n - 1, 0]))
    sol[n, -1] = 1 / 2 * (sol[n - 1, -2] + sol[n - 1, -1]) - k / (2 * h) * (
            f(sol[n - 1, -1]) - f(sol[n - 1, -1]))
    return sol

def Lax_Wendrof_update(sol, k, h, n, f, f_prime):
    sol[n, 1:-1] = sol[n - 1, 1:-1] - k / (2 * h) * (
            f(sol[n - 1, 2:]) - f(sol[n - 1, :-2])) + k ** 2 / (2 * h ** 2) * (
                           f_prime((sol[n - 1, 1:-1] + sol[n - 1, 2:]) / 2) * (
                           f(sol[n - 1, 2:]) - f(sol[n - 1, 1:-1]))
                           - f_prime((sol[n - 1, 1:-1] + sol[n - 1, :-2]) / 2) * (
                                   f(sol[n - 1, 1:-1]) - f(sol[n - 1, :-2])))
    sol[n, 0] = sol[n - 1, 0] - k / (2 * h) * (
            f(sol[n - 1, 1]) - f(sol[n - 1, 0])) + k ** 2 / (2 * h ** 2) * (
                        f_prime((sol[n - 1, 0] + sol[n - 1, 1]) / 2) * (
                        f(sol[n - 1, 1]) - f(sol[n - 1, 0]))
                        - f_prime((sol[n - 1, 0] + sol[n - 1, 0]) / 2) * (
                                f(sol[n - 1, 0]) - f(sol[n - 1, 1])))
    sol[n, -1] = sol[n - 1, -1] - k / (2 * h) * (
            f(sol[n - 1, -1]) - f(sol[n - 1, -2])) + k ** 2 / (2 * h ** 2) * (
                         f_prime((sol[n - 1, -1] + sol[n - 1, -1]) / 2) * (
                         f(sol[n - 1, -1]) - f(sol[n - 1, -1]))
                         - f_prime((sol[n - 1, -1] + sol[n - 1, -2]) / 2) * (
                                 f(sol[n - 1, -1]) - f(sol[n - 1, -2])))
    return sol

def Lax_Wendrof_lecture_update(sol, k, h, n, f):
    U_mp = (sol[n-1, 2:] + sol[n-1, 1:-1])/2 - k/(2*h) * (f(sol[n-1, 2:]) - f(sol[n-1, 1:-1]))
    U_mm = (sol[n-1, 1:-1] + sol[n-1, :-2])/2 - k/(2*h) * (f(sol[n-1, 1:-1]) - f(sol[n-1, :-2]))
    sol[n, 1:-1] = sol[n-1, 1:-1] - k/h * (f(U_mp) - f(U_mm))

    u_mp = (sol[n-1, 1] + sol[n-1, 0])/2 - k/(2*h) * (f(sol[n-1, 1]) - f(sol[n-1, 0]))
    u_mm = sol[n-1, 0]
    sol[n, 0] = sol[n-1, 0] - k/h * (f(u_mp) - f(u_mm))

    u_mp = sol[n-1, -1]
    u_mm = (sol[n - 1, -1] + sol[n - 1, -2]) / 2 - k / (2 * h) * (f(sol[n - 1, -1]) - f(sol[n - 1, -2]))
    sol[n, -1] = sol[n - 1, -1] - k / h * (f(u_mp) - f(u_mm))

    return sol

def left_sided(sol, k, h, n, f):
    sol[n, 1:] = sol[n-1, 1:] + k/h * (f(sol[n-1, 0:-1]) - f(sol[n-1, 1:]))
    sol[n, 0] = sol[n-1, 0] + k/h * (f(sol[n-1, 0]) - f(sol[n-1, 0]))
    return sol

def right_sided(sol, k, h, n, f):
    sol[n, :-1] = sol[n-1, :-1] + k/h * (f(sol[n-1, :-1]) - f(sol[n-1, 1:]))
    sol[n, -1] = sol[n-1, -1] + k/h * (f(sol[n-1, -1]) - f(sol[n-1, -1]))
    return sol

def Godunov(sol, k, h, n, f, f_prime, U_0):
    end = np.shape(sol[n-1, :])[0]
    for i in range(end):
        prime_i = f_prime(sol[n-1, i])
        if i == end-1:
            prime_p1 = f_prime(sol[n-1, i])
        else:
            prime_p1 = f_prime(sol[n-1, i+1])

        if prime_i > 0 and prime_p1 > 0:
            f_p = f(sol[n-1, i])
            if i == 0:
                f_m = f(sol[n - 1, 0])
            else:
                f_m = f(sol[n - 1, i-1])

        elif prime_i < 0 and prime_p1 < 0:
            if i == end-1:
                f_p = f(sol[n-1, i])
            else:
                f_p = f(sol[n - 1, i+1])
            f_m = f(sol[n-1, i])

        elif prime_i > 0 and prime_p1 < 0:
            t = n * h
            if i == 0:
                ul = sol[n - 1, i]
                ur = sol[n - 1, i + 1]
            elif i == end-1:
                ul = sol[n - 1, i - 1]
                ur = sol[n - 1, i]
            else:
                ul = sol[n-1, i-1]
                ur = sol[n-1, i+1]
            xs = t * (f(ul) - f(ur))/(ul - ur)
            if xs >= 0:
                f_p = f(sol[n - 1, i])
                if i == 0:
                    f_m = f(sol[n - 1, 0])
                else:
                    f_m = f(sol[n - 1, i - 1])
            else:
                if i == end-1:
                    f_p = f(sol[n - 1, i])
                else:
                    f_p = f(sol[n - 1, i + 1])
                f_m = f(sol[n - 1, i])
        else:
            if i == end-1:
                us_p = 0.5 * (sol[n-1, i-1] + sol[n-1, i])
            else:
                us_p = 0.5 * (sol[n-1, i] + sol[n-1, i+1])
            f_p = f(us_p)
            if i == 0:
                us_m = 0.5 * (sol[n-1, i+1] + sol[n-1, i])
            else:
                us_m = 0.5 * (sol[n-1, i] + sol[n-1, i-1])
            f_m = f(us_m)

        sol[n, i] = sol[n-1, i] + k/h * (f_m - f_p)

    return sol












