import tkinter as tk



ventana = tk.Tk()
etiqueta = tk.Label(ventana, text="Splavia Unitecnar", bg="RoyalBlue4", fg="blue", font=("Times New Roman", 22), width=25, height=5, anchor="n")
etiqueta.pack()

ventana.geometry("300x200")
usuario1 = tk.Entry(ventana, text="Usuario", width="10", fg="grey", font=("Ariall", 17))
usuario = tk.Label(ventana, text="Usuario", width="10", bg="RoyalBlue4", fg="blue", font=("Ariall", 17))
usuario.place(x=50, y=90)
usuario1.place(x=50, y=120)


ventana.geometry("400x200")
contraseña1 = tk.Label(ventana, text="Contraseña", width="10", bg="RoyalBlue4", fg="blue", font=("Bahnchrift Light", 15))
contraseña1.place(x=210, y=90)
contraseña = tk.Entry(ventana, text="Contraseña", width="10", fg="grey", font=("Bahnchrift Light", 15))
contraseña.place(x=210, y=120)

boton1 = tk.Button(ventana, text="Acceder", command="cambiar_texto", bg="black", relief="raised", fg="blue", width=50, height=5, font=("Times New Roman", 15))
boton1.pack()


ventana.mainloop()