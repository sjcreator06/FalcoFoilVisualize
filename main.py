from flask import Flask, render_template, request, jsonify, json
from airfoils import Airfoil
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tensorflow as tf
import torch

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template("index.html")

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

"""# Output Plot 1
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
plt.show()"""

# Finding Maximum Y Coordinate for Each Airfoil 
thinFoilsYMax = []
curvedFoilsYMax = []
mediumFoilsYMax = []
thickFoilsYMax = []


for foil in thinFoils:
    maxYCoord = max(y[foil])
    thinFoilsYMax.append(maxYCoord)

for foil in curvedFoils:
    maxYCoord = max(y[foil])
    curvedFoilsYMax.append(maxYCoord)

for foil in mediumFoils:
    maxYCoord = max(y[foil])
    mediumFoilsYMax.append(maxYCoord)

for foil in thickFoils:
    maxYCoord = max(y[foil])
    thickFoilsYMax.append(maxYCoord)

# Creating Dictionaries Key Value Pairs (Air Foil Index - Max Y Coordinate)
thinFoilsDict = dict(zip(thinFoils,thinFoilsYMax))
curvedFoilsDict = dict(zip(curvedFoils, curvedFoilsYMax))
mediumFoilsDict = dict(zip(mediumFoils, mediumFoilsYMax))
thickFoilsDict = dict(zip(thickFoils, thickFoilsYMax))

# Sorted Dictionaries by Max Y Coordinate Value (Air Foil Index - Max Y Coordinate) in Increasing Order
thinFoilsDictSorted = dict(sorted(thinFoilsDict.items(), key=lambda item: item[1])) # Note: .items() returns a list of tuples, sorted() sorts it by the value as key = lambda item: item[1] which means value and not key. [1] means value and [0] means key.
curvedFoilsDictSorted = dict(sorted(curvedFoilsDict.items(), key=lambda item: item[1]))
mediumFoilsDictSorted = dict(sorted(mediumFoilsDict.items(), key=lambda item: item[1]))
thickFoilsDictSorted = dict(sorted(thickFoilsDict.items(), key=lambda item: item[1]))

# Airfoil Indexes in Increasing Order of Thickness
thinFoilIndexSorted = list(thinFoilsDictSorted.keys())
curvedFoilIndexSorted = list(curvedFoilsDictSorted.keys())
mediumFoilIndexSorted = list(mediumFoilsDictSorted.keys())
thickFoilIndexSorted = list(thickFoilsDictSorted.keys())

print("Thin Foils Sorted by Thickness: ", thinFoilIndexSorted)
print("Curved Foils Sorted by Thickness: ", curvedFoilIndexSorted)
print("Medium Foils Sorted by Thickness: ", mediumFoilIndexSorted)
print("Thick Foils Sorted by Thickness: ", thickFoilIndexSorted)


x1 = [0]*len(thinFoilIndexSorted)
y1= [0]*len(thinFoilIndexSorted)
x2 = [0]*len(curvedFoilIndexSorted)
y2= [0]*len(curvedFoilIndexSorted)
x3 = [0]*len(mediumFoilIndexSorted)
y3= [0]*len(mediumFoilIndexSorted)
x4 = [0]*len(thickFoilIndexSorted)
y4= [0]*len(thickFoilIndexSorted)

i =0
for index in thinFoilIndexSorted:
    x1[i] = x[index]
    y1[i] = y[index]
    i+=1
i=0
for index in curvedFoilIndexSorted:
    x2[i] = x[index]
    y2[i] = y[index]
    i+=1
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



"""x20 = np.array(x2)
y20 = np.array(y2)

x3 = np.array(x3)
y3 = np.array(y3)

x4 = np.array(x4)
y4 = np.array(y4)"""

plt.plot(x1[0],y1[0], label="Thin Foil")
plt.plot(x3[1],y3[1], label="Curved Foil")

min_len = min(len(x1), len(x2))
x1 = x1[:min_len]
x2 = x2[:min_len]
y1 = y1[:min_len]
y2 = y2[:min_len]

x1 = np.array(x1[0])
y1 = np.array(y1[0])

x2 = np.array(x1[1])
y2 = np.array(y1[1])



def foilTransform(frame):
    t = frame/100
    
    x = (1 - t) * x1 + t * x2
    y = (1 - t) * y1 + t * y2
    
    foil.set_data(x, y)
    return (foil)

ani = animation.FuncAnimation(fig=figure, func = foilTransform, frames=100, interval=10)
writergif = animation.PillowWriter(fps=30)
ani.save('filename.gif',writer=writergif)
plt.show()
