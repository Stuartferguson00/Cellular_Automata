import matplotlib.pyplot as plt

from SIR_Lattice import SIR_Lattice
import sys
import time
import numpy as np



#immune testing


def main(probs):
    """
    Function to run a GOL glider, and lot it's displacement from the origin


    Parameters
    ----------
    probs: bool
        whether or not to plot animation of GOL

    Returns
    -------


    """



    def find_avg_infs(immunities,w_s,n_tot_s,probs):

        avg_infs = []
        #Lattices =  []
        for im in immunities:

            L = SIR_Lattice(50, lattice = "uniform", immune = im)


            L.run(probs,wait_sweeps = w_s, num_tot_sweeps = n_tot_s, plot_anim = False)

            if np.count_nonzero(L.frac_inf) < len(L.frac_inf):
                avg_infs.append(0)
            else:
                avg_infs.append(np.mean(L.frac_inf))

        return avg_infs


    #make a guess with quick simulation
    orig_wait_sweeps = 50
    orig_num_tot_sweeps = 1000
    orig_immunities = np.linspace(0,1,10)
    orig_avg_infs = find_avg_infs(orig_immunities,orig_wait_sweeps,orig_num_tot_sweeps, probs)

    #find first 0
    provisional_guess = np.min(orig_immunities[np.argmin(orig_avg_infs)])



    #focus in on important region with longer simulation
    acc_wait_sweeps = 100
    acc_num_tot_sweeps = 2000
    num_fracs = 20
    num_repeats = 3

    #create test immunity fractions
    acc_immunities = np.linspace(provisional_guess-0.15,provisional_guess+0.15,num_fracs)
    #repeat multiple times
    acc_immunities = np.repeat(acc_immunities, num_repeats)

    #run
    acc_avg_infs = find_avg_infs(acc_immunities,acc_wait_sweeps,acc_num_tot_sweeps)
    acc_avg_infs = np.array(acc_avg_infs)
    #account for the multiple repeats
    acc_avg_infs = np.mean(acc_avg_infs.reshape(num_fracs,num_repeats),axis = 1)
    acc_immunities = np.unique(acc_immunities)


    out_orig = np.array([orig_avg_infs,orig_immunities])
    out_acc = np.array([acc_avg_infs,acc_immunities])


    np.savetxt("avg_inf_immunities_orig_data_"+str(probs[0])+str(probs[1])+str(probs[2])+".txt",out_orig, delimiter = ",")
    np.savetxt("avg_inf_immunities_acc_data_"+str(probs[0])+str(probs[1])+str(probs[2])+".txt",out_acc, delimiter = ",")




if __name__ == "__main__":


    #if incorrect umbe rof arguments are given, state what arguments are expected for which process
    if len(sys.argv) != 4:
        print("Usage: \n  p1, p1, p3")
        print(sys.argv)
        print("For further usage instructions, see README or documentation")
        sys.exit(1)

    #if only one Temperature is to be evaluated
    elif len(sys.argv) == 4:
        main((float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3])))