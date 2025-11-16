# Task 1: Calculator CLI Application

## 📋 Overview
A command-line calculator application built with Python that performs basic arithmetic operations. The application provides an interactive menu-driven interface for performing calculations with proper error handling and input validation.

## ✨ Features Implemented

### Core Functionality
- ✅ **Addition** - Add two numbers
- ✅ **Subtraction** - Subtract one number from another
- ✅ **Multiplication** - Multiply two numbers
- ✅ **Division** - Divide numbers with zero-division protection
- ✅ **Interactive Menu** - User-friendly command-line interface
- ✅ **Continuous Operation** - Perform multiple calculations in one session

### Technical Features
- ✅ **Error Handling** - Graceful handling of invalid inputs
- ✅ **Input Validation** - Validates numeric inputs
- ✅ **Zero Division Protection** - Prevents division by zero errors
- ✅ **Float Support** - Works with both integers and decimal numbers
- ✅ **Clean Exit** - Proper program termination

## 🛠️ Technologies Used
- **Language**: Python 3
- **Standard Libraries**: Built-in Python functions only

## 📁 Project Structure
```
Task 1/
├── calculator.py     # Main application file
├── requirement.md    # Task requirements
└── README.md         # This file
```

## 🚀 How to Run

1. **Navigate to the project directory**:
   ```bash
   cd "/workspaces/ElevenLabs/Task 1"
   ```

2. **Run the application**:
   ```bash
   python calculator.py
   ```

3. **Follow the on-screen menu** to perform calculations

## 💡 Usage Guide

### Main Menu
```
========================================
        CALCULATOR CLI APP
========================================
Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exit
========================================
```

### Performing Calculations

1. **Select an operation** by entering the corresponding number (1-4)
2. **Enter the first number** when prompted
3. **Enter the second number** when prompted
4. **View the result** displayed on screen
5. **Repeat** or select option 5 to exit

### Example Usage

```
========================================
        CALCULATOR CLI APP
========================================
Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exit
========================================
Enter choice (1/2/3/4/5): 1
Enter first number: 15
Enter second number: 27

Result: 15.0 + 27.0 = 42.0

========================================
        CALCULATOR CLI APP
========================================
Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)
5. Exit
========================================
Enter choice (1/2/3/4/5): 4
Enter first number: 100
Enter second number: 5

Result: 100.0 / 5.0 = 20.0
```

## 🔧 Implementation Details

### Function Structure

#### **Arithmetic Functions**
```python
def add(x, y)       # Returns x + y
def subtract(x, y)  # Returns x - y
def multiply(x, y)  # Returns x * y
def divide(x, y)    # Returns x / y (with zero-check)
```

#### **Helper Functions**
- **`display_menu()`** - Displays the calculator menu interface
- **`get_numbers()`** - Handles user input and validation for two numbers
- **`main()`** - Main program loop managing user interaction

### Key Design Decisions

1. **Function-Based Architecture**
   - Each arithmetic operation is a separate function
   - Promotes code reusability and maintainability
   - Easy to test and extend

2. **Error Handling**
   ```python
   # Division by zero protection
   if y == 0:
       return "Error: Cannot divide by zero"
   
   # Invalid input handling
   try:
       num1 = float(input("Enter first number: "))
       num2 = float(input("Enter second number: "))
   except ValueError:
       print("Error: Invalid input. Please enter numeric values.")
   ```

3. **Input Validation**
   - Uses `try-except` blocks to catch `ValueError`
   - Converts input to `float` for decimal support
   - Returns `None` values for invalid inputs to signal error

4. **User Experience**
   - Clear visual separators using `=` characters
   - Descriptive operation symbols in menu
   - Informative error messages
   - Clean result formatting

5. **Program Flow**
   - Continuous loop for multiple calculations
   - Graceful exit with confirmation message
   - Invalid choice handling with helpful feedback

## 📊 Supported Operations

| Operation      | Symbol | Example           | Result |
|---------------|--------|-------------------|--------|
| Addition      | +      | 5 + 3            | 8      |
| Subtraction   | -      | 10 - 4           | 6      |
| Multiplication| *      | 7 * 6            | 42     |
| Division      | /      | 20 / 4           | 5      |

### Special Cases Handled

- **Division by Zero**: Returns error message instead of crashing
- **Invalid Input**: Prompts user with error and continues
- **Decimal Numbers**: Supports floating-point arithmetic
- **Negative Numbers**: Works correctly with negative values

## 🎯 Learning Outcomes

Through this project, the following concepts were practiced:
- ✅ Function definition and usage in Python
- ✅ User input handling with `input()`
- ✅ Type conversion and validation
- ✅ Exception handling with try-except blocks
- ✅ Control flow (if-elif-else, while loops)
- ✅ String formatting and output
- ✅ Creating interactive CLI applications
- ✅ Error handling best practices

## 🧪 Testing Examples

### Test Case 1: Addition
```
Input: 1, 25, 75
Output: Result: 25.0 + 75.0 = 100.0
```

### Test Case 2: Division by Zero
```
Input: 4, 10, 0
Output: Result: 10.0 / 0.0 = Error: Cannot divide by zero
```

### Test Case 3: Invalid Input
```
Input: 1, "abc", 5
Output: Error: Invalid input. Please enter numeric values.
```

### Test Case 4: Decimal Numbers
```
Input: 3, 3.5, 2.5
Output: Result: 3.5 * 2.5 = 8.75
```

### Test Case 5: Negative Numbers
```
Input: 2, 10, -3
Output: Result: 10.0 - -3.0 = 13.0
```

## 🔍 Code Quality Features

- **Docstrings**: All functions have descriptive docstrings
- **Type Handling**: Proper conversion to float for calculations
- **Error Messages**: Clear and user-friendly error messages
- **Code Organization**: Logical separation of concerns
- **Readability**: Clean formatting and meaningful variable names

## 🔮 Future Enhancements (Optional)

Potential features that could be added:
- Advanced operations (power, square root, modulo)
- Scientific functions (sin, cos, tan, log)
- Memory functions (store and recall values)
- Calculation history
- Expression evaluation (e.g., "5 + 3 * 2")
- GUI version using Tkinter
- Unit tests for all operations

## 📝 Notes

- The calculator works with floating-point numbers
- All results are displayed as floats (even for integer operations)
- The program continues running until user selects "Exit"
- Input validation prevents crashes from invalid data

## 👨‍💻 Author

Developed as part of the ElevenLabs coding assessment - Task 1

## 📄 License

This project is created for educational purposes.
