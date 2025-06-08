<p align="center">
  <img width="250" src="https://github.com/user-attachments/assets/9c95b7ae-0d6a-4402-862a-7ce00865c143" alt="Falco Foil" />
</p>
<h2 align="center"> Metamorphic Airfoil Analysis </h2>

<p align="center">
Python-based Interactive GUI that plots Airfoils and runs CFD Simulations
</p>

<p align="center">
Libraries Used: Matplotlib, Scipy, Numpy, and Tkinter 
</p>


## Installation
```bash
git clone https://github.com/sjcreator06/FalcoFoil.git
```

### | About Falco Foil
This library aims to visualize the transformation movement of a metamorphic airfoil. A metamorphic airfoil is an airfoil that can change its shape. The library uses NACA 4-digit foils aquired from [Airfoil Tools]([url](http://airfoiltools.com/search/index?m%5Bgrp%5D=naca4d&m%5Bsort%5D=1)). The library can also be easily adapted to add more foils from different foil categories. 

Four categories of airfoils can be identified in the NACA 4-Digit airfoil group: thin, curved, medium, and thick foils. The primary focus of this library is on medium and thick foils. This is because the library is used as part of a larger research project to develop a metamorphic wing that has the properties of a medium and thick airfoil. 

In future releases, Computational Fluid Dynamics will be integrated to perform fluid analysis on metamorphic foils as they change shape and more complex transformations like thin and curved airfoils. 

### | Using the GUI

<img src="https://github.com/user-attachments/assets/48af30e7-fb43-4c1e-bd81-0faa300344f1" alt="drawing" width="500"/>

**Step 1**: Run Foil_Analysis/foilGUI.py

To perform metamorphic airfoil transformation, identify 2 foils in the same category from the list shown on the right and note their index number. 

**Step 2**: To plot the transformation, type the following syntax in the search field:

Foil Category + Foil 1 Index + Foil 2 Index

**Ex**: To transform thick foil 0021 to thick foil 2424, type this in the search field: thick + 1 + 4


### | Adding Custom Foils

**Step 1**: To store the raw data, append new foil data from Airfoil Tools or custom data to the file stored in Foil_Data/airfoil_data.csv.

Note: Append the x row first, then the y row. This ensures that the odd rows are x values and the even rows are y values. 

Plotting requires the x and y coordinate lists to be the same size. 

**Step 2**: Input your data in the MATLAB file stored in Foil_Data/Data_Equalization.m to randomly remove values and create a new X and Y area of the same size. 

**Step 3**: Append the new X and Y areas of equal size to the CSV file stored in Foil_Data/airfoil_data_equalized.csv.

## Features
### | Plots each Airfoil Category
There are 4 different Categories: Thin, Curved, Medium, and Thick Foils

**Example Output:**

<img width="400" src="https://github.com/user-attachments/assets/d737e5c5-4719-47e5-b2d2-ae3a987aa9ed" alt="Output Plot 1" />
<img width="400" src="https://github.com/user-attachments/assets/555e13fa-8831-4ed0-9551-f98e570d358a" alt="Output Plot 2" />

### | Animation Transformation
**Example Output:**

<img width="400" src="https://github.com/user-attachments/assets/001941b6-10c3-49cc-b071-d799b161660b" alt="Foil Expansion" />
<img width="400" src="https://github.com/user-attachments/assets/912ab2af-4c28-4757-ab9a-105c2339e228" alt="Foil Contraction" />
