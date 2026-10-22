
# Improved code - better readability and structure

def calculate_result(first_number, second_number, multiplier):
    """Add two numbers and multiply the sum."""
    total = first_number + second_number
    result = total * multiplier

    print("Result:", result)
    return result


def print_names_in_uppercase(names):
    """Print each name in uppercase."""
    for name in names:
        print(name.upper())


student_names = ["Harshit", "Deepak", "priya", "aman"]

print_names_in_uppercase(student_names)
calculate_result(10, 20, 2)
