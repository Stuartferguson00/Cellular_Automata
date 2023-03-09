
import numpy as np
import matplotlib.pyplot as plt
import sys

from GOL_Lattice import GOL_Lattice



def main(N, init_lattice, num_sweeps, plot_anim):


    """
    Function to run a basic Game Of Life


    Parameters
    ----------
    N: int
        Size of lattice. Assumes square NxN lattice.

    init_lattice : numpy array or str
        An option to input starting lattice. Must be of size (NxN).
        Can also input string with options: "uniform" "blinker" "glider" (see functions for specifics)

    num_sweeps: int
        total number of sweeps required in the simulation.

    plot_anim: bool
        whether or not to plot animation of GOL

    Returns
    -------


    """

    #initialise and run lattice
    L = GOL_Lattice(N, lattice = init_lattice)
    L.run(wait_sweeps = 0, num_tot_sweeps = num_sweeps, plot_anim = plot_anim)




if __name__ == "__main__":

    #if incorrect umbe rof arguments are given, state what arguments are expected for which process
    if len(sys.argv) != 5:
        print("Usage: \n N (int), init_lattice (str 'uniform' or other), num_sweeps (int), plot_anim (bools)")
        len(sys.argv)
        print("For further usage instructions, see README or documentation")
        sys.exit(1)

    #if only one Temperature is to be evaluated
    elif len(sys.argv) == 5:
        main(int(sys.argv[1]), str(sys.argv[2]), int(sys.argv[3]), eval(sys.argv[4]))









