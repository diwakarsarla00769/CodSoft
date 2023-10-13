import tkinter as tk
from datetime import datetime
from tkinter import messagebox  # Import the messagebox module
import re

def add_task():
    task = entry_task.get()
    date_str = entry_date.get()
    time_str = entry_time.get()
    priority = priority_var.get()

    # Validate time format (24-hour format: HH:MM)
    if not re.match(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', time_str):
        messagebox.showerror("Invalid Time Format", "Please enter a valid time in HH:MM format")
        return
    
    if not re.match(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', time_str):
        messagebox.showerror("Invalid Time Format", "Please enter a valid time in HH:MM format")
        return
    
    if task:
        if priority != "Select":  # Check if a priority is selected
            formatted_task = f"Task: {task}, Priority: {priority}, Date: {date_str}, Time: {time_str}"
            display_output.config(state=tk.NORMAL)
            display_output.insert(tk.END, formatted_task + "\n" + "-" * 60 + "\n")
            display_output.config(state=tk.DISABLED)
        else:
            messagebox.showwarning("Priority Not Selected", "Please select a priority for the task.")
        entry_task.delete(0, tk.END)
        entry_date.delete(0, tk.END)
        entry_time.delete(0, tk.END)

def remove_task():
    selected_task_index = display_output.tag_ranges("sel")
    if selected_task_index:
        display_output.config(state=tk.NORMAL)
        display_output.delete(selected_task_index[0], selected_task_index[1])
        display_output.config(state=tk.DISABLED)

def update_task():
    selected_task_index = display_output.tag_ranges("sel")
    if selected_task_index:
        updated_task = entry_task.get()
        updated_text = f"Task: {updated_task}, Priority: {priority_var.get()}, Date: {entry_date.get()}, Time: {entry_time.get()}"

        display_output.config(state=tk.NORMAL)
        display_output.delete(selected_task_index[0], selected_task_index[1])
        display_output.insert(selected_task_index[0], updated_text)
        display_output.config(state=tk.DISABLED)

        entry_task.delete(0, tk.END) 
        entry_date.delete(0, tk.END)
        entry_time.delete(0, tk.END)

def search_task():
    search_text = entry_search.get()
    search_result = display_output.search(search_text, "1.0", stopindex=tk.END)

    if search_result:
        display_output.tag_add("search", search_result, f"{search_result.split('.')[0]}.end")
        display_output.tag_config("search", background="yellow")
    else:
        print("Task not found.")

def exit_app():
    root.destroy()

root = tk.Tk()
root.title("To-Do List")

task_label = tk.Label(root, text="Write the Task:", font=('arial', 12))
task_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

entry_task = tk.Entry(root, width=40, font=('Helvetica', 14))
entry_task.grid(row=0, column=1, padx=10, pady=5, sticky='w')

priority_label = tk.Label(root, text="Priority:", font=('Helvetica', 12))
priority_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

priority_var = tk.StringVar(root)
priority_var.set("Select")
priority_menu = tk.OptionMenu(root, priority_var, "Select", "Favourites", "Unfavourites")
priority_menu.grid(row=1, column=1, padx=10, pady=5, sticky='w')

date_label = tk.Label(root, text="Date (DD-MM-YYYY):", font=('Helvetica', 12))
date_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')

entry_date = tk.Entry(root, width=20, font=('Helvetica', 12))
entry_date.grid(row=2, column=1, padx=10, pady=5, sticky='w')

hours_label = tk.Label(root, text="Time (HH:MM):", font=('Helvetica', 12))
hours_label.grid(row=3, column=0, padx=10, pady=5, sticky='w')

entry_time = tk.Entry(root, width=20, font=('Helvetica', 12))
entry_time.grid(row=3, column=1, padx=10, pady=5, sticky='w')

add_button = tk.Button(root, text="Add Task", command=add_task, font=('Helvetica', 12), bg='yellow', fg='black')
remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=('Helvetica', 12), bg='#FF5733', fg='white')
update_button = tk.Button(root, text="Update Task", command=update_task, font=('Helvetica', 12), bg='green', fg='white')
search_button = tk.Button(root, text="Search Task", command=search_task, font=('Helvetica', 12), bg='blue', fg='white')
exit_button = tk.Button(root, text="Exit", command=exit_app, font=('Helvetica', 12), bg='red', fg='white')

display_output = tk.Text(root, wrap=tk.WORD, width=60, height=15, font=('Helvetica', 14), state=tk.DISABLED)
display_output.tag_configure("search", background="yellow")

entry_search = tk.Entry(root, width=40, font=('Helvetica', 14))

goodnight_label = tk.Label(root, text="", font=('Helvetica', 12))
goodnight_label.grid(row=11, column=0, columnspan=2, pady=10)

add_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2, sticky='w')
remove_button.grid(row=5, column=0, padx=10, pady=5, sticky='w')
update_button.grid(row=5, column=1, padx=10, pady=5, sticky='w')
search_button.grid(row=6, column=0, padx=10, pady=5, sticky='w')
exit_button.grid(row=6, column=1, padx=10, pady=5, sticky='w')
display_output.grid(row=7, column=0, padx=10, pady=10, columnspan=2, sticky='w')

root.mainloop()
