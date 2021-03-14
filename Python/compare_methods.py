import numpy as np
import matplotlib.pyplot as plt
import plotter as plot
import initial_condition as init
import conversation_laws as step
import matplotlib
import os

cwd = os.getcwd()
plt.style.use(cwd + '/poster.mplstyle')

save = True
'~~~~~~~~~~ SELECT THE PROBLEM FUNCTIONS ~~~~~~~~~~'
#name_of_problem = 'traffic'
#name_of_problem = 'linear'
name_of_problem = 'Burger'
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

T = 5
X = 10
h = 0.01

X, h, x_step, T, k, t_step, U_0 = init.get_initial(name_of_init, U=0, X=X, T=T, h=h)

f, f_prime, speed = init.get_problemfunction(name_of_problem, c=c)

sols = []
methods = ['Lax-Wendsdroff from lecture', 'Godunov', 'Lax-Friedrichs']
'------------------ SOLVE THE PDE WITH ALL METHODS -----------------------------------------------------------------------------------------'
for method in methods:
    sols.append(step.solve_problem(method, U_0, X, T, h, k, x_step, t_step, f, f_prime))



'------------------ PLOT SOLUTION ---------------------------------------------------------------------------------------------'
'PLOT SOLUTION'
col_span = 1
save = True
if col_span == 2:
    lw = 3
    matplotlib.rcParams['figure.figsize'] = (14.78636, 11.089770003*1.25)
elif col_span == 1:
    lw = 2
    matplotlib.rcParams['figure.figsize'] = (6.8025, 5.101875001*1.25)

i = 0
colors = ['navy', 'darkorange', 'green']
name = ['Lax-Wendroff', 'Godunov', 'Lax-Friedrichs']
x_steplist = np.arange(0, X, h)
for method in name:
    plt.plot(x_steplist, sols[i][-1], label='\\rmfamily ' + method, linewidth=lw, color = colors[i]) #Plotting the solution for each method
    i += 1

if name_of_problem == 'linear':
    real_sol = step.get_true_linear_sol(U_0, t_step, h, k, c)[0]
    plt.plot(x_steplist, real_sol, ':', label='\\rmfamily ' + 'Real solution', linewidth=lw, color = 'dimgrey')
    plt.xlim([4.4, 7.5])
elif name_of_problem == 'Burgers':
    plt.xlim([1, 5])

plt.title('\\rmfamily\\bfseries Solutions', pad=15)
plt.xlabel('\\rmfamily Space')
plt.gca().xaxis.set_label_coords(0.5, -0.175)
plt.ylabel('\\rmfamily Density')
plt.legend(bbox_to_anchor=(0., -0.425, 1., .102), loc='upper left',
            ncol=2, mode="expand", borderaxespad=0., handlelength=1., fontsize=21.6)

if save:
    plt.savefig('figures/linear_comparing.png', dpi=300)
plt.show()

