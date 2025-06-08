<p align="center">
  <img width="250" src="https://github.com/user-attachments/assets/9c95b7ae-0d6a-4402-862a-7ce00865c143" alt="Falco Foil" />
</p>

<h2 align="center">Metamorphic Airfoil Analysis</h2>

<p align="center">
  Python-based Interactive GUI that visualizes the transformation movement of a metamorphic airfoil.
</p>

<p align="center">
  <strong>External Libraries Used:</strong> Matplotlib, Numpy, and Tkinter
</p>

---

## 🚀 Installation

```bash
git clone https://github.com/sjcreator06/FalcoFoil.git
```

---

## 📘 About Falco Foil Visualize

This library is used as part of a larger research project called Falco Foil to develop a metamorphic wing. A metamorphic airfoil is an airfoil that can change its shape. The library uses NACA 4-digit foils acquired from [Airfoil Tools](http://airfoiltools.com/search/index?m%5Bgrp%5D=naca4d&m%5Bsort%5D=1).

Four categories of airfoils can be identified in the NACA 4-Digit airfoil group: **thin**, **curved**, **medium**, and **thick** foils. The primary focus of this library is on medium and thick foils, as the metamorphic wing will have properties of a medium and thick airfoil. The library can also be easily adapted to add more foils from different foil categories.

In future releases, Computational Fluid Dynamics will be integrated to perform fluid analysis on metamorphic foils as they change shape and more complex transformations like thin and curved airfoils.

---

## 🖥️ Using the GUI

<p align="center">
  <img src="https://github.com/user-attachments/assets/48af30e7-fb43-4c1e-bd81-0faa300344f1" alt="drawing" width="500" />
</p>

**Step 1**: Run `Foil_Analysis/foilGUI.py`

To perform metamorphic airfoil transformation, identify 2 foils in the same category from the list shown on the right and note their index number.

**Step 2**: To plot the transformation, type the following syntax in the search field:

```
Foil Category + Foil 1 Index + Foil 2 Index
```

**Example**:  
To transform thick foil `0021` to thick foil `2424`, type this in the search field:

```
thick + 1 + 4
```

---

## 🧩 Adding Custom Foils

**Step 1**: To store the raw data, append new foil data from Airfoil Tools or custom data to the file stored in `Foil_Data/airfoil_data.csv`.

> Note: Append the `x` row first, then the `y` row. This ensures that the odd rows are x values and the even rows are y values.  
> Plotting requires the x and y coordinate lists to be the same size.

**Step 2**: Input your data in the MATLAB file stored in `Foil_Data/Data_Equalization.m` to randomly remove values and create a new X and Y array of the same size.

**Step 3**: Append the new X and Y arrays of equal size to the CSV file stored in `Foil_Data/airfoil_data_equalized.csv`.

---

## ✨ Features

### 📊 Plots Each Airfoil Category

There are 4 different categories: **Thin**, **Curved**, **Medium**, and **Thick** foils.

**Example Output:**

<p float="left">
  <img width="400" src="https://github.com/user-attachments/assets/d737e5c5-4719-47e5-b2d2-ae3a987aa9ed" alt="Output Plot 1" />
  <img width="400" src="https://github.com/user-attachments/assets/555e13fa-8831-4ed0-9551-f98e570d358a" alt="Output Plot 2" />
</p>

---

### 🔁 Animation Transformation

**Example Output:**

> Note: When analysis files are run, the animation plots are exported as a GIF.

<p float="left">
  <img width="400" src="https://github.com/user-attachments/assets/001941b6-10c3-49cc-b071-d799b161660b" alt="Foil Expansion" />
  <img width="400" src="https://github.com/user-attachments/assets/912ab2af-4c28-4757-ab9a-105c2339e228" alt="Foil Contraction" />
</p>
