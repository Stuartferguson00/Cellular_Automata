import matplotlib.pyplot as plt

from SIR_Lattice import SIR_Lattice


#L = Lattice(50, lattice = "blinker")
#L = SIR_Lattice(50, lattice = "uniform")
L = SIR_Lattice(50, lattice = "blobby")
#L = SIR_Lattice(50, lattice = "wave")
probs = (0.6,1,0)
L.run(probs,wait_sweeps = 0, num_tot_sweeps = 200, plot_anim = True)

plt.show()
#plt.plot(L.sweep_list, L.num_activ_sites)
#plt.show()


