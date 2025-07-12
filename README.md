
# Board-Games-OOP-Project – A Simple Board Game Shop in Python

**Board-Games-OOP** is a small project built in Python using object-oriented programming. It's a simulation of a board game shop where you can manage inventory, add and sell different types of board games, and apply discounts.


## Project Overview

- Different board game genres (strategy, family, party, etc.)
- Genre-specific features like complexity, recommended age, number of players, and more
- A shop system to add, remove, and view games
- Optional discount system that can be applied to individual games or entire genres

## Structure

# 🎲 BGames – A Simple Python Board Game Shop

**BGames** is a small Python OOP project that simulates a board game shop.  
You can add games from different genres, manage inventory, apply discounts, and more.

---

## 📁 Project Structure

```
.
├── src/                  # Core source code
│   ├── bgames.py         # Abstract base class for games
│   ├── genres.py         # Game genres with specific logic
│   ├── discounts.py      # Discount logic
│   ├── new_bgames.py     # Factory method to create new games
│   ├── shop.py           # Shop class to manage the game inventory
│   ├── tracker.py        # Tracks inventory changes
│   └── __init__.py
│
├── tests/                # Unit tests using unittest
│   ├── test_bgames.py
│   ├── test_discounts.py
│   ├── test_genres.py
│   ├── test_new_bgames.py
│   ├── test_shop.py
│   └── __init__.py
│
├── venv/                 # Virtual environment (optional)
│
└── WhatITriedToDo.txt    # Notes & reflections

```

## Features

* **Genre Support**: Strategy, family, party games, and more
* **Custom Attributes**: Max players, age recommendations, tips, complexity, etc.
* **Inventory System**: Add, view, and sell games
* **Factory Method**: Create new games dynamically by genre
* **Discount Module**: Apply optional discounts to individual games or genres
* **Basic Tracking**: Monitor actions like adding or selling games

## How to Run and Test

### Requirements

* Python 3.7+
* No external packages required

### Running the Project

You can run individual modules inside `src/` depending on what you'd like to test:

```bash
cd src
python shop.py
```

### Running Unit Tests

```bash
python -m unittest discover tests
```

---

## Notes

* All game info (names, prices, complexity) is based on real board games.
* The `discounts.py` file is separate to avoid overcomplicating base game classes
* `new_bgames.py` uses a simple factory method to assign new games to the right genre
* `tracker.py` tracks actions, useful for potential logging or analytics

## About

This project was built for fun and practice with Python OOP.
Inspired partly by a book joke about starting a seed shop—why not board games instead?

Thanks for checking it out.
