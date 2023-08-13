import pyexifinfo as pxi
from datetime import datetime
import os
import sys

def rename_image(file_path, preview=False):
    # EXIF-Daten extrahieren
    exif_data = pxi.get_json(file_path)[0]

    # Datumsformate der Attribute
    date_formats = [
        "%Y:%m:%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S+00:00"
    ]

    # List der möglichen Datumswerte
    date_values = [
        exif_data.get("EXIF:DateTimeOriginal"),
        exif_data.get("EXIF:DateTimeDigitized"),
        exif_data.get("File:FileModifyDate"),
        exif_data.get("File:FileCreateDate"),
        exif_data.get("Composite:DateTimeCreated"),
    ]

    # Datumsobjekte konvertieren
    dates = []
    for date_value in date_values:
        for date_format in date_formats:
            try:
                dates.append(datetime.strptime(date_value, date_format))
                break
            except (ValueError, TypeError):
                continue

    # Niedrigstes Datum finden
    min_date = min(dates, default=None)
    if min_date:
        new_name = min_date.strftime("%Y%m%d%H%M%S")

        # Dateiendung beibehalten
        file_extension = os.path.splitext(file_path)[1]
        new_file_path = os.path.join(os.path.dirname(file_path), new_name + file_extension)

        # Datei umbenennen, wenn Vorschau nicht aktiviert ist
        if not preview:
            os.rename(file_path, new_file_path)
            print(f"File renamed to {new_file_path}")
        else:
            print(f"Preview: {file_path} would be renamed to {new_file_path}")
    else:
        print(f"No valid dates found in {file_path}")

def process_folder(folder_path, preview=False):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, filename)
                rename_image(file_path, preview)

if __name__ == "__main__":
    folder_path = sys.argv[1] if len(sys.argv) > 1 else "path/to/your/folder"
    preview = '--preview' in sys.argv

    process_folder(folder_path, preview)
