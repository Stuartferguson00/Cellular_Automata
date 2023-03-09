
import numpy as np
import matplotlib.pyplot as plt

from GOL_Lattice import GOL_Lattice



#L = GOL_Lattice(50, lattice = "blinker")
L = GOL_Lattice(50, lattice = "glider")
#L = GOL_Lattice(50)

L.run(wait_sweeps = 0, num_tot_sweeps = 100, plot_anim = True)

plt.show()
plt.title("Glider distance from origin with sweeps")
plt.ylabel("Position of glider center of mass")
plt.xlabel("Sweep")
plt.plot(L.sweep_list, L.glider_pos)

time = 10 #sweeps
pos = np.array(L.glider_pos)
distance = pos[7+time]-pos[7]
velocity = distance/time

print("The velocity of the glider")
print(velocity)
#print(np.sqrt((50**2)+(50**2))/200)
print("please note that this is equivalent to: "+str(velocity/np.sqrt(2))+" if considering one diagonal step to be equal in distance to one step")
plt.show()