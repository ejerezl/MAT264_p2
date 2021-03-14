import numpy as np
import matplotlib.pyplot as plt
import plotter as plot
import initial_condition as init
import conversation_laws as step
import matplotlib
import os
import time

cwd = os.getcwd()
plt.style.use(cwd + '/poster.mplstyle')

save = True
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

T = 5
X = 10
h = 0.01

X, h, x_step, T, k, t_step, U_0 = init.get_initial(name_of_init, U=0, X=X, T=T, h=h)

f, f_prime, speed = init.get_problemfunction(name_of_problem, c=c)

sols = []
methods = ['Lax-Wendsdroff from lecture', 'Godunov', 'Lax-Friedrichs']
time_list = []
'------------------ SOLVE THE PDE WITH ALL METHODS -----------------------------------------------------------------------------------------'
for method in methods:
    START = time.time()
    sols.append(step.solve_problem(method, U_0, X, T, h, k, x_step, t_step, f, f_prime))
    END = time.time()
    time_list.append(END - START)


'----------------- compute true solution ---------------------------------------------------'
datapoint = int(np.floor(T/k))
true_sol = step.get_true_linear_sol(U_0, datapoint, h, k, c)[0]

'------------------ PLOT SOLUTION ---------------------------------------------------------------------------------------------'
'PLOT SOLUTION'
col_span = 1
save = True
if col_span == 2:
    lw = 3
    matplotlib.rcParams['figure.figsize'] = (14.78636, 11.089770003)
elif col_span == 1:
    lw = 2
    matplotlib.rcParams['figure.figsize'] = (6.8025, 5.101875001*0.8)

i = 0
colors = ['navy', 'darkorange', 'green']
name = ['Lax-Wendroff', 'Godunov', 'Lax-Friedrichs']
x_steplist = np.arange(0, X, h)
for method in name:
    plt.plot(x_steplist, sols[i][-1], label='\\rmfamily ' + method, linewidth=lw, color=colors[i]) #Plotting the solution for each method
    i += 1

if name_of_problem == 'traffic':
    plt.xlim([3.3, 7])

elif name_of_problem == 'linear':
    plt.plot(x_steplist, true_sol, ':', label='\\rmfamily true solution', linewidth=lw, color='dimgray', zorder=0)
    #plt.xlim([4.4, 7.5])
    plt.xlim([4.4, 7.85])

if name_of_problem == 'Burger':
    plt.xlim([1, 5.2])

#plt.title('\\rmfamily\\bfseries Solutions', pad=15)
plt.title('\\rmfamily\\bfseries ', pad=15,  fontsize=21.6)
plt.xlabel('\\rmfamily Space')
#plt.gca().xaxis.set_label_coords(0.5, -0.175)
plt.gca().xaxis.set_label_coords(0.89, -0.1)
plt.ylabel('\\rmfamily Density', rotation=0)
plt.gca().yaxis.set_label_coords(-0.15, 0.95)
#plt.legend(bbox_to_anchor=(0., -0.35, 1., .102), loc='upper left',
#            ncol=2, mode="expand", borderaxespad=0., handlelength=1., fontsize=21.6)

if save:
    plt.savefig('figures/traffic_comprehension_.png', dpi=300)
plt.show()

print(methods)
print(time_list)

