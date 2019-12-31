import pickle
from huffman_coding.HuffmanTree import HuffmanTree


file_data = 'mississippi river'

# In case of text compression, we give data to the constructor
huffman_tree = HuffmanTree(data=file_data)
huffman_tree.create_tree()

compressed_file_data = huffman_tree.get_compressed_file(key=2)
meta_data = compressed_file_data[0]
bit_array = compressed_file_data[1]
# print(binary_presentation)
#
# bit_array = bitarray.bitarray(binary_presentation)

print(bit_array)
print(huffman_tree.garbage_bits)

with open('metadata.dat', 'wb') as fp:
    pickle.dump(meta_data, fp)

with open('compressed.bin', 'wb') as fp:
    fp.write(bit_array)
