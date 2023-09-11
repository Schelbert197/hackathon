from random import choice
import matplotlib.pyplot as plt
import numpy as np

class RandomTree:
    """A class to generate random trees"""

    def __init__(self, K=100):
        """initialize some attributes of the tree"""

    self.k = K # Number of vertices used
    self.q_init = (50, 50)
    self.delta = 1

    self.q_near = []


    def get_q_rand():
        """Generate the random points"""

        for x in range(0,self.k):
            # find a point

            # find the nearest vertex

            # add point to array



    def plot_tree(self.x_axis=100, y_axis=100):
        """Plot the tree with the defined size"""

        plt.style.use('seaborn')
        fig, ax = plt.subplots()

        # Set the range for each axis
        ax.axis([0, x_axis, 0, y_axis])

        plt.show()