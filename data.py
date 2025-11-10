
import random

# Category 1: Social Media Followers
social_media_data = [
    {'name': 'Instagram', 'metric': 672, 'metric_label': 'million followers'},
    {'name': 'Cristiano Ronaldo', 'metric': 631, 'metric_label': 'million followers'},
    {'name': 'Lionel Messi', 'metric': 503, 'metric_label': 'million followers'},
    {'name': 'Selena Gomez', 'metric': 429, 'metric_label': 'million followers'},
    {'name': 'Kylie Jenner', 'metric': 400, 'metric_label': 'million followers'},
    {'name': 'Dwayne "The Rock" Johnson', 'metric': 397, 'metric_label': 'million followers'},
    {'name': 'Ariana Grande', 'metric': 379, 'metric_label': 'million followers'},
    {'name': 'Kim Kardashian', 'metric': 364, 'metric_label': 'million followers'},
    {'name': 'Beyoncé', 'metric': 319, 'metric_label': 'million followers'},
    {'name': 'Khaby Lame', 'metric': 164, 'metric_label': 'million followers'},
]

# Category 2: Movie Box Office
movie_data = [
    {'name': 'Avatar', 'metric': 2.92, 'metric_label': 'billion $ box office'},
    {'name': 'Avengers: Endgame', 'metric': 2.79, 'metric_label': 'billion $ box office'},
    {'name': 'Avatar: The Way of Water', 'metric': 2.32, 'metric_label': 'billion $ box office'},
    {'name': 'Titanic', 'metric': 2.25, 'metric_label': 'billion $ box office'},
    {'name': 'Star Wars: The Force Awakens', 'metric': 2.06, 'metric_label': 'billion $ box office'},
    {'name': 'Avengers: Infinity War', 'metric': 2.04, 'metric_label': 'billion $ box office'},
    {'name': 'Spider-Man: No Way Home', 'metric': 1.92, 'metric_label': 'billion $ box office'},
    {'name': 'The Lion King (2019)', 'metric': 1.66, 'metric_label': 'billion $ box office'},
    {'name': 'Jurassic World', 'metric': 1.67, 'metric_label': 'billion $ box office'},
    {'name': 'The Avengers', 'metric': 1.52, 'metric_label': 'billion $ box office'},
    {'name': 'Barbie', 'metric': 1.44, 'metric_label': 'billion $ box office'},
]

# Category 3: Country Population
country_data = [
    {'name': 'India', 'metric': 1441, 'metric_label': 'million people'},
    {'name': 'China', 'metric': 1425, 'metric_label': 'million people'},
    {'name': 'United States', 'metric': 341, 'metric_label': 'million people'},
    {'name': 'Indonesia', 'metric': 279, 'metric_label': 'million people'},
    {'name': 'Pakistan', 'metric': 245, 'metric_label': 'million people'},
    {'name': 'Nigeria', 'metric': 229, 'metric_label': 'million people'},
    {'name': 'Brazil', 'metric': 217, 'metric_label': 'million people'},
    {'name': 'Bangladesh', 'metric': 174, 'metric_label': 'million people'},
    {'name': 'Russia', 'metric': 144, 'metric_label': 'million people'},
    {'name': 'Mexico', 'metric': 129, 'metric_label': 'million people'},
    {'name': 'Japan', 'metric': 123, 'metric_label': 'million people'},
]

# Main dictionary to hold all categories
CATEGORIES = {
    "1": {
        "name": "Social Media Followers",
        "data": social_media_data
    },
    "2": {
        "name": "Movie Box Office",
        "data": movie_data
    },
    "3": {
        "name": "Country Population",
        "data": country_data
    }
}

def get_random_item(data_list):
    """Pulls a random item from a *specific* data list."""
    return random.choice(data_list)