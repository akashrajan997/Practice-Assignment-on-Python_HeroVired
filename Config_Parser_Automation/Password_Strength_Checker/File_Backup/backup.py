"""
backup.py - Simple file backup script

Usage:
    python backup.py /path/to/source /path/to/destination

This script copies all files from the source directory to the destination directory.
If a file with the same name exists in the destination, a timestamp is appended to the filename.
"""

import os
import sys
import shutil
from datetime import datetime

# Function to print usage instructions
def print_usage():
    print("Usage: python backup.py <source_dir> <destination_dir>")

# Main function
if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 3:
        print("Error: Incorrect number of arguments.")
        print_usage()
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    # Check if source directory exists
    if not os.path.isdir(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        sys.exit(1)

    # Create destination directory if it doesn't exist
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created destination directory: {dest_dir}")

    try:
        # Iterate over all files in the source directory
        for filename in os.listdir(source_dir):
            src_file = os.path.join(source_dir, filename)
            # Only process files (ignore subdirectories)
            if os.path.isfile(src_file):
                dest_file = os.path.join(dest_dir, filename)
                # If file exists in destination, append timestamp
                if os.path.exists(dest_file):
                    name, ext = os.path.splitext(filename)
                    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                    dest_file = os.path.join(dest_dir, f"{name}_{timestamp}{ext}")
                # Copy the file
                shutil.copy2(src_file, dest_file)
                print(f"Backed up: {os.path.basename(dest_file)}")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
