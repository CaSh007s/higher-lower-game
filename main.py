
from data import get_random_item
from utils import LOGO, VS_LOGO, GREEN, RED, YELLOW, CYAN, RESET, clear_screen
import colorama

# Initialize colorama
colorama.init(autoreset=True)

def play_game():
    """The main game loop for Higher / Lower."""
    
    score = 0
    game_over = False
    
    # Get the first item
    item_a = get_random_item()
    
    while not game_over:
        # Clear screen for the new round
        clear_screen()
        
        # Display the logo only at the start of the game (score 0)
        if score == 0:
            print(LOGO)

        # Get the second item, make sure it's not the same as A
        item_b = get_random_item()
        while item_a == item_b:
            item_b = get_random_item()
            
        # Display the comparison
        print(f"Compare A: {item_a['name']}, {item_a['metric_label']}.")
        
        print(CYAN + VS_LOGO) # Add some color to the VS logo
        
        print(f"Against B: {item_b['name']}.")
        
        # Get user's guess
        guess = input("Who has more? Type 'A' or 'B': ").upper()
        
        # Determine the correct answer
        if item_a['metric'] > item_b['metric']:
            correct_answer = 'A'
        else:
            correct_answer = 'B'
            
        # Check the guess
        if guess == correct_answer:
            score += 1
            print(GREEN + f"You're right! Current score: {score}")
            
            # The winner becomes the new item_a for the next round
            if correct_answer == 'B':
                item_a = item_b
        else:
            game_over = True
            print(RED + f"Sorry, that's wrong. {item_b['name']} has {item_b['metric']} {item_b['metric_label']}.")
            print(YELLOW + f"Game Over! Your final score is: {score}")
        
        # Pause before the next round or ending
        if not game_over:
            input("Press Enter to continue...")

# --- Main execution ---
if __name__ == "__main__":
    play_game()