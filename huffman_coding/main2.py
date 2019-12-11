import pickle
import bitarray
from huffman_coding import tree


string = 'mississippi river'

huffman_tree = tree.Tree(string)
huffman_tree.create_tree()

compressed_file = huffman_tree.get_compressed_file(key=2)
binary_presentation = compressed_file[1]
print(binary_presentation)

bit_array = bitarray.bitarray(binary_presentation)
# for bit in binary_presentation:
#     bit_array.append(bit)

print(bit_array)

# for i in range(0, len(binary_presentation)):
#     byte_array.append(int(binary_presentation[i]))

with open('metadata.dat', 'wb') as fp:
    pickle.dump(huffman_tree, fp)

with open('testing2.bin', 'wb') as fp:
    fp.write(bit_array)
