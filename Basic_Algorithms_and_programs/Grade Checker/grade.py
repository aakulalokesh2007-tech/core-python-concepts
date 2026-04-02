# .center(60) automatically centers the text perfectly!
print("Welcome to Grade Checker".center(60))
print("-" * 60)

while True:
    raw_input = input("Enter your percentage (or press Enter to exit): ")
    
    if raw_input == "":
        break
        
    try:
        
        a = float(raw_input)
        
        # Using Python's chained comparisons!
        if 90 < a <= 100:
            print("Super! You got an A+ grade.\n")
        elif 80 < a <= 90:
            print("Good! You got an A grade.\n")
        elif 70 < a <= 80: 
            print("Better! You got a B grade.\n")
        elif 60 < a <= 70:
            print("Well done, you got a C grade.\n")
        elif 50 < a <= 60:
            print("Not bad, you got a D grade.\n")
        elif 35 < a <= 50:
            print("Work hard, you got an E grade.\n")
        elif 0 <= a <= 35:
            print("Sorry to inform you that you have failed.\n")
        else:
            # This catches numbers over 100 or below 0
            print("Please enter a valid percentage between 0 and 100.\n")
            
    except ValueError:
        # This prevents the code from crashing if they type a word instead of a number
        print("Invalid input! Please enter a numeric value.\n")