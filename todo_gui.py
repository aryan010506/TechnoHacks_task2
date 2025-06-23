import tkinter as tk
from tkinter import messagebox

# Create main window
app = tk.Tk()
app.title("To-Do List")
app.geometry("400x500")
app.configure(bg="#0f172a")

# Task list
tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    try:
        selected_index = listbox.curselection()[0]
        removed = tasks.pop(selected_index)
        update_listbox()
        messagebox.showinfo("Task Removed", f"Removed: {removed}")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Title
tk.Label(app, text="📝 To-Do List", font=("Arial", 24), bg="#0f172a", fg="#7dd3fc").pack(pady=10)

# Entry field
entry = tk.Entry(app, font=("Arial", 14), bg="#1e293b", fg="white", insertbackground="white")
entry.pack(padx=20, pady=10, fill="x")

# Buttons
btn_frame = tk.Frame(app, bg="#0f172a")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Task", command=add_task, bg="#2563eb", fg="white", font=("Arial", 12))
add_btn.pack(side="left", padx=10)

remove_btn = tk.Button(btn_frame, text="Remove Task", command=remove_task, bg="#dc2626", fg="white", font=("Arial", 12))
remove_btn.pack(side="left", padx=10)

# Listbox
listbox = tk.Listbox(app, font=("Arial", 14), bg="#1e293b", fg="white", selectbackground="#2563eb")
listbox.pack(padx=20, pady=20, fill="both", expand=True)

app.mainloop()
