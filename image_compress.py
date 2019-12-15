import pickle

from PIL import Image
from bitarray import bitarray

from huffman_coding.HuffmanTree import HuffmanTree

img = Image.open('images/sample.bmp')
data = img.getdata()

print(data.size)
# print(list(data))

data_list = []
for tup in list(data):
    for val in tup:
        data_list.append(val)

# print(data_list)


huffman_tree = HuffmanTree(data=data_list)
huffman_tree.create_tree()
root_node = huffman_tree.root_node
compressed_file_data = huffman_tree.get_compressed_file(key=2)

meta_data = compressed_file_data[0]
bit_array = compressed_file_data[1]

# print(meta_data)

with open('images/metadata.dat', 'wb') as fp:
    pickle.dump(meta_data, fp)

# bit_array = bitarray(binary_presentation)

with open('images/compressed.bin', 'wb') as fp:
    fp.write(bit_array)
