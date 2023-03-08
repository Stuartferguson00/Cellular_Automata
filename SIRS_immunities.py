import matplotlib.pyplot as plt

from SIR_Lattice import SIR_Lattice

import time
import numpy as np



#immune testing

wait_sweeps = 30
num_tot_sweeps = 100
immunities = np.linspace(0,1,10)

print("hi")
print(immunities)
avg_infs = []
Lattices =  []
for im in immunities:

    L = SIR_Lattice(50, lattice = "uniform", immune = im)

    probs = (0.5,0.5,0.5)
    L.run(probs,wait_sweeps = wait_sweeps, num_tot_sweeps = num_tot_sweeps, plot_anim = False)


    avg_infs.append(np.mean(L.frac_inf))
    #L.plot_frac_inf(label = str(im))

    #plt.plot(L.sweep_list,L.frac_inf)
    Lattices.append(L)

out = np.array([avg_infs,immunities])
print(out)

np.savetxt("avg_inf_immunities_data.txt",out, delimiter = ",")


