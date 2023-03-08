import matplotlib.pyplot as plt

from SIR_Lattice import SIR_Lattice

import time
import numpy as np


start = time.time()
#L = Lattice(50, lattice = "blinker")
L = SIR_Lattice(50, lattice = "uniform", immune = 0)
#L = SIR_Lattice(50, lattice = "blobby")
#L = SIR_Lattice(50, lattice = "wave")
probs = (1,0.5,1)
L.run(probs,wait_sweeps = 0, num_tot_sweeps = 10, plot_anim = False)

plt.show()
plt.plot(L.sweep_list, L.frac_inf)
plt.show()


end = time.time()

print("total time:")
print(end-start)

"""

start = time.time()
probs_l_0 = np.linspace(1,0, 20)
probs_l_1= np.linspace(1,0, 20)


n_t_s = 1100
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

        end_arr[j,i] = np.mean(L.frac_inf)
    print(end_arr)
np.savetxt("SIR_avg_I.txt",end_arr,delimiter = ",")

end = time.time()
print("time")
print(start-end)

"""
"""

end_arr = np.flip(np.loadtxt("SIR_avg_I.txt",delimiter = ","), axis = 1)
im = plt.imshow(end_arr, animated=True, cmap="hot", extent=[0,1,0,1])  # Oranges")
plt.colorbar(im)
plt.show()
"""




"""
#immune testing


immunities = np.linspace(0,1,3)

print("hi")
print(immunities)
avg_infs = []
for im in immunities:

    L = SIR_Lattice(50, lattice = "uniform", immune = im)

    probs = (0.5,0.5,0.5)
    L.run(probs,wait_sweeps = 30, num_tot_sweeps = 50, plot_anim = False)


    avg_infs.append(np.mean(L.frac_inf))
    #L.plot_frac_inf(label = str(im))

    #plt.plot(L.sweep_list,L.frac_inf)

plt.title("Fraction of sites infected agaist sweeps ")
plt.xlabel("Sweeps")
plt.ylabel("Immune fraction")
plt.show()

plt.title("Average infected fraction against immunity fraction")
plt.ylabel("Average infected fraction")
plt.xlabel("Immunity fraction")
plt.plot(immunities,avg_infs)
plt.show()
"""
