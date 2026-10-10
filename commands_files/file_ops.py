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
                    if e.is_dir(follow_symlinks=False):
                        stack.append(e.path)
                    elif e.name == filename:
                        found.append(e.path)
        except (PermissionError, FileNotFoundError, OSError):
            pass


    print(f"Located {len(found)} possible matches :")
    for p in found:
        print("->  " + p)

def tree(dir_path: str):
    pass

def check(dir_path: str): # Gather info about a given folder and display it

    total_size = 0 # Bytes
    total_folders = 0
    total_files = 0
    most_common_extensions = {}
    biggest_file = (0, "")
    exes = []

    found = {}
    stack = [dir_path]

    while stack:
        current_path = stack.pop()
        try:
            with os.scandir(current_path) as entries:
                for e in entries:
                    if e.is_dir(follow_symlinks=False):
                        total_folders += 1
                        stack.append(e.path)


                    elif e.is_file(follow_symlinks=False):
                        total_files += 1
                        total_size += e.stat().st_size

                        if e.stat().st_size > biggest_file[0]:
                            biggest_file = (e.stat().st_size, e.name)

                        if not str(Path(e.path).parent) in found: # Create Tree of the folder (only folders that contain files create entries)
                            found[str(Path(e.path).parent)] = [f"{e.path}"]
                            continue

                        found[str(Path(e.path).parent)].append(f"{e.path}")

                        if not os.path.splitext(e.name)[1] in most_common_extensions:
                            most_common_extensions[os.path.splitext(e.name)[1]] = 1

                        else:
                            most_common_extensions[os.path.splitext(e.name)[1]] += 1

                        if os.path.splitext(e.name)[1] == ".exe":
                            exes.append(e.path)

            
        except (PermissionError, FileNotFoundError, OSError) as e:
            print(e)

    for k, v in found.items():
        print(f"\n{k} :")
        for f in v:
            print(f"->  {f}")

        print("")

    # Apadt size unit for larger or smaller files
    if total_size < 1000:
        print(f"Total Size | {total_size} Bytes")

    elif total_size < 100 * 1000:
        print(f"Total Size | {total_size / 1000} KB")

    elif total_size < 100 * 1000 * 1000:
        print(f"Total Size | {total_size / 1000 / 1000} MB")

    else:
        print(f"Total Size | {total_size / 1000 / 1000 / 1000} GB")

    current_most_common = (0, None)
    for k in most_common_extensions.keys():
        if most_common_extensions[k] > current_most_common[0]:
            current_most_common = [most_common_extensions[k], k]

    print(f"Most Common Extension : {current_most_common[1]}")
    print(f"Total Files : {total_files}")
    print(f"Total Subfolders : {total_folders}")
    print(f"Largest File : {biggest_file[1]}")
    print(f"Exe(s) : {exes if len(exes) > 0 else "No Exe(s)"}\n")


        



