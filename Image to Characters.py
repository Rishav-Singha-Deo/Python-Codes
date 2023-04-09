from PIL import Image

img = Image.open("example2.jpg")

width, height = img.size
aspect_ratio = height / width
new_width = 150
new_height = int(new_width * aspect_ratio)
img = img.resize((new_width, new_height))

ascii_chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

for y in range(new_height):
    line = ''
    for x in range(new_width):
        pixel = img.getpixel((x, y))
        intensity = sum(pixel) / 3
        char_index = int(intensity / 25.5)
        line += ascii_chars[char_index]
    print(line)
