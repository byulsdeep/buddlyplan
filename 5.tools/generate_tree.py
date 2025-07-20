import os

def generate_directory_tree(startpath, output_file, ignore_dirs, ignore_files):
    """
    Generates a text-based directory tree and saves it to a file.
    Ignores specified directories and files.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        # Get the project root name and write the header
        project_root_name = os.path.basename(os.path.abspath(startpath))
        f.write("```text\n")
        f.write(f"{project_root_name}/\n")

        # Start the recursive helper function
        _walk_and_write(startpath, '', f, ignore_dirs, ignore_files)

        f.write("```\n")

def _walk_and_write(current_path, prefix, file_object, ignore_dirs, ignore_files):
    """
    A recursive helper function to walk the directory and write lines.
    """
    # Get all items in the current directory
    try:
        entries = os.listdir(current_path)
    except OSError:
        # Handle cases where permissions might be an issue
        return

    # Separate directories and files, and filter out ignored ones
    dirs = sorted([d for d in entries if os.path.isdir(os.path.join(current_path, d)) and d not in ignore_dirs])
    files = sorted([f for f in entries if os.path.isfile(os.path.join(current_path, f)) and f not in ignore_files])
    
    # Combine the lists for pointer logic
    all_entries = dirs + files
    
    for i, entry in enumerate(all_entries):
        # Determine the correct pointer for the item
        is_last = (i == len(all_entries) - 1)
        pointer = '└── ' if is_last else '├── '
        
        # Write the entry to the file
        file_object.write(f"{prefix}{pointer}{entry}")

        # If it's a directory, add a slash and recurse
        if os.path.isdir(os.path.join(current_path, entry)):
            file_object.write("/\n")
            # The new prefix for the children depends on whether the current item was the last one
            extension = '    ' if is_last else '│   '
            _walk_and_write(os.path.join(current_path, entry), prefix + extension, file_object, ignore_dirs, ignore_files)
        else:
            file_object.write("\n")

# --- Main execution block ---
if __name__ == "__main__":
    # Directories and files to ignore
    ignore_dirs_set = {'.git', 'venv', 'node_modules', '__pycache__', '.vscode', 'dist'}
    ignore_files_set = {'.DS_Store', 'Thumbs.db'}
    
    # Get the directory where the script itself is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths relative to the script's location
    start_path = os.path.join(script_dir, '..')
    output_filename = os.path.join(script_dir, '..', '1.docs', 'DirectoryStructure.md')

    print(f"Generating directory tree. Ignoring: {ignore_dirs_set}")
    generate_directory_tree(start_path, output_filename, ignore_dirs_set, ignore_files_set)
    print(f"Success! Directory tree saved to '{output_filename}'")