import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry   # aseguramos que siempre se use

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("700x420")

        # Lista de eventos en memoria
        self.events = []

        # Frame izquierdo: Treeview
        left_frame = tk.Frame(root)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        tk.Label(left_frame, text="Eventos Programados", font=(None, 12, 'bold')).pack(anchor=tk.W)

        columns = ("fecha", "hora", "descripcion")
        self.tree = ttk.Treeview(left_frame, columns=columns, show='headings')
        self.tree.heading('fecha', text='Fecha')
        self.tree.heading('hora', text='Hora')
        self.tree.heading('descripcion', text='Descripción')
        self.tree.column('fecha', width=100)
        self.tree.column('hora', width=80)
        self.tree.column('descripcion', width=350)

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Frame derecho: formulario
        right_frame = tk.Frame(root)
        right_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)

        tk.Label(right_frame, text="Nuevo Evento", font=(None, 12, 'bold')).pack(anchor=tk.W, pady=5)

        form = tk.Frame(right_frame)
        form.pack()

        # Fecha con DatePicker
        tk.Label(form, text="Fecha:").grid(row=0, column=0, sticky=tk.W)
        self.date_entry = DateEntry(form, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=0, column=1, pady=2)

        # Hora
        tk.Label(form, text="Hora: 00:00").grid(row=1, column=0, sticky=tk.W)
        self.hora_entry = tk.Entry(form)
        self.hora_entry.grid(row=1, column=1, pady=2)

        # Descripción (multilínea)
        tk.Label(form, text="Descripción:").grid(row=2, column=0, sticky=tk.W)
        self.desc_text = tk.Text(form, height=4, width=30)
        self.desc_text.grid(row=2, column=1, pady=2)

        # Botones
        tk.Button(right_frame, text="Agregar Evento", command=self.add_event, width=20).pack(pady=4)
        tk.Button(right_frame, text="Eliminar Evento", command=self.delete_event, width=20).pack(pady=4)
        tk.Button(right_frame, text="Salir", command=self.root.quit, width=20).pack(pady=4)

    def add_event(self):
        fecha = self.date_entry.get_date().strftime("%Y-%m-%d")
        hora = self.hora_entry.get().strip()
        desc = self.desc_text.get("1.0", tk.END).strip()

        if not fecha or not hora or not desc:
            messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos.")
            return

        evento = {"fecha": fecha, "hora": hora, "descripcion": desc}
        self.events.append(evento)
        self.refresh_tree()

        # Limpiar entradas
        self.hora_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)

    def delete_event(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Eliminar", "Seleccione un evento para eliminar.")
            return
        if not messagebox.askyesno("Confirmar", "¿Eliminar el evento seleccionado?"):
            return
        idx = self.tree.index(sel[0])
        del self.events[idx]
        self.refresh_tree()

    def refresh_tree(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for e in self.events:
            self.tree.insert('', 'end', values=(e['fecha'], e['hora'], e['descripcion']))

if __name__ == '__main__':
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()