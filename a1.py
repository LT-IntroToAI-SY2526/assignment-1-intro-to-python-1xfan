# Assignment 1: AI-Generated Python Problems
# Name: Jacob Martinez

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
    I'm learning Python basics in a high school programming class. 
    I have some experience with Java. Can you create 5-7 practice problems that cover the basics? 
    These examples shouldn't be full programs (that take user input), they should be functions. 
    Please give example inputs/outputs.

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: Even or Odd
    Write a function that takes an integer and returns "even" if it's even or "odd" if it's odd.
    Example:
        even_or_odd(4) ➞ "even"
        even_or_odd(7) ➞ "odd"
Solution: """
def even_or_odd(n):
    return "even" if n % 2 == 0 else "odd"
"""

PROBLEM 2: Reverse a String
    Write a function that returns the reverse of the input string.
    Example:
        reverse_string("hello") ➞ "olleh"
        reverse_string("Python") ➞ "nohtyP"
Solution: """
def reverse_string(s):
    return s[::-1]
"""

PROBLEM 3: Count Vowels
    Write a function that counts how many vowels (a, e, i, o, u) are in a string. It should be case-insensitive.
    Example:
        count_vowels("Hello") ➞ 2
        count_vowels("PYTHON") ➞ 1
Solution: """
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
"""

PROBLEM 4: Double the Numbers
    Write a function that takes a list of integers and returns a new list where each number is doubled.
    Example:
        double_numbers([1, 2, 3]) ➞ [2, 4, 6]
        double_numbers([0, -1, 5]) ➞ [0, -2, 10]
Solution: """
def double_numbers(lst):
    return [x * 2 for x in lst]
"""

PROBLEM 5: Find the Maximum
    Write a function that returns the largest number in a list.
    Example:
        find_max([10, 5, 20, 8]) ➞ 20
        find_max([-1, -7, -3]) ➞ -1
Solution: """
def find_max(lst):
    return max(lst)
"""

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
print(even_or_odd(4))  # Output: "even"
print(even_or_odd(7))  # Output: "odd"


print("\nTesting Problem 2:")
print(reverse_string("hello"))   # Output: "olleh"
print(reverse_string("Python"))  # Output: "nohtyP"

print("\nTesting Problem 3:")
print(count_vowels("Hello"))  # Output: 2
print(count_vowels("PYTHON")) # Output: 1

print("\nTesting Problem 4:")
print(double_numbers([1, 2, 3]))   # Output: [2, 4, 6]
print(double_numbers([0, -1, 5]))  # Output: [0, -2, 10]

print("\nTesting Problem 5:")
print(find_max([10, 5, 20, 8]))   # Output: 20
print(find_max([-1, -7, -3]))     # Output: -1


