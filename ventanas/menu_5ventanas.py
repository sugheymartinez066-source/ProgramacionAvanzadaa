import tkinter as tk  

def menu_principal():
    global root
    root = tk.Tk()
    root.title("Menú de 5 Ventanas")
    root.geometry("400x400")
    root.config(bg="lightgray")

    tk.Label(root, text="MENU PRINCIPAL", font=("Arial", 16, "bold"), bg="lightgray").pack(pady=20)

    tk.Button(root, text="Ir a Ventana 1", width=20, command=lambda: [root.destroy(), ventana_1()]).pack(pady=5)
    tk.Button(root, text="Ir a Ventana 2", width=20, command=lambda: [root.destroy(), ventana_2()]).pack(pady=5)
    tk.Button(root, text="Ir a Ventana 3", width=20, command=lambda: [root.destroy(), ventana_3()]).pack(pady=5)
    tk.Button(root, text="Ir a Ventana 4", width=20, command=lambda: [root.destroy(), ventana_4()]).pack(pady=5)
    tk.Button(root, text="Ir a Ventana 5", width=20, command=lambda: [root.destroy(), ventana_5()]).pack(pady=5)
    
    tk.Button(root, text="SALIR", width=20, fg="white", bg="red", command=root.destroy).pack(pady=20)

    root.mainloop()



def ventana_1():
    v1 = tk.Tk()
    v1.geometry("300x200")
    v1.config(bg="pink")
    tk.Label(v1, text="ESTÁS EN LA VENTANA 1", bg="pink").pack(pady=40)
    tk.Button(v1, text="Volver al Menú", command=lambda: [v1.destroy(), menu_principal()]).pack()
    v1.mainloop()

def ventana_2():
    v2 = tk.Tk()
    v2.geometry("300x200")
    v2.config(bg="skyblue")
    tk.Label(v2, text="ESTÁS EN LA VENTANA 2", bg="skyblue").pack(pady=40)
    tk.Button(v2, text="Volver al Menú", command=lambda: [v2.destroy(), menu_principal()]).pack()
    v2.mainloop()

def ventana_3():
    v3 = tk.Tk()
    v3.geometry("300x200")
    v3.config(bg="lightgreen")
    tk.Label(v3, text="ESTÁS EN LA VENTANA 3", bg="lightgreen").pack(pady=40)
    tk.Button(v3, text="Volver al Menú", command=lambda: [v3.destroy(), menu_principal()]).pack()
    v3.mainloop()

def ventana_4():
    v4 = tk.Tk()
    v4.geometry("300x200")
    v4.config(bg="gold")
    tk.Label(v4, text="ESTÁS EN LA VENTANA 4", bg="gold").pack(pady=40)
    tk.Button(v4, text="Volver al Menú", command=lambda: [v4.destroy(), menu_principal()]).pack()
    v4.mainloop()

def ventana_5():
    v5 = tk.Tk()
    v5.geometry("300x200")
    v5.config(bg="orchid")
    tk.Label(v5, text="ESTÁS EN LA VENTANA 5", bg="orchid").pack(pady=40)
    tk.Button(v5, text="Volver al Menú", command=lambda: [v5.destroy(), menu_principal()]).pack()
    v5.mainloop()


menu_principal()