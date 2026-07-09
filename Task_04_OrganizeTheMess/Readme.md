# Organize The Mess

Organize The Mess is a Python folder-cleanup tool that scans one specific parent folder, finds duplicates, organizes files by type, and flags files over 1GB. It is designed to be safe by default because it shows a dry run first and only makes changes after typed approval.

## Tech Stack

- Python 3
- Standard library modules: `os`, `hashlib`, `shutil`

## How It Works

The script scans only the chosen parent folder, calculates file hashes to find duplicates, groups files into type-based folders, and lists any large files for review. Before doing anything destructive, it prints a dry-run plan and waits for the user to type `EXECUTE`.

## Files

- `messy.py` - main cleanup script
- `Readme.md` - project overview
- `Report.md` - project report
- `Result.png` - output screenshot
