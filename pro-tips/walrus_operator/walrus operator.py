# ==========================================
# 🦭 THE PYTHON WALRUS OPERATOR (:=)
# Introduced in Python 3.8
# ==========================================

# The walrus operator allows you to assign a value to a variable 
# AND return that value in the exact same line of code.

# --- Example 1: The Mood Check ---

# ❌ The Old Way (2 lines):
happy = True
print(happy)

# ✅ The Walrus Way (1 line):
print(happy := True)


# --- Example 2: The While Loop ---
# Let's say we are asking a user for input until they type 'quit'

# ❌ The Old Way:
user_input = input("Enter a command: ")
while user_input != "quit":
    print(f"Executing: {user_input}")
    user_input = input("Enter a command: ") # Have to write this twice!

# ✅ The Walrus Way:
# It assigns the input to 'command' and immediately checks if it equals 'quit'
while (command := input("Enter a command: ")) != "quit":
    print(f"Executing: {command}")
