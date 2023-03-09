import matplotlib.pyplot as plt

from SIR_Lattice import SIR_Lattice

import time
import numpy as np


def main():
    """
    Function to plot relevant graphs for SIR


    Parameters
    ----------

    Returns
    -------


    """

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #plot 2d histogram

    """end_arr = np.flip(np.loadtxt("SIR_avg_I.txt",delimiter = ","), axis = 1)
    #end_arr =np.loadtxt("SIRS_phase_avg_inf.txt",delimiter = ",")
    im = plt.imshow(end_arr, animated=True, cmap="hot", extent=[0,1,0,1])  # Oranges")
    plt.colorbar(im)
    plt.show()"""

    plt.title("Average infection fraction at p2 = 0.5")
    plt.xlabel("Probability of S --> I")
    plt.ylabel("Probability of R --> S")
    end_arr =np.loadtxt("SIRS_phase_avg_inf_2.txt",delimiter = ",")
    im = plt.imshow(end_arr, animated=True, cmap="hot", extent=[0,1,0,1])  # Oranges")
    plt.colorbar(im)
    plt.show()

    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #plot variance


    input = np.loadtxt("SIRS_variance_2.txt", delimiter = ",")

    probs = input[0]
    var = input[1]
    var_errs= input[2]

    plt.title("Variance in number of infections with p1")
    plt.ylabel("Variance in number of infections")
    plt.xlabel("Probability of S --> I")
    plt.errorbar(probs,var,var_errs)
    plt.show()





    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #plot immunities

    orig_input = np.loadtxt("avg_inf_immunities_orig_data_normal.txt", delimiter = ",")
    orig_avg_infs = orig_input[0]
    orig_immunities= orig_input[1]

    acc_input = np.loadtxt("avg_inf_immunities_acc_data_normal.txt", delimiter = ",")
    acc_avg_infs = acc_input[0]
    #acc_avg_infs = np.mean(acc_avg_infs.reshape(20,3),axis = 1)


    acc_immunities= acc_input[1]
    #acc_immunities = np.unique(acc_immunities)
    #print()
    #print(acc_immunities.reshape(20,3))


    plt.plot(orig_immunities,orig_avg_infs, color = "green", marker = "x", markersize = 3,linewidth = 0, label = "Rough normal", alpha = 0.3)
    plt.plot(acc_immunities,acc_avg_infs, color = "green", marker = "x",markersize = 3,linewidth = 0, label = "Accurate normal")







    orig_input = np.loadtxt("avg_inf_immunities_orig_data_hardcore.txt", delimiter = ",")
    orig_avg_infs = orig_input[0]
    orig_immunities= orig_input[1]

    acc_input = np.loadtxt("avg_inf_immunities_acc_data_hardcore.txt", delimiter = ",")
    acc_avg_infs = acc_input[0]
    #acc_avg_infs = np.mean(acc_avg_infs.reshape(20,3),axis = 1)


    acc_immunities= acc_input[1]
    #acc_immunities = np.unique(acc_immunities)
    #print()
    #print(acc_immunities.reshape(20,3))


    plt.title("Average infected fraction against immunity fraction")
    plt.ylabel("Average infected fraction")
    plt.xlabel("Immunity fraction")
    plt.plot(orig_immunities,orig_avg_infs,  color = "slateblue", marker = "^", markersize = 3, linewidth = 0, label = "Rough heavy", alpha = 0.5)
    plt.plot(acc_immunities,acc_avg_infs,  color = "slateblue", marker = "^", markersize = 3, linewidth = 0, label = "Accurate heavy")
    plt.legend()
    plt.show()


if __name__ == "__main__":

    main()

