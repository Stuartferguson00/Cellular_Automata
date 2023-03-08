import matplotlib.pyplot as plt

from SIR_Lattice import SIR_Lattice

import time
import numpy as np





start = time.time()


#weird order of 0 and 1 is purely because of how imshow works
probs_l_0 = np.linspace(1,0, 5)
probs_l_1= np.linspace(0,1, 5)



n_t_s = 300
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
        probs = (probs_l_0[i],0.5,probs_l_1[j])
        L.run(probs,wait_sweeps = w_s, num_tot_sweeps = n_t_s, plot_anim = False)

        end_arr[i,j] = np.mean(L.frac_inf)
    print(end_arr)
np.savetxt("SIRS_phase_avg_inf.txt",end_arr,delimiter = ",")

end = time.time()
print("time")
print(start-end)
