# 🐍 Python Higher-Lower Game 🐍

This is a complete, text-based "Higher or Lower" game built in Python. It's fully playable in the terminal and features a polished TUI (Terminal User Interface) with colors and custom ASCII art.

---

## 🚀 Features

* **Polished TUI:** Uses `colorama` for a colorful, modern terminal experience.
* **Custom ASCII Art:** A full main menu and "VERSUS" logo.
* **High Score System:** Your best score is saved in `highscore.txt` and displayed on the main menu.
* **Multiple Game Modes:**
    * **Classic Mode:** Play with static, reliable data decks (Social Media, Movie Box Office, Country Population).
    * **Live API Mode:** Play with real-time data from the PokeAPI, comparing Pokémon Base Experience.

---

## 🏃 How to Run

This project uses a virtual environment and requires a few packages.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/CaSh007s/higher-lower-game.git](https://github.com/CaSh007s/higher-lower-game.git)
    cd higher-lower-game
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the game!**
    ```bash
    # Navigate into the game directory
    cd game
    
    # Run the main file
    python main.py
    ```

Enjoy!
