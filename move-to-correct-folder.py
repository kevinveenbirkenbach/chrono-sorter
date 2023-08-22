import os
import shutil
import argparse

def move_files(source_dir, verbose=False, preview=False):
    if "Pictures" in source_dir:
        target_root = source_dir.replace("Pictures", "Videos")
        file_exts = ['.mp4', '.mkv', '.avi', '.mov', '.flv']
    elif "Videos" in source_dir:
        target_root = source_dir.replace("Videos", "Pictures")
        file_exts = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    else:
        print("Invalid source directory. Please provide either a 'Pictures' or 'Videos' directory.")
        return

    for dirpath, _, filenames in os.walk(source_dir):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in file_exts):
                source_path = os.path.join(dirpath, filename)
                relative_path = os.path.relpath(dirpath, source_dir)
                target_dir = os.path.join(target_root, relative_path)

                if not os.path.exists(target_dir) and not preview:
                    os.makedirs(target_dir)

                target_path = os.path.join(target_dir, filename)

                if preview:
                    print(f"Would move {source_path} to {target_path}")
                else:
                    shutil.move(source_path, target_path)
                    if verbose:
                        print(f"Moved {source_path} to {target_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Move files from Pictures to Videos and vice-versa.")
    parser.add_argument("--source", required=True, help="Source directory (either within 'Pictures' or 'Videos').")
    parser.add_argument("--verbose", action="store_true", help="Print verbose output.")
    parser.add_argument("--preview", action="store_true", help="Preview the moves without actually moving files.")

    args = parser.parse_args()

    move_files(args.source, args.verbose, args.preview)
