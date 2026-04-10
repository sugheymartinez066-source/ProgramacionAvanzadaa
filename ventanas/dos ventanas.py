import tkinter as tk

def ventana_principal():
    global ventana
    ventana = tk.Tk()
    ventana.title("Ventana Principal")
    ventana.geometry("500x200")
    ventana.config(bg = "skyblue")

    etiqueta1 = tk.Label(ventana,text ="Esta es la ventana princicpal")
    etiqueta1.pack()

    boton1 = tk.Button(ventana, text = "Ventana 2", command = ventana2)
    boton1.pack(pady = 20)


    ventana.mainloop()

def destruir_ventana(ventana_actual):
    ventana_actual.destroy()
    ventana_principal()

def ventana2():
    ventana.destroy()
    ventana2  = tk.Tk()
    ventana2.title("Ventana Principal")
    ventana2.geometry("500x200")
    ventana2.config(bg = "pink")
    etiqueta2 = tk.Label(ventana2,text ="Esta es la ventana 2")
    etiqueta2.pack()

    boton2 = tk.Button(ventana2, text = "Ventana Principal", command = lambda: destruir_ventana(ventana2))
    boton2.pack(pady = 20)


    ventana2.mainloop()
    
ventana_principal()