
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    # Keep searching as long as the search space is valid
    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] == target:
            return mid
            
        elif sorted_list[mid] > target:
            right = mid - 1
            
        
        elif sorted_list[mid] < target:
            left = mid + 1
        
    return -1

if __name__ == "__main__":
    print("--- Binary Search Tester ---")
    
    user_input = input("Enter a list of numbers separated by spaces: ")
    my_list = [int(x) for x in user_input.split()]
    
    
    my_list.sort() 
    print(f"Sorted Search Space: {my_list}")
    
    
    try:
        target_val = int(input("Enter the number to search for: "))
        
        # Run the search
        result_index = binary_search(my_list, target_val)
        
        if result_index != -1:
            print(f"Success! {target_val} found at index {result_index}.")
        else:
            print(f"Result: {target_val} was not found in the list (-1).")
            
    except ValueError:
        print("Error: Please enter a valid integer for the target.")
    


