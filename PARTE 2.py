import tkinter as tk
from tkinter import messagebox
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio ** 2
        return area

    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

    def calcular_perimetro(self):
        perimetro = 2 * self.base + 2 * self.altura
        return perimetro

class Cuadrado:
    def __init__(self, longitud):
        self.longitud = longitud

    def calcular_area(self):
        area = self.longitud ** 2
        return area

    def calcular_perimetro(self):
        perimetro = self.longitud * 4
        return perimetro

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area

    def calcular_hipotenusa(self):
        hipotenusa = math.sqrt((self.base) ** 2 + (self.altura) ** 2)
        return hipotenusa

    def calcular_perimetro(self):
        perimetro = self.base + self.altura + self.calcular_hipotenusa()
        return perimetro

    def calcular_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura and self.altura == hipotenusa:
            return "equilátero"
        elif self.base == self.altura or self.altura == hipotenusa or self.base == hipotenusa:
            return "isósceles"
        else:
            return "escaleno"

def calcular():
    figura = figura_var.get()
    if figura == "Círculo":
        radio = float(entry1.get())
        circulo = Circulo(radio)
        area = circulo.calcular_area()
        perimetro = circulo.calcular_perimetro()
        messagebox.showinfo("Resultados", f"El área del círculo es: {area}\nEl perímetro del círculo es: {perimetro}")

    elif figura == "Rectángulo":
        base = float(entry1.get())
        altura = float(entry2.get())
        rectangulo = Rectangulo(base, altura)
        area = rectangulo.calcular_area()
        perimetro = rectangulo.calcular_perimetro()
        messagebox.showinfo("Resultados", f"El área del rectángulo es: {area}\nEl perímetro del rectángulo es: {perimetro}")

    elif figura == "Cuadrado":
        longitud = float(entry1.get())
        cuadrado = Cuadrado(longitud)
        area = cuadrado.calcular_area()
        perimetro = cuadrado.calcular_perimetro()
        messagebox.showinfo("Resultados", f"El área del cuadrado es: {area}\nEl perímetro del cuadrado es: {perimetro}")

    elif figura == "Triángulo rectángulo":
        base = float(entry1.get())
        altura = float(entry2.get())
        triangulo = TrianguloRectangulo(base, altura)
        area = triangulo.calcular_area()
        perimetro = triangulo.calcular_perimetro()
        tipo = triangulo.calcular_tipo_triangulo()
        messagebox.showinfo("Resultados", f"El área del triángulo rectángulo es: {area}\nEl perímetro del triángulo rectángulo es: {perimetro}\nEs un triángulo: {tipo}")

def actualizar_campos(*args):
    figura = figura_var.get()
    if figura == "Círculo":
        label1.config(text="Radio:")
        label2.config(text="")
        entry2.grid_remove()
    elif figura == "Rectángulo" or figura == "Triángulo rectángulo":
        label1.config(text="Base:")
        label2.config(text="Altura:")
        entry2.grid()
    elif figura == "Cuadrado":
        label1.config(text="Longitud:")
        label2.config(text="")
        entry2.grid_remove()

root = tk.Tk()
root.title("Clases sobre figuras geométricas")

figura_var = tk.StringVar(value="Círculo")
figura_var.trace("w", actualizar_campos)

figura_label = tk.Label(root, text="Seleccione la figura:")
figura_label.grid(row=0, column=0, padx=10, pady=10)

figura_option = tk.OptionMenu(root, figura_var, "Círculo", "Rectángulo", "Cuadrado", "Triángulo rectángulo")
figura_option.grid(row=0, column=1, padx=10, pady=10)

label1 = tk.Label(root, text="Radio:")
label1.grid(row=1, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=1, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="")
label2.grid(row=2, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, padx=10, pady=10)

calcular_button = tk.Button(root, text="Calcular", command=calcular)
calcular_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
