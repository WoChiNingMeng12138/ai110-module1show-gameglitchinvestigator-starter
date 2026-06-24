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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
