"""
____________________________________Falco Foil Analysis____________________________________

This script creates an animation that transforms one foil into another in the same category. 

The user inputs two NACA foil names. The script will then display a plot and output a GIF.

Target Foil Categories: Medium and Thick Foils

                                      © 2025 Falco Foil
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.interpolate import CubicSpline

# NACA 4-Digit Airfoil Coordinates
i = 0
data = []
foilNames = []
x = []
y = []

# Creating Data Array from CSV File
dataFile = open("Foil Data/airfoil_data_equalized.csv", "r")
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
foilNamesFile = open("Foil Data/NACA_4-Digit_Foil_Names.txt", "r")

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
figure, axis = plt.subplots()
foil, = axis.plot([], [], lw=2, color='blue')
axis.set_xlim(-0.1, 1.1)
axis.set_ylim(-0.25, 0.25)


# User Input for Foil Transformation
print("___________Falco Foil Transformation Animation___________ \n")

print("Medium Foils")
for i in mediumFoilIndexSorted:
    print(str(mediumFoilIndexSorted.index(i))+ ": " + str(foilNames[i]))

print("Thick Foils")
for i in thickFoilIndexSorted:
    print(str(thickFoilIndexSorted.index(i))+ ": " + str(foilNames[i]))

foilCategory = input("Please enter the foil category you would like to transform (Medium or Thick): ")


if foilCategory.lower() == "medium":
    firstFoil = int(input("Please enter the corresponding index for your first foil: "))
    secondFoil = int(input("Please enter the corresponding index for your second foil: "))
    
    # Plotting Reference Plots
    plt.plot(x3[firstFoil],y3[firstFoil])
    plt.plot(x3[secondFoil],y3[secondFoil])
    
    # Creating NP Arrays for Transformation
    X1T = np.array(x3[firstFoil])
    Y1T = np.array(y3[firstFoil])
    X2T = np.array(x3[secondFoil])
    Y2T = np.array(y3[secondFoil])
    
    
elif foilCategory.lower() == "thick":
    firstFoil = int(input("Please enter the corresponding index for your first foil: "))
    secondFoil = int(input("Please enter the corresponding index for your second foil: "))
    
    # Plotting Reference Plots
    plt.plot(x4[firstFoil],y4[firstFoil])
    plt.plot(x4[secondFoil],y4[secondFoil])
    
    # Creating NP Arrays for Transformation
    X1T = np.array(x4[firstFoil])
    Y1T = np.array(y4[firstFoil])
    X2T = np.array(x4[secondFoil])
    Y2T = np.array(y4[secondFoil])
    
else:
    print("Invalid foil category. Please enter either 'Medium' or 'Thick'.")
    
def foilTransform(frame):
    t = frame/100  # Linear Interpolation Factor of 1 as Frames = 100 
    
    x = (1 - t) * X1T + t * X2T
    y = (1 - t) * Y1T + t * Y2T
    
    foil.set_data(x, y)
    return (foil)

ani = animation.FuncAnimation(fig=figure, func = foilTransform, frames=100, interval=10)

# Saves the Transformation Animation as a GIF
writergif = animation.PillowWriter(fps=30)
ani.save('Foil Transformation.gif',writer=writergif)

plt.show()
