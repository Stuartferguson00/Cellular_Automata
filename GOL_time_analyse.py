import numpy as np
import matplotlib.pyplot as plt

from GOL_Lattice import GOL_Lattice


end_points = []
for i in range(100):
    L = GOL_Lattice(50)
    L.run(wait_sweeps=0, num_tot_sweeps=5000, plot_anim=False)
    end_points.append(L.sweep_list[-1])
    #plt.plot(L.sweep_list, L.num_activ_sites)
    #plt.show()
    if i%10 == 0:
        print(i)

print(end_points)
#plt.show()

