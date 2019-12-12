import pickle
import bitarray
from huffman_coding.HuffmanTree import HuffmanTree


string = 'Mississippi river'

compression_huffman_tree = HuffmanTree(string)
compression_huffman_tree.create_tree()

compressed_file = compression_huffman_tree.get_compressed_file(key=2)
binary_presentation = compressed_file[1]
meta_data = compressed_file[0]
print(binary_presentation)

bit_array = bitarray.bitarray(binary_presentation)
# for bit in binary_presentation:
#     bit_array.append(bit)

print(bit_array)
print(compression_huffman_tree.garbage_bits)
# for i in range(0, len(binary_presentation)):
#     byte_array.append(int(binary_presentation[i]))

with open('metadata.dat', 'wb') as fp:
    pickle.dump(meta_data, fp)

with open('testing2.bin', 'wb') as fp:
    fp.write(bit_array)
