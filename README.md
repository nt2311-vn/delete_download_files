## DELETE UNUSED DOWNLOAD FILE BY SPECIFYING FILETYPES AND THE PATH TO LOOK

### Variable and set up for cleaning up
- Ensure python is installed in your system:
*Open your system terminal and type this:*
> python --version

- varable delete_filetypes: list of file extensions to look for
- variable path: path to look for files (only file in main directory to match and delete, no sub directory)
- Implement and env file and store your delete path to it (using python-dotenv)
- return: The number of file deletes and its name
- error: Handle error when the file is currently opening, show error close file and try again


