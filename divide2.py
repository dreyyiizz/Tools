def divide_numbers(numerator, denominator):
    if denominator == 0:
        return "Error: Division by zero is not allowed."
    return numerator / denominator

result = divide_numbers(10, 2)
print(f"The qoutient of the division is: {result}")
