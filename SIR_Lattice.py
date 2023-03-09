import random
import numpy as np
import matplotlib.pyplot as plt
import copy



class SIR_Lattice(object):
    """
    Class for a SIR_Lattice object
    """

    def __init__(self, N, lattice=None, immune = 0. ):
        """
        Initialisation function for SIR Lattice class.

        Parameters
        ----------

        N : int
            determines size of square lattce (NxN)


        lattice : str
            starting lattice with options: "uniform" or "blobby" (see functions for specifics)

        immune : float
            fraction of cells to start immune

        Returns
        -------

        """
        #initialise variables
        self.immune = immune
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
            # assume blobF
            self.lattice = self.blobby_generate()
        else:
            print("Must provide appropriate lattice input")


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

        probs = [1/3, 1/3,  1/3, self.immune]
        probs = probs / np.sum(probs)
        print(probs)

        a = np.random.choice((0, 1, 10,100), size=[self.N, self.N], replace=True, p=probs)
        return a



    def blobby_generate(self):

        """
        Generates "blobby" lattice, where one area of the lattice begins infected
        Parameters
        ----------
        Returns
        -------
        a : numpy array
            blob (NxN) array
        """
        #S, I, R
        a = np.zeros((self.N, self.N))
        a[15:20,15:20] = 1
        return a




    def find_variance(self, nums = None):

        """
        Function to calculate the variance
        Parameters
        ----------

        nums: optional array
            number or infected accross many sample sweep

        Returns
        -------

        err : float
            error in variance given by jacknife method
        """

        if nums is None:
            nums = np.array(self.num_inf)

        var = (np.mean(nums ** 2) - np.mean(nums) ** 2) / self.N ** 2

        if self.terminate:
            #as if an infinite number of samples were taken, it would go to 0 anyway
            return 0
        else:
            return var

    def jacknife_var(self):
        """
        Function to calculate the error in variance by jacknife method
        Parameters
        ----------

        Returns
        -------

        err : float
            error in variance given by jacknife method
        """

        var = self.find_variance()
        total_nums = self.num_inf



        sums = 0
        for i in range(len(total_nums) - 1):
            mini_nums = np.hstack((total_nums[:i], total_nums[i:-1]))
            # print(Es)
            var_i = self.find_variance(nums=mini_nums)
            sums += (var_i - var) ** 2
        err = np.sqrt(sums)
        return err



    def find_sum_NN(self):

        """
        Finds how many nearest neightbours for the entire lattice

        Parameters
        ----------

        Returns
        -------

        """
        #initialises 0 array, then counts NN by rolling
        NN_sum = np.zeros_like(self.lattice)

        NN_sum += np.roll(self.lattice, 1, axis=0)
        NN_sum += np.roll(self.lattice, -1, axis=0)
        NN_sum += np.roll(self.lattice, 1, axis=1)
        NN_sum += np.roll(self.lattice, -1, axis=1)

        return NN_sum


    def SIR(self):

        """
        Function to do update step for SIRS

        Parameters
        ----------

        Returns
        -------

        """
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
            if np.random.uniform(0,1)-self.p2<0:
                new_state = 10
            else:
                new_state = state
        elif state ==10:
            #recovered

            if np.random.uniform(0,1)-self.p3<0:
                new_state = 0
            else:
                new_state = state
        elif state ==100:
            #immune
            new_state = state

        else:
            print("somethings fucked")
            print(state)

        self.lattice[flip_coords[0], flip_coords[1]] = new_state



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
        It does not write to file to simplify the procedure.
        It plots directly from self.lattice.
        Parameters
        ----------
        Returns
        -------
        """

        plt.clf()


        plt.text(-0.1,-1.1, "Susc: black, Inf: orange, Recov: yellow, Immune: white", fontsize=14)#,        verticalalignment='top')

        lat = copy.copy(self.lattice)
        lat[lat == 10] = 2
        lat[lat == 100] = 3


        im = plt.imshow(lat, animated=True, cmap = "hot", vmin=0, vmax=3,)#Oranges")
        #plt.colorbar(im)
        plt.draw()
        plt.pause(0.1)



    def find_frac_inf(self):

        """
        Finds the fraction of lattice that are infected

        Parameters
        ----------

        Returns
        -------

        """
        
        num_inf = len(self.lattice[self.lattice == 1])
        self.num_inf.append(num_inf)
        frac_inf = num_inf/self.N**2
        self.frac_inf.append(frac_inf)

        if frac_inf ==0:
            self.terminate = True









    def run(self, probs, wait_sweeps=100, num_tot_sweeps=1000, plot_anim=True):

        """
         Function to run full SIRS given simulation inputs.
         It uses the specified dynamics of the system and simply loops through when required.
         Parameters
         ----------
         probs: arraylike
            [p1,p2,p3], the probabilities of S --> I, I-->R AND R --> S
         wait_sweeps : int
             number of sweeps to wait before starting measurements
        num_total_sweeps : int
            number of total sweeps to run
        plot_anim : bool
            whether or not to animate as it runs. Saves time on long simulations to not animate.
         Returns
         -------
         """

        #have to invert the probabilities because I kinda coded it in reverse
        self.p1 =probs[0]
        self.p2 =probs[1]
        self.p3 =probs[2]

        self.frac_inf = []
        self.num_inf = []
        self.terminate = False


        # loop for required number of sweeps
        for i in range(num_tot_sweeps* self.sweep_size):
            # self.N**2 is the required length of time between visualisations as in the lecture notes
            if i % self.sweep_size == 0:

                # if it is time to take a measurement
                if i % (self.sweep_size*10) == 0 and i >= wait_sweeps * self.sweep_size:


                    self.sweep_list.append(i / self.sweep_size)
                    self.find_frac_inf()


                    # plot animation if required
                    if plot_anim:
                        self.plot_lattice()
                # print every 100 sweeps to check the sim progress
                if i % (self.sweep_size * 100) == 0:
                    print(i / self.sweep_size)
                if self.terminate:
                    print("breaking")
                    break
            # run dynamics
            self.dynamics()
        plt.show()
        #self.plot_frac_inf()

