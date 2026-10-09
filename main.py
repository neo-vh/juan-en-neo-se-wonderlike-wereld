import shlex
from pathlib import Path # Later use (Commands from seperate files)
from rapidfuzz import fuzz, process # Ensure spelling mistakes can be accounted for (accepted)


command_map = { # Add imported classes / functions to dictionary along with trigger (key)
    "hello": lambda: print("Hello}"), # Example command

}

def main():

    instructions = parse_raw(input("Enter Command : "))

    if instructions["action"] in command_map:
        try:
            command_map[instructions["action"]](instructions["arguments"])
        except TypeError as e:
            print(f"Error {e} enocunterd while running command")

    else:
        fuz_check = process.extractOne(
            instructions["action"], 
            command_map.keys(), 
            scorer=fuzz.WRatio,
        )
    
        if fuz_check[1] > 80:
            command_map[fuz_check[0]](instructions["arguments"])

        else:
            print(f'Command {instructions["action"]} does not exist. Maybe you meant {fuz_check[0]}?')
    

def parse_raw(input: str):

    objs = [o.strip() for o in shlex.split(input)]

    structured_objs = {
        "action" : objs[0].lower(),
        "arguments": objs[1:]
    }

    print(structured_objs)

    return structured_objs

while True:
    main()