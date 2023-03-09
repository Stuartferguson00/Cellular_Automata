import numpy as np
import matplotlib.pyplot as plt

from GOL_Lattice import GOL_Lattice
import sys


def main(N, num_reps):


    """
    Function to run a basic Game Of Life


    Parameters
    ----------
    N: int
        Size of lattice. Assumes square NxN lattice.

    num_reps: int
        number of times to run GOL in order to build histogram data

    Returns
    -------


    """

    end_points = []
    for i in range(num_reps):
        L = GOL_Lattice(N)
        L.run(wait_sweeps=0, num_tot_sweeps=5000, plot_anim=False)
        end_points.append(L.sweep_list[-1])
        #plt.plot(L.sweep_list, L.num_activ_sites)
        #plt.show()
        if i%10 == 0:
            print(i)
    np.savetxt("GOL_hist_data.txt", end_points, delimiter=",")



if __name__ == "__main__":

    #if incorrect umbe rof arguments are given, state what arguments are expected for which process
    if len(sys.argv) != 3:
        print("Usage: \n N (int), num_reps (int)")
        print("For further usage instructions, see README or documentation")
        sys.exit(1)

    #if only one Temperature is to be evaluated
    elif len(sys.argv) == 3:
        main(int(sys.argv[1]), int(sys.argv[2]))




