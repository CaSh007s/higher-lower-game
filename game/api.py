
import requests
import random

# The base URL for the free Pokémon API
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_random_pokemon():
    """
    Fetches a random Pokémon and formats it for our game.
    """
    try:
        # We'll stick to the original 151 for classic, well-known data
        random_id = random.randint(1, 151)
        
        # 1. Make the API call
        response = requests.get(f"{BASE_URL}{random_id}/")
        
        # 2. Check if the request was successful
        response.raise_for_status() # This will raise an error if the request failed
        
        # 3. Parse the JSON response
        data = response.json()
        
        # 4. Format the data into our game's dictionary structure
        formatted_data = {
            'name': data['name'].capitalize(),
            'metric': data['base_experience'],
            'metric_label': 'base experience'
        }
        return formatted_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching Pokémon data: {e}")
        return None

# --- This part lets us test the file directly ---
if __name__ == "__main__":
    print("Testing PokeAPI fetch...")
    pokemon = get_random_pokemon()
    if pokemon:
        print("Successfully fetched:")
        print(pokemon)
    else:
        print("Fetch failed.")