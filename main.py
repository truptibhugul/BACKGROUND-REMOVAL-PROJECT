from rembg import remove
from PIL import Image
import os

input_folder = "input"
output_folder = "output"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.endswith(".jpg") or file.endswith(".png"):
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)

        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)

        print(f"Processed: {file}")

print("All images processed successfully!")
