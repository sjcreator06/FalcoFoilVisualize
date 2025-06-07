"""
____________________________Falco Foil Analysis____________________________

This script creates an interactive GUI to run various foil analysis scripts.

                            © 2025 Falco Foil
"""

from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

foilGUI = Tk()
fig,ax = plt.subplots()

foilGUI.geometry("1200x700")
foilGUI.configure(bg = "#333333")

foilGUI.title("Falco Foil Analysis")

canvas = Canvas(
    foilGUI,
    bg = "#333333",
    height = 800,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file="GUI/Assets/back_filler.png")
image_1 = canvas.create_image(
    599.0,
    179.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file= "GUI/Assets/search_bar.png")
entry_bg_1 = canvas.create_image(
    599.5,
    123.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=5,
    bg="#FFFFFF",
    fg="#000716",
    font=("Kodchasan Regular", 20),
    highlightthickness=0
)
entry_1.place(
    x=367.0,
    y=103.0,
    width=465.0,
    height=38.0
)

image_image_2 = PhotoImage(
    file= "GUI/Assets/title.png")
image_2 = canvas.create_image(
    599.0,
    65.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file= "GUI/Assets/category_plot.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=369.0,
    y=161.0,
    width=194.0,
    height=37.57142639160156
)

button_image_2 = PhotoImage(
    file= "GUI/Assets/foil_transformation.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=636.0,
    y=161.0,
    width=194.0,
    height=37.57142639160156
)

image_image_3 = PhotoImage(
    file= "GUI/Assets/logo.png")
image_3 = canvas.create_image(
    91.0,
    85.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file= "GUI/Assets/background_1.png")
image_4 = canvas.create_image(
    438.0,
    450.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file= "GUI/Assets/background_2.png")
image_5 = canvas.create_image(
    1029.0,
    450.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file= "GUI/Assets/foils_list.png")
image_6 = canvas.create_image(
    1029.0,
    448.0,
    image=image_image_6
)

foilGUI.resizable(True, True)
foilGUI.mainloop()