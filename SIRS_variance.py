import matplotlib.pyplot as plt

from SIR_Lattice import SIR_Lattice

import time
import numpy as np

def main():

    """
    Function to run SIRS simulations over a range of probabilities to give a variance diagram data


    Parameters
    ----------


    Returns
    -------


    """




    #weird order of 0 and 1 is purely because of how imshow works
    probs_l_0 = np.linspace(0.2,0.5, 30)





    n_t_s = 10100
    #n_t_s = 1100
    w_s = 100

    var_arr = np.zeros((len(probs_l_0)))
    err_arr = np.zeros((len(probs_l_0)))

    size = 50 #ie N = 50

    for i in range(len(probs_l_0)):

        L = SIR_Lattice(size, lattice = "uniform")

        probs = (probs_l_0[i],0.5,0.5)
        L.run(probs,wait_sweeps = w_s, num_tot_sweeps = n_t_s, plot_anim = False)



        var_arr[i] = L.find_variance()
        err_arr[i] = L.jacknife_var()

        if  L.frac_inf[0] == 0:
            L.frac_inf.append(0)

    output = [probs_l_0, var_arr, err_arr]


    np.savetxt("SIRS_variance.txt",output,delimiter = ",")



if __name__ == "__main__":
    main()

