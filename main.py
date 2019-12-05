from huffman_coding import tree

dic = {'M': 1, 'I': 5, 'S': 4, 'P': 2, 'R': 2, 'V': 1, 'E': 1, ' ': 1}

huffman_tree = tree.Tree(dic)
huffman_tree.create_tree()

huffman_tree.encode_elements()

print(huffman_tree.encoded_elements)
