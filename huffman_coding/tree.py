import collections

from .node import Node


class Tree:
    nodesList = []
    root = None
    encoded_elements = {}

    def __init__(self, elements_dict):
        """
        elements_dict is the dictionary of values and their frequencies.
        :type elements_dict: dict
        """
        self.elements_dict = elements_dict
        self.elements_length = len(elements_dict)

    def sort_elements_dict(self):
        """This method sorts the elements_dict in ascending order based on the
        frequencies"""
        # Creating a sorted list of tuples of value and frequency
        sorted_list = sorted(self.elements_dict.items(), key=lambda kv: kv[1])
        # Converting the list of tuples into dictionary
        self.elements_dict = collections.OrderedDict(sorted_list)

    def create_base_nodes(self):
        """Creates base (leaf) nodes of the tree"""
        self.sort_elements_dict()
        for value in self.elements_dict:
            node = Node(value=value,
                        frequency=self.elements_dict[value],
                        is_leaf=True)
            self.nodesList.append(node)

    def insert_single_node(self, node):
        """Inserts a single node into the nodesList in the sorted manner"""
        # if len(self.nodesList) == 0:
        #     self.nodesList.append(node)

        for i in range(len(self.nodesList)):
            if self.nodesList[i].frequency > node.frequency:
                self.nodesList.insert(i, node)
                break
        else:
            self.nodesList.append(node)

    def create_tree(self):
        self.create_base_nodes()
        i = 0
        """Creates huffman tree based on 'elements_dict'"""
        while len(self.nodesList) > 1:
            combined_frequency = self.nodesList[i].frequency + \
                                 self.nodesList[i+1].frequency
            current_node = Node(left=self.nodesList[i],
                                right=self.nodesList[i+1],
                                frequency=combined_frequency)
            # Deleting the first two nodes that are in the current_node
            if len(self.nodesList) > 1:
                del self.nodesList[0:2]
            self.insert_single_node(current_node)

        self.root = self.nodesList[0]

    def map_encoding(self):
        """Maps the binary encoding of the corresponding element into a dic"""
        binary_encoding = ''
        current_node = self.root
        while len(self.encoded_elements) < self.elements_length:
            if current_node.is_leaf:
                self.encoded_elements[current_node.value] = binary_encoding

            while not current_node.is_leaf:
                if current_node.left is not None:
                    binary_encoding += '0'
                    current_node = current_node.left
                    continue

