import tkinter as tk

# Función para agregar lo que el usuario escriba
def agregar():
    dato = entrada.get()   # tomar el texto del campo
    if dato != "":         # si no está vacío
        lista.insert(tk.END, dato)  # ponerlo en la lista
        entrada.delete(0, tk.END)   # borrar lo escrito para volver a escribir

# Función para limpiar
def limpiar():
    # si hay algo seleccionado se borra
    seleccion = lista.curselection()
    if seleccion:
        lista.delete(seleccion)
    else:  # si no hay nada seleccionado borra tod0
        lista.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Mi primera App con Tkinter")  # título de la ventana
ventana.geometry("400x300")  # tamaño de la ventana

# Etiqueta
lbl = tk.Label(ventana, text="Escribe algo:")
lbl.pack()

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack()

# Botón para agregar
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar)
btn_agregar.pack()

# Botón para limpiar
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
btn_limpiar.pack()

# Lista para mostrar los datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack()

# Mantener la ventana abierta
ventana.mainloop()