Loading Tasks (load_tasks):
When you start the program, it tries to open the "tasks.txt" file.
If the file exists, it reads all your tasks and loads them into the program.
If the file doesn't exist (like the first time you use it), it just starts with an empty list.
Saving Tasks (save_tasks):
Whenever you add or remove a task, it updates the "tasks.txt" file.
This ensures your tasks are saved for next time.
Showing Tasks (show_tasks):
Displays all your current tasks with numbers (1, 2, 3, etc.).
If you have no tasks, it says "No tasks yet!"
Adding a Task (add_task):
Asks you to type in a new task.
Adds it to your list and confirms it was added.
Removing a Task (remove_task):
First shows you all your current tasks.
Asks you for the number of the task you want to remove.
Checks if you entered a valid number and removes that task.
If you enter something that's not a number or a number that doesn't match any task, it shows an error message.
The Main Program (main):
This is the part that actually runs the show.
It starts by loading your existing tasks.
Then it shows you a menu with 4 options:
View your tasks
Add a new task
Remove a task
Exit the program
It waits for you to choose an option and then does what you asked.
After you add or remove something, it automatically saves your changes.
When you choose to exit, it saves everything one last time and says goodbye.
