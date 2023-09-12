from random import choice, randrange
from tree_node import TreeNode
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import math
import numpy as np

class RandomTree:
    """A class to generate random trees"""

    def __init__(self, K=100):
        """initialize some attributes of the tree"""

        self.k = K # Number of vertices used
        self.q_init = [50, 50]
        self.delta = 1

        self.node1 = TreeNode(self.q_init, None)

        self.xs = [self.q_init[0]]
        self.ys = [self.q_init[1]]

        self.segments = []
        #self.line_coll = 
        self.nodes = [self.node1]
        #self.fake_node_pos = [[0.4, 9.8], [99.1, 89.2], [1.3, 98.4], [84.3, 3.0]]
        self.node_pos = [self.q_init]


    def get_q_rand(self):
        """Generate the random points"""

        q_rand = [randrange(0,100), randrange(0, 100)]
        #print(q_rand)
        return q_rand

    def closest_node(self):
        """Return the closest node from a random point"""
        new_point = self.get_q_rand()
        distances = []
        min_dist = 0
        index_no = 0

        # Find shortest distance in the list of distances and change 
        # the index no to be that point
        for node_no in range(len(self.node_pos)):
            dist = math.dist(new_point, self.node_pos[node_no])
            
            distances.append(dist)

            if dist == min(distances):
                index_no = node_no
                min_dist = dist
            
        #print(new_point)
        delta_x = new_point[0] - self.node_pos[index_no][0]
        delta_y = new_point[1] - self.node_pos[index_no][1]
        new_node_posx = self.node_pos[index_no][0] + delta_x/min_dist
        new_node_posy = self.node_pos[index_no][1] + delta_y/min_dist
        new_node_pos = [new_node_posx * self.delta, new_node_posy*self.delta]

        # # Append the segments array to include new line
        

        return index_no, new_node_pos
        #print(index_no, new_node_pos)

    def create_node(self, pos, parent):
        node = TreeNode(pos, parent)
        parent.add_child(node)


    def plot_G(self, x_axis=100, y_axis=100):
        """Plot the tree with the defined size"""



        # """create line segments"""
        # for point in range(1,4):
        #     self.segments.append(np.array([[self.xs[0], self.ys[0]],[self.xs[point],self.ys[point]]]))
            

        line_coll = LineCollection(self.segments)
        print(type(line_coll))

        plt.style.use('seaborn')
        fig, ax = plt.subplots()

        # add line segments to plot
        ax.add_collection(line_coll)

        # Set the range for each axis
        ax.axis([0, x_axis, 0, y_axis])
        ax.scatter(self.xs, self.ys)
        plt.show()

    def create_tree(self, k):

        for i in range(0, k):
            # Create a random point, node, and return nearest node index and new node position
            index, pos = self.closest_node()

            # append new node position to points
            self.xs.append(pos[0])
            self.ys.append(pos[1])

            # Append node pos array
            self.node_pos.append(pos)

            # create new node instance
            print(index)
            print(f"length of nodes list is: {len(self.nodes)}")
            self.nodes.append(TreeNode(pos, self.nodes[index]))

            print(self.nodes[index].position)

            # Append line segments array
            self.segments.append(np.array([self.nodes[index].position, pos]))

        # Create plot
        self.plot_G()








thing = RandomTree()
#thing.plot_G()
thing.node1.print_node_list()
#thing.closest_node()
thing.create_tree(500)
