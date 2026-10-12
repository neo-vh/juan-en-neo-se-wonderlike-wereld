from pathlib import Path
import os
from datetime import datetime

def log(message, log_dst:str = "C:\\Users\\Neo van Heerden\\OneDrive\\Desktop\\juan-en-neo-se-wonderlike-wereld\\log.txt"):
    
    with open(log_dst, 'r+') as f:
        old_content = f.read()
        
        dt = datetime.fromtimestamp(datetime.timestamp(datetime.now()))
        
        f.seek(0)    
        f.write(old_content + "\n" + f"[{dt}] {message}")
        f.truncate()
        
if __name__ == "__main__":
    log("this is a test")