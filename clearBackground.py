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

folderpath = input("Foldername (warning: will modify all pngs in the folder)")
clearcolor = input("Hex of clear color (if multiple sep by comma, e.g. '#FFFFFF,#00aaff')")
colors = clearcolor.split(",")
rgbcolors = [hex_to_rgb(c) for c in colors]

for filename in os.listdir(folderpath):
    if filename.lower().endswith(".png"):
        file_path = os.path.join(folderpath, filename)
        
        # Open image
        img = Image.open(file_path)

        # Example processing
        
        for rgb in rgbcolors:
            img = replace_color_with_transparency(img, rgb)


        # Save or overwrite the image
        os.makedirs(folderpath + "_clear", exist_ok=True)
        img.save(os.path.join(folderpath + "_clear", f"{filename}"))

        print(f"Processed {filename}")
