import os
import shutil
import sys
import time

def backup_files(src, dst):
    if not os.path.isdir(src):
        print(f"Source directory '{src}' does not exist.")
        return
    if not os.path.isdir(dst):
        print(f"Destination directory '{dst}' does not exist.")
        return
    for filename in os.listdir(src):
        src_file = os.path.join(src, filename)
        dst_file = os.path.join(dst, filename)
        if os.path.isfile(src_file):
            if os.path.exists(dst_file):
                base, ext = os.path.splitext(filename)
                timestamp = time.strftime("%Y%m%d%H%M%S")
                dst_file = os.path.join(dst, f"{base}_{timestamp}{ext}")
            try:
                shutil.copy2(src_file, dst_file)
                print(f"Copied: {src_file} -> {dst_file}")
            except Exception as e:
                print(f"Failed to copy {src_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_dir> <destination_dir>")
    else:
        backup_files(sys.argv[1], sys.argv[2])
