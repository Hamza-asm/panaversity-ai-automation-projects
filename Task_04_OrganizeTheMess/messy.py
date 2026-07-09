import os
import hashlib
import shutil

# ==========================================================
# SAFETY CONFIGURATION - CHANGE THIS PATH BEFORE RUNNING
# ==========================================================
TARGET_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
# ==========================================================

ONE_GB_IN_BYTES = 1073741824

# File type mapping for organization
CATEGORY_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz']
}

def get_file_hash(filepath, block_size=65536):
    """Safely reads a file in chunks to calculate its SHA-256 hash without crashing RAM on large files."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(block_size), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except Exception as e:
        return None

def get_category(extension):
    """Returns the target folder name based on file extension."""
    ext = extension.lower()
    for category, extensions in CATEGORY_MAP.items():
        if ext in extensions:
            return category
    return "Other"

def ensure_safe_path(base_path, potential_child):
    """Security check to ensure no operations happen outside the target directory."""
    abs_base = os.path.abspath(base_path)
    abs_child = os.path.abspath(potential_child)
    return abs_child.startswith(abs_base)

def main():
    # 1. Validate Target Directory
    if not os.path.exists(TARGET_DIRECTORY) or not os.path.isdir(TARGET_DIRECTORY):
        print(f"ERROR: The directory '{TARGET_DIRECTORY}' does not exist or is not a folder.")
        return

    print(f"SCANNING DIRECTORY: {os.path.abspath(TARGET_DIRECTORY)}")
    print("Gathering data... Please wait.\n")

    # Data structures to hold our dry-run plans
    large_files = []
    duplicate_groups = []
    move_plan = []
    hash_map = {} # Format: { hash_value: [list_of_file_paths] }

    # 2. Scanning Phase
    for root, dirs, files in os.walk(TARGET_DIRECTORY):
        # Security: Skip hidden/system directories like回收站 or System Volume Information
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['System Volume Information', '$RECYCLE.BIN']]
        
        for file in files:
            full_path = os.path.join(root, file)
            
            # Skip symbolic links to prevent following them out of the parent folder
            if os.path.islink(full_path):
                continue

            try:
                file_size = os.path.getsize(full_path)
                _, ext = os.path.splitext(file)
                
                # --- TASK 1: Flag files over 1GB ---
                if file_size > ONE_GB_IN_BYTES:
                    large_files.append((full_path, file_size))
                
                # --- TASK 2: Find Duplicates ---
                file_hash = get_file_hash(full_path)
                if file_hash:
                    if file_hash not in hash_map:
                        hash_map[file_hash] = [full_path]
                    else:
                        hash_map[file_hash].append(full_path)
                
                # --- TASK 3: Organize by file type ---
                # Only plan to move if the file is sitting directly in the root of the target directory
                if root == TARGET_DIRECTORY:
                    category = get_category(ext)
                    dest_folder = os.path.join(TARGET_DIRECTORY, category)
                    dest_path = os.path.join(dest_folder, file)
                    
                    # Handle name conflicts if a file with the same name already exists in the category folder
                    counter = 1
                    while os.path.exists(dest_path):
                        name, ex = os.path.splitext(file)
                        dest_path = os.path.join(dest_folder, f"{name}_{counter}{ex}")
                        counter += 1
                    
                    # Only add to plan if it's not already in the correct folder
                    if full_path != dest_path:
                        move_plan.append((full_path, dest_path))

            except PermissionError:
                print(f"SKIPPING (Permission Denied): {full_path}")
            except Exception as e:
                print(f"SKIPPING (Error: {e}): {full_path}")

    # Extract only the groups that actually have duplicates
    for paths in hash_map.values():
        if len(paths) > 1:
            duplicate_groups.append(paths)

    # 3. Output the DRY RUN PLAN
    print("="*60)
    print("                   DRY RUN PLAN                 ")
    print("="*60)

    print("\n[1] FILES OVER 1GB (Flagged for review):")
    if not large_files:
        print("  - None found.")
    for path, size in large_files:
        size_gb = size / ONE_GB_IN_BYTES
        print(f"  - {size_gb:.2f} GB | {path}")

    print("\n[2] DUPLICATE FILES FOUND:")
    if not duplicate_groups:
        print("  - None found.")
    for group in duplicate_groups:
        print(f"  - Duplicate Group:")
        for i, path in enumerate(group):
            status = "[KEEP]" if i == 0 else "[DELETE]"
            print(f"      {status} {path}")

    print("\n[3] FILES TO BE ORGANIZED (Moved to subfolders):")
    if not move_plan:
        print("  - None found (files are already organized or in subfolders).")
    for old_path, new_path in move_plan:
        print(f"  - MOVE: {old_path}")
        print(f"        TO: {new_path}")

    # 4. The Approval Gate
    print("\n" + "="*60)
    print("WARNING: This will create folders and move/delete files.")
    print("Type 'EXECUTE' to proceed. Type anything else to abort safely.")
    print("="*60)
    
    user_input = input("Your decision: ").strip()

    # 5. Execution Phase
    if user_input != "EXECUTE":
        print("\nAborted. No changes were made to your system.")
        return

    print("\nExecuting plan... DO NOT CLOSE THE TERMINAL.")
    errors_occurred = False

    try:
        # Execute Moves
        for old_path, new_path in move_plan:
            if not ensure_safe_path(TARGET_DIRECTORY, new_path):
                print(f"SAFETY CANCELLED: Move target escaped root directory! {new_path}")
                continue
            os.makedirs(os.path.dirname(new_path), exist_ok=True)
            shutil.move(old_path, new_path)

        # Execute Duplicate Deletions
        for group in duplicate_groups:
            for path in group[1:]: # Skip index 0 (the one marked [KEEP])
                os.remove(path)

        print("\n✅ SUCCESS: Cleanup completed successfully.")

    except Exception as e:
        errors_occurred = True
        print(f"\n❌ ERROR: An error occurred mid-execution: {e}")
        print("Some files may have been moved, but the script halted to prevent data loss.")

    if not errors_occurred:
        print("Please review the 'Files over 1GB' list manually to decide if you want to delete them.")

if __name__ == "__main__":
    main()