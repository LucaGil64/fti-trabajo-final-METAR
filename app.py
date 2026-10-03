import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    # Función que se ejecuta al hacer clic en el botón
    messagebox.showinfo("Saludo", "¡Hola! Has hecho clic en el botón.")

# 1. Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Primera App con Tkinter")
ventana.geometry("600x400")  # Ancho x Alto

# 2. Crear los componentes (Widgets)
etiqueta = tk.Label(ventana, text="Bienvenido al trabajo final de fti", font=("Arial", 14))
etiqueta.pack(pady=20)  # El método pack coloca el elemento en la ventana

boton = tk.Button(ventana, text="Haz clic aquí", command=mostrar_mensaje, font=("Arial", 11))
boton.pack(pady=10)

# 3. Iniciar el bucle principal de la aplicación
ventana.mainloop()