# 📋 Proyecto: Formulario de Reservas con Tkinter

Este proyecto es una aplicación de escritorio desarrollada en Python utilizando Tkinter. Está diseñada como un formulario visualmente atractivo para reservar cursos, donde se recolecta información esencial del usuario mediante una interfaz intuitiva.

---

## 🧱 1. Configuración Inicial y Ventana Principal

### 1.1. Importaciones Esenciales

Antes de comenzar a crear la interfaz, se importan las bibliotecas necesarias:

```python
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar  # pip install tkcalendar
import re
```

**Importaciones clave:**

* `tkinter`: Base para la interfaz gráfica.
* `ttk`: Widgets modernos.
* `messagebox`: Cuadros de diálogo.
* `tkcalendar`: Selector de fechas.
* `re`: Validaciones con expresiones regulares.

### 1.2. Crear la Ventana Principal

```python
def crear_formulario_reserva():
    ventana = tk.Tk()
    ventana.title("Reserva tu Curso")
    ventana.geometry("600x850")
    ventana.resizable(False, False)
    ventana.configure(bg="#212121")
    return ventana
```

**Características:**

* Título de la ventana.
* Tamaño fijo (600x850 px).
* Fondo oscuro.

### 1.3. Estilos con `ttk.Style`

```python
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
```

---

## 🧩 2. Título y Contenedores

### 2.1. Título Principal

```python
titulo_label = tk.Label(ventana, text="Reserva tu Curso",
                         font=("Arial", 24, "bold"), fg="white", bg="#e60000")
titulo_label.pack(pady=20, fill="x")
```

### 2.2. Contenedor de Campos

```python
frame_campos = tk.Frame(ventana, bg="#212121")
frame_campos.pack(pady=10, padx=20, fill="x")
```

**Ventajas del uso de `Frame`:**

* Agrupa visualmente los campos.
* Facilita la organización del layout.

---

## 🧾 3. Campos de Entrada Básicos

### 3.1. Etiquetas de Descripción (`tk.Label`)

```python
label_sede = tk.Label(frame_campos, text="Sede:", font=("Arial", 12), fg="white", bg="#212121")
label_sede.pack(anchor="w", pady=(10, 0))
```

**Notas:**

* `anchor="w"`: Alineación a la izquierda.
* `pady`: Espaciado vertical.

### 3.2. Listas Desplegables (`ttk.Combobox` + `tk.StringVar`)

```python
opciones_sede = ["Seleccione una sede", "Sede A", "Sede B", "Sede C"]
sede_seleccionada = tk.StringVar()
combo_sede = ttk.Combobox(frame_campos, textvariable=sede_seleccionada,
                          values=opciones_sede, state="readonly")
combo_sede.set(opciones_sede[0])
combo_sede.pack(fill="x", ipady=2)
```

**Características:**

* `StringVar()`: Enlace entre la interfaz y el código.
* `state="readonly"`: Solo permite seleccionar.
* `fill="x"`: Expande el ancho.

### 3.3. Campos de Texto (`tk.Entry`)

```python
entry_nombre = tk.Entry(frame_campos, font=("Arial", 12))
entry_nombre.pack(fill="x", ipady=2)
```

**Aplicación similar:**

* Para cédula, teléfono, correo y confirmación de cédula.

---

---

# 📋 Proyecto: Calendario Desplegable con Tkinter y tkcalendar

En esta sección del proyecto, incorporamos un calendario interactivo para mejorar la selección de fechas en la interfaz gráfica con Tkinter. Utilizamos el módulo `tkcalendar` junto con ventanas emergentes (`tk.Toplevel`) para una experiencia amigable.

---

## 4. El Calendario Desplegable

### Selección de Fechas Amigable con tkcalendar

Para facilitar al usuario la elección de fechas, implementamos un calendario desplegable que aparece en una ventana secundaria. Esto requiere manejar ventanas emergentes y conectar el calendario con un campo de entrada.

---

### 4.1. Configurando el Campo de Fecha y el Botón

El campo donde se mostrará la fecha seleccionada es un `tk.Entry` de solo lectura, y un botón permitirá abrir el calendario.

```python
# Campo para mostrar la fecha seleccionada
entry_fecha = tk.Entry(frame_campos, font=("Arial", 12))
entry_fecha.pack(fill="x", ipady=2)

# Botón que abre la ventana del calendario
boton_calendario = tk.Button(
    frame_campos, 
    text="Abrir Calendario", 
    command=abrir_calendario,
    font=("Arial", 10),
    bg="#e60000",
    fg="white"
)
boton_calendario.pack(fill="x", pady=5)
```

* **entry\_fecha**: Aquí aparecerá la fecha seleccionada.
* **boton\_calendario**: Botón que activa la ventana emergente con el calendario. Su `command` es la función `abrir_calendario`.

---

### 4.2. La Ventana Emergente del Calendario (`tk.Toplevel`)

La función `abrir_calendario` crea una ventana secundaria que contiene el widget calendario. El usuario debe seleccionar una fecha y confirmar.

```python
def abrir_calendario():
    # Crear ventana emergente hija de la ventana principal
    top = tk.Toplevel(ventana)
    top.title("Seleccionar Fecha")
    top.transient(ventana)  # La ventana 'top' depende de 'ventana'
    top.grab_set()          # Captura el foco, obliga a interactuar con 'top'

    # Crear el widget calendario
    cal = Calendar(
        top,
        selectmode='day',
        font="Arial 10",
        background="gray",
        foreground="white",
        selectbackground="#e60000",
        selectforeground="white",
        borderwidth=2
    )
    cal.pack(pady=20, padx=20)

    # Función para asignar la fecha seleccionada al entry y cerrar la ventana
    def set_fecha():
        selected_date = cal.selection_get()  # Fecha como objeto datetime.date
        entry_fecha.delete(0, tk.END)        # Limpiar el entry
        entry_fecha.insert(0, selected_date.strftime("%d/%m/%Y"))  # Formatear e insertar
        top.destroy()                        # Cerrar ventana emergente

    # Botón para confirmar la selección
    confirm_btn = tk.Button(
        top,
        text="Seleccionar",
        command=set_fecha,
        font=("Arial", 12),
        bg="#e60000",
        fg="white"
    )
    confirm_btn.pack(pady=10)

    # Centrar ventana emergente sobre la ventana principal
    top.update_idletasks()
    x = ventana.winfo_x() + (ventana.winfo_width() // 2) - (top.winfo_width() // 2)
    y = ventana.winfo_y() + (ventana.winfo_height() // 2) - (top.winfo_height() // 2)
    top.geometry(f"+{x}+{y}")
```

---

### Conceptos Clave

* `tk.Toplevel`: Crea ventanas secundarias o emergentes.
* `top.grab_set()`: Obliga al usuario a interactuar con la ventana emergente antes de volver a la principal.
* `Calendar`: Widget del calendario, configurable para seleccionar fechas.
* `.selection_get()`: Obtiene la fecha seleccionada como objeto `datetime.date`.
* `.strftime("%d/%m/%Y")`: Da formato de texto a la fecha (día/mes/año).

---

---

## 5. Validación de Entrada Numérica

### Asegurando la Calidad de los Datos (Cédulas y Teléfono)

Es vital que los campos de cédula y teléfono solo acepten números. Tkinter permite validar la entrada en tiempo real para garantizar datos correctos.

---

### 5.1. La Función de Validación

Creamos una función que Tkinter llamará cada vez que el usuario intente modificar un campo validado. Recibe el contenido que tendría el campo si la última tecla fuera permitida.

```python
import re  # Para usar expresiones regulares

def validate_numeric_input(new_value):
    # Permite solo dígitos o cadena vacía
    if re.fullmatch(r'\d*', new_value):
        return True
    else:
        # Opcional: mostrar mensaje de error (no obligatorio)
        # messagebox.showerror("Error de Entrada", "Solo se permiten números en este campo.")
        return False
```

* `re.fullmatch(r'\d*', new_value)`: Verifica que toda la cadena sea dígitos o vacía.
* Retorna `True` para permitir la entrada, `False` para bloquearla.

---

### 5.2. Registrando el Comando y Vinculándolo a los Campos `tk.Entry`

Para que Tkinter use la función de validación, hay que registrarla y luego asignarla en los `Entry` que queremos validar.

```python
# Registro de la función en la ventana principal
vcmd = ventana.register(validate_numeric_input)

# Campo Cédula
label_cedula = tk.Label(frame_campos, text="Cédula:", font=("Arial", 12), fg="white", bg="#212121")
label_cedula.pack(anchor="w", pady=(10, 0))

entry_cedula = tk.Entry(frame_campos, font=("Arial", 12), validate='key', validatecommand=(vcmd, '%P'))
entry_cedula.pack(fill="x", ipady=2)

# Campo Confirmar Cédula (misma configuración)
entry_confirmar_cedula = tk.Entry(frame_campos, font=("Arial", 12), validate='key', validatecommand=(vcmd, '%P'))
entry_confirmar_cedula.pack(fill="x", ipady=2)

# Campo Teléfono (misma configuración)
entry_telefono = tk.Entry(frame_campos, font=("Arial", 12), validate='key', validatecommand=(vcmd, '%P'))
entry_telefono.pack(fill="x", ipady=2)
```

* `ventana.register()`: Convierte la función Python para que Tkinter la pueda llamar.
* `validate='key'`: Valida en cada pulsación de tecla.
* `validatecommand=(vcmd, '%P')`: Pasa el contenido futuro del `Entry` a la función.

---

## 6. Checkboxes (Casillas de Verificación)

### Opciones Sí/No y un "Enlace" Simulado

Para opciones binarias, usamos `tk.Checkbutton` con variables `tk.BooleanVar`. También simulamos un enlace para "Términos y Condiciones".

---

### 6.1. Creando Checkboxes con `tk.BooleanVar`

```python
# Variables para controlar el estado de los checkbuttons
acepto_terminos = tk.BooleanVar()
recibir_confirmacion = tk.BooleanVar()

# Frame para agrupar checkbox y "enlace"
checkbox_terminos_frame = tk.Frame(frame_campos, bg="#212121")
checkbox_terminos_frame.pack(anchor="w", pady=(15, 0))

# Checkbox de aceptación de términos
checkbox_terminos = tk.Checkbutton(
    checkbox_terminos_frame,
    text="He leído y Acepto los ",
    variable=acepto_terminos,
    fg="white",
    bg="#212121",
    font=("Arial", 10),
    selectcolor="#212121"  # Color del recuadro marcado igual al fondo
)
checkbox_terminos.pack(side="left")
```

* `tk.BooleanVar()`: Variable True/False para el estado.
* `selectcolor` igual al fondo para solo mostrar el "tick" blanco.

---

### 6.2. Simular un Enlace y Responder a Clicks

El texto "Términos y Condiciones" es una etiqueta con evento de clic que simula un enlace.

```python
# Label simulando enlace para Términos y Condiciones
label_link_terminos = tk.Label(
    checkbox_terminos_frame,
    text="Términos y Condiciones",
    fg="#FFA500",  # Naranja
    bg="#212121",
    font=("Arial", 10, "underline"),
    cursor="hand2"  # Cursor tipo mano
)
label_link_terminos.pack(side="left")

# Función que se ejecuta al hacer clic en el "enlace"
def abrir_terminos_condiciones(event):
    messagebox.showinfo("Términos y Condiciones", "Aquí irían los términos y condiciones completos.")

# Asociar clic izquierdo a la función
label_link_terminos.bind("<Button-1>", abrir_terminos_condiciones)

# Checkbox para confirmación por correo
checkbox_confirmacion = tk.Checkbutton(
    frame_campos,
    text="Deseo recibir la confirmación de mi reserva por correo",
    variable=recibir_confirmacion,
    fg="white",
    bg="#212121",
    font=("Arial", 10),
    selectcolor="#212121"
)
checkbox_confirmacion.pack(anchor="w", pady=(5, 10))
```

* `cursor="hand2"`: Cambia el cursor al pasar por encima para indicar interacción.
* `.bind("<Button-1>", func)`: Vincula evento de clic izquierdo a una función.
* `messagebox.showinfo()`: Muestra un cuadro de diálogo informativo.

---



## 7: El Botón de Acción y Lógica del Formulario

### Procesando la Reserva y Validaciones Finales

El botón "RESERVAR" es el elemento central que dispara toda la lógica del formulario: recopilar datos, validar la información y mostrar mensajes al usuario.

### 7.1. La Función `reservar_cita()`: El Cerebro del Formulario

Esta función se ejecuta cuando el usuario hace clic en "RESERVAR". Su trabajo es:

* Obtener todos los datos ingresados.
* Validar que sean correctos y completos.
* Informar al usuario si hay errores o confirmar la reserva.

```python
def reservar_cita():
    # Obtener valores actuales de los campos y variables
    sede = sede_seleccionada.get()
    fecha = entry_fecha.get()
    hora = hora_seleccionada.get()
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    confirmar_cedula = entry_confirmar_cedula.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    acepta_terminos = acepto_terminos.get()        # True o False
    recibe_confirmacion = recibir_confirmacion.get()  # True o False

    # Validar campos obligatorios no vacíos
    if sede == "Seleccione una sede" or \
       hora == "Seleccione una hora" or \
       not fecha or not nombre or not cedula or not telefono or not correo:
        messagebox.showerror("Error de Reserva", "Por favor, complete todos los campos obligatorios.")
        return

    # Validar que las cédulas coincidan
    if cedula != confirmar_cedula:
        messagebox.showerror("Error de Reserva", "Las cédulas no coinciden.")
        return

    # Validar aceptación de términos y condiciones
    if not acepta_terminos:
        messagebox.showerror("Error de Reserva", "Debe aceptar los Términos y Condiciones.")
        return

    # Validación básica del formato de fecha (ejemplo: dd/mm/yyyy)
    try:
        import datetime
        datetime.datetime.strptime(fecha, "%d/%m/%Y")
        # Opcional: evitar fechas pasadas
        # if datetime.datetime.strptime(fecha, "%d/%m/%Y").date() < datetime.date.today():
        #     messagebox.showerror("Error de Fecha", "No puedes reservar en una fecha pasada.")
        #     return
    except ValueError:
        messagebox.showerror("Error de Fecha", "Formato de fecha incorrecto. Por favor, seleccione una fecha del calendario.")
        return

    # Si todo es válido, construir mensaje de confirmación
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
    if recibe_confirmacion:
        mensaje_confirmacion += "\nRecibirá una confirmación por correo."

    # Mostrar mensaje de éxito
    messagebox.showinfo("Reserva Confirmada", mensaje_confirmacion)

    # Opcional: Limpiar campos después de reservar
    # sede_seleccionada.set(opciones_sede[0])
    # entry_fecha.delete(0, tk.END)
    # entry_hora.delete(0, tk.END)
    # entry_nombre.delete(0, tk.END)
    # ... limpiar otros campos
```

---

### 7.2. Creando el Botón "RESERVAR"

Este botón es el disparador de toda la función anterior.

```python
boton_reservar = tk.Button(
    ventana,
    text="RESERVAR",
    command=reservar_cita,          # Al hacer clic, se ejecuta reservar_cita()
    font=("Arial", 16, "bold"),
    bg="#e60000",                   # Rojo fuerte
    fg="white",
    activebackground="#cc0000",    # Rojo oscuro al presionar
    activeforeground="white",
    relief="raised",                # Borde con efecto 3D
    bd=3
)
boton_reservar.pack(pady=30, ipadx=50, ipady=10)  # Espacio y tamaño para fácil clic
```

---

## 8: Ejecución de la Aplicación

### Dando Vida a Nuestro Formulario: El Bucle Principal

Para que la ventana de Tkinter se muestre y funcione, es necesario iniciar el bucle de eventos con `mainloop()`.

### 8.1. El Bloque `if __name__ == "__main__":`

Este bloque garantiza que el formulario se ejecute solo si este script es el programa principal, no cuando se importe como módulo.

```python
if __name__ == "__main__":
    app = crear_formulario_reserva()  # Función que crea y configura el formulario
    app.mainloop()                    # Inicia el bucle de eventos de Tkinter
```

### 8.2. ¿Qué hace `app.mainloop()`?

* Inicia un bucle infinito que está a la espera de eventos (clics, teclas, etc.).
* Mantiene la ventana abierta y receptiva.
* Procesa y dirige cada interacción del usuario al código correspondiente.

Sin esta llamada, la ventana aparecería y desaparecería inmediatamente.


