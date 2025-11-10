
import os
from colorama import Fore, Style

# ASCII Art Logo
LOGO = r"""
$$\   $$\ $$\           $$\                           
$$ |  $$ |\__|          $$ |                          
$$ |  $$ |$$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
$$$$$$$$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
$$  __$$ |$$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
$$ |  $$ |$$ |\$$$$$$$ |$$ |  $$ |\$$$$$$$\ $$ |      
\__|  \__|\__| \____$$ |\__|  \__| \_______|\__|      
              $$\   $$ |                              
              \$$$$$$  |                              
               \______/                               
$$\                                                   
$$ |                                                  
$$ |      $$$$$$\  $$\  $$\  $$\  $$$$$$\   $$$$$$\   
$$ |     $$  __$$\ $$ | $$ | $$ |$$  __$$\ $$  __$$\  
$$ |     $$ /  $$ |$$ | $$ | $$ |$$$$$$$$ |$$ |  \__| 
$$ |     $$ |  $$ |$$ | $$ | $$ |$$   ____|$$ |       
$$$$$$$$\\$$$$$$  |\$$$$$\$$$$  |\$$$$$$$\ $$ |       
\________|\______/  \_____\____/  \_______|\__|       
                                                      
                                                      
                                                                                                         
"""

# VS Logo (Provided by you - "VERSUS")
VS_LOGO = r"""                                              
,--.  ,--.,---. ,--.--. ,---. ,--.,--. ,---.  
 \  `'  /| .-. :|  .--'(  .-' |  ||  |(  .-'  
  \    / \   --.|  |   .-'  `)'  ''  '.-'  `) 
   `--'   `----'`--'   `----'  `----' `----'  
                                              
"""

# Color definitions
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
BLUE = Fore.BLUE  # <-- NEW COLOR
RESET = Style.RESET_ALL

# Path to the high score file (one level up from main.py)
HIGHSCORE_FILE = "../highscore.txt"

def clear_screen():
    """Clears the terminal screen."""
    # 'nt' is for Windows, 'posix' is for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def get_high_score():
    """Reads the high score from the file."""
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            score = int(f.read())
            return score
    except (FileNotFoundError, ValueError):
        # File doesn't exist or is empty/corrupt, create it
        save_high_score(0)
        return 0

def save_high_score(new_score):
    """Saves the new high score to the file."""
    try:
        with open(HIGHSCORE_FILE, "w") as f:
            f.write(str(new_score))
    except IOError as e:
        print(f"{RED}Error: Could not save high score.{RESET}")
        print(e)