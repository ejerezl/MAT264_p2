import numpy as np
import plotter as plot
import initial_condition as init
import conversation_laws as step
import matplotlib.pyplot as plt
import helper_functions as help

'~~~~~~~~~~ SELECT THE PROBLEM FUNCTIONS (only linear possible) ~~~~~~~~~~'
name_of_problem = 'linear'


'~~~~~~~~~~ SELECT THE METHOD ~~~~~~~~~~'
method = 'Lax-Friedrichs'
#method = 'Lax-Wendsdroff'
#method = 'Lax-Wendsdroff from lecture'
#method = 'left sided'
#method = 'right sided'
#method = 'Godunov'


c = 1

X = 10
T = 0.5


#x_step_list = np.geomspace(0.0001, 0.01, num=5)     # work for Lax-Friedrich and Lax-Wendroff (too slow for Godunov)
x_step_list = np.geomspace(0.005, 0.05, num=5)

'------------------ FERRY PROBLEM ---------------------------------------------------------------------------------------------'
'------------------ SOLVE THE PDE ---------------------------------------------------------------------------------------------'

sol_list = []
U_0_list = []
k_list = []

for x_step in x_step_list:
    X, h, x_step, T, k, t_step, U_0 = init.get_initial('ferry problem', U=0, X=X, T=T, h=x_step)
    k_list.append(k)
    U_0_list.append(U_0)

    f, f_prime, speed = init.get_problemfunction(name_of_problem, c=c)

    sol = step.solve_problem(method, U_0, X, T, h, k, x_step, t_step, f, f_prime)

    sol_list.append(sol[-1, :])


'------------------ PLOT SOLUTION ---------------------------------------------------------------------------------------------'

errors = []

for i in range(len(sol_list)):
    k = k_list[i]
    h = x_step_list[i]
    t_max_index = np.shape(sol_list[i])[0] - 1
    true_sol = step.get_true_linear_sol(U_0_list[i], int(np.floor(T / k)), h, k, c)
    err = help.norm_1_two(sol_list[i], true_sol[0], h) / help.norm_1(true_sol[0], h)
    errors.append(err)

plt.plot(x_step_list, errors, label='Ferry Problem')

'------------------ POLICE PROBLEM ---------------------------------------------------------------------------------------------'
'------------------ SOLVE THE PDE ---------------------------------------------------------------------------------------------'

sol_list = []
U_0_list = []
k_list = []

for x_step in x_step_list:
    X, h, x_step, T, k, t_step, U_0 = init.get_initial('police problem', U=0, X=X, T=T, h=x_step)
    k_list.append(k)
    U_0_list.append(U_0)

    f, f_prime, speed = init.get_problemfunction(name_of_problem, c=c)

    sol = step.solve_problem(method, U_0, X, T, h, k, x_step, t_step, f, f_prime)

    sol_list.append(sol[-1, :])


'------------------ PLOT SOLUTION ---------------------------------------------------------------------------------------------'

errors = []

for i in range(len(sol_list)):
    k = k_list[i]
    h = x_step_list[i]
    t_max_index = np.shape(sol_list[i])[0] - 1
    true_sol = step.get_true_linear_sol(U_0_list[i], int(np.floor(T / k)), h, k, c)
    err = help.norm_1_two(sol_list[i], true_sol[0], h) / help.norm_1(true_sol[0], h)
    errors.append(err)

plt.plot(x_step_list, errors, label='Police Problem')

'------------------ COS PROBLEM ---------------------------------------------------------------------------------------------'
'------------------ SOLVE THE PDE ---------------------------------------------------------------------------------------------'

sol_list = []
U_0_list = []
k_list = []

for x_step in x_step_list:
    X, h, x_step, T, k, t_step, U_0 = init.get_initial('cos function 2', U=0, X=X, T=T, h=x_step)
    k_list.append(k)
    U_0_list.append(U_0)

    f, f_prime, speed = init.get_problemfunction(name_of_problem, c=c)

    sol = step.solve_problem(method, U_0, X, T, h, k, x_step, t_step, f, f_prime)

    sol_list.append(sol[-1, :])


'------------------ PLOT SOLUTION ---------------------------------------------------------------------------------------------'

#plt.show()

errors = []

for i in range(len(sol_list)):
    k = k_list[i]
    h = x_step_list[i]
    t_max_index = np.shape(sol_list[i])[0] - 1
    true_sol = step.get_true_linear_sol(U_0_list[i], int(np.floor(T / k)), h, k, c)
    err = help.norm_1_two(sol_list[i], true_sol[0], h) / help.norm_1(true_sol[0], h)
    errors.append(err)
    #plt.plot(sol_list[i])
    #plt.plot(true_sol[0], label='true')
    #plt.legend()
    #plt.show()

plt.plot(x_step_list, errors, label='Cos Problem')


plt.xscale('log')
plt.yscale('log')
plt.xticks(x_step_list, x_step_list)
plt.legend()
plt.tight_layout()
plt.show()






















