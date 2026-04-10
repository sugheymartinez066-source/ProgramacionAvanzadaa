import tkinter as tk
from tkinter import messagebox

def ventanas():
    if var.get()==1:
        messagebox.showinfo("Ventana de informacion","Aca puedes escribir informacion al ususario")
    elif var.get()==2:
        messagebox.showwarning("Ventana de advertencia","Esta es una ADVERTENCIA")
    elif var.get()==3:
        messagebox.showerror("Ventana de error ","Has cometido un ERROR")   
    elif var.get()==4:
        respuesta=messagebox.askyesno("Ventana de opcion","¿Te gusta esta clase?") 
        if respuesta:
            messagebox.showinfo("Ventana de respuesta","Mas te vale")
        else: 
            messagebox.showinfo("Ventana de respuesta","Por eso vas a reprobar")
    elif var.get()==5:
        respuesta=messagebox.askokcancel("Ventana de opcion","¿Das tu alma a esta clase?") 
        if respuesta:
            messagebox.showinfo("Ventana de respuesta","Por eso vas a sacar 10")
        else: 
            messagebox.showinfo("Ventana de respuesta","Por eso repruebas")
    else:
         messagebox.showinfo("Ventana de respuesta","No elegiste nada") 


ventana=tk.Tk()
ventana.title("Uso de las diferentes messagebox")
ventana.geometry("400x500")
ventana.config(bg="pink")

etiqueta1=tk.Label(ventana,text="Veremeos el uso de las messagebox")
etiqueta1.pack(pady=20)

var=tk.IntVar()
rad1=tk.Radiobutton(ventana,text="Mostrar informacion",variable=var,value=1)
rad1.pack()
rad2=tk.Radiobutton(ventana,text="Advertencia",variable=var,value=2)
rad2.pack()
rad3=tk.Radiobutton(ventana,text="Error",variable=var,value=3)
rad3.pack()
rad4=tk.Radiobutton(ventana,text="Pregunta si o no",variable=var,value=4)
rad4.pack()
rad5=tk.Radiobutton(ventana,text="Pregunta aceptar o cancelar",variable=var,value=5)
rad5.pack()


boton1=tk.Button(ventana,text="Sacar ventana",command=ventanas)
boton1.pack(pady=30)


ventana.mainloop()