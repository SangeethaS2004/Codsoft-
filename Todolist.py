import tkinter as tk
from tkinter import messagebox
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)
def add_task():
    new_task = task_entry.get()
    if new_task != "":
        tasks.append(new_task)
        save_tasks(tasks)
        task_entry.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = tasks.pop(selected_task_index)
        save_tasks(tasks)
        update_task_list()
        messagebox.showinfo("Task Deleted", f"Task '{task}' has been deleted.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index] = tasks[selected_task_index] + " (Completed)"
        save_tasks(tasks)
        update_task_list()
        messagebox.showinfo("Task Completed", "Task marked as completed.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")
root = tk.Tk()
root.title("To-Do List Application")
root.config(bg="#f5f5f5")

tasks = load_tasks()

task_entry = tk.Entry(root, width=40, bg="#e0e0e0", fg="#333333", font=("Arial", 14))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 12))
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#f44336", fg="white", font=("Arial", 12))
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark Completed", command=mark_completed, bg="#2196F3", fg="white", font=("Arial", 12))
complete_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=40, height=10, bg="#ffffff", fg="#333333", font=("Arial", 12), selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

update_task_list()

root.mainloop()
