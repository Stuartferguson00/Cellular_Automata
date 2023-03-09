import random
import numpy as np
import matplotlib.pyplot as plt






    
    
class GOL_Lattice(object):
    """
    Class for a Game of Life Lattice object

    """
    def __init__(self, N, dynamics = "GOL", lattice = None):
        """
        Initialisation function for Lattice class.

        Parameters
        ----------

        N : int
            determines size of square lattce (NxN)

        dynamics : str
            Dynamics to use within the simulation, options are "GOL"

        lattice : numpy array or str
            An option to input starting lattice. Must be of size (NxN).
            Can also input string with options: "uniform" "blinker" "glider" (see functions for specifics)

        Returns
        -------


        """

        #initialise variables
        self.N = N
        self.num_activ_sites = []


        self.sweep_list = []
        #N**2 is the required length of time between visualisations as in the lecture notes
        #self.sweep_size = self.N**2

        #this isnt necessary anymore, but no harm
        if dynamics == "GOL":
            self.dynamics = self.game_of_life
        else:
            print("here becaus eyou havent done this yet")


        #set innactive stop (for if the sim should stop if innactive)
        #set lattice
        self.glider_meas = False
        if type(lattice) == np.ndarray:#'numpy.ndarray':
            if lattice.shape == (N,N):
                #print("yeye")
                self.lattice = lattice
                self.innactive_stop = True
            else:
                print("input lattice must be correct shape!!")
        elif lattice is None:
            #assume uniform
            self.innactive_stop = True
            self.lattice = self.uniform_generate()
        elif lattice == "uniform":
            self.innactive_stop = True
            self.lattice = self.uniform_generate()
        elif lattice == "glider":
            self.innactive_stop = False
            self.glider_meas = True
            self.lattice = self.glider_generate()
        elif lattice == "blinker":
            self.innactive_stop = False
            self.lattice = self.blinker_generate()
        else:
            print("your lattice input is wrong")

        #vectorise update function
        self.vec_update_point_gol = np.vectorize(self.update_point_gol)



    def blinker_generate(self):

        """
        Generates "blinker" lattice, where the lattice has been layed out speciffically to show one blinker

        Parameters
        ----------

        Returns
        -------

        """


        blinker_lattice = np.zeros((self.N,self.N))
        if self.N<3:
            print("lattice is too small")
        blinker_lattice[0,1] = 1
        blinker_lattice[1,1] = 1
        blinker_lattice[2,1] = 1
        return blinker_lattice

    def glider_generate(self):

        """
        Generates "blinker" lattice, where the lattice has been layed out specifically to show one glider,
        starting at the origin and moving diagonally

        Parameters
        ----------

        Returns
        -------

        """

        glider_lattice = np.zeros((self.N, self.N))
        if self.N < 3:
            print("lattice is too small")
        glider_lattice[0, 1] = 1
        glider_lattice[1, 2] = 1
        glider_lattice[2, 1] = 1
        glider_lattice[2, 0] = 1
        glider_lattice[2, 2] = 1
        return glider_lattice

    def game_of_life(self):
        """
        GOL dynamics function

        Parameters
        ----------

        Returns
        -------

        """

        #assumes dead = 0 and alive = 1
        #sums nearest enighbours of each point
        NN_sum = self.find_sum_NN()

        #updates according to NN
        new_lattice  = self.update_gol(NN_sum)

        #finds numbe rof active sites (for possible termination)
        self.num_activ_sites.append(self.N**2-np.sum(np.isclose(self.lattice,new_lattice)))

        #update lattice
        self.lattice = new_lattice


    def update_gol(self, NN_sum):

        """
        updates according to GOL rules

        Parameters
        ----------
        NN_sum : array
            lattice of NN neighbour sums
        Returns
        -------

        """

        next_step = self.vec_update_point_gol(self.lattice, NN_sum)

        return next_step



    def update_point_gol(self, bef, sums):


        """
        lays out update rules will be vectorized

        Parameters
        ----------
        bef: int
            alive or dead (binary)
        sum: int
            numbe rof NN
        Returns
        -------

        """


        if bef == 0:
            #cell is dead
            if sums == 3:
                #becomes alive
                aft = 1
            else:
                #stays dead
                aft = 0
        elif bef ==1:
            if sums <2:

                #dies
                aft = 0
            elif sums >3:
                #dies
                aft = 0
            elif sums ==2 or sums == 3:
                #stays alive
                aft = 1
            else:
                print("you have fucked something else up")
        else:
            print("you have fucked something up")
        return aft

    def find_sum_NN(self):


        """
        finds how many nearest neightbours for the entire lattice

        Parameters
        ----------

        Returns
        -------

        """

        #zero array
        NN_sum = np.zeros_like(self.lattice)


        #use rolls to find NN sums
        NN_sum += np.roll(self.lattice, 1, axis=0)
        NN_sum += np.roll(self.lattice, -1, axis=0)
        NN_sum += np.roll(self.lattice, 1, axis=1)
        NN_sum += np.roll(self.lattice, -1, axis=1)


        NN_sum += np.roll(self.lattice, (1, 1), axis=(0,1))
        NN_sum += np.roll(self.lattice, (1, -1), axis=(0, 1))
        NN_sum += np.roll(self.lattice, (-1, 1), axis=(0, 1))
        NN_sum += np.roll(self.lattice, (-1, -1), axis=(0, 1))

        return NN_sum







       

    def uniform_generate(self):

        """
        Generates "uniform" lattice, where each point on the lattice has equal probability of being -1 or 1

        Parameters
        ----------

        Returns
        -------
        a : numpy array
            uniform (NxN) array
        """
        a = np.random.choice((1,0), size=[self.N,self.N], replace=True, p=[0.5,0.5])
        return a
    
    def ground_generate(self):

        """
        Generates "ground" lattice, where every point on the lattice is set to 1,
        not used, or properly coded at th moment

        Parameters
        ----------

        Returns
        -------
        a : numpy array
            uniform (NxN) array
        """


        #a = np.rint(np.random.uniform(0,1,(self.N,self.N))).astype(int)
        #a = np.where(a == 1,a,-1)
        a = np.ones((self.N,self.N))
        return a

    def find_glider_pos(self):
        #this is extremely bad coding
        pos_list = []
        for i in range(self.N):
            for j in range(self.N):
                if self.lattice[i,j] == 1:
                    if i%self.N >1 and j%self.N >1:
                        pos_list.append(np.sqrt(i**2+j**2))
                    else:
                        #if boundary condition
                        return None
        r_cm = np.sum(pos_list)/len(pos_list)
        return r_cm
    

    
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

        plt.cla()
        plt.imshow(self.lattice, animated=True)
        plt.draw()
        plt.pause(0.00001)
        
        
        
    def run(self,wait_sweeps = 100, num_tot_sweeps = 1000, plot_anim = True):

        """
        Function to run GOL simulation

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
        if self.glider_meas:
            self.glider_pos = []

        #loop for required number of sweeps
        for i in range(num_tot_sweeps):

            #print(i)
            #if it is time to take a measurement
            if i%1 == 0 and i >= wait_sweeps:
                self.sweep_list.append(i)
                #plot animation if required
                if plot_anim:
                    #print(i)
                    self.plot_lattice()
                if self.glider_meas:
                    self.glider_pos.append(self.find_glider_pos())

            #print every 100 sweeps to check the sim progress
            if i%100 == 0:
                pass
                print(i)
            #run dynamics
            self.dynamics()
            if len(self.sweep_list)>3:
                if self.innactive_stop and len(self.num_activ_sites)>10:
                    if  np.all(np.isclose(self.num_activ_sites[-9:], self.num_activ_sites[-10])):
                        print("its done now so stop!!")
                        return

    
        


        

            
