import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")

        # Lista donde se guardarán las tareas
        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)  # Permite añadir con Enter

        # Botones de acción
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Listbox para mostrar tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)

        # Permitir marcar completada con doble clic
        self.task_listbox.bind("<Double-Button-1>", self.complete_task)

    def add_task(self, event=None):
        """Agrega una tarea escrita en el Entry al Listbox."""
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Limpiar entrada
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self, event=None):
        """Marca una tarea seleccionada como completada, cambiando su texto."""
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)

            # Verificar si ya está completada
            if not task.startswith("(Hecha) "):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, "(Hecha) " + task)
            else:
                messagebox.showinfo("Información", "La tarea ya está completada.")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla.")

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()