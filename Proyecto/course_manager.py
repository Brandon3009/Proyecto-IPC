import tkinter as tk
from tkinter import messagebox
from tkinter import Listbox

class Course:
    def __init__(self, nombre_curso, costo, horario, codigo, cupo, catedratico):
        self.nombre_curso = nombre_curso
        self.costo = costo
        self.horario = horario
        self.codigo = codigo
        self.cupo = cupo
        self.catedratico = catedratico
        self.estudiantes = []  # Lista de estudiantes inscritos
        self.pagos = {}  # Diccionario para rastrear los pagos de los estudiantes

    def inscribir_estudiante(self, estudiante):
        if len(self.estudiantes) < self.cupo:
            self.estudiantes.append(estudiante)
            self.pagos[estudiante.username] = False  # Inicialmente, el estudiante no ha pagado
            return True
        else:
            return False

class Student:
    def __init__(self, username):
        self.username = username
        self.inscrito_cursos = []

    def inscribir_curso(self, codigo_curso):
        self.inscrito_cursos.append(codigo_curso)

    def verificar_inscripcion(self, codigo_curso):
        return codigo_curso in self.inscrito_cursos

    def pagar_curso(self, codigo_curso, monto):
        if codigo_curso in self.inscrito_cursos:
            curso = course_manager.cursos[codigo_curso]
            if monto == curso.costo:
                curso.pagos[self.username] = True
                guardar_informacion_estudiantes(course_manager)
                return True
        return False

class CourseManager:
    def __init__(self):
        self.cursos = {}  # Un diccionario donde la clave es el código del curso y el valor es la instancia del curso
    
    def crear_curso(self, nombre_curso, descripcion_curso, costo, horario, codigo, cupo, catedratico):
        if codigo not in self.cursos:
            curso = Course(nombre_curso, descripcion_curso, costo, horario, codigo, cupo, catedratico)
            self.cursos[codigo] = curso
            return curso
    
    def listar_cursos(self):
        return self.cursos.values()

    def inscribir_estudiante(self, codigo_curso, estudiante):
        if codigo_curso in self.cursos:
            curso = self.cursos[codigo_curso]
            return curso.inscribir_estudiante(estudiante)
        else:
            return False

def guardar_informacion_estudiantes(course_manager):
    with open("estudiantes.txt", "w") as file:
        for codigo_curso, curso in course_manager.cursos.items():
            for estudiante in curso.estudiantes:
                file.write(f"{estudiante.username},{codigo_curso},{curso.pagos[estudiante.username]}\n")

def cargar_informacion_estudiantes(course_manager):
    try:
        with open("estudiantes.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                username, codigo_curso, pagado = line.strip().split(',')
                if codigo_curso in course_manager.cursos:
                    curso_manager = course_manager.cursos[codigo_curso]
                    curso_manager.estudiantes.append(Student(username))
                    curso_manager.pagos[username] = (pagado == "True")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron cargar los estudiantes: {str(e)}")

def cargar_cursos_desde_archivo(course_manager):
    try:
        with open("cursos.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                nombre_curso, costo, horario, codigo, cupo, catedratico = line.strip().split(',')
                course_manager.crear_curso(nombre_curso, costo, horario, codigo, cupo, catedratico)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron cargar los cursos: {str(e)}")

# Crear instancias de CourseManager y cargar cursos desde el archivo
course_manager = CourseManager()
cargar_informacion_estudiantes(course_manager)
cargar_cursos_desde_archivo(course_manager)

# Interfaz de estudiante
root = tk.Tk()
root.title("Ventana de Estudiante")
root.geometry("500x400")
root.config(bd=10, bg="lavender")

# Agregar una Listbox para mostrar los cursos
cursos_listbox = Listbox(root)
cursos_listbox.pack()

# Cargar la lista de cursos en la Listbox
for curso in course_manager.listar_cursos():
    cursos_listbox.insert(tk.END, f"Código: {curso.codigo}, Nombre: {curso.nombre_curso}")

# Agregar un Entry para el código del curso
label_codigo_curso = tk.Label(root, text="Código del Curso:", bg="lavender")
label_codigo_curso.pack()

entry_codigo_curso = tk.Entry(root)
entry_codigo_curso.pack()

# Definir la función inscribir_curso
def inscribir_curso():
    codigo_curso = entry_codigo_curso.get()
    if course_manager.inscribir_estudiante(codigo_curso, student):
        guardar_informacion_estudiantes(course_manager)  # Guarda la información del estudiante inscrito
        messagebox.showinfo("Mensaje", "Inscripción exitosa en el curso.")
    else:
        messagebox.showinfo("Error", "No se pudo inscribir en el curso.")

button_inscribir_curso = tk.Button(root, text="Inscribir en el Curso", command=inscribir_curso)
button_inscribir_curso.pack()

def pagar_curso():
    codigo_curso = entry_codigo_curso.get()
    curso = course_manager.cursos.get(codigo_curso)
    if not curso:
        messagebox.showinfo("Error", "El curso no existe.")
        return

    if student.pagar_curso(codigo_curso, curso.costo):
        guardar_informacion_estudiantes(course_manager)  # Actualiza la información del pago
        messagebox.showinfo("Pago Exitoso", "El curso ha sido pagado con éxito.")
    else:
        messagebox.showinfo("Error de Pago", "El monto del pago no coincide con el costo del curso o no estás inscrito.")

button_pagar_curso = tk.Button(root, text="Pagar Curso", command=pagar_curso)
button_pagar_curso.pack()

def mostrar_ventana_curso_seleccionado(codigo_curso):
    if codigo_curso in course_manager.cursos:
        curso = course_manager.cursos[codigo_curso]
        if student.username in curso.pagos and curso.pagos[student.username]:
            messagebox.showinfo("Información del Curso",
                                f"Nombre del Curso: {curso.nombre_curso}\n"
                                f"Costo: {curso.costo}\n"
                                f"Horario: {curso.horario}\n"
                                f"Código del Curso: {curso.codigo}\n"
                                f"Cupo Disponible: {curso.cupo}\n"
                                f"Catedrático: {curso.catedratico}")
        else:
            messagebox.showinfo("Información del Curso",
                                "Debes pagar el curso para ver la información detallada.")

button_mostrar_curso = tk.Button(root, text="Mostrar Curso Seleccionado",
                                 command=lambda: mostrar_ventana_curso_seleccionado(entry_codigo_curso.get()))
button_mostrar_curso.pack()

root.mainloop()
