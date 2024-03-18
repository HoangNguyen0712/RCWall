# Software introduction

This code package is develeloped the graphical user interface (GUI) for predicting the seismic response of reinforced concrete wall structures using deep neural networks. 

# Developers

Developed by Hoang D. Nguyen (nguyenhoangkt712@unist.ac.kr), Chanyoung Kim, Kihak Lee, and Myoungsu Shin. 

Institution: Ulsan National Institute of Science and Technology (UNIST) and Sejong University.

# Reference

DEVELOPMENT OF SURROGATE MODELS TO PREDICT SEISMIC RESPONSE OF R/C WALL STRUCTURE: AN APPLICATION OF DEEP NEURAL NETWORKS (In preparation).

# Required software and libraries

Python 3.8 with Numpy version '1.24.3', PySimpleGUI version '4.60.5', and tensorflow version '2.12.0'.

# Steps to use the package

Step 1: Download all file in this repository into one folder. 

Step 2: Run the python file GUI_RCWallStructures.py to open the GUI.

Step 3: Fill out all the required input variables (consider ground motion type (13 variables) or without consider it (14 input variables)) in the GUI.

Step 4: Press "Predict" button to obtain the maximum interstory drift of RC wall structure.

# Note

CNN_InputSet1.h5 and CNN_InputSet2.h5 are the developed models for input set 1 and input set 2, respectively. 
