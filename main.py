from huffman_coding import tree
import pickle


string = 'mississippi river mississippi river mississippi river mississippi river'

huffman_tree = tree.Tree(string)
huffman_tree.create_tree()

compressed_file = huffman_tree.get_compressed_file()
binary_presentation = compressed_file[1]


with open('testing.bin', 'wb') as fp:
    # pickle.dump(int(binary_presentation), fp)
    for i in range(len(binary_presentation)):
        fp.write(bytearray(int(binary_presentation[i])))

with open('test.txt', 'wb') as fp:
    pickle.dump(int(binary_presentation), fp)

