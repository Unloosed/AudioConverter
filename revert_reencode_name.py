import os

def revert_reencode_name(folder_path):
    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        # Check if the filename starts with "reencoded_"
        if filename.startswith("reencoded_"):
            # Construct the new filename by removing "reencoded_"
            new_filename = filename[len("reencoded_"):]
            # Construct full file paths
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} to {new_file}")

if __name__ == "__main__":
    # Welcome message
    print("Welcome to the Prefix Removal Tool!")
    print("This tool removes the \'reencoded_\' prefix from your files after they've been re-encoded.\n")

    # Get user input for the folder path
    folder_path = input("Please enter the full path for the folder that contains your files: ")
    # Call the function to revert the file names
    revert_reencode_name(folder_path)
    print("Renaming complete!")
