text = input("Enter any message: ")


if not text.strip():
    print("You entered an empty string!")
else:
    total_chars = len(text)
    
    # .split() with no arguments handles multiple spaces perfectly!
    word_count = len(text.split()) 
    
    letters = 0
    numbers = 0
    
    for char in text:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            numbers += 1
        
        
            
    
    alphanumeric_percent = ((letters + numbers) / total_chars) * 100
    
    print("\n--- Text Analysis ---")
    print(f"Message: '{text}'")
    print(f"Number of words: {word_count}")
    print(f"Number of characters (with spaces): {total_chars}")
    print(f"Number of digits: {numbers}")
    print(f"Alphanumeric percentage: {round(alphanumeric_percent, 2)}%")