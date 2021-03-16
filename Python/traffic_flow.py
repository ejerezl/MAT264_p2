import numpy as np
import matplotlib.pyplot as plt
import plotter as plot
import initial_condition as init
import conversation_laws as step


'~~~~~~~~~~ SELECT THE PROBLEM FUNCTIONS ~~~~~~~~~~'
#name_of_problem = 'traffic'
#name_of_problem = 'linear'
#name_of_problem = 'Burger'
name_of_problem = 'Buckley-Leverett'


'~~~~~~~~~~ SELECT THE METHOD ~~~~~~~~~~'
method = 'Lax-Friedrichs'
#method = 'Lax-Wendsdroff'
#method = 'Lax-Wendsdroff from lecture'
#method = 'left sided'
#method = 'right sided'
#method = 'Godunov'


'~~~~~~~~~~ SELECT THE INITIAL DATA ~~~~~~~~~~'
#name_of_init = 'ferry problem'
#name_of_init = 'traffic jam'
#name_of_init = 'two step function'
name_of_init = 'police problem'
#name_of_init = 'police problem 2'
#name_of_init = 'police problem 3'
#name_of_init = 'cos function'
#name_of_init = 'cos function 2'


c = 1

T = 15
X = 20
h = 0.01

'------------------ SOLVE THE PDE ---------------------------------------------------------------------------------------------'

X, h, x_step, T, k, t_step, U_0 = init.get_initial(name_of_init, U=0, X=X, T=T, h=h)

f, f_prime, speed = init.get_problemfunction(name_of_problem, c=c)

sol = step.solve_problem(method, U_0, X, T, h, k, x_step, t_step, f, f_prime)

'------------------ PLOT SOLUTION ---------------------------------------------------------------------------------------------'
num = 5

if name_of_problem == 'traffic':
    plot.plot_density(sol, num, X, T, h, k, U_0, c, speed, plot_mode='none')#, save=True)
elif name_of_problem == 'linear':
    plot.plot_density(sol, num, X, T, h, k, U_0, c, speed, plot_mode='true_sol', ymin=0, ymax=1)
elif name_of_problem == 'Burger':
    plot.plot_density(sol, num, X, T, h, k, U_0, c, speed, plot_mode='none')
elif name_of_problem == 'Buckley-Leverett':
    plot.plot_density(sol, num, X, T, h, k, U_0, c, speed, plot_mode='none')
