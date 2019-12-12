from bitarray import bitarray
import pickle

from huffman_coding.HuffmanTree import HuffmanTree

with open('metadata.dat', 'rb') as fp:
    meta_deta = pickle.load(fp)

print('this is metadeta')
print(meta_deta)

huffman_tree = HuffmanTree(elements_dict=meta_deta)

compressed_file_data = huffman_tree.read_and_get_from_file('compressed.bin')
encoded_data = compressed_file_data['encoded_data']

huffman_tree.decompress(encoded_file_text=encoded_data)
print('Decoded Text')
print(huffman_tree.decoded_data)
