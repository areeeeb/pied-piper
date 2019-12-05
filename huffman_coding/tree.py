import collections

from .node import Node


class Tree:
    nodes_list = []
    base_nodes = []
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
        for key in self.elements_dict:
            node = Node(value=key,
                        frequency=self.elements_dict[key],
                        is_leaf=True)
            self.nodes_list.append(node)
        self.base_nodes = self.nodes_list.copy()

    def insert_single_node(self, node):
        """Inserts a single node into the nodesList in the sorted manner"""
        # if len(self.nodesList) == 0:
        #     self.nodesList.append(node)

        for i in range(len(self.nodes_list)):
            if self.nodes_list[i].frequency > node.frequency:
                self.nodes_list.insert(i, node)
                return
        self.nodes_list.append(node)

    def create_tree(self):
        self.create_base_nodes()
        i = 0
        """Creates huffman tree based on 'elements_dict'"""
        while len(self.nodes_list) > 1:
            left_node = self.nodes_list[i]
            right_node = self.nodes_list[i + 1]
            left_node.is_left_child = True
            right_node.is_right_child = True
            combined_frequency = left_node.frequency + right_node.frequency
            current_node = Node(left=left_node,
                                right=right_node,
                                frequency=combined_frequency)
            current_node.left.parent = current_node
            current_node.right.parent = current_node
            # Deleting the first two nodes that are in the current_node
            if len(self.nodes_list) > 1:
                del self.nodes_list[0:2]
            self.insert_single_node(current_node)
        self.root = self.nodes_list[0]

    def encode_elements(self):
        """Maps the binary encoding of the corresponding element into a dic"""
        binary_encoding = []

        for i in range(len(self.base_nodes)):
            current_node = self.base_nodes[i]
            while current_node.parent != None:
                if current_node.is_left_child:
                    binary_encoding.insert(0, '0')
                if current_node.is_right_child:
                    binary_encoding.insert(0, '1')
                current_node = current_node.parent

            self.encoded_elements[self.base_nodes[i].value] = binary_encoding.\
                copy()
            binary_encoding = []
