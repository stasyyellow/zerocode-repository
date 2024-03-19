import tkinter as tk

def add_task():
    task = task_entry.get()
    priority_index = priority_entry.get() #поле ввода

    if task:
        if priority_index:  # Если указан приоритет
            index = int(priority_index) - 1
            task_listbox_contents.insert(index, task)
            task_statuses.insert(index, False)
        else:  # Если приоритет не указан
            task_listbox_contents.append(task)
            task_statuses.append(False)
        update_task_numbers()
        task_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)

def delete_task():
    selection = task_listbox.curselection()
    if selection:
        task_listbox.delete(selection[0])
        del task_listbox_contents[selection[0]]
        del task_statuses[selection[0]]
        update_task_numbers()

def mark_task():
    selection = task_listbox.curselection()
    if selection:
        task_statuses[selection[0]] = True
        task_listbox.itemconfig(selection, {'foreground': 'gray'})

def update_task_numbers():
    task_listbox.delete(0, tk.END)
    for i, (task, status) in enumerate(zip(task_listbox_contents, task_statuses), start=1):
        if status:
            task_listbox.insert(tk.END, f"{i}. {task}",  ('completed'))
        else:
            task_listbox.insert(tk.END, f"{i}. {task}")

root = tk.Tk()
root.title("Список задач")
root.configure(background="dark olive green")

task_statuses = []
task_listbox_contents = []
task_listbox = tk.Listbox(root, height=10, width=50, bg="DarkOliveGreen2", selectbackground='green', selectforeground='white', font=('Helvetica', 12))
task_listbox.pack(pady=10)

text1 = tk.Label(root, text="Введите задачу: ", bg="dark olive green", fg="white", font=("Verdana", 15, "bold"))
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="white")
task_entry.pack(pady=5)

priority_label = tk.Label(root, text="Укажите номер задачи (необязательно): ", bg="dark olive green",  fg="white", font=("Verdana", 13))
priority_label.pack()

priority_entry = tk.Entry(root, width=30, bg="white")
priority_entry.pack(pady=5)

tk.Button(root, text="Добавить задачу", command=add_task).pack(pady=5)
tk.Button(root, text="Удалить задачу", command=delete_task).pack(pady=5)
tk.Button(root, text="Отметить выполненную задачу", command=mark_task).pack(pady=5)

root.mainloop()