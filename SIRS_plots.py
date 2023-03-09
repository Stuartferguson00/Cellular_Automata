import matplotlib.pyplot as plt

from SIR_Lattice import SIR_Lattice

import time
import numpy as np




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
print(input)
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


plt.plot(orig_immunities,orig_avg_infs, color = "green", marker = "x", markersize = 3,linewidth = 0, label = "Initialisation data", alpha = 0.3)
plt.plot(acc_immunities,acc_avg_infs, color = "green", marker = "x",markersize = 3,linewidth = 0, label = "Accurate data")







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
plt.plot(orig_immunities,orig_avg_infs,  color = "slateblue", marker = "^", markersize = 3, linewidth = 0, label = "Initialisation data", alpha = 0.5)
plt.plot(acc_immunities,acc_avg_infs,  color = "slateblue", marker = "^", markersize = 3, linewidth = 0, label = "Accurate data")
plt.legend()
plt.show()




"""
def find_variance(fracs):
    squared_avg= np.mean(fracs ** 2)
    avg_sqared = np.mean(fracs) ** 2
    var = (squared_avg - avg_sqared) #/ 50**2

    return var

vars  =[]
for i in range(6):
    frac_inf = np.loadtxt("variance_saves_" + str(i) + ".txt", delimiter=",")
    print("frac_inf")
    print(frac_inf)
    plt.plot(np.arange(100,len(frac_inf)*10+100,10),frac_inf)
    vars.append(find_variance(frac_inf))
plt.show()

probs = np.linspace(0.2,0.5, i+1)
plt.plot(probs,vars )

plt.show()

"""








"""



probs_l_0  = np.linspace(1,0,10)
probs_l_1  = np.linspace(0,1,10)
end_arr = np.zeros((len(probs_l_0),len(probs_l_1)))

for i in range(len(probs_l_0)):
    for j in range(len(probs_l_1)):
        end_arr[i,j] = probs_l_0[i]


print(end_arr)


im = plt.imshow(end_arr, animated=True, cmap="hot", extent=[0,1,0,1])  # Oranges")
plt.colorbar(im)
plt.show()
"""