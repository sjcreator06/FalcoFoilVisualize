"""
____________________________Falco Foil Analysis____________________________

This script creates an interactive GUI to run various foil analysis scripts.

                            © 2025 Falco Foil
"""

from tkinter import *
import numpy as np
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import foilTransformations as ft
import foilCurves as fc

foilGUI = Tk()

foilGUI.geometry("1200x700")
foilGUI.configure(bg = "#333333")

foilGUI.title("Falco Foil Analysis")

# Tkinter GUI Styling
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
    file="Foil_Analysis/Assets/back_filler.png")
image_1 = canvas.create_image(
    599.0,
    179.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file= "Foil_Analysis/Assets/search_bar.png")
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
    file= "Foil_Analysis/Assets/title.png")
image_2 = canvas.create_image(
    599.0,
    65.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file= "Foil_Analysis/Assets/category_plot.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: displayFoilCurves(),
    relief="flat"
)

button_1.place(
    x=369.0,
    y=161.0,
    width=194.0,
    height=37.57142639160156
)

button_image_2 = PhotoImage(
    file= "Foil_Analysis/Assets/foil_transformation.png")
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: foilUserInput(),
    relief="flat"
)
button_2.place(
    x=636.0,
    y=161.0,
    width=194.0,
    height=37.57142639160156
)

image_image_3 = PhotoImage(
    file= "Foil_Analysis/Assets/logo.png")
image_3 = canvas.create_image(
    91.0,
    85.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file= "Foil_Analysis/Assets/background_1.png")
image_4 = canvas.create_image(
    438.0,
    450.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file= "Foil_Analysis/Assets/background_2.png")
image_5 = canvas.create_image(
    1029.0,
    450.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file= "Foil_Analysis/Assets/foils_list.png")
image_6 = canvas.create_image(
    1029.0,
    448.0,
    image=image_image_6
)

# Data Anaysis and Plotting Functions from foilCurves.py
def displayFoilCurves():
    fc.foilData()
    fc.foilCurves()
    

# Search Bar Input Data 
def foilUserInput():
    searchInput = entry_1.get("1.0",END)
    print("The Search Input is: " + searchInput.strip())
    
    # Clean the Input Data
    searchInput.replace(" ","")
    inputList = searchInput.split("+")
    
    if len(inputList) == 3:
        global foilCategory, firstFoil, secondFoil
        foilCategory = inputList[0].strip()
        firstFoil = int(inputList[1].strip())
        secondFoil = int(inputList[2].strip())
        print("The Foil Category is: "+ str(foilCategory))
        print("The First Foil is: " + str(firstFoil))
        print("The Second Foil is: " + str(secondFoil))
        updatePlot()
        
    else:
        pass
    
    
# Airfoil Tranformation Animation
fig_1 = plt.Figure(figsize=(8.26, 4.62), facecolor='#fcfcfc')
ax1 = fig_1.add_subplot(111, frame_on=False)
foil, = ax1.plot([],[], lw=2, color='blue')

def foilTransform(frame):
    t = frame/100  
    
    x = (1 - t) * X1T + t * X2T
    y = (1 - t) * Y1T + t * Y2T
    
    foil.set_data(x,y)
    
    return (foil,)

# Update Plot Once Input Has Been Processed
def updatePlot():
    global X1T, X2T, Y1T, Y2T
    X1T, Y1T, X2T, Y2T = ft.GUIFoilTransform(foilCategory,firstFoil,secondFoil)
    
    ax1.plot(X1T,Y1T, color = 'g')
    ax1.plot(X2T,Y2T,color = 'r')
    
    # Function from foilTransformation.py
    def foilTransform(frame):
        t = frame/100  
    
        x = (1 - t) * X1T + t * X2T
        y = (1 - t) * Y1T + t * Y2T
    
        foil.set_data(x,y)
    
        return (foil,)
    
    # Outputing GIF and Drawing Animation Plot
    ani = animation.FuncAnimation(fig=fig_1, func = foilTransform, frames=100, interval=10)
    writergif = animation.PillowWriter(fps=30)
    ani.save('Foil Transformation.gif',writer=writergif)
    
    fig_1.canvas.draw()
    
        
def main():
    canvas = FigureCanvasTkAgg(figure = fig_1, master=foilGUI)
    canvas.draw()
    canvas.get_tk_widget().place(x=24, y=219)
    foilGUI.resizable(True, True)
    foilGUI.mainloop()
    
if __name__ == "__main__":
    main()
