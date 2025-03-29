import os
import shutil
import zipfile

def merge_folders(folder1, folder2, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Copy all contents of folder1 to the output folder
    for item in os.listdir(folder1):
        item_path = os.path.join(folder1, item)
        if os.path.isdir(item_path):
            shutil.copytree(item_path, os.path.join(output_folder, item))
        else:
            shutil.copy2(item_path, output_folder)
    
    # Copy all contents of folder2 to the output folder
    for item in os.listdir(folder2):
        item_path = os.path.join(folder2, item)
        if os.path.isdir(item_path):
            shutil.copytree(item_path, os.path.join(output_folder, item), dirs_exist_ok=True)
        else:
            shutil.copy2(item_path, output_folder)

def zip_folder(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))

def main():
    # Get the parent directory (one folder up from this script)
    script_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.dirname(script_dir)

    # Define paths for the "common" and "craftable-tridents" folders
    folder1 = os.path.join(parent_dir, 'common')
    folder2 = os.path.join(parent_dir, 'craftable-tridents')

    # Define the output folder and the zip file name
    output_folder = os.path.join(parent_dir, 'merged_output')
    zip_name = os.path.join(parent_dir, 'merged_output.zip')

    # Merge the folders and zip the result
    merge_folders(folder1, folder2, output_folder)
    zip_folder(output_folder, zip_name)
    print(f"Merged and zipped into {zip_name}")

if __name__ == '__main__':
    main()
