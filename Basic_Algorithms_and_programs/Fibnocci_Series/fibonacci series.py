while True:
    user_input = input("Enter the number of terms: ")
    
    if user_input.isdigit():
        n = int(user_input)
        
        # Handle the edge cases of 0 and 1
        if n == 0:
            print("Please enter a number greater than 0.")
            continue # Goes back to the start of the loop
        elif n == 1:
            print("Fibonacci series:\n0")
            break
            
        # Normal calculation for 2 or more terms
        b, c = 0, 1
        print("Fibonacci series:")
        print(f"{b} {c}", end=' ')
        
        for _ in range(n - 2):
            e = b + c
            print(e, end=' ')
            b, c = c, e
            
        print() # Adds a clean newline at the end
        break
    else:
        print("Please enter only positive numbers.")