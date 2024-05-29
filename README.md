# python-demos
This is a repo depicting basics of python library in projects

## How to Execute Python Programs in VSCode and PyCharm

This guide will walk you through the steps to run Python programs in Visual Studio Code (VSCode) and PyCharm.

### Prerequisites
- Python installed on your system. Download it from [python.org](https://www.python.org/).
- The desired IDE installed on your system:
  - [Visual Studio Code](https://code.visualstudio.com/)
  - [PyCharm](https://www.jetbrains.com/pycharm/)

---

## Running Python Programs in Visual Studio Code (VSCode)

### 1. Install VSCode and Python Extension
1. **Download and Install VSCode**: 
   - Download from [code.visualstudio.com](https://code.visualstudio.com/).
   - Install following the instructions for your operating system.

2. **Install Python Extension for VSCode**:
   - Open VSCode.
   - Go to the Extensions view by clicking the Extensions icon in the Activity Bar or by pressing `Ctrl+Shift+X`.
   - Search for "Python" and install the extension provided by Microsoft.

### 2. Running a Python Script
1. **Open or Create a Python File**:
   - Open an existing `.py` file by going to `File > Open File...`.
   - Or create a new Python file by going to `File > New File` and save it with a `.py` extension.

2. **Select Python Interpreter**:
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the Command Palette.
   - Type `Python: Select Interpreter` and select your Python interpreter.

3. **Run the Python Script**:
   - **Using the Terminal**:
     - Open the integrated terminal by going to `View > Terminal` or pressing `` Ctrl+` ``.
     - Navigate to your script’s directory using `cd path_to_your_script`.
     - Run your script by typing `python script_name.py` (or `python3 script_name.py` on some systems) and pressing Enter.
   - **Using the Run Button**:
     - Open the Python file you want to run.
     - Click the `Run` button in the top-right corner of the editor.
     - Alternatively, right-click the file in the Explorer view and select `Run Python File in Terminal`.

---

## Running Python Programs in PyCharm

### 1. Install PyCharm
1. **Download and Install PyCharm**:
   - Download from [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/).
   - Install following the instructions for your operating system.

### 2. Running a Python Script
1. **Open or Create a Python Project**:
   - Open PyCharm.
   - To open an existing project, go to `File > Open...` and select your project folder.
   - To create a new project, go to `File > New Project...`, choose a location, and set up a new project.

2. **Create or Open a Python File**:
   - In your project, right-click the project folder in the Project view, select `New > Python File`, and name it.
   - Or, open an existing Python file by double-clicking it in the Project view.

3. **Configure Python Interpreter**:
   - Go to `File > Settings...` (or `PyCharm > Preferences...` on macOS).
   - Navigate to `Project: <your_project_name> > Python Interpreter`.
   - Select the interpreter you want to use, or add a new interpreter if necessary.

4. **Run the Python Script**:
   - Right-click the Python file in the Project view or the editor, and select `Run 'filename'`.
   - Alternatively, with the file open, click the green play button in the top-right corner of the editor.

### Additional Tips
- **Running via Terminal**:
  - Open the terminal within PyCharm by going to `View > Tool Windows > Terminal`.
  - Navigate to your script’s directory and run it using `python script_name.py`.

By following these steps, you will be able to run your Python scripts efficiently in both Visual Studio Code and PyCharm.

---

## Troubleshooting
- Ensure Python is installed and added to your system's PATH.
- Check that the correct Python interpreter is selected in both IDEs.
- Make sure all necessary Python extensions/plugins are installed and enabled.

If you encounter any issues, refer to the official documentation or support for [VSCode](https://code.visualstudio.com/docs) and [PyCharm](https://www.jetbrains.com/pycharm/documentation/).
