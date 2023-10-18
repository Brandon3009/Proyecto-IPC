import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import os

class StudentWindow:
    def cerrar_student(self):
        self.root.destroy()  # Cierra la ventana de estudiante
        # Abre la ventana de inicio de sesión
        from login_window import LoginWindow
        root = tk.Tk()
        login_window = LoginWindow(root, "student")  # Proporciona los argumentos requeridos
        login_window.show()

    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.courses = []  # Lista de cursos inscritos por el estudiante
        self.notes = {}  # Diccionario para almacenar las notas del estudiante
        self.load_courses()
        self.load_notes()

    def load_courses(self):
        # Debes cargar los cursos inscritos por el estudiante aquí desde un archivo o base de datos
        # Ejemplo de cómo cargar cursos ficticios (debes adaptarlo a tus necesidades):
        self.courses = ["Curso 1", "Curso 2", "Curso 3"]

    def load_notes(self):
        # Debes cargar las notas del estudiante aquí desde un archivo o base de datos
        # Ejemplo de cómo cargar notas ficticias (debes adaptarlo a tus necesidades):
        self.notes = {"Curso 1": 90, "Curso 2": 85, "Curso 3": 98}

    def view_all_courses(self):
        # Cargar los cursos desde el archivo "cursos.txt"
        try:
            with open("cursos.txt", "r") as file:
                lines = file.readlines()
                course_list = []
                for line in lines:
                    nombre_curso, descripcion_curso, costo, horario, codigo, cupo, catedratico = line.strip().split(',')
                    course_list.append(f"Código: {codigo}, Nombre: {nombre_curso}, Costo: {costo}, Horario: {horario}, Cupo: {cupo}, Catedrático: {catedratico}")

            # Crear una nueva ventana o diálogo para mostrar la lista de cursos
            course_window = tk.Toplevel()
            course_window.title("Lista de Cursos Disponibles")

            # Crear un widget Text para mostrar la lista de cursos
            cursos_text = tk.Text(course_window, height=10, width=50)
            cursos_text.pack()

            # Mostrar los cursos en el widget Text
            for course in course_list:
                cursos_text.insert(tk.END, course + "\n")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar los cursos: {str(e)}")

    def view_notes(self):
        if not self.notes:
            messagebox.showinfo("Notas", "No hay notas cargadas.")
        else:
            # Muestra las notas del estudiante en una ventana o diálogo
            notes_window = tk.Toplevel()
            notes_window.title("Notas del Estudiante")

            notes_text = tk.Text(notes_window, height=10, width=50)
            notes_text.pack()

            for course, note in self.notes.items():
                notes_text.insert(tk.END, f"Curso: {course}, Nota: {note}\n")

    def inscribir_curso(self):
        from course_manager import CourseManager
        # Redirige a la ventana del administrador de cursos en course_manager.py
        root = tk.Tk()  # Crea una nueva instancia de Tk para la ventana del administrador de cursos
        course_manager = CourseManager(root)
        course_manager.show()  # Muestra la ventana del administrador de cursos

    def show(self):
        self.root.title(f"Ventana de Estudiante - {self.username}")
        self.root.geometry("400x400")  # Aumentar el tamaño de la ventana principal
        self.root.config(bd=10, bg="alice blue")

        # Crear un Frame en lugar de una nueva ventana
        frame = tk.Frame(self.root)
        frame.pack()

        # Agregar widgets al Frame
        courses_label = tk.Label(frame, text="Cursos Inscritos:", bg="alice blue")
        courses_label.pack()

        courses_listbox = tk.Listbox(frame)
        for course in self.courses:
            courses_listbox.insert(tk.END, course)
        courses_listbox.pack()

        view_courses_button = tk.Button(frame, text="Ver Todos los Cursos", command=self.view_all_courses, bg="alice blue")
        view_courses_button.pack()

        view_notes_button = tk.Button(frame, text="Ver Notas", command=self.view_notes, bg="alice blue")
        view_notes_button.pack()

        inscribir_button = tk.Button(frame, text="Inscribir Curso", command=self.inscribir_curso, bg="alice blue")
        inscribir_button.pack()


        # Agrega un botón de "Cerrar Sesión" en la esquina superior derecha
        boton_cerrar_sesion = ttk.Button(self.root, text="Cerrar Sesión", command=self.cerrar_student)
        boton_cerrar_sesion.place(x=300, y=10)

        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    student_window = StudentWindow(root, "Nombre del Estudiante")
    student_window.show()