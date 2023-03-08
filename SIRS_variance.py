import matplotlib.pyplot as plt

from SIR_Lattice import SIR_Lattice

import time
import numpy as np




start = time.time()


#weird order of 0 and 1 is purely because of how imshow works
probs_l_0 = np.linspace(0.2,0.5, 30)





n_t_s = 10100
#n_t_s = 1100
w_s = 100

var_arr = np.zeros((len(probs_l_0)))
err_arr = np.zeros((len(probs_l_0)))

size = 50 #ie N = 50

for i in range(len(probs_l_0)):
    start = time.time()
    #L = Lattice(50, lattice = "blinker")
    L = SIR_Lattice(size, lattice = "uniform")
    #L = SIR_Lattice(50, lattice = "blobby")
    #L = SIR_Lattice(50, lattice = "wave")
    probs = (probs_l_0[i],0.5,0.5)
    L.run(probs,wait_sweeps = w_s, num_tot_sweeps = n_t_s, plot_anim = False)

    #res_arr[i] = np.mean(L.frac_inf)
    #fracs = np.array(L.frac_inf)
    #var_arr[i] = (np.mean(fracs**2)-np.mean(fracs)**2)/size**2
    print("number of samples:")
    print(len(L.num_inf))
    print(L.num_inf)

    var_arr[i] = L.find_variance()
    err_arr[i] = L.jacknife_var()

    if  L.frac_inf[0] == 0:
        L.frac_inf.append(0)
    #np.savetxt("variance_saves_"+str(i)+".txt", L.num_inf, delimiter=",")

print(var_arr)
output = [probs_l_0, var_arr, err_arr]

print("output")
print(output)
#np.savetxt("SIRS_variance.txt",output,delimiter = ",")

end = time.time()
print("time")
print(start-end)
