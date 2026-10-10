import os
from pathlib import Path

def find(filename: str, search_root = "C:\\"):

    found = []
    stack = [search_root]

    while stack:
        current_path = stack.pop()

        with os.scandir(current_path) as entries:
            for e in entries:
                if e.is_dir():
                    stack.append(e.path)
                elif e.name == filename:
                    found.append(e.path)

    print(f"Located {len(found)} possible matches :")
    for p in found:
        print(p)
