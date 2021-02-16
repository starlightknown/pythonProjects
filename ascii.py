import sys
from PIL import Image

image_path = 'r.jpg'
# pass the image as command line argument
img = Image.open(image_path)

# resize the image
width, height = img.size
aspect_ratio = height/width
new_width = 170
new_height = aspect_ratio * new_width * 0.25
img = img.resize((new_width, int(new_height)))
# new size of image
# print(img.size)

# convert image to greyscale format
# https://stackoverflow.com/questions/52307290/what-is-the-difference-between-images-in-p-and-l-mode-in-pil
img = img.convert('L')

pixels = img.getdata()

# replace each pixel with a character from array
chars = ["#","&","@","$","%","*","!",":",".","i","l","o","v","e","y","u","h","a","t","n","d","~","{","+","[","|","?","^"]
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# split string of chars into multiple strings of length equal to new width and create a list
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)

# write to a text file.
with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)

