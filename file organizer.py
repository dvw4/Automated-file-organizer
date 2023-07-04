import os
import shutil

def organize_files(directory):
    # Create folders for different file types
    folders = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv"],
        "Music": [".mp3", ".wav", ".flac"],
        "Others": []  # Default folder for files with unknown extensions
    }

    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = os.path.splitext(filename)[1].lower()

            # Find the appropriate folder for the file type
            destination_folder = None
            for folder, extensions in folders.items():
                if file_extension in extensions:
                    destination_folder = folder
                    break

            # Create the destination folder if it doesn't exist
            if destination_folder is None:
                destination_folder = "Others"
                folders[destination_folder] = []
            if not os.path.exists(os.path.join(directory, destination_folder)):
                os.makedirs(os.path.join(directory, destination_folder))

            # Move the file to the destination folder
            source_path = os.path.join(directory, filename)
            destination_path = os.path.join(directory, destination_folder, filename)
            shutil.move(source_path, destination_path)

    print("File organization completed!")

# Specify the directory to organize files
directory_to_organize = "/path/to/directory"

# Call the function to organize files
organize_files(directory_to_organize)
