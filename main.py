from forms import abrir_nav, enviar_form, cerrar_nav
import customtkinter
from tkinter import messagebox

# Definir aperiencia de la aplicacion
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Crear la ventana
app = customtkinter.CTk()
app.geometry("400x300")
app.title("Responder Formularios")
app.iconbitmap("./icon.ico")


# Funcior de enviar
def enviar():
    # Obtener datos de las entrys
    url = entry_1.get()
    repeticiones = entry_2.get()

    # Validar datos
    if url == "":
        messagebox.showerror("Error", "Valor Para Url Invalida")
        url_check = False
    else:
        url_check = True
    try:
        repeticiones = int(repeticiones)
    except:
        messagebox.showerror("Error", "Numero de Repeticiones invalido")
        repeticiones_check = False
    else:
        repeticiones_check = True
    
    # Iniciar procedimientos
    if url_check and repeticiones_check:
        # Funcion para iniciar el navegador
        abrir_nav()

        # Repetir la funcion de enviar formulario
        # tantas veces como el usuario decida
        for a in range(0, repeticiones):
            enviar_form(url)

        # Funcion para cerrar el navegador
        cerrar_nav()
        
        # Mensaje de tarea finalizada
        messagebox.showinfo("Tarea Teminada", "Tarea Terminada con Exito")
        
# Crar el frame principal de la aplicacion
frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=20, fill="both", expand=True)

# Dar un titulo 
title = customtkinter.CTkLabel(master=frame_1, text="Responder Formularios", font=("sans serif", 32))
title.pack(pady=20, padx=10)

# Entrada para la url
entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Url", width=250)
entry_1.pack(pady=10, padx=10)

# Entrada para el numero de repeticiones
entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Repeticiones", width=250)
entry_2.pack(pady=10, padx=10)

# Boton para iniciar el procedimiento
button_1 = customtkinter.CTkButton(master=frame_1, text="Enviar", command=enviar)
button_1.pack(pady=10, padx=10)

# Copyright
autor = customtkinter.CTkLabel(master=frame_1, text="Create by: Melchor Ruiz", anchor='e', justify='right', width=350)
autor.pack(pady=10, padx=10)

# Ciclar aplicacion
app.mainloop()
