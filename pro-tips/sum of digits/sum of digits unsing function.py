def sum_digits(n):
    
    if n == 0:
        return 0
        
    # Recursive Step: Return the last digit + the sum of the remaining digits
    return (n % 10) + sum_digits(n // 10)


print(sum_digits(12345)) 
print(sum_digits(111))   