# Cellular_Automata


This repository hold aGame of life and a SIRS simulation aswell as example results.

Example results are for a simulation of a (50x50) lattice

# Running simulations

Game_Of_Life.py and SIRS.py can be called as basic simulations from the commandline, with both requiring arguments that determine the parameters of their respective Ising simulations.

Visualisation is also optional, chosen through a commandline argument. It is normally switched off during long computation to save time, and can be turned on to qualitatively study behaviour.

Results for specific experiments are saved to respective files, which are called by SIR_plots.py or GOL_plots.py 

Simple example usage from terminal:
To run SIRS at N = 50, probabilities(p1 = 0.1, p2 = 0.2, p3 = 0.3), 100 total sweeps, 10% of population immune ,no animation

>Python SIRS.py 50, 0.1, 0.2, 0.3, 100, 0.1, True 


Similar could be done with Game_Of_Life.py



# Code structure and usage details

Each simulation has an individualised latttice class, which encloses the dynamics and calculations of the simulation
All specific experiments are conducted on tertiary python files, the results of which can be seen by using the plotting python files
Code was written and tested on python 3.8 using pycharm IDE. 
