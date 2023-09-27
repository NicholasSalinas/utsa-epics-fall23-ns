import os

def rename_images(folder_path, new_prefix):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Filter out non-image files
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_files = [f for f in files if any(f.lower().endswith(ext) for ext in image_extensions)]
    
    # Sort the image files
    image_files.sort()
    
    # Renaming loop
    for idx, old_filename in enumerate(image_files, start=1):
        extension = os.path.splitext(old_filename)[1]
        new_filename = f"{new_prefix}_{idx:03d}{extension}"
        
        old_path = os.path.join(folder_path, old_filename)
        new_path = os.path.join(folder_path, new_filename)
        
        os.rename(old_path, new_path)
        print(f"Renamed {old_filename} to {new_filename}")

if __name__ == "__main__":
    folder_path = "/Users/nicholassalinas/Desktop/Python folder"
    new_filename_prefix = "Nick"
    
    rename_images(folder_path, new_filename_prefix)
