import pickle

from PIL import Image
from bitarray import bitarray

from huffman_coding.HuffmanTree import HuffmanTree

img = Image.open('images/red.jpg')
data = img.getdata()

print(data.size)

huffman_tree = HuffmanTree(data=list(data))
huffman_tree.create_tree()
root_node = huffman_tree.root_node
compressed_file_data = huffman_tree.get_compressed_file(key=2)

meta_data = compressed_file_data[0]
bit_array = compressed_file_data[1]

with open('images/metadata.dat', 'wb') as fp:
    pickle.dump(meta_data, fp)

# bit_array = bitarray(binary_presentation)

with open('images/compressed.bin', 'wb') as fp:
    fp.write(bit_array)


# img_copy = Image.new('RGB', data.size)  # Creating new RGB image object for
# # the original image size
#
# img_copy.putdata(data)  # Putting the original image's data to the new image
# object

# pixels_dict = {}

# for tup in list(data):
#     if tup in pixels_dict:
#         pixels_dict[tup] = pixels_dict[tup] + 1
#         continue
#     pixels_dict[tup] = 1


# with open('images/test.metadata', 'wb') as fp:
#     pickle.dump(pixels_dict, fp)

# img_copy.save('images/copy.png')
