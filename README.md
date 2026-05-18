
# File Organizer

A simple Python script that organizes files in a folder by their file extension. 
Each file type gets moved into its own folder, e.g. `.png` files go into `PNG_FILES`.

# how it works
 Scans a given folder for files
 Groups files into folders based on extension `TXT_Files`, `JPG_Files`, etc.
 Skips subfolders
 Logs all actions to `app.log`
 Prints status messages to the terminal

# Requirements
Python 3.14
No external libraries needed. Use only built in modules `os`, `shutil`, `argparse`, `logging`

# How to Run
Open a terminal in the project folder and run:

   python organizer.py sample_files

   This will organize all files inside the sample_files folder.
# OUTPUT 
Folders created: One folder per file extension, named PNG_Files.  
Example: JPEG_Files, PNG_Files
output: Shows each file as it gets moved.app.log: Log file created in the project folder with timestamps and actions for debugging.



