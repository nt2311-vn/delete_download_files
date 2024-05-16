from dotenv import load_dotenv
import os
import platform

load_dotenv()

system = platform.system()
delete_filetypes = {
    "xls": True,
    "xlsx": True,
    "csv": True,
    "docx": True,
    "json": True,
    "xml": True,
}
path_to_look = os.environ.get("LOOK_UP_PATH")


def main(current_os, path):
    if current_os != "Windows":
        path = "/".join(path.split("\\"))

    deleted_file_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path) and delete_filetypes.get(
            file.split(".")[-1], False
        ):
            try:
                os.remove(file_path)
                deleted_file_name.append(file)
            except PermissionError:
                print(f"Please close the file {file_path} and try again")

    print(f"Deleted {len(deleted_file_name)} files completed: {deleted_file_name}")


main(system, path_to_look)
