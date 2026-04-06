* While building this, I discovered a very common trap when counting words in Python.

 If you count words by splitting the string by a space character len(text.split(" ")), it works fine perfectly—until the user accidentally types two spaces. Then, Python counts the extra space as an empty string, artificially inflating your word count!

  The Solution:
 If you use .split() with no arguments, Python's built-in algorithm automatically handles multiple spaces, trailing spaces, and even tabs, giving you a completely bulletproof word count:
