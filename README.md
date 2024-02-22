## DELETE UNUSED DOWNLOAD FILE BY SPECIFYING FILETYPES AND THE PATH TO LOOK

### Variable and set up for cleaning up
- Ensure python is installed in your system
Open your system terminal and type this:
```sh
python --version
```
For python with version 3.8+, this is working fine
If you do not have one, please follow this link to install
[python download link](https://www.python.org/downloads/)

- Set up dotenv to declare the path you want to clean files
As common I assume, you use pip as package manager, if not please install dotenv by your package manager
```sh
pip install python-dotenv
```
- Create an .env file in the root path and bind the value of your cleaning path like this
> LOOK_UP_PATH="your/path/toclean"

- Finally run the script to delete files in the path
**For window**
```sh
python main.py
```

**For macOS and Linux**
```sh
python3 main.py
```


