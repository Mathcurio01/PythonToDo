todos = []

total_todo =int(input("How many todos you want to enter: "))

for i in range(1,total_todo):
    todo = input(f"Enter todo: {i} ")
    todos.append(todo)


# Display all todo
print("All Todo are: ")
for i in todos:
    print(i)
