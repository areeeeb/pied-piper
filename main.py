from huffman_coding import tree


string = 'mississippi river'

huffman_tree = tree.Tree(string)
huffman_tree.create_tree()

compressed_file = huffman_tree.get_compressed_file()
binary_presentation = compressed_file[1]

print(binary_presentation)

byte_array = bytearray()
for i in range(0, len(binary_presentation), 8):
    byte_array.append(int(binary_presentation[i:i+8], 2))

print(byte_array)

# for i in range(0, len(binary_presentation)):
#     byte_array.append(int(binary_presentation[i]))


with open('testing.bin', 'wb') as fp:
    fp.write(byte_array)
