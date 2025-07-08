# NumberComparison.py

# This program compares two numbers and tells which is larger, smaller, or if they are equal.

def compare_numbers(a, b):
    if a > b:
        return f"{a} is larger than {b}."
    elif a < b:
        return f"{a} is smaller than {b}."
    else:
        return f"{a} and {b} are equal."

if __name__ == "__main__":
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = compare_numbers(num1, num2)
        print(result)
    except ValueError:
        print("Please enter valid numbers.")
