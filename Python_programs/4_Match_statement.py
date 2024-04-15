"""In Python, the match statement was introduced in Python 3.10 as part of the Pattern Matching feature.
 Pattern Matching provides a more concise and readable way to perform conditional checks and extract information 
 from data structures such as lists, dictionaries, and classes.

The match statement is similar to a switch statement found in other programming languages but offers more powerful 
pattern matching capabilities. It allows you to specify patterns to match against values and execute corresponding code blocks
based on the matched pattern."""

def check_value(x):
    match x:
        case 0:
            print("Value is zero")
        case 1 | 2 | 3:
            print("Value is either 1, 2, or 3")
        case int(n) if n > 10:
            print("Value is an integer greater than 10")
        case _:
            print("Value does not match any pattern")

check_value(0)   # Output: Value is zero
check_value(2)   # Output: Value is either 1, 2, or 3
check_value(15)  # Output: Value is an integer greater than 10
check_value(5)   # Output: Value does not match any pattern
