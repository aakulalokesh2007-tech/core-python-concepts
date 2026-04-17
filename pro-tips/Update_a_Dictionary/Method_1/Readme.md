Cleaner Python Code: Upgrading how we merge dictionaries! 🐍✨

When building applications, handling default user data vs. provided user data is a daily task. For a long time, the standard way to merge dictionaries in Python was using the .update() method or dictionary unpacking (**).

While those work perfectly fine, I love using the dictionary update operator (|=) introduced in Python 3.9!

It works exactly like the += operator used in math. It takes your base default configuration, automatically overwrites any overlapping keys with the new user data, and keeps everything else intact—all in one highly readable line of code.

The evolution of merging:
1️⃣ default.update(user_data) (The classic way)
2️⃣ default = {**default, **user_data} (The unpacking way)
3️⃣ default |= user_data (The modern, Pythonic way! 🚀)
