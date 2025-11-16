
"""
Calculator CLI App
A command-line calculator supporting basic arithmetic operations.
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("        CALCULATOR CLI APP")
    print("="*40)
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("="*40)

def get_numbers():
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return None, None

def main():
    """Main calculator loop"""
    while True:
        display_menu()
        
        choice = input("Enter choice (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("\nThank you for using Calculator CLI App. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            num1, num2 = get_numbers()
            
            if num1 is None or num2 is None:
                continue
            
            if choice == '1':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4':
                result = divide(num1, num2)
                operation = "/"
            
            print(f"\nResult: {num1} {operation} {num2} = {result}")
        else:
            print("\nError: Invalid choice. Please select 1-5.")

if __name__ == "__main__":
    main()