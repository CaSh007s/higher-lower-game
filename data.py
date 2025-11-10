
import random

# We'll use a single category for now to build the logic.
# Let's use 'Social Media Followers'
TEST_DATA = [
    {
        'name': 'Instagram',
        'metric': 672,
        'metric_label': 'million followers'
    },
    {
        'name': 'Cristiano Ronaldo',
        'metric': 631,
        'metric_label': 'million followers'
    },
    {
        'name': 'Lionel Messi',
        'metric': 503,
        'metric_label': 'million followers'
    },
    {
        'name': 'Selena Gomez',
        'metric': 429,
        'metric_label': 'million followers'
    },
    {
        'name': 'Kylie Jenner',
        'metric': 400,
        'metric_label': 'million followers'
    },
    {
        'name': 'Dwayne "The Rock" Johnson',
        'metric': 397,
        'metric_label': 'million followers'
    },
    {
        'name': 'Ariana Grande',
        'metric': 379,
        'metric_label': 'million followers'
    },
    {
        'name': 'Kim Kardashian',
        'metric': 364,
        'metric_label': 'million followers'
    },
    {
        'name': 'Beyoncé',
        'metric': 319,
        'metric_label': 'million followers'
    },
    {
        'name': 'Khaby Lame',
        'metric': 164,
        'metric_label': 'million followers'
    },
]

def get_random_item():
    """Pulls a random item from the data list."""
    return random.choice(TEST_DATA)