import pyexifinfo as pxi
import exiftool as pet
import re
import argparse
from datetime import datetime
import os
import sys
import time

# Define the possible update tags
UPDATE_TAGS = [
    'EXIF:DateTimeOriginal',
    'EXIF:DateTimeDigitized',
    'File:FileModifyDate',
    'File:FileCreateDate',
    'Composite:DateTimeCreated'
]

def update_file_create_date(file_path, min_date, update_tags, preview=False):
    # Define a mapping from the provided keys to the correct exiftool tags
    tag_mapping = {tag: tag.split(":")[1] for tag in UPDATE_TAGS if ":" in tag}

    new_file_create_date = min_date.strftime("%Y:%m:%d %H:%M:%S")

    if not preview:
        # Define the new access time and modification time
        new_access_time = time.mktime(min_date.timetuple())
        new_modification_time = time.mktime(min_date.timetuple())
        # Apply the new times
        os.utime(file_path, (new_access_time, new_modification_time))
    else:
        print(f"Preview: Access, Modificataion and time would be set to {new_file_create_date}")

        
    with pet.ExifTool() as et:
        for tag_key in update_tags:
            exiftool_tag = tag_mapping.get(tag_key)
            if exiftool_tag:
                current_date = et.get_tag(tag_key, file_path)
                if current_date != new_file_create_date:
                    if not preview:
                        command = f"-{exiftool_tag}={new_file_create_date}"
                        et.execute(command.encode('utf-8'), file_path.encode('utf-8'))
                        print(f"{tag_key} set from {current_date} to {new_file_create_date}")
                    else:
                        print(f"Preview: {tag_key} would be set from {current_date} to {new_file_create_date}")
                else:
                    print(f"Skipped updating {tag_key}.")
            else:
                raise ValueError(f"Unknown tag: {tag_key}")


def rename_image(file_path, min_date, preview=False):
    # Check if the filename is already in the desired format
    filename = os.path.basename(file_path)
    if re.match(r'^\d{8}_\d{6}(\(\d+\))?(\.\w+)?$', filename):
        print("Skipped renaming.")
        return

    if min_date:
        new_name = min_date.strftime("%Y%m%d_%H%M%S")
        count = 0
        # Keep file extension
        file_extension = os.path.splitext(file_path)[1]
        new_file_path = os.path.join(os.path.dirname(file_path), new_name + file_extension)

        while os.path.exists(new_file_path):
            count += 1
            new_file_path = os.path.join(os.path.dirname(file_path), f"{new_name}({count}){file_extension}")

        if not preview:
            os.rename(file_path, new_file_path)
            print(f"Renamed to {new_file_path}")
        else:
            print(f"Would be renamed to {new_file_path}")

def process_file(file_path, rename, update_date, preview):
    # Extract EXIF data
    exif_data = pxi.get_json(file_path)[0]

    # Date formats for the attributes
    date_formats = [
        "%Y:%m:%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S%z"
    ]
    
    # List of possible date values
    date_values = [exif_data.get(tag) for tag in UPDATE_TAGS]

    # Convert date values to date objects
    dates = [datetime.fromtimestamp(func(file_path)) for func in (os.path.getctime, os.path.getmtime, os.path.getatime)]
    
    for date_value in date_values:
        if date_value:
            for date_format in date_formats:
                try:
                    date_obj = datetime.strptime(date_value, date_format)
                    dates.append(date_obj)
                    break
                except ValueError:
                    pass
   
    # Find the earliest date
    min_date = min(dates, default=None)

    print(f"Checking file: {file_path}")

    if update_date:
        update_file_create_date(file_path, min_date, update_date, preview)

    if rename:
        rename_image(file_path, min_date, preview)

def process_folder(folder_path, rename, update_date, preview=False):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, filename)
                process_file(file_path, rename, update_date, preview)

def main():
    parser = argparse.ArgumentParser(description="Sort media files by date.")
    parser.add_argument('folder_path', type=str, help="Path to the folder containing media files.")
    parser.add_argument('--rename', action='store_true', help="Rename the media files.")
    UPDATE_TAGS_HELP = ", ".join(UPDATE_TAGS)
    parser.add_argument('--update-date', nargs='*', choices=UPDATE_TAGS, default=['File:FileCreateDate'],
        help=f"Update the file creation date(s). Specify one or more of the following options: {UPDATE_TAGS_HELP}.")
    parser.add_argument('--preview', action='store_true', help="Preview the changes without applying them.")
    args = parser.parse_args()
    process_folder(args.folder_path, args.rename, args.update_date, args.preview)

if __name__ == "__main__":
    main()
