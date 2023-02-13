import random
import numpy as np
import matplotlib.pyplot as plt

from Lattice import Lattice


L = Lattice(20, lattice = "glider")

L.run(wait_sweeps = 0, num_tot_sweeps = 50)

plt.show()
plt.plot(L.sweep_list, L.num_activ_sites)
plt.show()


#print(L.glider_pos)
plt.plot(L.sweep_list, L.glider_pos)
plt.show()
#print(L)