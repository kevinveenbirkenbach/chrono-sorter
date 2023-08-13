import pyexifinfo as pxi
import exiftool as pet
import re
from datetime import datetime
import os
import sys

def update_file_create_date(file_path, min_date, preview=False):
    with pet.ExifTool() as et:
        current_file_create_date = et.get_tag('File:FileCreateDate', file_path)

    if min_date:
        new_file_create_date = min_date.strftime("%Y:%m:%d %H:%M:%S")
        if current_file_create_date != new_file_create_date:
            if not preview:
                with pet.ExifTool() as et:
                    et.execute(f'-FileCreateDate={new_file_create_date}'.encode('utf-8'), file_path.encode('utf-8'))
                print(f"FileCreateDate set from {current_file_create_date} to {new_file_create_date}")
            else:
                print(f"Preview: FileCreateDate would be set from {current_file_create_date} to {new_file_create_date}")
        else:
            print("Skipped update file create date.")


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
    date_values = [
        exif_data.get("EXIF:DateTimeOriginal"),
        exif_data.get("EXIF:DateTimeDigitized"),
        exif_data.get("File:FileModifyDate"),
        exif_data.get("File:FileCreateDate"),
        exif_data.get("Composite:DateTimeCreated"),
    ]

    # Convert date values to date objects
    dates = []
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

    if rename:
        rename_image(file_path, min_date, preview)

    if update_date:
        update_file_create_date(file_path, min_date, preview)

def process_folder(folder_path, rename, update_date, preview=False):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, filename)
                process_file(file_path, rename, update_date, preview)

if __name__ == "__main__":
    folder_path = sys.argv[1]
    rename = '--rename' in sys.argv
    update_date = '--update-date' in sys.argv
    preview = '--preview' in sys.argv
    process_folder(folder_path, rename, update_date, preview)
