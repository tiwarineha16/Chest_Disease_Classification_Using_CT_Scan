import shutil
import os

def copy_model(src_folder, dest_folder, model_filename):
    # Construct the full file paths
    src_file = os.path.join(src_folder, model_filename)
    dest_file = os.path.join(dest_folder, model_filename)
    
    # Ensure the source file exists
    if not os.path.exists(src_file):
        print(f"The source file {src_file} does not exist.")
        return
    
    # Create the destination folder if it doesn't exist
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    # Copy the file
    shutil.copy(src_file, dest_file)
    print(f"Copied {model_filename} from {src_folder} to {dest_folder}")

# Example usage:
src_folder = r"C:\Users\nehat\Documents\NEHA DOCS\Study folder\Ineuron\Chest_Disease\Chest_Disease\artifacts\training"
dest_folder = r"C:\Users\nehat\Documents\NEHA DOCS\Study folder\Ineuron\Chest_Disease\Chest_Disease\model"
model_filename = "model.h5"  # Replace with your actual model file name

copy_model(src_folder, dest_folder, model_filename)
