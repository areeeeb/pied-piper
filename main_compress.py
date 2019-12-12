import pickle
import bitarray
from huffman_coding.HuffmanTree import HuffmanTree


file_data = 'go go gophers'

huffman_tree = HuffmanTree(data=file_data)
huffman_tree.create_tree()

compressed_file = huffman_tree.get_compressed_file(key=2)
binary_presentation = compressed_file[1]
meta_data = compressed_file[0]
print(binary_presentation)

bit_array = bitarray.bitarray(binary_presentation)

print(bit_array)
print(huffman_tree.garbage_bits)

with open('metadata.dat', 'wb') as fp:
    pickle.dump(meta_data, fp)

with open('compressed.bin', 'wb') as fp:
    fp.write(bit_array)
