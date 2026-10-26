# 🗺️ Country Trivia CLI 🌍

A fun command-line interface (CLI) trivia game to test your knowledge of world capitals\!

<p align="center">
  <img width="380" height="172" alt="Screen Shot 2025-10-07 at 15 00 57" src="https://github.com/user-attachments/assets/de508e61-4f20-4aa0-b2f3-9b133eed2ba3" />
</p>
---

## 📜 Table of Contents

- [About The Project](#-about-the-project)
- [✨ Features](#-features)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [🎮 How to Play](#-how-to-play)
- [🧠 Data Structures & Algorithms](#-data-structures--algorithms)
- [⚠️ Archived Project](#️-archived-project)
- [🛠️ Known Issues](#️-known-issues)
- [📄 License](#-license)
- [📬 Contact](#-contact)

---

## 📖 About The Project

**Country Trivia CLI** is a simple yet engaging trivia game built with Python. It's designed to challenge your geography skills by asking you to guess the capital of a given country or the country of a given capital. Country data is loaded directly from a local CSV file using Python's built-in `csv` module — no external dependencies required.

This project was created as a fun way to practice Python fundamentals, file handling, and data structures.

**Tech Stack:**

- **Python 3** (stdlib only — `csv`, `random`)

---

## ✨ Features

- **Two Game Modes:** Guess the capital city or guess the country.
- **Randomized Questions:** The trivia questions are shuffled for a new experience every time.
- **Simple CLI:** Easy-to-use and intuitive command-line interface.
- **Score Tracking:** (As seen in `player_data.py`) The structure is in place to easily add player and score tracking functionality.

---

## 🚀 Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

Make sure you have **Python 3** and **pip** installed on your system. You can check by running:

```sh
python --version
pip --version
```

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/rajivghandi767/country-trivia-cli.git
    ```

2.  **Navigate to the project directory:**

    ```bash
    cd country-trivia-cli
    ```

3.  **No installation needed** — the game uses Python's standard library only (`pyproject.toml` and `uv.lock` are included for project metadata and `uv` environment management).

---

## 🎮 How to Play

1.  **Run the main script:**

    ```bash
    python trivia.py
    ```

2.  **Choose a category from the Main Menu:**

    - Type `1` to guess capitals.
    - Type `2` to guess countries.

3.  **Answer the prompts\!**

    - Type your answer and press `Enter`.
    - If you want to go back to the main menu, type `0` and press `Enter`.
    - To exit the game at any time, press `Ctrl+C`.

<p align="center">
 <img width="371" height="124" alt="Screen Shot 2025-10-07 at 15 03 15" src="https://github.com/user-attachments/assets/cf7a68bd-85f1-47bc-804e-9b8af630964e" />

<img width="373" height="123" alt="Screen Shot 2025-10-07 at 15 03 47" src="https://github.com/user-attachments/assets/379c5601-b6c5-47c8-80b7-d8978076912d" />
</p>

---

## 🧠 Data Structures & Algorithms

This project utilizes fundamental concepts of data structures and algorithms to function effectively.

- **Data Structure: Hash Map (Dictionary)**

  - In the `modules/player_data.py` file, the `Scoreboard` class uses a Python dictionary (`self.players`) to store `Player` objects.
  - **Why it's good:** Using a dictionary provides an efficient way to manage player data. It allows for **O(1)** or constant time complexity on average for adding new players (`add_player`), retrieving a player's score (`get_player_score`), and updating scores (`add_score`), as it uses the player's name as a unique key.

- **Algorithm: Random Sampling**

  - The `shuffle_pack` function in `modules/game_functions.py` uses `random.sample(country_data, len(country_data))`.
  - **Why it's good:** This is an efficient way to create a shuffled copy of the country data list for each new game, ensuring that the order of questions is random and unpredictable for the user.

---

## ⚠️ Archived Project

This CLI application is **no longer in active development**, and no new features will be added. The project is being continuously developed as a full-stack web application.

For the latest version, please visit the new repository:
**[github.com/rajivghandi767/country-trivia-web](https://github.com/rajivghandi767/country-trivia-web)**

---

## 🛠️ Known Issues

- Answers require exact matches, including spacing and capitalization.
- "Saint" must be fully spelled out (e.g., "Saint John's").
- Only "Pretoria" is accepted as the capital of South Africa.
- Some capitals, like Kingston, are shared by multiple territories (Jamaica & Norfolk Island), which can lead to ambiguity.

---

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.

---

## 📬 Let's Connect

**Rajiv Wallace**  
*Self-taught Software Engineer based in NYC (originally from Dominica 🇩🇲). Aviation nerd, Formula One fan, Chelsea FC supporter, and passionate about robust Backend Development and bare-metal DevOps.*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rajiv-wallace)
[![Email](https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:dev@rajivwallace.com)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=flat-square&logo=dev.to&logoColor=white)](https://rajivwallace.com)
