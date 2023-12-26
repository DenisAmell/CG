import numpy as np
import matplotlib.pyplot as plt
from scipy.special import binom
import customtkinter


def Bernstein(n, k):
    coeff = binom(n, k)

    def _bpoly(x):
        return coeff * x ** k * (1 - x) ** (n - k)

    return _bpoly


def Bezier(points, num=200):
    N = len(points)
    t = np.linspace(0, 1, num=num)
    curve = np.zeros((num, 2))
    for ii in range(N):
        curve += np.outer(Bernstein(N - 1, ii)(t), points[ii])
    return curve


def window():
    customtkinter.set_appearance_mode("dark")

    customtkinter.set_default_color_theme("dark-blue")

    root = customtkinter.CTk()
    root.geometry("320x320")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label1 = customtkinter.CTkLabel(master=frame, text="parameter a value")
    label1.pack(pady=30, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter x pointers")
    entry1.pack(pady=10, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter y pointers")
    entry2.pack(pady=10, padx=10)

    def DoIt():
        x_1 = float(entry1.get().split()[0])
        x_2 = float(entry1.get().split()[1])
        x_3 = float(entry1.get().split()[2])
        y_1 = float(entry2.get().split()[0])
        y_2 = float(entry2.get().split()[1])
        y_3 = float(entry2.get().split()[2])

        main(x_1, x_2, x_3, y_1, y_2, y_3)

    button = customtkinter.CTkButton(master=frame, text="Do it", command=DoIt)
    button.pack(pady=10, padx=10)

    root.mainloop()


def main(x_1, x_2, x_3, y_1, y_2, y_3):
    xp = np.array([x_1, x_2, x_3])
    yp = np.array([y_1, y_2, y_3])
    x, y = Bezier(list(zip(xp, yp))).T

    plt.plot(x, y)
    plt.plot(xp, yp, "ro")
    plt.plot(xp, yp, "b--")

    plt.show()

if __name__ == "__main__":
    window()