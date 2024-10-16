
# Simple To-Do List Script

This Python script allows users to input a specific number of tasks (To-Dos) and then displays all the tasks at the end. The tasks are stored in a list and displayed sequentially.

## How It Works

1. **Input Number of To-Dos**: The user is first prompted to enter how many tasks (to-dos) they would like to input.
2. **Input To-Dos**: The user is then asked to input the tasks one by one.
3. **Display To-Dos**: After all tasks are entered, the script displays the entire list of tasks.

## Code Explanation

### 1. List Initialization
```python
todos = []
```
The `todos` list is used to store all the tasks entered by the user.

### 2. Input the Number of To-Dos
```python
total_todo = int(input("How many todos you want to enter: "))
```
The script asks the user to specify how many tasks they want to enter.

### 3. For Loop to Input To-Dos
```python
for i in range(1, total_todo):
    todo = input(f"Enter todo: {i} ")
    todos.append(todo)
```
A loop runs from 1 to the specified number of tasks (`total_todo`), prompting the user to input each task. Each task is added to the `todos` list.

### 4. Display All To-Dos
```python
print("All Todo are: ")
for i in todos:
    print(i)
```
After all tasks are entered, the script displays them by iterating through the `todos` list.

## Example

```bash
How many todos you want to enter: 3
Enter todo 1: Buy groceries
Enter todo 2: Finish homework
All Todo are:
Buy groceries
Finish homework
```

## How to Run the Script

1. Make sure you have Python installed on your system. If not, download it from [here](https://www.python.org/downloads/).
2. Copy the script to a `.py` file (e.g., `todo_app.py`).
3. Run the script using the terminal or command prompt:
   ```bash
   python todo_app.py
   ```
4. Enter the number of tasks and the tasks when prompted.

## Requirements

- Python 3.x or above

## Notes

- The current implementation doesn't include task editing, removing, or saving the tasks. This is a basic version focused on inputting and displaying tasks.
- In future versions, you might want to add additional features like:
  - Marking tasks as completed
  - Deleting tasks
  - Saving the tasks in a file
