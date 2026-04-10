import tkinter as tk

root = tk.Tk()
root.title("Ejemplo de Grid")
root.geometry("500x200")
root.config(bg="pink")

etiqueta1=tk.Label(root,text="Nombre",bg="blue",fg='white',font=('Arial',16,'bold'))
etiqueta1.grid(row=0, column=0, padx=5, pady=5, sticky="w")
entrada1=tk.Entry(root,width=60)
entrada1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Correo:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entrada2=tk.Entry(root, width=45)
entrada2.grid=(row = 1, column = 1, padx = 5, pady = 5, sticky = "e")

tk.Button(root, text="Enviar").grid(row=2, column=0, columnspan=5, pady=10)

root.mainloop()