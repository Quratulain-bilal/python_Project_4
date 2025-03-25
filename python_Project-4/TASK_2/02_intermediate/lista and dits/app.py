#List Practice Solution
def main():
    """
    Demonstrates basic list operations in Python.
    Creates a fruit list, prints its length, adds an item, and displays the updated list.
    """
    # Create and initialize the fruit list
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print(f"Initial list length: {len(fruit_list)}")
    
    # Add 'mango' to the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit list:")
    for index, fruit in enumerate(fruit_list, 1):
        print(f"{index}. {fruit}")

if __name__ == '__main__':
    main()                                                                                          
#index game solution
def access_element(lst, index):
    """Accesses an element at the given index with error handling."""
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return "Error: Index out of range."

def modify_element(lst, index, new_value):
    """Modifies an element at the given index with error handling."""
    try:
        lst[index] = new_value
        return f"Updated list: {lst}"
    except IndexError:
        return "Error: Index out of range."

def slice_list(lst, start, end):
    """Returns a slice of the list with error handling."""
    try:
        return f"Sliced list: {lst[start:end]}"
    except IndexError:
        return "Error: Invalid indices."

def index_game():
    """
    Interactive game to practice list operations.
    Allows users to access, modify, and slice elements in a list.
    """
    lst = [1, 2, 3, 4, 5]  # Initial list
    
    while True:
        print("\nCurrent list:", lst)
        print("Available operations:")
        print("1. Access element (access)")
        print("2. Modify element (modify)")
        print("3. Slice list (slice)")
        print("4. Exit (exit)")
        
        operation = input("Enter operation: ").lower()
        
        if operation == 'exit':
            print("Thanks for playing!")
            break
            
        elif operation == "access":
            try:
                index = int(input("Enter index to access: "))
                print(access_element(lst, index))
            except ValueError:
                print("Invalid input. Please enter a number.")
                
        elif operation == "modify":
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                # Try to convert to int if possible for consistency
                try:
                    new_value = int(new_value)
                except ValueError:
                    pass
                print(modify_element(lst, index, new_value))
            except ValueError:
                print("Invalid input. Please enter a number for the index.")
                
        elif operation == "slice":
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print(slice_list(lst, start, end))
            except ValueError:
                print("Invalid input. Please enter numbers for indices.")
                
        else:
            print("Invalid operation. Please try again.")

if __name__ == '__main__':
    index_game()