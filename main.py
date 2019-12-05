from huffman_coding import tree


string = 'mississippi river'

huffman_tree = tree.Tree(string)
huffman_tree.create_tree()

huffman_tree.encode_elements()

print(huffman_tree.encoded_elements)
