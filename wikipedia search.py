import tkinter as tk
from tkinter import Button, LEFT, Label
from wikipedia import set_lang, summary


def getWeather(canvas):
    global set_lang
    global summary
    city = textField.get()
    set_lang("en")
    a = summary(city)
    label1.config(text=a)


canvas = tk.Tk()
canvas.geometry("1800x900")
canvas.title("luya Wiki App")
f = ("poppins", 15, "bold")
t = ("poppins", 12, "bold")
textField = tk.Entry(canvas, justify="center", width=None, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind("<Return>", getWeather)
label1 = tk.Label(canvas, wraplength=1200, justify=LEFT, font=t)
label1.pack()
Button(canvas, text="exit", command=canvas.destroy).pack()

canvas.mainloop()
