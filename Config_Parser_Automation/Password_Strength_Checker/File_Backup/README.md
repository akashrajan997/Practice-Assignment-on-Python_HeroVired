# File Backup

Simple Python script to back up files from a source directory to a destination directory.

## Description

`backup.py` copies all files (not directories) from a source directory into a destination directory. If a file with the same name already exists in the destination, the script appends a timestamp (format: YYYYMMDDHHMMSS) to the filename to avoid overwriting.

The script will create the destination directory if it does not exist.

## Requirements

- Python 3.6+ (for f-strings and datetime formatting)

## Usage

Run from PowerShell or any shell:

```powershell
python "backup.py" "C:\path\to\source" "C:\path\to\destination"
```

Example:

```powershell
python "backup.py" "D:\FileBackupSource" "D:\FileBackupDestination"
```

Expected output for each file copied:

```
Backed up: filename.txt
```

If a file named `filename.txt` already exists in the destination, the script will copy the file as `filename_20251005131600.txt` (timestamp will reflect the current date/time).

## Behavior and error handling

- If the source directory doesn't exist, the script prints an error and exits.
- If the destination directory doesn't exist, the script creates it.
- The script catches unexpected exceptions and prints a descriptive message.

## Notes

- The script only copies files at the top level of the source directory (it does not recurse into subdirectories).
- File metadata (timestamps and permissions) are preserved using `shutil.copy2`.

## License

Include a license file if you want to open-source this repository. For small personal projects, a permissive license like MIT is common.

## Contributing

Feel free to open issues or PRs on the GitHub repository to add features such as recursive copying, dry-run mode, logging, or tests.
