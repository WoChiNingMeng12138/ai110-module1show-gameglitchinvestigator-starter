# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [✓] Describe the game's purpose.
This project is a number guessing game. The player chooses a difficulty, enters guesses, receives higher/lower hints, and tries to find the secret number before running out of attempts.

- [✓] Detail which bugs you found.
I found several bugs in the original game. First, after clicking the New Game button, the game appeared to reset, but the Submit Guess button did not work correctly because the game status was not reset to "playing". Second, the hint logic was reversed: when the guess was too high, the game told the player to go higher instead of lower. Third, changing the difficulty in the sidebar did not start a fresh game. Fourth, the difficulty settings were inconsistent because Hard mode had a smaller number range than Normal mode.

- [✓] Explain what fixes you applied.
I refactored the core logic into logic_utils.py, including functions for difficulty ranges, input parsing, guess checking, and score updating. I fixed the higher/lower hint logic so that guesses above the secret number return "Too High" and tell the player to go lower. I also added a reset_game() function in app.py to reset the secret number, attempts, score, status, and history when starting a new game or changing difficulty. Finally, I adjusted the difficulty settings so they increase more logically from Easy to Normal to Hard.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. The user opens the app with python -m streamlit run app.py.
2. The user selects a difficulty level. For example, on Normal mode, the game uses a range of 1 to 100 and allows 7 attempts.
3. The user opens the Developer Debug Info section to confirm the secret number for testing. For example, assume the secret number is 50.
4. The user enters a guess of 60 and clicks Submit Guess. The game returns "Too High" and displays a message telling the user to go lower.
5. The user enters a guess of 40 and clicks Submit Guess. The game returns "Too Low" and displays a message telling the user to go higher.
6. The user enters the correct guess, 50. The game displays a win message, shows the final score, and triggers the celebration animation.
7. The user clicks New Game. The game resets correctly, creates a new secret number, clears the previous history, and allows the user to submit guesses again.
8. The user changes the difficulty in the sidebar. The game refreshes with a new number range, a new attempt limit, and a new secret number.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
============================================================================ test session starts ============================================================================ 
platform win32 -- Python 3.14.0, pytest-9.0.3, pluggy-1.6.0
rootdir: F:\UniversityDocument\US_TAMU\2026_Summer\Interview\AI_project_1\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 15 items                                                                                                                                                            

tests\test_game_logic.py ...............

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
