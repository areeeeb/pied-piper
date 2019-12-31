import pickle

from huffman_coding.HuffmanTree import HuffmanTree


# Giving the compressed file to the huffman_tree for it to be decompressed
# using meta_data
compressed_file_data = HuffmanTree.read_and_get_from_file('compressed.bin')
encoded_data = compressed_file_data['encoded_data']
key = compressed_file_data['key']
print(key)

# After getting the key, get the corresponding meta_data
with open('metadata.dat', 'rb') as fp:
    meta_data = pickle.load(fp)

print('this is metadata')
print(meta_data)

# In case of decompression, we provide elements_dict (aka meta_data)
# creating huffman tree obj using the meta_data
huffman_tree = HuffmanTree(elements_dict=meta_data, is_decompression=True)

# decompress function requires encoded_data as argument
huffman_tree.decompress(encoded_file_data=encoded_data)
print('Decoded Text')
print(huffman_tree.decoded_data)
