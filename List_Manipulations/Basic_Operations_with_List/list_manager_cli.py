

def run_list_manager():
    """A menu-driven command-line interface to manipulate a Python list."""
    
   
   
    print("--- Welcome to the List Manager ---")
    user_data = input("Enter your initial numbers separated by spaces (e.g., 5 10 15): ")
    
    # Convert the string input into a list of integers
    
    
    my_list = [int(x) for x in user_data.split()]

   
   
    while True:
        print("\n" + "="*30)
        print(f"Current List: {my_list}")
        print("="*30)
        print("1. Insert an element")
        print("2. Delete an element")
        print("3. Sort the list")
        print("4. Exit Program")
        
        choice = input("Choose an operation (1-4): ")

        # --- INSERT ---
        if choice == '1':
            try:
                val = int(input("Enter the number to insert: "))
                pos = int(input(f"Enter the index position (0 to {len(my_list)}): "))
                my_list.insert(pos, val)
                print(f"Success! {val} inserted at index {pos}.")
            except ValueError:
                print("Error: Please enter valid integers for value and position.")

        # --- DELETE ---
        elif choice == '2':
            try:
                val = int(input("Enter the number to delete: "))
                if val in my_list:
                    my_list.remove(val)
                    print(f"Success! {val} removed from the list.")
                else:
                    print(f"Error: The number {val} is not in the list.")
            except ValueError:
                 print("Error: Please enter a valid integer.")

        # --- SORT ---
        elif choice == '3':
            print("\nHow would you like to sort?")
            print("1. Ascending order (Small to Large)")
            print("2. Descending order (Large to Small)")
            sort_choice = input("Choose (1 or 2): ")
            
            if sort_choice == '1':
                my_list.sort()
                print("List sorted in ascending order.")
            elif sort_choice == '2':
                my_list.sort(reverse=True)
                print("List sorted in descending order.")
            else:
                print("Invalid sort choice.")

        # --- EXIT ---
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break # Breaks the main While loop

        # --- CATCH ALL ---
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")



if __name__ == "__main__":
    run_list_manager()