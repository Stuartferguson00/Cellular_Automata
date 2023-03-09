import matplotlib.pyplot as plt

from SIR_Lattice import SIR_Lattice

import time
import numpy as np

def main():


    """
    Function to run SIRS simulations over a range of probabilities to give a phase diagram


    Parameters
    ----------


    Returns
    -------


    """

    #weird order of 0 and 1 is purely because of how numpy works
    probs_l_0 = np.linspace(1,0, 21)
    probs_l_1= np.linspace(0,1, 21)



    n_t_s = 1000
    #n_t_s = 1100
    w_s = 100

    end_arr = np.zeros((len(probs_l_0),len(probs_l_1)))



    for i in range(len(probs_l_0)):
        for j in range(len(probs_l_1)):
            start = time.time()
            #L = Lattice(50, lattice = "blinker")
            L = SIR_Lattice(50, lattice = "uniform")
            #L = SIR_Lattice(50, lattice = "blobby")
            #L = SIR_Lattice(50, lattice = "wave")
            probs = (probs_l_1[j],0.5,probs_l_0[i])
            L.run(probs,wait_sweeps = w_s, num_tot_sweeps = n_t_s, plot_anim = False)

            end_arr[i,j] = np.mean(L.frac_inf)

    np.savetxt("SIRS_phase_avg_inf_2.txt",end_arr,delimiter = ",")


if __name__ == "__main__":

    main()