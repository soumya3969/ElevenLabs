# Task 2: To-Do List Application

## 📋 Overview
A console-based To-Do List Manager application built with Python that allows users to manage their daily tasks with persistent storage. The application provides a user-friendly command-line interface with full CRUD (Create, Read, Update, Delete) operations.

## ✨ Features Implemented

### Core Functionality
- ✅ **Add Task** - Add new tasks to your to-do list
- ✅ **View All Tasks** - Display all tasks in a numbered, organized format
- ✅ **Remove Task** - Delete completed or unwanted tasks
- ✅ **Clear All Tasks** - Remove all tasks at once (with confirmation)
- ✅ **Persistent Storage** - All tasks are saved to `tasks.txt` and persist between sessions

### Technical Features
- ✅ **Automatic Save** - Tasks are automatically saved after each operation
- ✅ **Auto-load** - Tasks are loaded from file when the application starts
- ✅ **Error Handling** - Graceful handling of invalid inputs and file operations
- ✅ **Input Validation** - Prevents empty tasks and invalid task numbers
- ✅ **Relative Path Storage** - Tasks file is created in the same directory as the script
- ✅ **User-Friendly Interface** - Clear menus with emoji indicators for better UX

## 🛠️ Technologies Used
- **Language**: Python 3
- **Standard Libraries**: 
  - `os` - For file path operations and directory management
  - Built-in file I/O operations

## 📁 Project Structure
```
Task 2/
├── todo.py           # Main application file
├── tasks.txt         # Persistent storage file (auto-generated)
├── requirement.md    # Task requirements
└── README.md         # This file
```

## 🚀 How to Run

1. **Navigate to the project directory**:
   ```bash
   cd "/workspaces/ElevenLabs/Task 2"
   ```

2. **Run the application**:
   ```bash
   python todo.py
   ```

3. **Follow the on-screen menu** to interact with your to-do list

## 💡 Usage Guide

### Main Menu Options
```
==================================================
📝 TO-DO LIST MANAGER
==================================================
1. View all tasks
2. Add a task
3. Remove a task
4. Clear all tasks
5. Exit
==================================================
```

### Adding a Task
1. Select option `2` from the menu
2. Enter your task description
3. Task is automatically saved to file

### Viewing Tasks
1. Select option `1` from the menu
2. All tasks are displayed with numbers
3. Total task count is shown at the bottom

### Removing a Task
1. Select option `3` from the menu
2. View the list of tasks with their numbers
3. Enter the number of the task you want to remove
4. Task is removed and changes are saved

### Clearing All Tasks
1. Select option `4` from the menu
2. Confirm with `yes` to clear all tasks
3. Type anything else to cancel

## 🔧 Implementation Details

### Class Structure
- **`TodoList`** - Main class handling all task operations
  - `__init__()` - Initializes the task list and loads existing tasks
  - `load_tasks()` - Loads tasks from the text file on startup
  - `save_tasks()` - Saves tasks to the text file after operations
  - `add_task()` - Adds a new task with validation
  - `remove_task()` - Removes a task by index
  - `view_tasks()` - Displays all tasks in formatted output
  - `clear_all_tasks()` - Clears all tasks with user confirmation

### Key Design Decisions

1. **File Path Management**
   ```python
   script_dir = os.path.dirname(os.path.abspath(__file__))
   self.filename = os.path.join(script_dir, filename)
   ```
   - Uses `__file__` to determine script location
   - Ensures `tasks.txt` is created in the same directory as the script
   - Works regardless of where the script is run from

2. **Data Persistence**
   - Tasks are stored in plain text format (one task per line)
   - File is automatically created if it doesn't exist
   - Changes are saved immediately after each operation

3. **Error Handling**
   - Try-except blocks for file operations
   - Input validation for task numbers
   - Empty task prevention
   - User-friendly error messages with emoji indicators

4. **User Experience**
   - Clear visual separators using `=` characters
   - Emoji indicators for different message types:
     - ✅ Success operations
     - ⚠️ Warnings and errors
     - 🗑️ Deletion operations
     - 📭 Empty state
     - 📋 Task list display
     - 👋 Exit message

## 📊 Example Usage

```
🎉 Welcome to To-Do List Manager!

==================================================
📝 TO-DO LIST MANAGER
==================================================
1. View all tasks
2. Add a task
3. Remove a task
4. Clear all tasks
5. Exit
==================================================
Enter your choice (1-5): 2
Enter the task: Complete Python assignment
✅ Task added: 'Complete Python assignment'

Enter your choice (1-5): 1

📋 Your To-Do List:
==================================================
1. Complete Python assignment
==================================================
Total tasks: 1
```

## 🎯 Learning Outcomes

Through this project, the following concepts were practiced:
- ✅ Object-Oriented Programming (OOP) with Python classes
- ✅ File I/O operations (reading and writing)
- ✅ Data persistence between program sessions
- ✅ User input handling and validation
- ✅ Error handling and exception management
- ✅ Path manipulation using `os` module
- ✅ Creating interactive command-line interfaces
- ✅ Code organization and clean architecture

## 📝 Notes

- The application stores tasks in plain text format for simplicity
- Each task is stored on a separate line in `tasks.txt`
- Empty lines are automatically filtered out when loading
- The tasks file is created in the same directory as `todo.py` for portability

## 🔮 Future Enhancements (Optional)

Potential features that could be added:
- Task priority levels (high, medium, low)
- Due dates and reminders
- Task categories/tags
- Mark tasks as complete without removing them
- Search and filter functionality
- Export tasks to different formats (CSV, JSON)
- Edit existing tasks

## 👨‍💻 Author

Developed as part of the ElevenLabs coding assessment - Task 2

## 📄 License

This project is created for educational purposes.
