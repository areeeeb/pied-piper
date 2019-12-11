from bitarray import bitarray
import pickle


bit_array = bitarray()

with open('testing2.bin', 'rb') as fp:
    bit_array.fromfile(fp)

with open('metadata.dat', 'rb') as fp:
    huffman_tree = pickle.load(fp)

print(huffman_tree.root_node.left)

print('Whole File')
print(bit_array)

key = bit_array[:8]
print('Key')
print(key)

binary_presentation = bit_array[8:]
print('Encoded Text')
byte_presentation = binary_presentation.tobytes()
byte_presentation_int = int.from_bytes(binary_presentation,
                                       byteorder='big',
                                       signed=False)
encoded_text = bin(byte_presentation_int)
print(encoded_text[2:])
