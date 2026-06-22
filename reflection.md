# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  It ran normally until the end, where it revealed that the secret number was higher than what the hint suggested.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  - incorrect hint
  - unable to start new game

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input          | Expected Behavior         | Actual Behavior              | Console Output / Error |
|----------------|---------------------------|------------------------------|------------------------|
| Incorrect hint | Either output higher/lower| Always outputted "go lower"  | "Go LOWER!"            |
|                | if the inputed number if  | despite the number always    |                        |
|                | higher/lower than the     | being lower than the secret  |                        |
|                | secret number.            | number.                      |                        |
|----------------|---------------------------|------------------------------|------------------------|
|Secret number   | Expected the number to be | At the summary 47 was the    |N/A                     |
|changing        | static                    | secret number despite it     |                        |
|                |                           | being 90 when the game ended |                        |
|----------------|---------------------------|------------------------------|------------------------|
| Unable to start|expected to start new      | Stucked at the end of the    | N/A                    |
| new game       |game                       | previous game                |                        |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Cluade
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

For the inverted hint bug involving the check_guess function the AI suggest to swap the hint's statements of going lower and higher. I verified fix via running the program to confirm if the hints are accurate.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Also involving the inverted hint bug, the AI would use < instead of > for comparing the guess and secret, which would be an incorrect fix since the opposite scenario would occur as the problem lies in the statements. I would verified the result by running the program to confirm if the hints are accurate and if not, I would continue to fix the bug.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  A bug is truly fixed after running the program without encountering any problem and considering cases where it could possibly appear to ensure it doesn't pop up.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  For the inverted hints, I used pytest to confirm if the fixed had worked as it passes through multiple tests and then I ran the program various times in streamlit to manually confirm it.

- Did AI help you design or understand any tests? How?

  I understood the tests for check_guess as it ran tests to check if the guess was either a correct, high, low, and to tell the user to higher/lower if it too low/high.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I wasn't aware of Streamlit "rerun" feature until this question as I had close each session after running the program to see if the fix had work, and hadn't notice the three dots in the top right corner.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
 - This could be a testing habit, a prompting strategy, or a way you used Git.

A prompting strategy that I would take away from this project would be to give context when prompting such as providing the files related to what I'm working instead of making up things that it needs that I haven't provide.

- What is one thing you would do differently next time you work with AI on a coding task?

One thing to take away from this project would be to allow the AI to describe the code and what it does before implementing it and not to blindly trust the code that the AI gives.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI generated code should be doubted and shouldn't recklessly be implemented into your program without prior testing its reliability and it ability to run.