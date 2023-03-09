
import numpy as np
import matplotlib.pyplot as plt

from GOL_Lattice import GOL_Lattice
import sys

def main(plot_anim):

    """
    Function to run SIRS simmulations over a range of immunity levels for given input probabilities in order to find
    the minimum immunity fraction required to dismiss the disease


    Parameters
    ----------
    probs: tupple
        (p1,p2,p3) the probabilities of S --> I, I-->R AND R --> S

    Returns
    -------


    """


    L = GOL_Lattice(50, lattice = "glider")
    L.run(wait_sweeps = 0, num_tot_sweeps = 400, plot_anim = plot_anim)

    plt.show()
    plt.title("Glider distance from origin with sweeps")
    plt.ylabel("Displacement from origin of glider center of mass")
    plt.xlabel("Sweep")
    plt.plot(L.sweep_list, L.glider_pos)

    time = 50 #sweeps
    pos = np.array(L.glider_pos)
    distance = pos[7+time]-pos[7]
    velocity = distance/time

    print("The velocity of the glider is: "+str(velocity))
    print("please note that this is equivalent to: "+str(velocity/np.sqrt(2))+" if considering one diagonal step to be equal in distance to one step")
    plt.show()


if __name__ == "__main__":


    #if incorrect umbe rof arguments are given, state what arguments are expected for which process
    if len(sys.argv) != 2:
        print("Usage: \n  plot_anim (bools)")
        len(sys.argv)
        print("For further usage instructions, see README or documentation")
        sys.exit(1)

    #if only one Temperature is to be evaluated
    elif len(sys.argv) == 2:
        main(eval(sys.argv[1]))

