from airfoils import Airfoil
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import torch

# NACA 4-Digit Airfoil Coordinates
i = 0
data = []
foilNames = []
x = []
y = []

# Creating Data Array from CSV File
dataFile = open("Foils/airfoil_data.csv", "r")
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
foilNamesFile = open("Foils/NACA_4-Digit_Foil_Names.txt", "r")

for foil in foilNamesFile:
    foilNames.append(foil)


# Airfoil Indicies (Follows the order of NACA_4-Digit_Foil_Names.txt)
thinFoils = [0,5,6,7,13,14,16,17,18,19]
curvedFoils = [4,29,24,25,26,27,28]
mediumFoils = [1,2,3,8,9,15,20,21]
thickFoils = [10,11,12,22,23]

# Output Plot 1
fig, axs = plt.subplots(1,2)
fig.suptitle("Plot of NACA 4-Digit Airfoil Coordinates")

# Airfoil Thin Foils Subplot 
for i in thinFoils:
    axs[0].plot(x[i],y[i], label=str(foilNames[i]))

# Airfoil Curved Foils Subplot 
for i in curvedFoils:
    axs[1].plot(x[i],y[i], label=str(foilNames[i]))

axs[0].legend(fontsize='small')
axs[1].legend(fontsize='small')
axs[0].set_title("Thin Foils")
axs[1].set_title("Curved Foils")

# Output 2
fig, axs = plt.subplots(1,2)
fig.suptitle("Plot of NACA 4-Digit Airfoil Coordinates")

# Airfoil Medium Foils Subplot 
for i in mediumFoils:
    axs[0].plot(x[i],y[i], label=str(foilNames[i]))

   
# Airfoil Thick Foils Subplot 
for i in thickFoils:
    axs[1].plot(x[i],y[i], label=str(foilNames[i]))


axs[0].legend(fontsize='small')
axs[1].legend(fontsize='small')
axs[0].set_title("Medium Foils")
axs[1].set_title("Thick Foils")
plt.show()