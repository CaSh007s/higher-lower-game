
import os
from colorama import Fore, Style

# ASCII Art Logo
LOGO = """
    __  __ ___ ___ ___    _   _ ___    ___ _  _ ___ 
    |  \/  | __| _ \ __|  | | | | _ \  | _ \ \/ / __|
    | |\/| | _||   / _|   | |_| |  _/  |  _/>  <| _| 
    |_|  |_|___|_|_\___|   \___/|_|    |_| /_/\_\___|
                                                    
"""

# VS Logo
VS_LOGO = """
__   __
\ \ / /
 \ V / 
  \_/  
"""

# Color definitions
GREEN = Fore.GREEN
RED = Fore.RED
YELLOW = Fore.YELLOW
CYAN = Fore.CYAN
RESET = Style.RESET_ALL

def clear_screen():
    """Clears the terminal screen."""
    # 'nt' is for Windows, 'posix' is for Mac/Linux
    os.system('cls' if os.name == 'nt' else 'clear')