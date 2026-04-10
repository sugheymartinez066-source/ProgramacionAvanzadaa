import tkinter as tk

def ventana_principal():
    global ventana
    ventana = tk.Tk()
    ventana.title("Ventana Principal")
    ventana.geometry("500x200")
    ventana.config(bg = "skyblue")

    etiqueta1 = tk.Label(ventana,text ="Esta es la ventana princicpal")
    etiqueta1.pack()

    boton1 = tk.Button(ventana, text = "Ventana 2", command = ventana_2)
    boton1.pack()
    boton2 = tk.Button(ventana, text = "Ventana 3", command = ventana_3)
    boton2.pack()
    boton4 = tk.Button(ventana, text = "Ventana 4", command = ventana_4)
    boton4.pack()
    boton5 = tk.Button(ventana, text = "Ventana 5", command = ventana_5)
    boton5.pack()
   


    ventana.mainloop()

def destruir_ventana(ventana_actual):
    ventana_actual.destroy()
    ventana_principal()

def ventana_2():
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

def ventana_3():
    ventana.destroy()
    ventana3  = tk.Tk()
    ventana3.title("Ventana Principal")
    ventana3.geometry("500x200")
    ventana3.config(bg = "pink")
    etiqueta3 = tk.Label(ventana3,text ="Esta es la ventana 3")
    etiqueta3.pack()

    boton3 = tk.Button(ventana3, text = "Ventana Principal", command = lambda: destruir_ventana(ventana3))
    boton3.pack(pady = 20)


    ventana3.mainloop()

def ventana_4():
    ventana.destroy()
    ventana4  = tk.Tk()
    ventana4.title("Ventana Principal")
    ventana4.geometry("500x200")
    ventana4.config(bg = "pink")
    etiqueta4 = tk.Label(ventana4,text ="Esta es la ventana 4")
    etiqueta4.pack()

    boton4 = tk.Button(ventana4, text = "Ventana Principal", command = lambda: destruir_ventana(ventana4))
    boton4.pack(pady = 20)


    ventana4.mainloop()

def ventana_5():
    ventana.destroy()
    ventana5  = tk.Tk()
    ventana5.title("Ventana Principal")
    ventana5.geometry("500x200")
    ventana5.config(bg = "pink")
    etiqueta5 = tk.Label(ventana5,text ="Esta es la ventana 5")
    etiqueta5.pack()

    boton5 = tk.Button(ventana5, text = "Ventana Principal", command = lambda: destruir_ventana(ventana5))
    boton5.pack(pady = 20)


    ventana5.mainloop()


    
ventana_principal()