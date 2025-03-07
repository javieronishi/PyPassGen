import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGenerator:
    def __init__(self, password_length):
        self.password_length = password_length

    def generate_password(self):
        # Define the allowed characters
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate the password
        password = "".join(
            random.choice(characters) for _ in range(self.password_length)
        )
        return password

def generate_password_gui():
    try:
        length = int(entry_length.get())
        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1.")
        elif length > 64:
            messagebox.showerror("Error", "Password length cannot exceed 64.")
        else:
            password = PasswordGenerator(length)
            generated_password = password.generate_password()
            # Copiar al portapapeles usando tkinter
            root.clipboard_clear()
            root.clipboard_append(generated_password)
            root.update()  # Actualizar el portapapeles
            messagebox.showinfo("Success", "Password generated and copied to clipboard!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Crear la ventana principal
root = tk.Tk()
root.title("Password Generator")

# Tamaño fijo de la ventana (ancho x alto)
root.geometry("300x200")
# Deshabilitar redimensionamiento
root.resizable(False, False)

# Crear y colocar los widgets en la ventana
label_instruction = tk.Label(root, text="Enter the desired password length (max 64):")
label_instruction.pack(pady=10)

entry_length = tk.Entry(root)
entry_length.pack(pady=10)

button_generate = tk.Button(root, text="Generate Password", command=generate_password_gui)
button_generate.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()