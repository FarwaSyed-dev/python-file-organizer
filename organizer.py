import os
import shutil
import argparse
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def organize_files(folder_path):

    try:
        if not os.path.exists(folder_path):
            print("Folder not found.")
            return

        for file_name in os.listdir(folder_path):

            file_path = os.path.join(folder_path, file_name)

            if os.path.isdir(file_path):
                continue

            extension = file_name.split(".")[-1].lower()

            folder_name = extension.upper() + "_Files"

            destination_folder = os.path.join(folder_path, folder_name)

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            shutil.move(file_path, os.path.join(destination_folder, file_name))

            print(f"Moved: {file_name}")

            logging.info(f"Moved file: {file_name}")

    except Exception as error:
        print("Error:", error)
        logging.error(error)

parser = argparse.ArgumentParser(description="File Organizer")

parser.add_argument("folder", help="Enter folder path")

args = parser.parse_args()

organize_files(args.folder)