import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry.get().strip()
    if task:
        tasks.append({"task": task, "done": False})
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

def complete_task(event=None):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task_info = tasks[index]
        if not task_info["done"]:
            task_info["done"] = True
            listbox.delete(index)
            listbox.insert(index, "✔ " + task_info["task"])
            listbox.itemconfig(index, fg="green")
        else:
            messagebox.showinfo("Info", "La tarea ya está completada.")
    else:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla.")

def delete_task(event=None):
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        listbox.delete(index)
    else:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")

# Ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")
root.configure(bg = '#9ED1DB')

tasks = []

# Campo de entrada
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.focus()

# Botones
btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Añadir", width=10, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Completar", width=10, command=complete_task).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Eliminar", width=10, command=delete_task).grid(row=0, column=2, padx=5)

# Lista de tareas
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Atajos de teclado
entry.bind("<Return>", add_task)           # Enter añade tarea (solo en Entry)
listbox.bind("<c>", complete_task)         # C completa (solo en Listbox)
listbox.bind("<d>", delete_task)           # D elimina (solo en Listbox)
listbox.bind("<Delete>", delete_task)      # Delete elimina (solo en Listbox)
root.bind("<Escape>", lambda e: root.quit()) # Escape cierra app

root.mainloop()