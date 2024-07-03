from tkinter import *

# Functions to add and delete items
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()
    if new_task:  # Check if the entry is not empty
        listbox.insert(END, new_task)
        with open('tasks.txt', 'a') as tasks_list_file:
            tasks_list_file.write(f'\n{new_task}')
        entry.delete(0, END)  # Clear the entry after adding the task

def delete_item(listbox: Listbox):
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        with open('tasks.txt', 'r') as tasks_list_file:
            lines = tasks_list_file.readlines()
        with open('tasks.txt', 'w') as tasks_list_file:
            for line in lines:
                if line.strip() != selected_task:
                    tasks_list_file.write(line)

# Initializing the python to-do list GUI window
root = Tk()
root.title('To-Do List')
root.geometry('300x400')
root.resizable(0, 0)
root.config(bg="navyblue")

# Heading Label
Label(root, text='To Do List', bg='navyblue', font=("Comic Sans MS", 15), wraplength=300).place(x=35, y=0)

# Listbox with all the tasks with a Scrollbar
tasks = Listbox(root, selectbackground='Gold', bg='Silver', font=('Helvetica', 12), height=12, width=25)
scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
scroller.place(x=260, y=50, height=232)
tasks.config(yscrollcommand=scroller.set)
tasks.place(x=35, y=50)

# Adding items to the Listbox from tasks.txt
with open('tasks.txt', 'r') as tasks_list:
    for task in tasks_list:
        tasks.insert(END, task.strip())

# Creating the Entry widget where the user can enter a new item
new_item_entry = Entry(root, width=37)
new_item_entry.place(x=35, y=310)

# Creating the Buttons
add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('Helvetica', 12),
                 command=lambda: add_item(new_item_entry, tasks))
add_btn.place(x=45, y=350)

delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('Helvetica', 12),
                    command=lambda: delete_item(tasks))
delete_btn.place(x=150, y=350)

# Finalizing the window
root.update()
root.mainloop()