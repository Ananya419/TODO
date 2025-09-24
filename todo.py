#!/usr/bin/env python3
"""
To-Do List Application (Console-based)
A simple command-line to-do list manager with persistent storage.

Features:
- Add tasks
- Remove tasks
- View all tasks
- Mark tasks as completed
- Persistent storage in a text file
"""

import os
import json
from datetime import datetime

class TodoApp:
    def __init__(self, filename="tasks.txt"):
        """Initialize the TodoApp with a filename for persistent storage."""
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from the text file."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as file:
                    content = file.read().strip()
                    if content:
                        self.tasks = json.loads(content)
                    else:
                        self.tasks = []
            else:
                self.tasks = []
        except (json.JSONDecodeError, FileNotFoundError):
            print(f"Warning: Could not load tasks from {self.filename}. Starting with empty list.")
            self.tasks = []
    
    def save_tasks(self):
        """Save tasks to the text file."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(self.tasks, file, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, task_description):
        """Add a new task to the list."""
        if not task_description.strip():
            print("Error: Task description cannot be empty!")
            return False
        
        task = {
            "id": len(self.tasks) + 1,
            "description": task_description.strip(),
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Task added successfully: '{task_description}'")
        return True
    
    def remove_task(self, task_id):
        """Remove a task by its ID."""
        try:
            task_id = int(task_id)
        except ValueError:
            print("Error: Please enter a valid task ID (number)!")
            return False
        
        # Find task by ID
        task_to_remove = None
        task_index = None
        
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                task_to_remove = task
                task_index = i
                break
        
        if task_to_remove:
            removed_task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"✓ Task removed: '{removed_task['description']}'")
            return True
        else:
            print(f"Error: No task found with ID {task_id}")
            return False
    
    def mark_completed(self, task_id):
        """Mark a task as completed."""
        try:
            task_id = int(task_id)
        except ValueError:
            print("Error: Please enter a valid task ID (number)!")
            return False
        
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_tasks()
                print(f"✓ Task marked as completed: '{task['description']}'")
                return True
        
        print(f"Error: No task found with ID {task_id}")
        return False
    
    def view_tasks(self, show_completed=True):
        """Display all tasks."""
        if not self.tasks:
            print("\n📝 No tasks found! Your to-do list is empty.")
            return
        
        print(f"\n📋 Your To-Do List ({len(self.tasks)} tasks):")
        print("-" * 60)
        
        pending_tasks = [task for task in self.tasks if not task["completed"]]
        completed_tasks = [task for task in self.tasks if task["completed"]]
        
        # Show pending tasks
        if pending_tasks:
            print("🔄 PENDING TASKS:")
            for task in pending_tasks:
                status = "⏳"
                print(f"  {status} [{task['id']}] {task['description']}")
                print(f"      Created: {task['created_at']}")
        
        # Show completed tasks if requested
        if show_completed and completed_tasks:
            print("\n✅ COMPLETED TASKS:")
            for task in completed_tasks:
                status = "✓"
                print(f"  {status} [{task['id']}] {task['description']}")
                print(f"      Completed: {task.get('completed_at', 'Unknown')}")
        
        print("-" * 60)
        print(f"📊 Summary: {len(pending_tasks)} pending, {len(completed_tasks)} completed")
    
    def view_pending_only(self):
        """Display only pending tasks."""
        pending_tasks = [task for task in self.tasks if not task["completed"]]
        
        if not pending_tasks:
            print("\n🎉 Great! No pending tasks. You're all caught up!")
            return
        
        print(f"\n⏳ Pending Tasks ({len(pending_tasks)}):")
        print("-" * 40)
        
        for task in pending_tasks:
            print(f"  [{task['id']}] {task['description']}")
            print(f"      Created: {task['created_at']}")
        
        print("-" * 40)
    
    def clear_completed(self):
        """Remove all completed tasks."""
        completed_count = len([task for task in self.tasks if task["completed"]])
        
        if completed_count == 0:
            print("No completed tasks to clear!")
            return
        
        self.tasks = [task for task in self.tasks if not task["completed"]]
        self.save_tasks()
        print(f"✓ Cleared {completed_count} completed task(s)")
    
    def show_stats(self):
        """Display task statistics."""
        if not self.tasks:
            print("\n📊 Statistics: No tasks available")
            return
        
        total = len(self.tasks)
        completed = len([task for task in self.tasks if task["completed"]])
        pending = total - completed
        completion_rate = (completed / total * 100) if total > 0 else 0
        
        print(f"\n📊 Task Statistics:")
        print(f"  Total tasks: {total}")
        print(f"  Completed: {completed}")
        print(f"  Pending: {pending}")
        print(f"  Completion rate: {completion_rate:.1f}%")


def show_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("📝 TO-DO LIST MANAGER")
    print("="*50)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks Only")
    print("4. Mark Task as Completed")
    print("5. Remove Task")
    print("6. Clear Completed Tasks")
    print("7. Show Statistics")
    print("8. Help")
    print("9. Exit")
    print("-"*50)


def show_help():
    """Display help information."""
    print("\n📖 HELP - How to use this To-Do List Manager:")
    print("-" * 50)
    print("• Add Task: Enter a description for your new task")
    print("• View Tasks: See all your tasks with their status")
    print("• Mark Completed: Enter the task ID to mark it as done")
    print("• Remove Task: Enter the task ID to delete it permanently")
    print("• Task IDs: Each task has a unique number in [brackets]")
    print("• Data Storage: Tasks are automatically saved to 'tasks.txt'")
    print("-" * 50)


def main():
    """Main application loop."""
    todo_app = TodoApp()
    
    print("🚀 Welcome to your Personal To-Do List Manager!")
    print(f"📁 Tasks are stored in: {todo_app.filename}")
    
    while True:
        show_menu()
        
        try:
            choice = input("Enter your choice (1-9): ").strip()
            
            if choice == '1':
                # Add Task
                task_desc = input("\n📝 Enter task description: ").strip()
                if task_desc:
                    todo_app.add_task(task_desc)
                else:
                    print("❌ Task description cannot be empty!")
            
            elif choice == '2':
                # View All Tasks
                todo_app.view_tasks()
            
            elif choice == '3':
                # View Pending Tasks Only
                todo_app.view_pending_only()
            
            elif choice == '4':
                # Mark Task as Completed
                todo_app.view_pending_only()
                if any(not task["completed"] for task in todo_app.tasks):
                    task_id = input("\n✅ Enter task ID to mark as completed: ").strip()
                    todo_app.mark_completed(task_id)
            
            elif choice == '5':
                # Remove Task
                todo_app.view_tasks()
                if todo_app.tasks:
                    task_id = input("\n🗑️  Enter task ID to remove: ").strip()
                    todo_app.remove_task(task_id)
            
            elif choice == '6':
                # Clear Completed Tasks
                todo_app.clear_completed()
            
            elif choice == '7':
                # Show Statistics
                todo_app.show_stats()
            
            elif choice == '8':
                # Help
                show_help()
            
            elif choice == '9':
                # Exit
                print("\n👋 Thank you for using To-Do List Manager!")
                print("💾 All your tasks have been saved automatically.")
                break
            
            else:
                print("❌ Invalid choice! Please enter a number between 1-9.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Your tasks have been saved.")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")


if __name__ == "__main__":
    main()