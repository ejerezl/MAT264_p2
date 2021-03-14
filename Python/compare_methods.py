import numpy as np
import matplotlib.pyplot as plt
import plotter as plot
import initial_condition as init
import conversation_laws as step
import matplotlib
import os

cwd = os.getcwd()
plt.style.use(cwd + '/poster.mplstyle')


'~~~~~~~~~~ SELECT THE PROBLEM FUNCTIONS ~~~~~~~~~~'
name_of_problem = 'traffic'
#name_of_problem = 'linear'
#name_of_problem = 'Burger'
#name_of_problem = 'Buckley-Leverett'


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

T = 15.
X = 20
h = 0.1

X, h, x_step, T, k, t_step, U_0 = init.get_initial(name_of_init, U=0, X=X, T=T, h=h)

f, f_prime, speed = init.get_problemfunction(name_of_problem, c=c)

sols = []
methods = ['Godunov', 'Lax-Wendsdroff from lecture', 'Lax-Friedrichs']
'------------------ SOLVE THE PDE WITH ALL METHODS -----------------------------------------------------------------------------------------'
for method in methods:
    sols.append(step.solve_problem(method, U_0, X, T, h, k, x_step, t_step, f, f_prime))



'------------------ PLOT SOLUTION ---------------------------------------------------------------------------------------------'
'PLOT SOLUTION'
col_span = 1
save = True
if col_span == 2:
    lw = 3
    matplotlib.rcParams['figure.figsize'] = (14.78636, 11.089770003)
elif col_span == 1:
    lw = 2
    matplotlib.rcParams['figure.figsize'] = (6.8025, 5.101875001)

i = 0
x_steplist = np.arange(0, X, h)
for method in methods:
    plt.plot(x_steplist, sols[i][-1], label='\\rmfamily ' + method, linewidth=lw) #Plotting the solution for each method
    i += 1

plt.xlim([8, 20])

plt.legend()
plt.show()
