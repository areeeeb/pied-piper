import pickle
from datetime import datetime

from PIL import Image

from huffman_coding.HuffmanTree import HuffmanTree


compressed_file_data = HuffmanTree.\
    read_and_get_from_file('images/compressed.bin')
encoded_data = compressed_file_data['encoded_data']
key = compressed_file_data['key']
print(key)

# After getting the key, get the corresponding meta_data
with open('images/metadata.dat', 'rb') as fp:
    meta_data = pickle.load(fp)

print('this is metadata')
print(meta_data)

huffman_tree = HuffmanTree(elements_dict=meta_data,
                           is_decompression=True,
                           is_image=True)

START_TIME = datetime.now()

# decompress function requires encoded_data as argument
huffman_tree.decompress(encoded_file_data=encoded_data)

decoded_image_data = huffman_tree.decoded_data
image_size = huffman_tree.image_size
print(image_size)

new_image = Image.new('RGB', size=image_size)
new_image.putdata(decoded_image_data)
new_image.save('images/decompressed.bmp')

end_time = datetime.now() - START_TIME
print(f'Image decompressed in {end_time}')
