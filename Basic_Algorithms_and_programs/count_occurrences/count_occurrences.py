a = input("Enter the string: ")
b = input("Enter the character you want to find: ")


if len(b) == 0:
    print("You didn't enter a character to find!")
else:
    # Python Pro-Tip: Use .lower() on both strings for a case-insensitive search!
    c = a.lower().count(b.lower())

    # Using f-strings (f"...") to clean up the print statements
    if b.isalpha():
        print(f"The letter '{b}' occurs {c} times.")
    elif b.isdigit():
        print(f"The number '{b}' occurs {c} times.")
    else:
        print(f"The special character '{b}' occurs {c} times.")