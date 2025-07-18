from PIL import Image
import os

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    if len(hex_str) != 6:
        raise ValueError("Hex color must be 6 digits long.")
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def replace_color_with_transparency(i, target_color, tolerance=0):
    img = i.convert("RGBA")
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if all(abs(channel1 - channel2) <= tolerance for channel1, channel2 in zip((r, g, b), target_color)):
                pixels[x, y] = (0, 0, 0, 0)  # Fully transparent

    return img

path = input("Spritesheet path:")



raw = Image.open(path)
width, height = raw.size

cellWidth = int(input("Cell width (pixels):"))
cellHeight = int(input("Cell height (pixels):"))
xN = int(input("Sprites per row:"))
yN = int(input("Number of rows:"))
xOff = int( input("X offset/gap between cells (pixels):"))
yOff = int(input("Y offset/gap between cells (pixels):"))
topMargin = int(input("Margin from top (pixels):"))
leftMargin = int(input("Margin from left (pixels):"))
#clearcolor = input("Hex of clear color (if multiple sep by comma, e.g. '#FFFFFF,#00aaff')")

#outputPath = input("Output folder name:")
outputPath = path.replace(".png","") # default
prefix = path.replace(".png","")
#prefix = input("Output prefix:")

# Replace transparency
'''
colors = clearcolor.split(",")
img = raw
for c in colors:
    img = replace_color_with_transparency(img, hex_to_rgb(c))
'''
img = raw
os.makedirs(outputPath, exist_ok=True)

count = 0
for row in range(yN):
        for col in range(xN):
            left = leftMargin + (col*cellWidth) + (col*xOff)
            upper = topMargin + (row * cellHeight) + (row*yOff)
            right = leftMargin + left + cellWidth
            lower = topMargin + upper + cellHeight

            tile = img.crop((left, upper, right, lower))
            
            tile.save(f"{outputPath}\\{prefix}_{count}.png")
            count += 1

print("Done!")
input()
# Open the sprite
# Replace clear color
# Chop accoridng to thing

