import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
import numpy as np
import conversation_laws as conv
import tikzplotlib


# std_path = "/home/carla/Dokumente/Uni/Bachelor/Computational Science/Hyperbolic_conversation_laws/MAT264_p2/Poster-Latex/uibposter-images/"
std_path = "../Poster-Latex/uibposter-images/"


def plot_flow_traffic(sol, X, T, h, k, speed, number=5):
    if number > 12:
        number = 12

    colors = ['midnightblue', 'royalblue', 'teal', 'mediumturquoise', 'mediumseagreen', 'forestgreen', 'yellowgreen',
              'goldenrod', 'darkorange', 'orangered', 'red', 'firebrick']
    c = 0

    fig = plt.figure(figsize=(15, 5))
    ax = plt.subplot()

    for datapoint_raw in np.linspace(0, T-1, number):
        datapoint = int(np.floor(datapoint_raw/k))
        data = sol[datapoint, :]
        velo = speed(sol[datapoint, :])
        x_mesh = np.arange(0, X, h)
        ax.plot(x_mesh, data, color=colors[c])
        ax.plot(x_mesh, velo, ':', color=colors[c])
        c += 1

    ax.plot(np.array([]), np.array([]), '-', color='black', label='aproximation')
    ax.plot(np.array([]), np.array([]), ':', color='black', label='speed of the cars')
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_flow_linear(sol, X, T, h, k, c, U_0, number=5):
    if number > 12:
        number = 12

    colors = ['midnightblue', 'royalblue', 'teal', 'mediumturquoise', 'mediumseagreen', 'forestgreen', 'yellowgreen',
              'goldenrod', 'darkorange', 'orangered', 'red', 'firebrick']
    counter = 0

    fig = plt.figure(figsize=(15, 5))
    ax = plt.subplot()

    for datapoint_raw in np.linspace(0, T - 1, number):
        datapoint = int(np.floor(datapoint_raw / k))
        data = sol[datapoint, :]

        n = len(U_0[0, :])
        shift = int(np.floor(c * datapoint_raw/h))
        left_bound = min(max(0 + shift, 0), n)
        right_bound = max(min(n + shift, n), 0)
        velo = np.copy(U_0)
        velo[0, :left_bound] = U_0[0, 0]
        velo[0, right_bound:] = U_0[0, n-1]
        velo[0, left_bound:right_bound] = U_0[0, left_bound - shift:right_bound - shift]

        x_mesh = np.arange(0, X, h)
        ax.plot(x_mesh, data, color=colors[counter])
        ax.plot(x_mesh, velo[0], ':', color=colors[counter])
        counter += 1

    ax.plot(np.array([]), np.array([]), '-', color='black', label='aproximation')
    ax.plot(np.array([]), np.array([]), ':', color='black', label='true solution')
    plt.legend()

    plt.tight_layout()
    tikzplotlib.clean_figure()
    tikzplotlib.save("test.tex")
    plt.show()


def plot_density(sol, num, X, T, h, k, U_0, c, speed, ymin=np.nan, ymax=np.nan, colormap=cm.viridis, num_cticks=None, plot_mode='none'):
    """
    plots the density of the solution.

    :param sol: computed solution
    :param num: density is plotted at num approx equal spaced time steps, including first and last one.
    plots only the last state if num = 1
    :param ymin: minimum of y axes, autoscale if omitted
    :param ymax: maximum of y axes, autoscale if omitted
    :param colormap: select the colormap. Good options might be: viridis, plasma, inferno, summer, winter, cool.
    Note: the first three are very intensive.
    :param num_cticks: number of labeled ticks on the colorbar
    :param plot_mode: 'none' , 'car_speed' for traffic problem or 'true_sol' for linear Rieman problem
    """
    steplist = np.arange(0, T, k)
    x_steplist = np.arange(0, X, h)

    # generate equally spaced numbers
    if num == 1:
        # linspace takes start if num = 1
        # but here end is a better choice
        steps = np.array([sol.shape[0] - 1])
    else:
        steps = np.linspace(0, sol.shape[0] - 1, num=num)

    # round to next integer to use them as indices
    steps = np.array([int(np.round(s)) for s in steps])
    # ticks on the colormap
    if num_cticks is None:
        cticks = steplist[steps]
    else:
        cticks = np.linspace(steplist[0], steplist[-1], num=num_cticks)

    colors = colormap(np.linspace(0, 1, num=len(steps)))

    fig = plt.figure(figsize=(15, 5))

    for (i, s) in enumerate(steps):
        if s == 0:
            plt.plot(x_steplist, sol[s, :], color=colors[i],  label='approximated solution')
        else:
            plt.plot(x_steplist, sol[s, :], color=colors[i])
        if plot_mode == 'true_sol':
            velo = conv.get_true_linear_sol(U_0, s, h, k, c)
            if s == 0:
                plt.plot(x_steplist, velo[0], ':', color=colors[i], label='true solution')
            else:
                plt.plot(x_steplist, velo[0], ':', color=colors[i])
        elif plot_mode == 'car_speed':
            if s == 0:
                plt.plot(x_steplist, speed(sol[s, :]), ':', color=colors[i], label='true solution')
            else:
                plt.plot(x_steplist, speed(sol[s, :]), ':', color=colors[i])


    # add colorbar
    norm = matplotlib.colors.Normalize(vmin=cticks.min(), vmax=cticks.max())
    cmap = cm.ScalarMappable(norm=norm, cmap=colormap)
    cmap.set_array([])
    cbar = plt.colorbar(cmap, ticks=cticks)
    cbar.ax.set_ylabel('time')

    if not np.isnan(ymin):
        plt.ylim(bottom=ymin)
    if not np.isnan(ymax):
        plt.ylim(top=ymax)

    plt.legend()
    plt.tight_layout()

    tikzplotlib.clean_figure()
    tikzplotlib.save(std_path + "test1.tikz")
    plt.show()




















