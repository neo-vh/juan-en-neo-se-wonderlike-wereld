import shlex
from pathlib import Path # Later use (Commands from seperate files)

command_map = { # Add imported classes / functions to dictionary along with trigger (key)
    "hello": lambda x: print("Hello"),

}

def main():

    instructions = parse_raw(input("Enter Command : "))

def parse_raw(input: str):

    objs = [o.strip() for o in shlex.split(input)]

    structured_objs = {
        "action" : objs[0].lower(),
        "arguments": objs[1:]
    }

    print(structured_objs)

while True:
    main()