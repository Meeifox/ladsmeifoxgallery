import os
from PIL import Image
import sys

def resize_by_percentage(input_path, output_path, scale_percent):
    img = Image.open(input_path)
    width = int(img.width * scale_percent / 100)
    height = int(img.height * scale_percent / 100)
    resized = img.resize((width, height), Image.LANCZOS)
    resized.save(output_path)

def main():
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    scale_percent = int(sys.argv[3])

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                input_path = os.path.join(root, file)
                
                # Structure du sous-dossier à reproduire
                relative_path = os.path.relpath(root, input_folder)
                output_dir = os.path.join(output_folder, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                output_path = os.path.join(output_dir, file)
                resize_by_percentage(input_path, output_path, scale_percent)

    print(f"✅ Redimensionnement terminé à {scale_percent}% dans '{output_folder}/'")

if __name__ == "__main__":
    main()
