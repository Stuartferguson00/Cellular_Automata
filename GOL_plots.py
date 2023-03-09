import matplotlib.pyplot as plt

from SIR_Lattice import SIR_Lattice

import time
import numpy as np

def main():


    """
    Function to plot relevant graphs for GOL


    Parameters
    ----------

    Returns
    -------


    """

    end_points = np.loadtxt("GOL_hist_data.txt",delimiter = ",")
    #end_points = [447, 1029, 525, 453, 272, 528, 886, 953, 528, 154, 387, 383, 820, 564, 393, 1414, 159, 225, 891, 280, 1031, 980, 457, 306, 1069, 781, 876, 2069, 168, 272, 133, 234, 1204, 966, 710, 430, 327, 912, 215, 254, 356, 323, 679, 236, 387, 1287, 828, 795, 576, 274, 380, 700, 797, 607, 1158, 207, 1552, 904, 137, 665, 226, 129, 205, 174, 1540, 1033, 2002, 636, 270, 356, 547, 1043, 119, 440, 447, 756, 576, 626, 462, 739, 875, 1391, 405, 1059, 439, 117, 506, 60, 1167, 561, 527, 602, 686, 953, 1784, 976, 470, 1405, 406, 743, 450, 382, 730, 119, 1072, 847, 157, 1015, 558, 1164, 1073, 596, 390, 650, 488, 266, 409, 304, 173, 377, 523, 215, 1147, 371, 495, 259, 1433, 576, 380, 905, 431, 266, 166, 1311, 703, 37, 638, 172, 387, 1246, 83, 587, 787, 571, 712, 230, 710, 229, 234, 965]
    counts, bins = np.histogram(end_points,50)
    plt.title("Histogram of time needed to equilibrate")
    plt.xlabel("time")
    plt.ylabel("counts")
    plt.stairs(counts, bins)
    plt.show()


if __name__ == "__main__":

    main()
