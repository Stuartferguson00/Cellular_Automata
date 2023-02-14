import random
import numpy as np
import matplotlib.pyplot as plt

from Lattice import Lattice


#L = Lattice(50, lattice = "blinker")
L = Lattice(50)

L.run(wait_sweeps = 0, num_tot_sweeps = 1000, plot_anim = True)

plt.show()
plt.plot(L.sweep_list, L.num_activ_sites)
plt.show()


#print(L.glider_pos)
#print(L.sweep_list)
#plt.plot#(L.sweep_list, L.glider_pos)
#plt.show()

"""
end_points = []
for i in range(100):
    L = Lattice(50)
    L.run(wait_sweeps=0, num_tot_sweeps=3000, plot_anim=False)
    end_points.append(L.sweep_list[-1])
    plt.plot(L.sweep_list, L.num_activ_sites)
    #plt.show()
    if i%10 == 0:
        print(i)

print(end_points)
plt.show()
counts, bins = np.histogram(end_points)
plt.stairs(counts, bins)
plt.show()
"""