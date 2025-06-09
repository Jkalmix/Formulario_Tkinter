import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import re
import datetime

def crear_formulario_reserva():
    # Configuración inicial de la ventana principal
    ventana = tk.Tk()
    ventana.title("Reserva tu Curso")
    ventana.geometry("600x850")  # Tamaño fijo para acomodar todos los widgets
    ventana.resizable(False, False)
    ventana.configure(bg="#212121")  # Fondo oscuro

    # Estilos personalizados para Combobox (ttk)
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox",
                    fieldbackground="white",
                    background="lightgray",
                    foreground="black",
                    selectbackground="#e60000",
                    selectforeground="white",
                    bordercolor="#505050",
                    arrowcolor="black")

    # Título principal del formulario
    titulo_label = tk.Label(ventana,
                            text="Reserva tu Curso",
                            font=("Arial", 24, "bold"),
                            fg="white",
                            bg="#e60000")
    titulo_label.pack(pady=20, fill="x")

    # Frame para organizar campos del formulario
    frame_campos = tk.Frame(ventana, bg="#212121")
    frame_campos.pack(pady=10, padx=20, fill="x")

    # Campo "Sede" con combobox
    label_sede = tk.Label(frame_campos, text="Sede:", font=("Arial", 12), fg="white", bg="#212121")
    label_sede.pack(anchor="w", pady=(10, 0))
    opciones_sede = ["Seleccione una sede", "Sede A", "Sede B", "Sede C"]
    sede_seleccionada = tk.StringVar()
    combo_sede = ttk.Combobox(frame_campos, textvariable=sede_seleccionada,
                              values=opciones_sede, state="readonly")
    combo_sede.set(opciones_sede[0])
    combo_sede.pack(fill="x", ipady=2)

    # Campo "Fecha" con entrada y botón para calendario desplegable
    label_fecha = tk.Label(frame_campos, text="Fecha:", font=("Arial", 12), fg="white", bg="#212121")
    label_fecha.pack(anchor="w", pady=(10, 0))
    entry_fecha = tk.Entry(frame_campos, font=("Arial", 12))
    entry_fecha.pack(fill="x", ipady=2)

    def abrir_calendario():
        # Ventana secundaria para seleccionar fecha con calendario
        top = tk.Toplevel(ventana)
        top.title("Seleccionar Fecha")
        top.transient(ventana)
        top.grab_set()

        cal = Calendar(top, selectmode='day',
                       font="Arial 10", background="gray",
                       foreground="white",
                       selectbackground="#e60000",
                       selectforeground="white",
                       borderwidth=2)
        cal.pack(pady=20, padx=20)

        def set_fecha():
            # Inserta la fecha seleccionada en el entry y cierra la ventana
            selected_date = cal.selection_get()
            entry_fecha.delete(0, tk.END)
            entry_fecha.insert(0, selected_date.strftime("%d/%m/%Y"))
            top.destroy()

        confirm_btn = tk.Button(top, text="Seleccionar", command=set_fecha,
                                font=("Arial", 12),
                                bg="#e60000", fg="white")
        confirm_btn.pack(pady=10)

        # Centrar ventana del calendario sobre la principal
        top.update_idletasks()
        x = ventana.winfo_x() + (ventana.winfo_width() // 2) - (top.winfo_width() // 2)
        y = ventana.winfo_y() + (ventana.winfo_height() // 2) - (top.winfo_height() // 2)
        top.geometry(f"+{x}+{y}")

    boton_calendario = tk.Button(frame_campos, text="Abrir Calendario", command=abrir_calendario,
                                 font=("Arial", 10),
                                 bg="#e60000", fg="white")
    boton_calendario.pack(fill="x", pady=5)

    # Campo "Hora" con combobox
    label_hora = tk.Label(frame_campos, text="Hora:", font=("Arial", 12), fg="white", bg="#212121")
    label_hora.pack(anchor="w", pady=(10, 0))
    opciones_hora = ["Seleccione una hora", "09:00", "10:00", "11:00", "12:00", "14:00", "15:00"]
    hora_seleccionada = tk.StringVar()
    combo_hora = ttk.Combobox(frame_campos, textvariable=hora_seleccionada,
                              values=opciones_hora, state="readonly")
    combo_hora.set(opciones_hora[0])
    combo_hora.pack(fill="x", ipady=2)

    # Campo "Nombre" (entrada de texto)
    label_nombre = tk.Label(frame_campos, text="Nombre:", font=("Arial", 12), fg="white", bg="#212121")
    label_nombre.pack(anchor="w", pady=(10, 0))
    entry_nombre = tk.Entry(frame_campos, font=("Arial", 12))
    entry_nombre.pack(fill="x", ipady=2)

    # Validación numérica para campos cédula y teléfono
    def validate_numeric_input(new_value):
        return bool(re.fullmatch(r'\d*', new_value))

    vcmd = ventana.register(validate_numeric_input)

    # Campo "Cédula"
    label_cedula = tk.Label(frame_campos, text="Cédula:", font=("Arial", 12), fg="white", bg="#212121")
    label_cedula.pack(anchor="w", pady=(10, 0))
    entry_cedula = tk.Entry(frame_campos, font=("Arial", 12), validate='key', validatecommand=(vcmd, '%P'))
    entry_cedula.pack(fill="x", ipady=2)

    # Campo "Confirmar Cédula"
    label_confirmar_cedula = tk.Label(frame_campos, text="Confirmar Cédula:", font=("Arial", 12), fg="white", bg="#212121")
    label_confirmar_cedula.pack(anchor="w", pady=(10, 0))
    entry_confirmar_cedula = tk.Entry(frame_campos, font=("Arial", 12), validate='key', validatecommand=(vcmd, '%P'))
    entry_confirmar_cedula.pack(fill="x", ipady=2)

    # Campo "Teléfono"
    label_telefono = tk.Label(frame_campos, text="Teléfono:", font=("Arial", 12), fg="white", bg="#212121")
    label_telefono.pack(anchor="w", pady=(10, 0))
    entry_telefono = tk.Entry(frame_campos, font=("Arial", 12), validate='key', validatecommand=(vcmd, '%P'))
    entry_telefono.pack(fill="x", ipady=2)

    # Campo "Correo Electrónico"
    label_correo = tk.Label(frame_campos, text="Correo Electrónico:", font=("Arial", 12), fg="white", bg="#212121")
    label_correo.pack(anchor="w", pady=(10, 0))
    entry_correo = tk.Entry(frame_campos, font=("Arial", 12))
    entry_correo.pack(fill="x", ipady=2)

    # Variables para checkboxes
    acepto_terminos = tk.BooleanVar()
    recibir_confirmacion = tk.BooleanVar()

    # Checkbox para Términos y Condiciones con "enlace"
    checkbox_terminos_frame = tk.Frame(frame_campos, bg="#212121")
    checkbox_terminos_frame.pack(anchor="w", pady=(15, 0))

    checkbox_terminos = tk.Checkbutton(checkbox_terminos_frame,
                                       text="He leído y Acepto los ",
                                       variable=acepto_terminos,
                                       fg="white",
                                       bg="#212121",
                                       font=("Arial", 10),
                                       selectcolor="#212121")
    checkbox_terminos.pack(side="left")

    label_link_terminos = tk.Label(checkbox_terminos_frame,
                                   text="Términos y Condiciones",
                                   fg="#FFA500", bg="#212121",
                                   font=("Arial", 10, "underline"),
                                   cursor="hand2")
    label_link_terminos.pack(side="left")

    def abrir_terminos_condiciones(event):
        # Muestra un mensaje con los términos y condiciones (puedes personalizarlo)
        messagebox.showinfo("Términos y Condiciones", "Aquí irían los términos y condiciones completos.")

    label_link_terminos.bind("<Button-1>", abrir_terminos_condiciones)

    # Checkbox para recibir confirmación por correo
    checkbox_confirmacion = tk.Checkbutton(frame_campos,
                                           text="Deseo recibir la confirmación de mi reserva por correo",
                                           variable=recibir_confirmacion,
                                           fg="white",
                                           bg="#212121",
                                           font=("Arial", 10),
                                           selectcolor="#212121")
    checkbox_confirmacion.pack(anchor="w", pady=(5, 10))

    # Función que valida y procesa la reserva
    def reservar_cita():
        sede = sede_seleccionada.get()
        fecha = entry_fecha.get()
        hora = hora_seleccionada.get()
        nombre = entry_nombre.get()
        cedula = entry_cedula.get()
        confirmar_cedula = entry_confirmar_cedula.get()
        telefono = entry_telefono.get()
        correo = entry_correo.get()
        acepta_terminos_val = acepto_terminos.get()
        recibe_confirmacion_val = recibir_confirmacion.get()

        # Validar campos obligatorios
        if (sede == "Seleccione una sede" or hora == "Seleccione una hora" or not fecha or
            not nombre or not cedula or not telefono or not correo):
            messagebox.showerror("Error de Reserva", "Por favor, complete todos los campos obligatorios.")
            return

        # Validar que las cédulas coincidan
        if cedula != confirmar_cedula:
            messagebox.showerror("Error de Reserva", "Las cédulas no coinciden.")
            return

        # Validar aceptación de términos
        if not acepta_terminos_val:
            messagebox.showerror("Error de Reserva", "Debe aceptar los Términos y Condiciones.")
            return

        # Validar formato de fecha
        try:
            datetime.datetime.strptime(fecha, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error de Fecha", "Formato de fecha incorrecto. Por favor, seleccione una fecha del calendario.")
            return

        # Construir mensaje de confirmación
        mensaje_confirmacion = (
            f"Reserva Exitosa!\n\n"
            f"Sede: {sede}\n"
            f"Fecha: {fecha}\n"
            f"Hora: {hora}\n"
            f"Nombre: {nombre}\n"
            f"Cédula: {cedula}\n"
            f"Teléfono: {telefono}\n"
            f"Correo: {correo}\n"
        )
        if recibe_confirmacion_val:
            mensaje_confirmacion += "\nRecibirá una confirmación por correo."

        messagebox.showinfo("Reserva Confirmada", mensaje_confirmacion)

    # Botón para enviar la reserva
    boton_reservar = tk.Button(ventana,
                              text="RESERVAR",
                              command=reservar_cita,
                              font=("Arial", 16, "bold"),
                              bg="#e60000",
                              fg="white",
                              activebackground="#cc0000",
                              activeforeground="white",
                              relief="raised",
                              bd=3)
    boton_reservar.pack(pady=30, ipadx=50, ipady=10)

    return ventana


if __name__ == "__main__":
    app = crear_formulario_reserva()
    app.mainloop()
