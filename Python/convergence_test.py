import numpy as np
import plotter as plot
import matplotlib
import initial_condition as init
import conversation_laws as step
import matplotlib.pyplot as plt
import helper_functions as help
import timeit
import os

cwd = os.getcwd()
plt.style.use(cwd + '/poster.mplstyle')

'~~~~~~~~~~ SELECT THE PROBLEM FUNCTIONS (only linear possible) ~~~~~~~~~~'
name_of_problem = 'linear'


'~~~~~~~~~~ SELECT THE INITIAL DATA ~~~~~~~~~~'
#name_of_init = 'ferry problem'
#name_of_init = 'traffic jam'
#name_of_init = 'two step function'
name_of_init = 'police problem'
#name_of_init = 'cos function'
#name_of_init = 'cos function 2'


c = 1
T = 20


'------------------ PLOT SOLUTION ---------------------------------------------------------------------------------------------'


t_max_index = np.shape(sol_laxF)[0] - 1
time_list = []

error_laxF = []
for datapoint_raw in np.linspace(0, t_max_index, int(np.floor(t_max_index/50))):
    datapoint_raw = int(np.floor(datapoint_raw))
    time_list.append(datapoint_raw*k)
    velo = step.get_true_linear_sol(U_0, datapoint_raw, h, k, c)
    err = help.norm_1_two(sol_laxF[datapoint_raw, :], velo[0], h) / help.norm_1(velo[0], h)
    error_laxF.append(err)
"""
error_laxW = []
for datapoint_raw in np.linspace(0, t_max_index, int(np.floor(t_max_index/50))):
    datapoint_raw = int(np.floor(datapoint_raw))
    velo = step.get_true_linear_sol(U_0, datapoint_raw, h, k, c)
    err = help.norm_1_two(sol_laxW[datapoint_raw, :], velo[0], h) / help.norm_1(velo[0], h)
    error_laxW.append(err)
"""
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


'PLOT SOLUTION'
col_span = 1
save = True
if col_span == 2:
    lw = 3
    matplotlib.rcParams['figure.figsize'] = (14.78636, 11.089770003)
elif col_span == 1:
    lw = 2
    matplotlib.rcParams['figure.figsize'] = (6.8025, 5.101875001)


plt.plot(time_list, error_laxF, label='\\rmfamily Lax Friedrich', color='green', linewidth=lw)
#plt.plot(error_laxW, label='Lax Wendroff')
plt.plot(time_list, error_Godu, label='\\rmfamily Godunov', color='darkorange', linewidth=lw)
plt.plot(time_list, error_laxW_l, label='\\rmfamily Lax Wendroff', color='navy', linewidth=lw)

plt.title('\\rmfamily\\bfseries Error over time', pad=15)
plt.xlabel('\\rmfamily t')
plt.gca().xaxis.set_label_coords(1.05, -0.1)
plt.ylabel('\\rmfamily Error', rotation=0)
plt.gca().yaxis.set_label_coords(-0.15, 0.9)
plt.legend(bbox_to_anchor=(0., -0.25, 1., .102), loc='upper left',
            ncol=2, mode="expand", borderaxespad=0., handlelength=1., fontsize=21.6)
plt.tight_layout()
if save:
    plt.savefig('figures/error_over_time.png', dpi=300)
plt.show()






>>>>>>> 84a43eb82a13c5e1c1ec1b75dc3af14d2d02cf86
