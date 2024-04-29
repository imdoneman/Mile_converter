import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

#window
window = ttk.Window()
window.title("Mile converter")
window.geometry('400x150')

#title
title_label = ttk.Label(master=window, text="Miles to Kilometers", font='Roboto 20 bold')
title_label.pack()

#function for calculation
def convert():
    tempVar = str(round(inputVar.get()*1.60934,2))+ ' KM'
    outputVar.set(tempVar)

#GUI variable declaration
inputVar = tk.IntVar()
outputVar = tk.StringVar()

#input feild
inputFrame = ttk.Frame(master = window)
entry = ttk.Entry(master = inputFrame, textvariable=inputVar)
button = ttk.Button(master = inputFrame, text= 'convert', command=convert)
entry.pack(side='left', padx = 10)
button.pack(side='left')
inputFrame.pack(pady = 10)

#output feild
outputLabel = ttk.Label(master = window, text='KM:', font='Roboto 20', textvariable=outputVar)
outputLabel.pack()

#run
window.mainloop()