import matplotlib.pyplot as plt

from SIR_Lattice import SIR_Lattice

import time
import numpy as np




"""
input = np.loadtxt("avg_inf_immunities_data.txt", delimiter = ",")

avg_infs = input[0]
immunities= input[1]

plt.title("Average infected fraction against immunity fraction")
plt.ylabel("Average infected fraction")
plt.xlabel("Immunity fraction")
plt.plot(immunities,avg_infs)
plt.show()

"""


"""
#
#end_arr = np.flip(np.loadtxt("SIR_avg_I.txt",delimiter = ","), axis = 1)
end_arr =np.loadtxt("SIRS_phase_avg_inf.txt",delimiter = ",")
im = plt.imshow(end_arr, animated=True, cmap="hot", extent=[0,1,0,1])  # Oranges")
plt.colorbar(im)
plt.show()
"""





input = np.loadtxt("SIRS_variance.txt", delimiter = ",")
print(input)
probs = input[0]
var = input[1]
#var_errs= input[2]

plt.title("")
plt.ylabel("Variance")
plt.xlabel("Prob_1")
plt.plot(probs,var)
plt.show()













"""
probs_l_0  = np.linspace(1,0,10)
probs_l_1  = np.linspace(0,1,10)
end_arr = np.zeros((len(probs_l_0),len(probs_l_1)))

for i in range(len(probs_l_0)):
    for j in range(len(probs_l_1)):
        end_arr[i,j] = probs_l_1[j]


print(end_arr)


im = plt.imshow(end_arr, animated=True, cmap="hot", extent=[0,1,0,1])  # Oranges")
plt.colorbar(im)
plt.show()
"""