"""
____________________________Falco Foil Analysis____________________________

This script creates an interactive GUI to run various foil analysis scripts.

                            © 2025 Falco Foil
"""

from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import foilTransformation as ft

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
    file="Foil_Analysis/GUI/Assets/back_filler.png")
image_1 = canvas.create_image(
    599.0,
    179.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file= "Foil_Analysis/GUI/Assets/search_bar.png")
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
    file= "Foil_Analysis/GUI/Assets/title.png")
image_2 = canvas.create_image(
    599.0,
    65.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file= "Foil_Analysis/GUI/Assets/category_plot.png")
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
    file= "Foil_Analysis/GUI/Assets/foil_transformation.png")
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
    file= "Foil_Analysis/GUI/Assets/logo.png")
image_3 = canvas.create_image(
    91.0,
    85.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file= "Foil_Analysis/GUI/Assets/background_1.png")
image_4 = canvas.create_image(
    438.0,
    450.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file= "Foil_Analysis/GUI/Assets/background_2.png")
image_5 = canvas.create_image(
    1029.0,
    450.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file= "Foil_Analysis/GUI/Assets/foils_list.png")
image_6 = canvas.create_image(
    1029.0,
    448.0,
    image=image_image_6
)

def foilUserInput():
    searchInput = entry_1.get("1.0",END)
    print("The Search Input is: " + searchInput.strip())
    
    # Clean the Input Data
    searchInput.replace(" ","")
    inputList = searchInput.split("+")
    
    if len(inputList) == 3:
        global foilCategory, firstFoil, secondFoil
        foilCategory = inputList[0].strip()
        firstFoil = inputList[1].strip()
        secondFoil = inputList[2].strip()
        print("The Foil Category is: "+ foilCategory)
        print("The First Foil is: " + firstFoil)
        print("The Second Foil is: " + secondFoil)
    else:
        pass
    

# NACA 4-Digit Airfoil Coordinates
i = 0
data = []
foilNames = []
x = []
y = []

# Creating Data Array from CSV File
dataFile = open("Foil_Data/airfoil_data_equalized.csv", "r")
for line in dataFile:
    data.append(line.strip())

# Creating X and Y Coordinate String Arrays
for line in range(len(data)):
    if i % 2 == 0:
        x.append(data[i].split(","))
    else:
        y.append(data[i].split(","))
    
    i += 1
    
# Converting String Arrays to Float Arrays
for i in range(len(x)):
    for j in range(len(x[i])):
        x[i][j] = float(x[i][j])
        y[i][j] = float(y[i][j])

# Creating an Array of Airfoil Names
foilNamesFile = open("Foil_Data/NACA_4-Digit_Foil_Names.txt", "r")

for foil in foilNamesFile:
    foilNames.append(foil)


# Airfoil Indicies (Follows the order of NACA_4-Digit_Foil_Names.txt)
mediumFoils = [1,2,3,8,9,15,20,21]
thickFoils = [10,11,12,22,23]

# Finding Maximum Y Coordinate for Each Airfoil 
mediumFoilsYMax = []
thickFoilsYMax = []

for foil in mediumFoils:
    maxYCoord = max(y[foil])
    mediumFoilsYMax.append(maxYCoord)

for foil in thickFoils:
    maxYCoord = max(y[foil])
    thickFoilsYMax.append(maxYCoord)

# Creating Dictionaries Key Value Pairs (Air Foil Index - Max Y Coordinate)
mediumFoilsDict = dict(zip(mediumFoils, mediumFoilsYMax))
thickFoilsDict = dict(zip(thickFoils, thickFoilsYMax))

# Sorted Dictionaries by Max Y Coordinate Value (Air Foil Index - Max Y Coordinate) in Increasing Order
mediumFoilsDictSorted = dict(sorted(mediumFoilsDict.items(), key=lambda item: item[1]))
thickFoilsDictSorted = dict(sorted(thickFoilsDict.items(), key=lambda item: item[1]))

# Airfoil Indexes in Increasing Order of Thickness
mediumFoilIndexSorted = list(mediumFoilsDictSorted.keys())
thickFoilIndexSorted = list(thickFoilsDictSorted.keys())

# print("Medium Foils Sorted by Thickness: ", mediumFoilIndexSorted)
# print("Thick Foils Sorted by Thickness: ", thickFoilIndexSorted)

# Pre-Allocating Arrays
x3 = [0]*len(mediumFoilIndexSorted)
y3= [0]*len(mediumFoilIndexSorted)
x4 = [0]*len(thickFoilIndexSorted)
y4= [0]*len(thickFoilIndexSorted)

# Sorting X and Y Arrays
i=0
for index in mediumFoilIndexSorted:
    x3[i] = x[index]
    y3[i] = y[index]
    i+=1

i=0
for index in thickFoilIndexSorted:
    x4[i] = x[index]
    y4[i] = y[index]
    i+=1
    
# Airfoil Tranformation Animation
fig_1 = plt.Figure(figsize=(8.26, 4.62), facecolor='#fcfcfc')
ax1 = fig_1.add_subplot(111, frame_on=False)
foil, = ax1.plot([],[], lw=2, color='blue')
ax1.set_xlim(-0.1, 1.1)
ax1.set_ylim(-0.25, 0.25)


def GUIFoilTransform():
 
        """# Plotting Reference Plots
        plt.plot(x3[1],y3[1])
        plt.plot(x3[4],y3[4])
    
        # Creating NP Arrays for Transformation
        global X1T, Y1T, X2T, Y2T  
        
        X1T = np.array(x3[1])
        Y1T = np.array(y3[1])
        X2T = np.array(x3[4])
        Y2T = np.array(y3[4])"""
    
        # Plotting Reference Plots
        plt.plot(x4[1],y4[1])
        plt.plot(x4[4],y4[4])
    
        # Creating NP Arrays for Transformation
        global X1T, Y1T, X2T, Y2T 
        X1T = np.array(x4[1])
        Y1T = np.array(y4[1])
        X2T = np.array(x4[4])
        Y2T = np.array(y4[4])
        
    

    
def foilTransform(frame):
    t = frame/100  
    
    x = (1 - t) * X1T + t * X2T
    y = (1 - t) * Y1T + t * Y2T
    
    foil.set_data(x,y)
    
    return (foil)

        
def main():
    GUIFoilTransform()

    canvas = FigureCanvasTkAgg(figure = fig_1, master=foilGUI)
    canvas.draw()
    canvas.get_tk_widget().place(x=24, y=219)
    
    ani = animation.FuncAnimation(fig=fig_1, func = foilTransform, frames=100, interval=10)
    writergif = animation.PillowWriter(fps=30)
    ani.save('Foil Transformation.gif',writer=writergif)
    
    ax1.plot(x4[1],y4[1])
    ax1.plot(x4[4],y4[4])
    
    foilGUI.resizable(True, True)
    foilGUI.mainloop()
    
    
if __name__ == "__main__":
    main()
