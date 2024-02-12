import os
import platform

system = platform.system()
delete_filetypes = ["xls", "xlsx", "docx"]
path_to_look = "D:/"


def main(current_os, path):
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
