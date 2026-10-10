import shlex
from rapidfuzz import fuzz, process # Ensure spelling mistakes can be accounted for (accepted)
from commands_files.turtle_example_commands import draw_square, draw_triangle # Example Commands from separate file
from commands_files.file_ops import find # File operations commands


command_map = { # Add imported classes / functions to dictionary along with trigger (key)
    "hello": lambda x: print(f"Hello {x[1]}"), # Example command
    "square": draw_square,
    "triangle": draw_triangle,
    "find": find,
    "end": lambda x: exit(0)

}

def main():

    instructions = parse_raw(input("\nEnter Command : "))

    if instructions["action"] in command_map:
        try:
            command_map[instructions["action"]](instructions["arguments"])
        except (TypeError, IndexError, ValueError) as e:
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
        "arguments": objs[1:] if len(objs[1:]) > 1 else objs[1] if len(objs[1:]) == 1 else None
    }

    print(structured_objs) # For debugging purposes, can be removed later

    return structured_objs

while True:
    main()