import tkinter as tk
from tkinter import messagebox

def opcion():
    if var.get()==1:
        messagebox.showinfo("Opcion elegida","Te gustan los Tacos")
    elif var.get()==2:
        messagebox.showinfo("Opcion elegida","Te gustan las Pizzas")
    elif var.get()==3:
        messagebox.showinfo("Opcion elegida","Te gustan los Huaraches")   
    elif var.get()==4:
        messagebox.showinfo("Opcion elegida","Te gustan el Espaghetti") 
    else:
        messagebox.showinfo("Opcion elegida","No seleccionaste nada") 


ventana=tk.Tk()
ventana.title("Radio button")
ventana.geometry("300x400")

etiqueta1=tk.Label(ventana,text="¿Cual es tu comida favorita?")
etiqueta1.pack(pady=20)

var=tk.IntVar()
rad1=tk.Radiobutton(ventana,text="Tacos",variable=var,value=1)
rad1.pack()
rad2=tk.Radiobutton(ventana,text="Pizza",variable=var,value=2)
rad2.pack()
rad3=tk.Radiobutton(ventana,text="Huaraches",variable=var,value=3)
rad3.pack()
rad4=tk.Radiobutton(ventana,text="Espaghetti",variable=var,value=4)
rad4.pack()

boton1=tk.Button(ventana,text="Verificar",command=opcion)
boton1.pack(pady=30)


ventana.mainloop()