import os

class TodoList:
    def __init__(self, filename='tasks.txt'):
        script_dir = os.path.dirname(os.path.abspath(__file__)) 
        #! i have added this line to get the directory of the current script
        # * This ensures the tasks file is always relative to the script location
        # * Else we can use  self.filename = filename to use a relative or absolute path directly(root)
        self.filename = os.path.join(script_dir, filename)
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file on startup"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.tasks = [line.strip() for line in f.readlines() if line.strip()]
                print(f"✅ Loaded {len(self.tasks)} task(s) from file.")
            except Exception as e:
                print(f"⚠️  Error loading tasks: {e}")
        else:
            print("📝 No existing tasks file found. Starting fresh!")
    
    def save_tasks(self):
        """Save tasks to file after each operation"""
        try:
            with open(self.filename, 'w') as f:
                for task in self.tasks:
                    f.write(f"{task}\n")
        except Exception as e:
            print(f"⚠️  Error saving tasks: {e}")
    
    def add_task(self, task):
        """Add a new task"""
        if task.strip():
            self.tasks.append(task.strip())
            self.save_tasks()
            print(f"✅ Task added: '{task.strip()}'")
        else:
            print("⚠️  Cannot add empty task!")
    
    def remove_task(self, index):
        """Remove a task by index"""
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"🗑️  Removed: '{removed_task}'")
        else:
            print(f"⚠️  Invalid task number! Please choose between 1 and {len(self.tasks)}")
    
    def view_tasks(self):
        """View all tasks"""
        if not self.tasks:
            print("\n📭 No tasks yet! Add some tasks to get started.\n")
        else:
            print("\n📋 Your To-Do List:")
            print("=" * 50)
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
            print("=" * 50)
            print(f"Total tasks: {len(self.tasks)}\n")
    
    def clear_all_tasks(self):
        """Clear all tasks"""
        if self.tasks:
            confirm = input("⚠️  Are you sure you want to clear all tasks? (yes/no): ").lower()
            if confirm == 'yes':
                self.tasks.clear()
                self.save_tasks()
                print("🗑️  All tasks cleared!")
            else:
                print("❌ Clear operation cancelled.")
        else:
            print("📭 No tasks to clear!")

def print_menu():
    """Display the menu"""
    print("\n" + "=" * 50)
    print("📝 TO-DO LIST MANAGER")
    print("=" * 50)
    print("1. View all tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Clear all tasks")
    print("5. Exit")
    print("=" * 50)

def main():
    """Main function to run the to-do list application"""
    todo = TodoList()
    
    print("\n🎉 Welcome to To-Do List Manager!")
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            todo.view_tasks()
        
        elif choice == '2':
            task = input("Enter the task: ")
            todo.add_task(task)
        
        elif choice == '3':
            todo.view_tasks()
            if todo.tasks:
                try:
                    index = int(input("Enter task number to remove: "))
                    todo.remove_task(index)
                except ValueError:
                    print("⚠️  Please enter a valid number!")
        
        elif choice == '4':
            todo.clear_all_tasks()
        
        elif choice == '5':
            print("\n👋 Goodbye! Your tasks have been saved.")
            break
        
        else:
            print("⚠️  Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    main()