

from turtle import position


class TreeNode:
    def __init__(self, position, parent):
        self.position = position
        self.children = []
        self.parent = parent

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_node_list(self):
        print(f"{self.position}, Parent: {self.parent}, Children: {self.children}")
        
    def traverse(self):
        nodes_to_visit = self
        while len(nodes_to_visit >0):
            current_node = nodes_to_visit.pop()
            # do stuff here
            nodes_to_visit += current_node.children