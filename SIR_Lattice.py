import random
import numpy as np
import matplotlib.pyplot as plt
import copy


class SIR_Lattice(object):
    """
    Class for a SIR_Lattice object
    """

    def __init__(self, N, lattice=None):
        """
        Initialisation function for Lattice class.
        Parameters
        ----------
        N : int
            determines size of square lattce (NxN)
        T : float
            Temperature of lattice. Tested between 1K and 3K

        lattice : numpy array or str
            An option to input starting lattice. Must be of size (NxN).
            Can also input string with options: "uniform" "ground" "halved" (see functions for specifics)
        Returns
        -------
        """

        # initialise variables
        self.N = N


        self.sweep_list = []
        # N**2 is the required length of time between visualisations as in the lecture notes
        self.sweep_size = self.N ** 2



        if type(lattice) == np.ndarray:  # 'numpy.ndarray':
            if lattice.shape == (N, N):
                # print("yeye")
                self.lattice = lattice
            else:
                print("input lattice must be correct shape!!")

        elif lattice == "uniform":
            # assume uniform
            self.lattice = self.uniform_generate()

        elif lattice == "blobby":
            # assume blob
            self.lattice = self.blobby_generate()
        elif lattice == "wave":
            # assume blob
            self.lattice = self.wave_generate()

        self.dynamics = self.SIR



    def uniform_generate(self):

        """
        Generates "uniform" lattice, where each point on the lattice has equal probability of being -1 or 1
        Parameters
        ----------
        Returns
        -------
        a : numpy array
            uiform (NxN) array
        """
        #S, I, R
        a = np.random.choice((0, 1, 10), size=[self.N, self.N], replace=True, p=[1/3, 1/3, 1/3])
        return a

    def wave_generate(self):

        """
        Generates "uniform" lattice, where each point on the lattice has equal probability of being -1 or 1
        Parameters
        ----------
        Returns
        -------
        a : numpy array
            uiform (NxN) array
        """
        #S, I, R
        a = np.zeros((self.N, self.N))
        a[:,15] = 1
        return a

    def blobby_generate(self):

        """
        Generates "uniform" lattice, where each point on the lattice has equal probability of being -1 or 1
        Parameters
        ----------
        Returns
        -------
        a : numpy array
            uiform (NxN) array
        """
        #S, I, R
        a = np.zeros((self.N, self.N))
        a[15:20,15:20] = 1
        return a


    def SIR_stoopid(self):

        NN_sum = self.find_sum_NN()

        possible_contract_matrix = np.where(NN_sum%10>0, 1, 0)#, np.random.uniform(0,1), 0)
        rand_matrix = np.random.uniform(0,1,possible_contract_matrix.shape)
        prob_contract = possible_contract_matrix*rand_matrix

        # if susc
        susc = np.where(self.lattice == 0, 1, 0)

        #if recovered
        recovered = np.where(self.lattice == 10, 1, 0)

        # if infected
        infected = np.where(self.lattice == 0, 1, 0)



        #if recovered, probability of contraction will becomes negative negative.
        #If infected, negative aswell (but doesn't matter)
        #if susc, no change so still uniform between 0 and 1

        prob_contract -= self.lattice


        #!!!! INFECT
        #where probability is still >0 (after checking for immunity and minusing p1), infect
        contract_matrix = np.where(prob_contract - self.p1 > 0, 1, 0)
        self.lattice[contract_matrix] = 1

        # !!!! RECOVER
        self.lattice[infected] = np.where(np.random.uniform(0, 1,self.lattice.shape)-self.p2>0,10,1)[infected]

        # !!!! BECOME SUSC
        self.lattice[recovered] = np.where(np.random.uniform(0, 1,self.lattice.shape)-self.p3>0,0,10)[recovered]








    def find_sum_NN(self):
        NN_sum = np.zeros_like(self.lattice)

        NN_sum += np.roll(self.lattice, 1, axis=0)
        NN_sum += np.roll(self.lattice, -1, axis=0)
        NN_sum += np.roll(self.lattice, 1, axis=1)
        NN_sum += np.roll(self.lattice, -1, axis=1)

        return NN_sum

    def SIR(self):
        # randomly choose a point to assess
        flip_coords = self.rand_flip_coords()


        state = self.lattice[flip_coords[0], flip_coords[1]]

        if state == 0:
            #susc
            NN = [self.lattice[(flip_coords[0]-1)%self.N,flip_coords[1]],self.lattice[(flip_coords[0]+1)%self.N,flip_coords[1]],
                  self.lattice[flip_coords[0],(flip_coords[1]-1)%self.N],self.lattice[flip_coords[0],(flip_coords[1]+1)%self.N]]
            #find if Nearest Neighbours are infected
            NN_inf = False
            for i in NN:
                if i == 1:
                    NN_inf = True



            if NN_inf:

                if np.random.uniform(0,1)-self.p1<0:

                    new_state = 1
                else:
                    new_state = state
            else:
                new_state = state

        elif state == 1:
            #infected

            if np.random.uniform(0,1)-self.p2>0:
                new_state = 10
            else:
                new_state = state
        elif state ==10:
            #recovered

            if np.random.uniform(0,1)-self.p3>0:
                new_state = 0
            else:
                new_state = state
        else:
            print("somethings fucked")
            print(state)

        self.lattice[flip_coords[0], flip_coords[1]] = new_state

    def glauber(self):

        """
        Function to update the lattice with glauber dynamics
        Parameters
        ----------
        Returns
        -------
        """

        # randomly choose a point to possibly flip
        flip_coords = self.rand_flip_coords()

        # find energy corresponding to this point wrt the nearest neighbours
        E_init = self.compute_E(flip_coords)

        # change in E  if flipped is defined by -2*init_E (proven in my notes)
        delta_E = -2 * E_init

        # if energy efficient, change
        if delta_E < 0:
            # flip point
            self.lattice[flip_coords[0], flip_coords[1]] = -1 * self.lattice[flip_coords[0], flip_coords[1]]


        # if energy innefficient, change with probability related to temperature
        else:

            p = min(1, np.exp(-self.beta * delta_E))
            if np.random.uniform(0, 1, 1) <= p:
                self.lattice[flip_coords[0], flip_coords[1]] = -1 * self.lattice[flip_coords[0], flip_coords[1]]



    def rand_flip_coords(self):
        """
        Function to choose a random point on the lattice
        Parameters
        ----------
        Returns
        -------
        rand_coords : numpy array
            [x,y] random point on graph
        """
        # randint is very slow
        r = int(self.N * random.random())
        r_2 = int(self.N * random.random())
        # return np.random.randint(0,self.N,2)
        return np.asarray([r, r_2])





    def plot_lattice(self):

        """
        Function to plot the lattice
        This function uses pyplot not gnuplot or other.
        It does not write to file to simplify the procedure.
        It plots directly from self.lattice.
        Parameters
        ----------
        Returns
        -------
        """

        plt.clf()
        lat = copy.copy(self.lattice)
        lat[lat == 10] = lat[lat == 10]/5

        im = plt.imshow(lat, animated=True, cmap = "hot")#Oranges")
        plt.colorbar(im)
        plt.draw()
        plt.pause(0.001)

    def run(self, probs, wait_sweeps=100, num_tot_sweeps=1000, plot_anim=True):

        """
         Function to run full dynamics given simulation inputs.
         It uses the specified dynamics of the system and simply loops through when required.
         Parameters
         ----------
         wait_sweeps : int
             number of sweeps to wait before starting measurements
        num_total_sweeps : int
            number of total sweeps to run
        plot_anim : bool
            whether or not to animate as it runs. Saves time on long simulations to not animate.
         Returns
         -------
         """
        self.p1,self.p2,self.p3 = probs

        # loop for required number of sweeps
        for i in range(num_tot_sweeps* self.sweep_size):
            # self.N**2 is the required length of time between visualisations as in the lecture notes
            if i % self.sweep_size == 0:
                # if it is time to take a measurement
                if i % (self.sweep_size * 1) == 0 and i >= wait_sweeps * self.sweep_size:

                    self.sweep_list.append(i / self.sweep_size)

                    # plot animation if required
                    if plot_anim:
                        self.plot_lattice()
                # print every 100 sweeps to check the sim progress
                if i % (self.sweep_size * 10) == 0:
                    print(i / self.sweep_size)
            # run dynamics
            self.dynamics()

