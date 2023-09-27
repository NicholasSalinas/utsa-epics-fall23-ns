import os
import shutil

# Set your folder path
folder_path = "path_to_your_folder"

# Create folders to organize the images
for i in range(1, 6):
    subfolder_path = os.path.join(folder_path, f"folder_{i}")
    os.makedirs(subfolder_path, exist_ok=True)

# List all files in the folder
files = os.listdir(folder_path)

# Filter out only image files (you can customize this based on your needs)
image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
image_files = [f for f in files if os.path.isfile(os.path.join(folder_path, f)) and os.path.splitext(f)[1].lower() in image_extensions]

# Sort the image files
image_files.sort()

# Move the images to the respective folders
images_per_folder = 10
for i, image_file in enumerate(image_files):
    folder_index = i // images_per_folder + 1
    destination_folder = os.path.join(folder_path, f"folder_{folder_index}")
    source_path = os.path.join(folder_path, image_file)
    destination_path = os.path.join(destination_folder, image_file)
    shutil.move(source_path, destination_path)

print("Images organized into folders successfully.")

