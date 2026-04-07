# Program for file handling

total_expense = 0

# --- 1. WRITING TO THE FILE ---
with open("expense.txt", 'w') as file:
    num_months_write = int(input("Enter number of months to record: "))
    
    for i in range(num_months_write):
        expense = input("Enter month {}'s entry: ".format(i + 1))
        # Adding a colon ":" to separate the text from the number
        file.write("Month No {}:{}\n".format(i + 1, expense))

# --- 2. READING FROM THE FILE ---
num_months_read = int(input("Enter the no of months to calculate total for: "))

with open("expense.txt", 'r') as file:
    for i in range(num_months_read):
        line = file.readline()
        
        # Split the line at the colon, grab the right side [1], and strip the \n
        amount_string = line.split(':')[1].strip()
        
        # Add it to the total
        total_expense += int(amount_string)

print("{} months total entry is {}".format(num_months_read, total_expense))