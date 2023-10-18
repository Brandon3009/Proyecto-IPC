import tkinter as tk
import hashlib
from tkinter import messagebox
from tkcalendar import Calendar

class LoginWindow:
    def __init__(self, root, user_type):
        self.root = root
        self.user_type = user_type

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Inicio de Sesión")
ventana_principal.geometry("300x250")
ventana_principal.resizable(0, 0)
ventana_principal.config(bd=10, bg="lightblue")  # Cambia el color de fondo a lightblue

# Campos de entrada para el nombre de usuario y contraseña
label_usuario = tk.Label(ventana_principal, text="Nombre de Usuario:", bg="lightblue")  # Cambia el fondo a lightblue
label_usuario.pack(padx=10, pady=5)
entry_usuario = tk.Entry(ventana_principal)
entry_usuario.pack(padx=10, pady=5)

label_contraseña = tk.Label(ventana_principal, text="Contraseña:", bg="lightblue")  # Cambia el fondo a lightblue
label_contraseña.pack(padx=10, pady=5)
entry_contraseña = tk.Entry(ventana_principal, show="*")
entry_contraseña.pack(padx=10, pady=5)

entry_fecha_nacimiento = None  # Variable para el campo de fecha de nacimiento

def guardar_fecha(fecha):
    entry_fecha_nacimiento.delete(0, tk.END)
    entry_fecha_nacimiento.insert(0, fecha)
    ventana_calendario.destroy()

# Funciones para abrir las ventanas de inicio de sesión
def verificar_contraseña(contraseña, contraseña_encriptada):
    # Verificar la contraseña encriptada
    hasher = hashlib.sha256()
    hasher.update(contraseña.encode())
    return hasher.hexdigest() == contraseña_encriptada

# Funciones para abrir las ventanas relacionadas con el tipo de usuario
def abrir_ventana_estudiante(nombre):
    ventana_estudiante = tk.Toplevel(ventana_principal)
    ventana_estudiante.title("Ventana de Estudiante")
    label_bienvenida = tk.Label(ventana_estudiante, text=f"¡Bienvenido, Estudiante - {nombre}!")
    label_bienvenida.pack(padx=10, pady=10)
    ventana_principal.withdraw()
    from student_window import StudentWindow
    # Crear una instancia de StudentWindow
    student_window = StudentWindow(ventana_estudiante, nombre)
    student_window.show()  # Oculta la ventana de inicio
    

def abrir_ventana_profesor(nombre):
    ventana_profesor = tk.Toplevel(ventana_principal)
    ventana_profesor.title("Ventana de Profesor")
    ventana_profesor.geometry("400x200")
    label_bienvenida = tk.Label(ventana_profesor, text=f"¡Bienvenido, Profesor- {nombre}!")
    label_bienvenida.pack(padx=10, pady=10)
    ventana_principal.withdraw()

def abrir_ventana_admin():
    ventana_admin = tk.Toplevel(ventana_principal)
    ventana_admin.title("Ventana de Administrador")
    ventana_admin.geometry("600x400")
    from admin_window import AdminWindow
    # Crea la instancia de AdminWindow
    admin_window = AdminWindow(ventana_admin)
    ventana_principal.withdraw()

# Declarar cal, ventana_registro y ventana_calendario a nivel de ventana principal
cal = None
ventana_registro = None
ventana_calendario = None

# Función para abrir la ventana de registro
def abrir_ventana_registro():
    global entry_fecha_nacimiento, ventana_registro
    ventana_registro = tk.Toplevel(ventana_principal)
    ventana_registro.title("Registro de Usuario")
    ventana_registro.geometry("500x750")
    ventana_registro.resizable(0, 0)
    ventana_registro.config(bd=10, bg="lightgreen")

    # Etiquetas y campos de entrada
    label_cui = tk.Label(ventana_registro, text="CUI:", bg="lightgreen")
    label_cui.pack(padx=10, pady=5)
    entry_cui = tk.Entry(ventana_registro)
    entry_cui.pack(padx=10, pady=5)

    label_nombre = tk.Label(ventana_registro, text="Nombre:",bg="lightgreen")
    label_nombre.pack(padx=10, pady=5)
    entry_nombre = tk.Entry(ventana_registro)
    entry_nombre.pack(padx=10, pady=5)

    label_apellido = tk.Label(ventana_registro, text="Apellido:",bg="lightgreen")
    label_apellido.pack(padx=10, pady=5)
    entry_apellido = tk.Entry(ventana_registro)
    entry_apellido.pack(padx=10, pady=5)

    label_usuario = tk.Label(ventana_registro, text="Nombre de Usuario:",bg="lightgreen")
    label_usuario.pack(padx=10, pady=5)
    entry_usuario = tk.Entry(ventana_registro)
    entry_usuario.pack(padx=10, pady=5)

    label_genero = tk.Label(ventana_registro, text="Género:",bg="lightgreen")
    label_genero.pack(padx=10, pady=5)
    var_genero = tk.StringVar()
    var_genero.set("Masculino")
    radio_masculino = tk.Radiobutton(ventana_registro, text="Masculino", variable=var_genero, value="Masculino",bg="lightgreen")
    radio_femenino = tk.Radiobutton(ventana_registro, text="Femenino", variable=var_genero, value="Femenino",bg="lightgreen")
    radio_masculino.pack(padx=10, pady=5)
    radio_femenino.pack(padx=10, pady=5)

    label_edad = tk.Label(ventana_registro, text="Edad:",bg="lightgreen")
    label_edad.pack(padx=10, pady=5)
    entry_edad = tk.Entry(ventana_registro)
    entry_edad.pack(padx=10, pady=5)

    label_fecha_nacimiento = tk.Label(ventana_registro, text="Fecha de Nacimiento:",bg="lightgreen")
    label_fecha_nacimiento.pack(padx=10, pady=5)
    entry_fecha_nacimiento = tk.Entry(ventana_registro)
    entry_fecha_nacimiento.pack(padx=10, pady=5)
    boton_calendario = tk.Button(ventana_registro, text="Calendario", command=abrir_calendario,bg="lightblue")
    boton_calendario.pack(padx=10, pady=5)

    label_email = tk.Label(ventana_registro, text="Correo Electrónico:",bg="lightgreen")
    label_email.pack(padx=10, pady=5)
    entry_email = tk.Entry(ventana_registro)
    entry_email.pack(padx=10, pady=5)

    label_contraseña = tk.Label(ventana_registro, text="Contraseña:",bg="lightgreen")
    label_contraseña.pack(padx=10, pady=5)
    entry_contraseña = tk.Entry(ventana_registro, show="*")
    entry_contraseña.pack(padx=10, pady=5)

    label_rep_contraseña = tk.Label(ventana_registro, text="Repetir Contraseña:",bg="lightgreen")
    label_rep_contraseña.pack(padx=10, pady=5)
    entry_rep_contraseña = tk.Entry(ventana_registro, show="*")
    entry_rep_contraseña.pack(padx=10, pady=5)

    var_tipo_usuario = tk.StringVar()
    var_tipo_usuario.set("Estudiante")

    # Función para guardar los datos del nuevo usuario
    def guardar_usuario():
        cui = entry_cui.get()
        nombre = entry_nombre.get()
        apellido = entry_apellido.get()
        usuario = entry_usuario.get()
        genero = var_genero.get()
        edad = entry_edad.get()
        fecha_nacimiento = entry_fecha_nacimiento.get()
        email = entry_email.get()
        contraseña = entry_contraseña.get()
        rep_contraseña = entry_rep_contraseña.get()
        tipo_usuario = var_tipo_usuario.get()  # Esto ya es "Estudiante"

        # Verificar si alguno de los campos obligatorios está vacío
        if not cui or not nombre or not apellido or not usuario or not contraseña:
            messagebox.showerror("Error", "Por favor, complete todos los campos obligatorios.")
            return

        # Verificar si las contraseñas coinciden
        if contraseña != rep_contraseña:
            messagebox.showerror("Error", "Las contraseñas no coinciden. Por favor, inténtelo nuevamente.")
            return

        # Encriptar la contraseña usando SHA-256
        hasher = hashlib.sha256()
        hasher.update(contraseña.encode())
        contraseña_encriptada = hasher.hexdigest()

        # Leer usuarios del archivo "usuarios.txt" y verificar la existencia del usuario
        with open("usuarios.txt", "r") as file:
            usuarios = file.read().splitlines()

        for user in usuarios:
            parts = user.split(':')
            if len(parts) >= 4:
                cui_guardado, nombre_usuario_guardado, bloqueado = parts[0], parts[3], "bloqueado" in parts[-1]
                if usuario == nombre_usuario_guardado or cui == cui_guardado:
                    if bloqueado:
                        messagebox.showerror("Usuario Bloqueado", f"El usuario '{usuario}' está bloqueado.")
                    else:
                        messagebox.showerror("Error", "El CUI o el nombre de usuario ya existen. Por favor, elija otro.")
                    return

        # Guardar el nuevo usuario en el archivo usuarios.txt
        with open("usuarios.txt", "a") as file:
            file.write(f"{cui}:{nombre}:{apellido}:{usuario}:{genero}:{edad}:{fecha_nacimiento}:{email}:{contraseña_encriptada}:{tipo_usuario}\n")

        messagebox.showinfo("Registro Exitoso", "El usuario se registró con éxito.")
        ventana_registro.destroy()

    # Botón para registrar el nuevo usuario
    boton_registrar = tk.Button(ventana_registro, text="Registrar", command=guardar_usuario)
    boton_registrar.pack(padx=10, pady=10)

# Función para abrir el calendario
def abrir_calendario():
    global ventana_calendario, cal
    ventana_calendario = tk.Toplevel(ventana_registro)
    ventana_calendario.title("Calendario")
    ventana_calendario.configure(bg="lightgreen")
    cal = Calendar(ventana_calendario, date_pattern="yyyy-mm-dd")
    cal.pack(padx=10, pady=10)
    boton_seleccionar_fecha = tk.Button(ventana_calendario, text="Seleccionar Fecha", command=seleccionar_fecha)
    boton_seleccionar_fecha.pack(padx=10, pady=10)

# Función para seleccionar la fecha del calendario
def seleccionar_fecha():
    global ventana_calendario, entry_fecha_nacimiento
    fecha_seleccionada = cal.get_date()
    entry_fecha_nacimiento.delete(0, "end")
    entry_fecha_nacimiento.insert(0, fecha_seleccionada)
    ventana_calendario.destroy()

# Botón para registrarse
boton_registro = tk.Button(ventana_principal, text="Registrarse", command=abrir_ventana_registro)
boton_registro.pack(padx=10, pady=10)

# Función para iniciar sesión
def iniciar_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()

    if not usuario or not contraseña:
        messagebox.showerror("Error", "Por favor, complete los campos de usuario y contraseña.")
        return

    # Comprobar si el usuario es el administrador predeterminado
    if usuario == "admin" and contraseña == "admin2468":
        abrir_ventana_admin()  # Abre la ventana del administrador
        messagebox.showinfo("Inicio de Sesión Exitoso", f"Bienvenido, {usuario} (Administrador).")
        return

    # Leer usuarios del archivo "usuarios.txt" y verificar la existencia del usuario
    with open("usuarios.txt", "r") as file:
        usuarios = file.read().splitlines()

    for user in usuarios:
        parts = user.split(':')
        if len(parts) >= 4:
            cui, nombre, apellido, nombre_usuario, _, _, _, _, contraseña_encriptada, tipo_usuario = parts
            if usuario == nombre_usuario and verificar_contraseña(contraseña, contraseña_encriptada):
                if "bloqueado" in parts[-1]:
                    messagebox.showerror("Usuario Bloqueado", f"El usuario '{usuario}' está bloqueado.")
                else:
                    if tipo_usuario == "Estudiante":
                        abrir_ventana_estudiante(nombre)
                    elif tipo_usuario == "Profesor":
                        abrir_ventana_profesor(nombre)
                    messagebox.showinfo("Inicio de Sesión Exitoso", f"Bienvenido, {usuario} ({tipo_usuario}).")
                return

    messagebox.showerror("Error", "Usuario o contraseña incorrectos. Por favor, inténtelo nuevamente.")

# Botón para iniciar sesión
boton_iniciar_sesion = tk.Button(ventana_principal, text="Iniciar Sesión", command=iniciar_sesion)
boton_iniciar_sesion.pack(padx=10, pady=10)

# Iniciar el bucle principal
ventana_principal.mainloop()

