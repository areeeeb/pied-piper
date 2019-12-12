from bitarray import bitarray
import pickle

from huffman_coding.HuffmanTree import HuffmanTree


bit_array = bitarray()

with open('testing2.bin', 'rb') as fp:
    bit_array.fromfile(fp)

with open('metadata.dat', 'rb') as fp:
    meta_deta = pickle.load(fp)

print('this is metadeta')
print(meta_deta)


print('Whole File')
print(bit_array)

key = bit_array[:8]
print('Key')
print(key)

binary_presentation = bit_array[8:]

binary_presentation_length = len(binary_presentation)

byte_presentation = binary_presentation.tobytes()
byte_presentation_int = int.from_bytes(binary_presentation,
                                       byteorder='big',
                                       signed=False)
encoded_text = bin(byte_presentation_int)[2:]

significant_bits_length = binary_presentation_length - len(encoded_text)
significant_bits = '0' * significant_bits_length
encoded_text = significant_bits + encoded_text


print('Encoded Text')
print(encoded_text)


huffman_tree = HuffmanTree(elements_dict=meta_deta)
huffman_tree.decompress(encoded_file_text=encoded_text)
print('Decoded Text')
print(huffman_tree.decoded_text)
