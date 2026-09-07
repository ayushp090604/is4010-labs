# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed and authenticated GitHub Copilot CLI successfully. I verified it was working by launching the CLI and receiving a response to my prompt. The displayed version was GitHub Copilot CLI v1.0.83.


### Antigravity CLI

I installed and authenticated Antigravity CLI successfully. I verified the installation by launching the CLI and receiving a response to the assigned prompt. The tool responded correctly and was available from inside the repository.


## Shared task

### Shared prompt

```text
Write a Python function called count_vowels(text: str) that counts the vowels a, e, i, o, and u regardless of case. Do not count y. Explain your approach briefly.
```

### Copilot CLI observations

Copilot suggested a solution that created a collection of vowels and used the sum function to count matching characters. The response converted each character to lowercase before checking if it was a vowel, which ensured the function was case insensitive. I verified that y was not included in the vowel set. The explanation was concise and easy to understand. I would still verify the behavior with automated tests before using the code in the final submission.

### Antigravity CLI observations

Antigravity suggested a solution that also counted vowels without regard to case. The explanation described looping through the text and checking whether each character belonged to a list or set of vowels. The response appeared correct and addressed all requirements from the prompt. I would verify edge cases such as empty strings and mixed uppercase and lowercase letters before accepting the solution.

### Comparison

Both tools produced correct solutions for the count_vowels function. Each approach handled uppercase and lowercase letters correctly and excluded the letter y from the vowel count. Copilot's response was very concise and used a compact expression with sum, while Antigravity provided a more detailed explanation of the logic. I found Copilot slightly easier to copy directly into the project because it was shorter, but Antigravity helped explain the reasoning behind the implementation. After comparing both responses, I chose the approach that used a vowel collection and the sum function because it was readable, efficient, and passed the automated tests. The two responses reached essentially the same result but presented the solution differently.

## Test-guided implementation

After creating lab02.py, I ran the provided test suite using pytest. All of the Python function tests passed successfully, which confirmed that make_greeting, is_even, and count_vowels behaved according to the provided contracts. The only failures were related to the prompt journal because the template still contained placeholder text. This demonstrated the value of automated testing because it identified exactly what was missing. I reviewed my implementation and confirmed that count_vowels handled uppercase and lowercase characters correctly and did not count y as a vowel. Once the journal sections were completed, I reran the tests to verify that both the implementation and documentation requirements were satisfied.

## Preferred tool combination

Each tool served a different purpose during this lab. Browser chat tools are useful when I need detailed explanations or help understanding instructions. GitHub Copilot in VS Code is convenient because suggestions appear while writing code, which reduces context switching. Copilot CLI was helpful for quickly asking coding questions from within the repository. Antigravity CLI offered another perspective on the same problem and made it easier to compare solutions. At the moment, my preferred workflow is VS Code with Copilot plus a browser chat for explanations. However, if I were working primarily in a terminal environment, I could see Copilot CLI or Antigravity CLI becoming my preferred tools because they allow quick access to assistance without leaving the command line.

