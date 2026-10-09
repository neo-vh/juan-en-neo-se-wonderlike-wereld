import shlex
from pathlib import Path # Later use (Commands from seperate files)

def main():

    instructions = parse_raw(input("Enter Command : "))

def parse_raw(input: str):

    objs = [o.strip() for o in shlex.split(input)]

    structured_objs = {
        "action" : objs[0].lower(),
        "arguements": objs[1:]
    }

    print(structured_objs)

while True:
    main()