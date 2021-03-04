import numpy as np
import plotter as plot
import initial_condition as init
import conversation_laws as step
import matplotlib.pyplot as plt
import helper_functions as help

'~~~~~~~~~~ SELECT THE PROBLEM FUNCTIONS (only linear possible) ~~~~~~~~~~'
name_of_problem = 'linear'


'~~~~~~~~~~ SELECT THE INITIAL DATA ~~~~~~~~~~'
#name_of_init = 'ferry problem'
#name_of_init = 'traffic jam'
#name_of_init = 'two step function'
#name_of_init = 'police problem'
name_of_init = 'cos function'
#name_of_init = 'cos function 2'


c = 1

'------------------ SOLVE THE PDE ---------------------------------------------------------------------------------------------'

'~~~~~ LAX-FRIEDRICHS ~~~~~'
X, h, x_step, T, k, t_step, U_0 = init.get_initial(name_of_init, U=0, X=20, T=25.01, h=0.01)

f, f_prime, speed = init.get_problemfunction(name_of_problem, c=c)

sol_laxF = step.solve_problem('Lax-Friedrichs', U_0, X, T, h, k, x_step, t_step, f, f_prime)


'~~~~~ LAX-WENDROF ~~~~~'
X, h, x_step, T, k, t_step, U_0 = init.get_initial(name_of_init, U=0, X=20, T=25.01, h=0.01)

f, f_prime, speed = init.get_problemfunction(name_of_problem, c=c)

sol_laxW = step.solve_problem('Lax-Wendsdroff', U_0, X, T, h, k, x_step, t_step, f, f_prime)


'~~~~~ LAX-WENDROF from lecture ~~~~~'
X, h, x_step, T, k, t_step, U_0 = init.get_initial(name_of_init, U=0, X=20, T=25.01, h=0.01)

f, f_prime, speed = init.get_problemfunction(name_of_problem, c=c)

sol_laxW_l = step.solve_problem('Lax-Wendsdroff from lecture', U_0, X, T, h, k, x_step, t_step, f, f_prime)


'~~~~~ Godunov ~~~~~'
X, h, x_step, T, k, t_step, U_0 = init.get_initial(name_of_init, U=0, X=20, T=25.01, h=0.01)

f, f_prime, speed = init.get_problemfunction(name_of_problem, c=c)

sol_Godu = step.solve_problem('Godunov', U_0, X, T, h, k, x_step, t_step, f, f_prime)


'------------------ PLOT SOLUTION ---------------------------------------------------------------------------------------------'

t_max_index = np.shape(sol_laxF)[0] - 1

error_laxF = []
for datapoint_raw in np.linspace(0, t_max_index, int(np.floor(t_max_index/50))):
    datapoint_raw = int(np.floor(datapoint_raw))
    velo = step.get_true_linear_sol(U_0, datapoint_raw, h, k, c)
    err = help.norm_1_two(sol_laxF[datapoint_raw, :], velo[0], h) / help.norm_1(velo[0], h)
    error_laxF.append(err)

error_laxW = []
for datapoint_raw in np.linspace(0, t_max_index, int(np.floor(t_max_index/50))):
    datapoint_raw = int(np.floor(datapoint_raw))
    velo = step.get_true_linear_sol(U_0, datapoint_raw, h, k, c)
    err = help.norm_1_two(sol_laxW[datapoint_raw, :], velo[0], h) / help.norm_1(velo[0], h)
    error_laxW.append(err)

error_laxW_l = []
for datapoint_raw in np.linspace(0, t_max_index, int(np.floor(t_max_index/50))):
    datapoint_raw = int(np.floor(datapoint_raw))
    velo = step.get_true_linear_sol(U_0, datapoint_raw, h, k, c)
    err = help.norm_1_two(sol_laxW_l[datapoint_raw, :], velo[0], h) / help.norm_1(velo[0], h)
    error_laxW_l.append(err)

error_Godu = []
for datapoint_raw in np.linspace(0, t_max_index, int(np.floor(t_max_index/50))):
    datapoint_raw = int(np.floor(datapoint_raw))
    velo = step.get_true_linear_sol(U_0, datapoint_raw, h, k, c)
    err = help.norm_1_two(sol_Godu[datapoint_raw, :], velo[0], h) / help.norm_1(velo[0], h)
    error_Godu.append(err)

plt.plot(error_laxF, label='Lax Friedrich')
plt.plot(error_laxW, label='Lax Wendroff')
plt.plot(error_laxW_l, label='Lax Wendroff from slides')
plt.plot(error_Godu, label='Godunov')
plt.legend()
plt.show()





