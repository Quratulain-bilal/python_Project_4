# Binary Search Function
def binary_search(arr, target):
    """
    Performs binary search on a sorted array.
    Returns the index of target if found, else -1.
    """
    low = 0                     # Start of the search range
    high = len(arr) - 1         # End of the search range

    while low <= high:
        mid = (low + high) // 2  # Calculate middle index

        if arr[mid] == target:   # Target found at mid
            return mid
        elif arr[mid] < target:  # Search right half
            low = mid + 1
        else:                    # Search left half
            high = mid - 1

    return -1  # Target not found

# Test Case 1: Numbers
numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

result = binary_search(numbers, target)
print(f"Target {target} found at index: {result}" if result != -1 else "Not found")

# Test Case 2: Strings (Alphabetical order required)
words = ["apple", "banana", "cherry", "dates", "figs", "grapes"]
target_word = "figs"

word_result = binary_search(words, target_word)
print(f"Word '{target_word}' found at index: {word_result}" if word_result != -1 else "Not found")