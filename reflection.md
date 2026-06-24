# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

  1. The "New Game" button starts a new round, but clicking "Submit" in the new game produces no response.
  2. In the difficulty adjustment section on the left, selecting a new difficulty level should refresh the game, but it does not.
  3. The difficulty settings are illogical: "Normal" mode offers a guessing range of 1–100 with 8 attempts, whereas "Hard" mode has a range of 1–50 with only 5 attempts, and "Easy" mode allows 6 attempts.
  4. Entering a number higher than the target displays "Go Higher" (it should show "Go Lower"), and vice versa.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess of 64| Go Lower      | Go Higher       | None                   |
|New Game| Playing the new game normally| Submit guess button did not work| None|
|Adjust difficulty| start a new game with new difficulty| Did not start a new game| None|

---

## 2. How did you use AI as a teammate?

- I used ChatGPT and the Claude extension in VS Code as AI coding assistants during this project. I used them to help me understand the bugs, decide which functions should move into logic_utils.py, and create tests for the game logic.

- One correct AI suggestion was to move the pure game logic functions out of app.py and into logic_utils.py. These functions included get_range_for_difficulty, parse_guess, check_guess, and update_score.  I verified this by importing the functions from logic_utils.py in tests/test_game_logic.py and running python -m pytest. The tests passed.

- There was a logic error in the initial AI-generated code: when I first specified that the allowed number of attempts should vary based on difficulty level, the AI ​​failed to make the change entirely—it only worked after I reiterated the requirement.

---

## 3. Debugging and testing your fixes

- I decided whether the bugs were fixed by using both automated tests and manual testing in the terminal. For automated testing, I added pytest tests in tests/test_game_logic.py.

- python -m pytest

- The result showed that all tests passed:

- 15 passed

- This confirmed that the core game logic worked correctly after my repairs.

- I also tested the live game manually by running:

- python -m streamlit run app.py

- In the app, I checked that entering a number higher than the secret number showed “Go LOWER,” and entering a number lower than the secret number showed “Go HIGHER.” I also checked that clicking “New Game” reset the game properly and allowed the “Submit Guess” button to keep working. Finally, I tested the difficulty select function and confirmed that changing the difficulty refreshed the game with the correct range and attempt limit.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
