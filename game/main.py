# game/main.py
from data import CATEGORIES, get_random_item
from api import get_random_pokemon  # <-- NEW IMPORT
from utils import (
    LOGO, VS_LOGO, GREEN, RED, YELLOW, CYAN, BLUE, RESET,
    clear_screen, get_high_score, save_high_score
)
import colorama
import time

# Initialize colorama
colorama.init(autoreset=True)

#
# GAME LOOP 1: FOR STATIC DATA (FROM data.py)
#
def play_game(category_data, current_high_score):
    """The main game loop for static data lists."""
    
    score = 0
    game_over = False
    item_a = get_random_item(category_data)
    
    while not game_over:
        clear_screen()
        print(LOGO)
        print(BLUE + f"Current High Score: {current_high_score}")
        print("---------------------------------")
        
        item_b = get_random_item(category_data)
        while item_a == item_b:
            item_b = get_random_item(category_data)
            
        print(f"Compare A: {item_a['name']}, who has {item_a['metric']} {item_a['metric_label']}.")
        print(CYAN + VS_LOGO)
        print(f"Against B: {item_b['name']}.")
        
        guess = input("Who has more? Type 'A' or 'B': ").upper()
        
        if item_a['metric'] > item_b['metric']:
            correct_answer = 'A'
        else:
            correct_answer = 'B'
            
        if guess == correct_answer:
            score += 1
            print(GREEN + f"You're right! Current score: {score}")
            if correct_answer == 'B':
                item_a = item_b
        else:
            game_over = True
            print(RED + f"Sorry, that's wrong. {item_b['name']} has {item_b['metric']} {item_b['metric_label']}.")
            print(YELLOW + f"Game Over! Your final score is: {score}")
            
            if score > current_high_score:
                print(YELLOW + f"NEW HIGH SCORE! Saving {score}...")
                save_high_score(score)
                current_high_score = score
            else:
                print(f"Your final score was {score}. The high score is {current_high_score}.")
        
        if not game_over:
            input("Press Enter to continue...")
        else:
            input("Press Enter to return to the main menu...")
    
    return current_high_score

#
# GAME LOOP 2: FOR LIVE API DATA (FROM api.py)
#
def play_api_game(current_high_score):
    """The main game loop for the live PokeAPI."""
    
    score = 0
    game_over = False
    
    print(YELLOW + "Fetching first Pokémon...")
    item_a = get_random_pokemon()
    # Keep trying if the API fails
    while item_a is None:
        print(RED + "Fetch failed, retrying...")
        time.sleep(1)
        item_a = get_random_pokemon()

    while not game_over:
        clear_screen()
        print(LOGO)
        print(BLUE + f"Current High Score: {current_high_score}")
        print(YELLOW + "CATEGORY: POKÉMON BASE EXPERIENCE")
        print("---------------------------------")
        
        print(YELLOW + "Fetching next Pokémon...")
        item_b = get_random_pokemon()
        while item_b is None or item_a['name'] == item_b['name']:
            print(RED + "Fetch failed or was a duplicate, retrying...")
            time.sleep(1)
            item_b = get_random_pokemon()
            
        print(f"Compare A: {item_a['name']}, who has {item_a['metric']} {item_a['metric_label']}.")
        print(CYAN + VS_LOGO)
        print(f"Against B: {item_b['name']}.")
        
        guess = input("Who has more? Type 'A' or 'B': ").upper()
        
        if item_a['metric'] > item_b['metric']:
            correct_answer = 'A'
        else:
            correct_answer = 'B'
            
        if guess == correct_answer:
            score += 1
            print(GREEN + f"You're right! Current score: {score}")
            if correct_answer == 'B':
                item_a = item_b
        else:
            game_over = True
            print(RED + f"Sorry, that's wrong. {item_b['name']} has {item_b['metric']} {item_b['metric_label']}.")
            print(YELLOW + f"Game Over! Your final score is: {score}")
            
            if score > current_high_score:
                print(YELLOW + f"NEW HIGH SCORE! Saving {score}...")
                save_high_score(score)
                current_high_score = score
            else:
                print(f"Your final score was {score}. The high score is {current_high_score}.")
        
        if not game_over:
            input("Press Enter to continue...")
        else:
            input("Press Enter to return to the main menu...")
    
    return current_high_score

#
# MAIN MENU
#
def main_menu():
    """Displays the main menu and handles user category selection."""
    
    high_score = get_high_score()
    
    while True:
        clear_screen()
        print(LOGO)
        print(BLUE + f"Current High Score: {high_score}\n")
        print(YELLOW + "Choose a category to play:")
        
        # Display all static categories
        for key, value in CATEGORIES.items():
            print(f"  [{key}] {value['name']}")
        
        # Display our new API category
        print(f"  [4] Pokémon Base Experience (Live from PokeAPI)")
        
        print(f"\n  [Q] Quit")
        
        choice = input("\nYour choice: ").upper()
        
        if choice == 'Q':
            print("Thanks for playing!")
            break
            
        if choice in CATEGORIES:
            # User chose a static category
            chosen_data = CATEGORIES[choice]["data"]
            high_score = play_game(chosen_data, high_score)
        elif choice == '4':
            # User chose the new API category
            high_score = play_api_game(high_score)
        else:
            print(RED + "Invalid choice. Please try again.")
            time.sleep(1) # Pause briefly to show the error

# --- Main execution ---
if __name__ == "__main__":
    main_menu()