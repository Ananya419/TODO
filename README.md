# To-Do List Application

A console-based to-do list manager built with Python that provides persistent storage and a user-friendly interface.

## Features

- ✅ **Add Tasks**: Create new tasks with descriptions
- 📋 **View Tasks**: Display all tasks or only pending ones  
- ✅ **Mark Complete**: Mark tasks as completed
- 🗑️ **Remove Tasks**: Delete tasks permanently
- 📊 **Statistics**: View completion rates and task counts
- 💾 **Persistent Storage**: Tasks saved automatically to `tasks.txt`
- 🧹 **Clear Completed**: Remove all completed tasks at once

## How to Run

1. Open terminal/command prompt in the project directory
2. Run the application:
   ```
   python todo.py
   ```

## Usage

1. **Adding a Task**: Choose option 1 and enter your task description
2. **Viewing Tasks**: Use option 2 for all tasks, or option 3 for pending only
3. **Completing Tasks**: Use option 4 and enter the task ID number
4. **Removing Tasks**: Use option 5 and enter the task ID number
5. **Statistics**: Option 7 shows your productivity stats

## File Structure

- `todo.py` - Main application file
- `tasks.txt` - Automatically created file that stores your tasks (JSON format)

## Example Usage

```
📝 TO-DO LIST MANAGER
==================================================
1. Add Task
2. View All Tasks
3. View Pending Tasks Only
4. Mark Task as Completed
5. Remove Task
6. Clear Completed Tasks
7. Show Statistics
8. Help
9. Exit
--------------------------------------------------
Enter your choice (1-9): 1

📝 Enter task description: Buy groceries
✓ Task added successfully: 'Buy groceries'
```

## Data Storage

Tasks are automatically saved to `tasks.txt` in JSON format, ensuring your data persists between sessions.

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in Python modules)