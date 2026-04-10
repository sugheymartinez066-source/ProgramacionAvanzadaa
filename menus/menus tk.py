import tkinter as tk
from tkinter import messagebox
import tkinter as tk

def nuevo_archivo():
    messagebox.showinfo("Información", "Creaste un nuevo archivo")

def abrir_archivo():
    messagebox.showinfo("Información", "abriste un archivo")

def guardar_archivo():
    messagebox.showinfo("Información", "guardaste un archivo")

def cortar():
    messagebox.showinfo("Información", "cortaste un texto")

def pegar():
    messagebox.showinfo("Información", "pegaste un texto")

ventana1 = tk.Tk()
ventana1.title("Uso de Menús")
ventana1.geometry("500x400")

barra_menu = tk.Menu(ventana1)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Nuevo", command=nuevo_archivo)
menu_archivo.add_command(label="Abrir", command=abrir_archivo)
menu_archivo.add_command(label="Guardar", command=guardar_archivo)

menu_edicion = tk.Menu(barra_menu, tearoff=0)
menu_edicion.add_command(label="Cortar", command=cortar)
menu_edicion.add_command(label="Pegar", command=pegar)

barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
barra_menu.add_cascade(label="Edición", menu=menu_edicion)
ventana1.config(menu=barra_menu)

ventana1.mainloop()