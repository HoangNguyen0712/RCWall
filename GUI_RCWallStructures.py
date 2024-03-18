# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:44:21 2020

@author: USER
"""

import PySimpleGUI as sg
import numpy as np
from pickle import load
from tensorflow import keras

# ADD TITLE COLOUR ,title_color='white'
sg.theme('Dark Blue 3')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Developed by Hoang Dac Nguyen')],
            [sg.Text('UNIST, South Korea')],
            [sg.Text('Email: nguyenhoangkt712@unist.ac.kr')],
            [sg.Text('Seismic dirft response prediction of R/C structures using DNN')],
            [sg.Text('Hoang D. Nguyen and Myoungsu Shin')],
              
            [sg.Frame(layout=[
            [sg.Text('PGA (g)',size=(15, 1)),sg.InputText(key='-f1-',size=(30, 1))],
            [sg.Text('PSA-1s (g)',size=(15, 1)), sg.InputText(key='-f2-',size=(30, 1))],
            [sg.Text('PSA-2s (g)',size=(15, 1)), sg.InputText(key='-f3-',size=(30, 1))],
            [sg.Text('PSA-3s (g)',size=(15, 1)), sg.InputText(key='-f4-',size=(30, 1))],
            [sg.Text('PSA-4s (g)',size=(15, 1)), sg.InputText(key='-f5-',size=(30, 1))],
            [sg.Text('PSA-5s (g)',size=(15, 1)), sg.InputText(key='-f6-',size=(30, 1))],
            [sg.Text('PSA-5s (g)',size=(15, 1)), sg.InputText(key='-f7-',size=(30, 1))],
            [sg.Text('T1 (s)',size=(15, 1)), sg.InputText(key='-f8-',size=(30, 1))],
            [sg.Text('T2 (s)',size=(15, 1)), sg.InputText(key='-f9-',size=(30, 1))],
            [sg.Text('T3 (s)',size=(15, 1)), sg.InputText(key='-f10-',size=(30, 1))],
            [sg.Text('T4 (s)',size=(15, 1)), sg.InputText(key='-f11-',size=(30, 1))],
            [sg.Text('T5 (s)',size=(15, 1)), sg.InputText(key='-f12-',size=(30, 1))],
            [sg.Text('GM Char (1, 2, or 3)',size=(15, 1)),sg.InputText(key='-f13-',size=(30, 1))]],title='Input variables')],
            [sg.Frame(layout=[   
            [sg.Text('Max.Interstory Drift',size=(15, 1)), sg.InputText(key='-OP-',size=(30, 1))]],title='Output')],
            [sg.Button('Predict'),sg.Button('Cancel')] 
            

            
            ]

# Create the Window
window = sg.Window('SEISMIC DRIFT RESPONSE PREDICTION OF R/C WALL', layout)

filename = 'CNN_InputSet1.h5'
loaded_model_Set1 =  keras.models.load_model(filename)

filename = 'CNN_InputSet2.h5'
loaded_model_Set2 =  keras.models.load_model(filename)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    #window['-OP-'].update('Please fill all the input parameters')
    if event == 'Predict':
        #window['-OP-'].update(values[0])
        #break
        if values['-f1-'] == '' or values['-f2-'] == '' or values['-f3-'] == '' or values['-f4-'] == '' or values['-f5-'] == '' or values['-f6-'] == '' or values['-f7-'] == '' or values['-f8-'] == '' or values['-f9-'] == '' or values['-f10-'] == '' or values['-f11-'] == '' or values['-f12-'] == '': 

            window['-OP-'].update('Please fill all the input parameters')

        elif values['-f13-'] != '':
            x_test=np.array([[float(values['-f1-']),float(values['-f2-']), float(values['-f3-']),float(values['-f4-']),float(values['-f5-']),float(values['-f6-']),float(values['-f7-']),float(values['-f8-']),float(values['-f9-']),float(values['-f10-']),float(values['-f11-']),float(values['-f12-']),float(values['-f13-'])]])
            y_pred_disp = loaded_model_Set2.predict(x_test)
            window['-OP-'].update(abs(np.round((y_pred_disp[0,0]*100),4)))
        else:
            x_test=np.array([[float(values['-f1-']),float(values['-f2-']), float(values['-f3-']),float(values['-f4-']),float(values['-f5-']),float(values['-f6-']),float(values['-f7-']),float(values['-f8-']),float(values['-f9-']),float(values['-f10-']),float(values['-f11-']),float(values['-f12-'])]])
            y_pred_disp = loaded_model_Set1.predict(x_test)
            window['-OP-'].update(abs(np.round((y_pred_disp[0,0]*100),4)))
            

window.close()
