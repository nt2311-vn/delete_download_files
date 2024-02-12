from dotenv import load_dotenv
import os
import platform

load_dotenv()

system = platform.system()
delete_filetypes = ["xls", "xlsx", "docx", "csv"]
path_to_look = os.environ.get("LOOK_UP_PATH")


def main(current_os, path):
    if current_os != "Windows":
        path = "/".join(path.split("\\"))

    print(f"Check the path {path_to_look}")

    deleted_file_name = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path) and file.split(".")[1] in delete_filetypes:
            try:
                os.remove(file_path)
                deleted_file_name.append(file)
            except PermissionError:
                print(f"Please close the file {file_path} and try again")

    print(f"Deleted {len(deleted_file_name)} files completed: {deleted_file_name}")


main(system, path_to_look)
