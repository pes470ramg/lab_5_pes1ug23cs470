# Reflection – Static Code Analysis Lab

### 1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest issues to fix were the unused import, missing docstrings, and formatting errors like missing blank lines or final newline.  
The hardest one was removing the use of `eval()` and properly handling file operations with `with open()` and encoding, since that required changing the structure of the functions slightly without breaking functionality.

---

### 2. Did the static analysis tools report any false positives? Give one example.
Yes. Pylint flagged the use of the `global` keyword as a warning even though it was necessary to share the `stock_data` dictionary between functions.  
That wasn’t really an error but a design choice for this simple lab.

---

### 3. How would you integrate static analysis tools into your actual development workflow?
I would integrate Pylint, Bandit, and Flake8 into a continuous integration (CI) pipeline so they automatically check every commit or pull request.  
For smaller projects, I’d also set them up as pre-commit hooks to catch issues before pushing code to the repository.

---

### 4. What improvements did you observe in code quality after applying the fixes?
The code is now cleaner, more readable, and follows proper PEP 8 conventions.  
Potential security issues like the `eval()` call are gone, error handling is explicit, and file operations are safe and well-documented.  
Overall, the program feels more reliable and professional.

---