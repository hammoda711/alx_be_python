def perform_operation(num1:float, num2:float, operation:str):
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
                return "Error!, invalid choice"
        case _:
            return "Invalid operation!"    
if __name__ == "__main__":
    print(perform_operation(4, 2, 'add'))        
    print(perform_operation(4, 2, 'subtract'))   
    print(perform_operation(4, 2, 'multiply'))  
    print(perform_operation(4, 2, 'divide'))    
    print(perform_operation(4, 0, 'divide'))     
    print(perform_operation(4, 2, 'modulus'))    