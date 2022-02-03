import time
import zipfile
from os.path import basename
from zipfile import ZipFile
import os.path


# https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
def zip_files_in_directory(dir_name, zip_file_name, condition=(lambda name: True)):
    print(f"Trying to create new zip-file: \"{zip_file_name}\"\n"
          f"Please be patient. Depending on the size of your directory, this can take a while...")

    now = time.time()
    count = 0

    with ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipObj:
        print("Creating empty zip file at target location.")

        for folderName, subfolders, filenames in os.walk(dir_name):
            # print(":", end="")

            for filename in filenames:
                print(".", end="")
                if condition(filename):
                    count += 1
                    file_path = os.path.join(folderName, filename)
                    zipObj.write(file_path, os.path.relpath(file_path, start=dir_name))

    print(f"\nIt took {time.time() - now} s to zip {count} files.")

    print(f"Created new zip-file: \"{zip_file_name}\"")


def easy_zip(dir_name):
    zip_files_in_directory(dir_name, f"{dir_name}.zip")
