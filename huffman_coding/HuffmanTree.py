import collections

from .node import Node


class HuffmanTree:
    elements_dict = {}
    elements_length = 0
    nodes_list = []
    base_nodes = []
    encoded_elements = {}
    encoded_text = ''
    decoded_text = ''
    root_node = None
    garbage_bits = 0

    def __init__(self, text='', elements_dict=None):
        """
        DO NOT ENTER BOTH ARGUMENTS, ONLY ONE OF THEM IS NEEDED FOR IT TO WORK
        elements_dict is the dictionary of values and their frequencies.
        :type text: str
        :type elements_dict: dict
        """
        self.text = text
        if text:
            # if user entered text then create elements_dict
            self.create_elements_dict()
        else:
            self.elements_dict = elements_dict
            self.garbage_bits = elements_dict.pop('g_bits')

    def create_elements_dict(self):
        """Creates elements_dict based on the text"""
        for char in self.text:
            if char in self.elements_dict:
                self.elements_dict[char] += 1
                continue
            self.elements_dict[char] = 1
        self.elements_length = len(self.elements_dict)

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
            right_node = self.nodes_list[i+1]
            left_node.is_left_child = True
            right_node.is_right_child = True
            combined_frequency = left_node.frequency + right_node.frequency
            current_node = Node(left=left_node,
                                right=right_node,
                                frequency=combined_frequency)
            current_node.left.parent = current_node
            current_node.right.parent = current_node
            # Deleting the first two nodes that are in the current_node
            del self.nodes_list[0:2]
            self.insert_single_node(current_node)

        self.root_node = self.nodes_list[0]

    def encode_elements(self):
        """Maps the binary encoding of the corresponding element into a dic"""
        # binary_encoding = []
        # binary_encoding = ''

        for i in range(len(self.base_nodes)):
            binary_encoding = ''
            current_node = self.base_nodes[i]
            while current_node.parent is not None:
                if current_node.is_left_child:
                    # binary_encoding.insert(0, '0')
                    binary_encoding = '0' + binary_encoding
                if current_node.is_right_child:
                    # binary_encoding.insert(0, '1')
                    binary_encoding = '1' + binary_encoding
                current_node = current_node.parent

            self.encoded_elements[self.base_nodes[i].value] = binary_encoding

    def compress(self, key):
        """Compresses the string in text"""
        self.encode_elements()
        for char in self.text:
            # self.compressed_text += ''.join(self.encoded_elements[char])
            self.encoded_text += self.encoded_elements[char]
        binary_key = bin(key)[2:]
        starting_bits = '0' * (8 - len(binary_key))
        binary_key = starting_bits + binary_key
        self.encoded_text = binary_key + self.encoded_text

        self.garbage_bits = 8 - (len(self.encoded_text) % 8)
        # TODO: delete line below it
        self.elements_dict['g_bits'] = self.garbage_bits

    def decompress(self, encoded_file_text):
        """Decompresses the file based on elements_dict"""
        self.create_tree()
        # current_node = self.root_node

        for i in range(self.garbage_bits):
            encoded_file_text = encoded_file_text[:-1]

        while len(self.decoded_text) != self.root_node.frequency:
            current_node = self.root_node
            while not current_node.is_leaf:
                if encoded_file_text[0] == '0':
                    current_node = current_node.left
                    encoded_file_text = encoded_file_text[1:]
                    continue
                if encoded_file_text[0] == '1':
                    current_node = current_node.right
                    encoded_file_text = encoded_file_text[1:]
                    continue
            self.decoded_text = self.decoded_text + current_node.value

    def get_compressed_file(self, key):
        """Returns the compressed file which contains compressed_text and
         encoded_elements"""
        self.compress(key)
        return [self.elements_dict, self.encoded_text]

    def __repr__(self):
        return f'root_node(frequency: {self.root_node.frequency})'