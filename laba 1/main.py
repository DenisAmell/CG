import matplotlib.pyplot as plt
import numpy as np
import customtkinter


def f(x, y, a):
    return x**2/3 + y**2/3 - a**2/3

def doit(a):
    x_min, x_max = -1.5, 1.5  # исправленные пределы
    y_min, y_max = -1.5, 1.5  # исправленные пределы

    x = np.linspace(x_min, x_max, 100)
    y = np.linspace(y_min, y_max, 100)

    X, Y = np.meshgrid(x, y)

    plt.contour(X, Y, f(X, Y, a), levels=[0], colors='black')
    plt.axis('equal')
    plt.show()


def DoIt():
    value = float(entry1.get())
    doit(value)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("320x240")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label1 = customtkinter.CTkLabel(master=frame, text="parameter a value")
label1.pack(pady=30, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter parameter value")  # исправлен виджет
entry1.pack(pady=10, padx=10)

buttom = customtkinter.CTkButton(master=frame, text="Do it", command=DoIt)
buttom.pack(pady=10, padx=10)

root.mainloop()
