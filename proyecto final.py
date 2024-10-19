import numpy as np
from sympy import Matrix
from tkinter import Tk, Entry, Button, StringVar, messagebox, Text, Frame

class MatrixCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Multifuncional de Matrices")  # Configura el título de la ventana
        self.root.geometry("800x400")  # Establece las dimensiones de la ventana
        self.root.configure(bg='lightblue')  # Fondo celeste

        # Frame para la calculadora a la izquierda
        calc_frame = Frame(root, bg='lightblue')  # Área donde están los botones y la entrada de la matriz
        calc_frame.pack(side="left", padx=10, pady=10)  # Paquete alineado a la izquierda con márgenes reducidos

        # Campo de entrada para la matriz
        self.matrix_input = Entry(calc_frame, width=40)  # Entrada para los elementos de la matriz
        self.matrix_input.pack(pady=5)

        # Botones de operaciones con la matriz
        Button(calc_frame, text="Gauss-Jordan", command=self.gauss_jordan, width=20, height=2).pack(pady=2)
        Button(calc_frame, text="Regla de Cramer", command=self.cramer, width=20, height=2).pack(pady=2)
        Button(calc_frame, text="Multiplicación de Matrices", command=self.multiplicar, width=20, height=2).pack(pady=2)
        Button(calc_frame, text="Matriz Inversa", command=self.inversa, width=20, height=2).pack(pady=2)

        # Frame para la explicación a la derecha
        explanation_frame = Frame(root, bg='lightblue')  # Área donde se muestra la explicación del código
        explanation_frame.pack(side="right", padx=10, pady=10)

        explanation_text = Text(explanation_frame, wrap="word", width=50, height=20)
        explanation_text.pack()

        # Inserta la explicación del código
        explanation = """
Este código crea una aplicación de interfaz gráfica utilizando la biblioteca `tkinter`, que permite realizar diversas operaciones con matrices.
"""
        explanation_text.insert("1.0", explanation)
        explanation_text.config(state="disabled")  # El área de texto es de solo lectura

    def get_matrix(self):
        try:
            # Convierte los datos ingresados en una lista de números y los organiza en una matriz cuadrada
            elements = list(map(float, self.matrix_input.get().split(',')))
            n = int(len(elements) ** 0.5)  # Calcula el tamaño de la matriz asumiendo que es cuadrada
            return np.array(elements).reshape(n, n)
        except Exception as e:
            messagebox.showerror("Error", f"Error en los datos de entrada: {e}")  # Muestra un mensaje de error si los datos no son válidos
            return None

    def gauss_jordan(self):
        matrix = self.get_matrix()  # Obtiene la matriz ingresada
        if matrix is not None:
            try:
                m = Matrix(matrix)
                result = m.rref()[0]  # Aplica la reducción Gauss-Jordan
                messagebox.showinfo("Resultado", f"Matriz en forma escalonada: \n{result}")  # Muestra el resultado
            except Exception as e:
                messagebox.showerror("Error", f"Error calculando Gauss-Jordan: {e}")  # Muestra un mensaje de error

    def cramer(self):
        matrix = self.get_matrix()  # Obtiene la matriz ingresada
        if matrix is not None:
            try:
                m = Matrix(matrix)
                det = m.det()  # Calcula el determinante
                if det == 0:
                    messagebox.showerror("Error", "El sistema no tiene solución (determinante es 0)")  # Si el determinante es 0, no tiene solución
                else:
                    messagebox.showinfo("Resultado", f"Determinante: {det}")  # Muestra el determinante
            except Exception as e:
                messagebox.showerror("Error", f"Error calculando Regla de Cramer: {e}")

    def multiplicar(self):
        matrix = self.get_matrix()  # Obtiene la matriz ingresada
        if matrix is not None:
            try:
                result = np.dot(matrix, matrix)  # Realiza la multiplicación de la matriz por sí misma
                messagebox.showinfo("Resultado", f"Multiplicación de matrices: \n{result}")  # Muestra el resultado de la multiplicación
            except Exception as e:
                messagebox.showerror("Error", f"Error multiplicando matrices: {e}")

    def inversa(self):
        matrix = self.get_matrix()  # Obtiene la matriz ingresada
        if matrix is not None:
            try:
                inv_matrix = np.linalg.inv(matrix)  # Calcula la inversa de la matriz
                messagebox.showinfo("Resultado", f"Matriz Inversa: \n{inv_matrix}")  # Muestra la matriz inversa
            except np.linalg.LinAlgError:
                messagebox.showerror("Error", "La matriz no es invertible.")  # Si la matriz no es invertible
            except Exception as e:
                messagebox.showerror("Error", f"Error calculando inversa: {e}")

# Configuración de la ventana principal
root = Tk()
app = MatrixCalculator(root)  # Crea una instancia de la calculadora
root.mainloop()  # Inicia el bucle principal de la interfaz gráfica
