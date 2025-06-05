# Folder Renamer

Folder Renamer is a simple Tkinter-based GUI application to rename files within folders to match their parent folder names while keeping the original file extension. It includes a preview window to show changes before applying them.

## Features

- Select a base directory containing subfolders with files.
- Preview the renaming operations before applying.
- Apply the renaming in one click.
- Dark theme for better user experience.

## Installation

### Prerequisites

- Python 3.x

### Running from Source Code

1. Clone this repository:
    ```bash
    git clone https://github.com/ashoover/file_renamer.git
    cd folder-renamer
    ```

2. Install the required packages (if any):
    ```bash
    pip install tkinter
    ```

3. Run the application:
    ```bash
    python file_renamer.py
    ```

### Running the Executable

An executable version of this application has been created using PyInstaller.

1. Download the latest release from the [Releases](https://github.com/ashoover/file_renamer/releases) section.
2. Extract the contents to a directory.
3. Run the `file_renamer.exe` file on Windows or the corresponding executable for other operating systems.

## Usage

### Selecting a Folder
1. Click on "Browse" to select the folder containing your subfolders with files.
2. The preview window will display all changes that will be made.

### Preview and Apply Changes
1. Review the changes in the preview window.
2. If everything looks correct, click the "Go" button to apply the changes.
3. A success message will appear once the renaming is complete.

## Building the Executable

If you want to create your own executable from the source code:

1. Ensure PyInstaller is installed:
    ```bash
    pip install pyinstaller
    ```

2. Run the following command in the project directory:
    ```bash
    pyinstaller --onefile app.py
    ```

3. The resulting executable will be located in the `dist` directory.

## Contributing

Feel free to submit issues, fork the repository and send pull requests!

## License

Free for use and edit
