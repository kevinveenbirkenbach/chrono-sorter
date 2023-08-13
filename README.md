# Media Sorting Tools
Collection of tools to sort media.

## sort-by-datetime.py

This tool is designed to rename image files in a directory based on the earliest date found in a set of specified attributes (`date:create`, `date:modify`, `date:timestamp`, `exif:DateTime`, `exif:DateTimeDigitized`, `exif:DateTimeOriginal`). It provides a convenient way to batch rename images according to timestamps.

### Setup

1. **Install Python:** Make sure you have Python installed on your system.
2. **Install Dependencies:** This tool requires libraries. You can install them using the following commands:
   ```bash
   pip install pillow
   pip install pyexifinfo
   pip install pyexiftool
   ```
3. **Download the Script:** Place the script in the directory where you want to run it.

### Usage

Run the script from the command line with the path to the folder containing the images you want to rename. You can also use the `--preview` option to see what the renaming would look like without making actual changes.

## Author

Created by Kevin Veen-Birkenbach
- Email: [kevin@veen.world](mailto:kevin@veen.world)
- Website: [www.veen.world](https://www.veen.world/)

Special thanks to [ChatGPT](https://openai.com) for assistance in the development of this tool. You can view the conversation that led to the creation of this tool [here](https://chat.openai.com/share/ea70a7a4-c936-4838-9912-508cff474779).

## License

This code is licensed under the GNU Affero General Public License Version 3. Please see the [LICENSE](LICENSE) file for more details or visit the [GNU website](https://www.gnu.org/licenses/agpl-3.0.html).
