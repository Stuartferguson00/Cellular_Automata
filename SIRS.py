import matplotlib.pyplot as plt
import sys
from SIR_Lattice import SIR_Lattice

import time
import numpy as np

def main(N,  probs, num_sweeps, immune, plot_anim):



    """
    Function to run a basic SIRS


    Parameters
    ----------
    N: int
        Size of lattice. Assumes square NxN lattice.

    init_lattice : numpy array or str
        An option to input starting lattice. Must be of size (NxN).
        Can also input string with options: "uniform" or other (see class functions for specifics)

    probs: tupple
        (p1,p2,p3) the probabilities of S --> I, I-->R AND R --> S

    num_sweeps: int
        total number of sweeps required in the simulation.

    immune : float
            fraction of cells to start immune

    plot_anim: bool
        whether or not to plot animation of GOL

    Returns
    -------
    """
    print(probs)

    L = SIR_Lattice(N, lattice = "uniform", immune = immune)

    L.run(probs,wait_sweeps = 0, num_tot_sweeps = num_sweeps, plot_anim = plot_anim)


    plt.plot(L.sweep_list, L.frac_inf)
    plt.show()





if __name__ == "__main__":

    #if incorrect umbe rof arguments are given, state what arguments are expected for which process
    if len(sys.argv) != 8:
        print("Usage: \n N (int),  p1, p2, p3, num_sweeps (int), immune (float), plot_anim (bools)")
        print("For absorbing state: p1 =  0.2, p2 = 0.5, p3 = 0.2, ")
        print("For dynamic equilibrium: p1 =  0.8, p2 = 0.5, p3 = 0.8, ")
        print("For waves: p1 =  0.8, p2 = 0.1, p3 = 0.01  (works better with N = 100)")
        print("For further usage instructions, see README or documentation")
        sys.exit(1)


    #if only one Temperature is to be evaluated
    elif len(sys.argv) == 8:
        main(int(sys.argv[1]), (float(sys.argv[2]), float(sys.argv[3]) ,float(sys.argv[4])), int(sys.argv[5]), float(sys.argv[6]), eval(sys.argv[7]))

