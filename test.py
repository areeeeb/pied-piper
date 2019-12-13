from PIL import Image

img = Image.open('images/sample.jpg')

pixel_val = list(img.getdata())
pixel_val_flat = [x for sets in pixel_val for x in sets]
# get_frequency(pixel_val_flat)
print(pixel_val)