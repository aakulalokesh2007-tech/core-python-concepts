while True:
    a = input("Enter a binary number (or press Enter to stop): ")
    
    if a == "":
        break

    # Pythonic Validation: Checks if every character is a 0, 1, or .
    
    if not all(char in '01.' for char in a) or a.count('.') > 1:
        print("Please enter a valid binary number.")
        continue

    
    parts = a.split('.')
    integer_part = parts[0][::-1] # Reverse the integer part
    decimal_total = 0.0

    # Calculate the Integer Part
    for i in range(len(integer_part)):
        decimal_total += int(integer_part[i]) * (2 ** i)

    #  Calculate the Fractional Part (if a decimal point exists)
    if len(parts) == 2:
        fractional_part = parts[1] 
        for i in range(len(fractional_part)):
            
            decimal_total += int(fractional_part[i]) * (2 ** -(i + 1))

    
    if len(parts) == 1:
        print(f"Decimal value: {int(decimal_total)}")
    else:
        print(f"Decimal value: {decimal_total}")