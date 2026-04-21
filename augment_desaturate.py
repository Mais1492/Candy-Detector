import os
from PIL import Image, ImageEnhance
import shutil

image_dir = "candy_dataset/images/train"
label_dir = "candy_dataset/labels/train"

# Set saturation to 30%
DESAT_FACTOR = 0.3

for filename in os.listdir(image_dir):
    if filename.lower().endswith(".jpg"):
        name, ext = os.path.splitext(filename)

        img_path = os.path.join(image_dir, filename)
        label_path = os.path.join(label_dir, name + ".txt")

        # append suffix "_desat"
        new_img_name = name + "_desat" + ext
        new_label_name = name + "_desat.txt"

        new_img_path = os.path.join(image_dir, new_img_name)
        new_label_path = os.path.join(label_dir, new_label_name)

        # Process images
        img = Image.open(img_path)
        enhancer = ImageEnhance.Color(img)
        desat_img = enhancer.enhance(DESAT_FACTOR)
        desat_img.save(new_img_path)

        # Copy labels
        if os.path.exists(label_path):
            shutil.copy(label_path, new_label_path)
        else:
            print(f"Warning: No label found for {filename}")

print("Desaturation completed.")