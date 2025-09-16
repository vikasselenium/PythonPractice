'''
**Why use logging? **
- To track how many requests came to server (utilization reports).
- To debug issues when something goes wrong.
- logs help in preparing RCA

**Python's `logging` module**
- We use 'Logging'  Built-in  python module for logging

**Logging Levels (from most to least severe):**
1. Critical (50) –  Very serious error, app might crash. means high level
                    attention is needed
2. Error (40) – it is a series error, suggests some part of application is
                not working
3. Warning (30) – it is alert, suggesting Something might go wrong, check it.
4. Info (20) – it is some important message
                (e.g., "Process started").
5. Debug (10) –  info that is used for debugging.
                (if we want to print some debugging statements)
6. NotSet (0) – No specific level set.
---

** there are two ways to create a logger in python **
   - root logger: it is a default logger provided by python
   - custom logger:  User-defined logger with a specific name

'''