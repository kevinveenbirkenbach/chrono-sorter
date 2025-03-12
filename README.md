# ChronoSorter (chroso) 🕒
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-blue?logo=github)](https://github.com/sponsors/kevinveenbirkenbach) [![Patreon](https://img.shields.io/badge/Support-Patreon-orange?logo=patreon)](https://www.patreon.com/c/kevinveenbirkenbach) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20Coffee-Funding-yellow?logo=buymeacoffee)](https://buymeacoffee.com/kevinveenbirkenbach) [![PayPal](https://img.shields.io/badge/Donate-PayPal-blue?logo=paypal)](https://s.veen.world/paypaldonate)


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/kevinveenbirkenbach/chronosorter.svg?style=social)](https://github.com/kevinveenbirkenbach/chronosorter/stargazers)

ChronoSorter is a command-line tool that updates media file metadata and renames image files based on their earliest timestamps. It extracts dates from EXIF data and file system metadata, then sets the file creation dates and renames the files accordingly. With its preview mode, you can review changes before applying them.

## 🛠 Features

- **Metadata Extraction:** Retrieves dates from various tags (e.g., DateTimeOriginal, FileCreateDate).
- **Date Update:** Updates file creation dates using exiftool and file system attributes.
- **File Renaming:** Renames images to a standardized format based on the earliest timestamp.
- **Recursive Processing:** Processes all eligible files in a folder (no subdirectories allowed).
- **Preview Mode:** Review changes without modifying any files.

## 📥 Installation

Install ChronoSorter via [Kevin's Package Manager](https://github.com/kevinveenbirkenbach/package-manager) under the alias `chroso`:

```bash
package-manager install chroso
```

This command installs ChronoSorter globally and makes it available as `chroso` in your terminal. 🚀

## 🚀 Usage

Run ChronoSorter by specifying the folder path containing your media files. Enable renaming and date updates with the options provided.

### Basic Example

```bash
chroso /path/to/folder --rename --update-date --preview
```

### Options

- **`folder_path`**: Path to the folder containing your media files.
- **`--rename`**: Rename image files based on the earliest date found.
- **`--update-date`**: Update file creation dates. You can specify one or more tags (default is `File:FileCreateDate`).
- **`--preview`**: Preview the changes without applying them.
- Additional options such as `--verbose` and other update tag selections can be viewed by running:
  
  ```bash
  chroso --help
  ```

## 📜 License

This project is licensed under the **MIT License**.

## 🧑‍💻 Author

Developed by **Kevin Veen-Birkenbach**  
- 📧 [kevin@veen.world](mailto:kevin@veen.world)  
- 🌐 [https://www.veen.world/](https://www.veen.world/)

Enjoy organizing your media files with ChronoSorter!
