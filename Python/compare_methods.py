import numpy as np
import matplotlib.pyplot as plt
import plotter as plot
import initial_condition as init
import conversation_laws as step


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

T = 8.0025
X = 20
h = 0.01

X, h, x_step, T, k, t_step, U_0 = init.get_initial(name_of_init, U=0, X=X, T=T, h=h)

f, f_prime, speed = init.get_problemfunction(name_of_problem, c=c)

sols = []
methods = ['Godunov', 'Lax-Wendsdroff from lecture', 'Lax-Friedrichs']
'------------------ SOLVE THE PDE WITH ALL METHODS -----------------------------------------------------------------------------------------'
for method in methods:
    sols.append(step.solve_problem(method, U_0, X, T, h, k, x_step, t_step, f, f_prime))



'------------------ PLOT SOLUTION ---------------------------------------------------------------------------------------------'
i = 0
for method in methods:
    plt.plot(sols[i][-1], label = method) #Plotting the solution for each method
    i += 1

plt.legend()
plt.show()