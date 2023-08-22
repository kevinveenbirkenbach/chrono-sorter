# Media Sorting Tools
Collection of tools to sort media.

## sort-by-datetime.py

This tool is designed to rename image files in a directory based on the earliest date found in a set of specified attributes (`date:create`, `date:modify`, `date:timestamp`, `exif:DateTime`, `exif:DateTimeDigitized`, `exif:DateTimeOriginal`). It provides a convenient way to batch rename images according to timestamps.

### Setup

1. **Install Python:** Make sure you have Python installed on your system.
2. **Install Dependencies:** This tool requires libraries. You can install them using the following commands:
   ```bash
   pip install pillow
   pacman -S perl-image-exiftool
   pip install pyexifinfo
   pip install git+https://github.com/smarnach/pyexiftool.git
   ```
3. **Download the Script:** Place the script in the directory where you want to run it.

### Usage

Run the script from the command line with the path to the folder containing the images you want to rename. You can also use the `--preview` option to see what the renaming would look like without making actual changes.

## move-to-correct-folder.py

### Description

This tool is designed to automatically move video files located in the "Pictures" directory to their corresponding paths in the "Videos" directory and vice versa. When the target folder doesn't exist, it will be created. 

### Usage

```bash
python move-to-correct-folder.py --source [SOURCE_PATH] [OPTIONS]
```

#### Parameters:

- `--source`: This is a required argument. Specify the source directory (either within 'Pictures' or 'Videos') from which you want to move the files.

- `--verbose`: (Optional) If provided, the tool will print verbose output showing each file move operation.

- `--preview`: (Optional) If provided, the tool will only display a preview of the moves that would occur without actually moving any files.

### Examples:

To move files from a Pictures folder to their corresponding Videos folder:

```bash
python move-to-correct-folder.py --source ~/Pictures/2023 --verbose
```

To preview the files that would be moved from a Videos folder to their corresponding Pictures folder:

```bash
python move-to-correct-folder.py --source ~/Videos/2023 --preview
```

### Note

Ensure that the provided `--source` is either a path within the 'Pictures' or 'Videos' directory for the tool to work correctly.


## Author

Created by Kevin Veen-Birkenbach
- Email: [kevin@veen.world](mailto:kevin@veen.world)
- Website: [www.veen.world](https://www.veen.world/)

Special thanks to [ChatGPT](https://openai.com) for assistance in the development of this tool. You can view the conversatios that led to the creation of this tool:

- https://chat.openai.com/share/ea70a7a4-c936-4838-9912-508cff474779
- https://chat.openai.com/share/b6d34152-8f7d-4b19-b451-342474c28555


## License

This code is licensed under the GNU Affero General Public License Version 3. Please see the [LICENSE](LICENSE) file for more details or visit the [GNU website](https://www.gnu.org/licenses/agpl-3.0.html).
