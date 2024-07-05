def perform_operation(num1: float, num2: float, operation: str):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error! Division by zero."  # Different error message
        case _:
            return "Invalid operation!"

if __name__ == "__main__":
    print(perform_operation(4, 2, 'add'))         # Output: 6.0
    print(perform_operation(4, 2, 'subtract'))    # Output: 2.0
    print(perform_operation(4, 2, 'multiply'))    # Output: 8.0
    print(perform_operation(4, 2, 'divide'))      # Output: 2.0
    print(perform_operation(4, 0, 'divide'))      # Output: Error! Division by zero.
    print(perform_operation(4, 2, 'modulus'))     # Output: Invalid operation!
