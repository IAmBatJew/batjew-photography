import os
import random
import string
from PIL import Image
import shutil

def create_random_foldername():
    # Generate a random string for the folder name
    return 'randomImages1'

def is_landscape(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        return width > height

def process_images():
    # Check if img directory exists
    if not os.path.exists('img'):
        print("Error: 'img' directory not found")
        return

    # Create new random folder name
    new_folder = create_random_foldername()
    new_folder_path = os.path.join('img', new_folder)
    
    # Create the new folder
    os.makedirs(new_folder_path, exist_ok=True)

    # Get list of image files
    image_files = [f for f in os.listdir('img') 
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    # Process only first 10 images
    # Randomly select 10 images (or less if there are fewer images)
    selected_files = random.sample(image_files, min(10, len(image_files)))
    for filename in selected_files:
        image_path = os.path.join('img', filename)
        
        try:
            if is_landscape(image_path):
                # Move landscape images to the new folder
                shutil.move(image_path, os.path.join(new_folder_path, filename))
                print(f"Moved {filename} to {new_folder}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    process_images()