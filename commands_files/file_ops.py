import os
from pathlib import Path

def find(filename: str, search_root = "C:\\"):

    if search_root == "C:\\":
        print("Be patient, this can take a few minutes depending on the size of your C:\\ drive and the speed of the drive \n")

    found = []
    stack = [search_root]

    while stack:
        current_path = stack.pop()

        try:
            with os.scandir(current_path) as entries:
                for e in entries:
                    if e.is_dir():
                        stack.append(e.path)
                    elif e.name == filename:
                        found.append(e.path)
        except PermissionError, FileNotFoundError, OSError:
            pass


    print(f"Located {len(found)} possible matches :")
    for p in found:
        print("->  " + p)
