# ~~~~~~~~ UNIT CONIVERTER ~~~~~~~~
# --- Import mudules ---
import tkinter as tk                # Import tkinter mas tk
from tkinter import ttk             # Import ttk modul
from unitconvert import lengthunits # Import uniconverter modul
# --- Window ---
root     = tk.Tk()                  # Create root widged/window
root.geometry("150x150")            # Define teh size of the window
# --- Variables definitions ---
userin   = tk.IntVar()              # Define the userinput
resultin = tk.IntVar()              # Define the result
uf       = tk.StringVar()           # Define the first unit as a string(text) variable
us       = tk.StringVar()           # Define the second unit as a string(text) variable
# --- Function---
def conv():                         # Define the function "conv" for the unit conversion
    a    = lengthunits.LengthUnit(userin.get(),f'{uf.get()}',f'{us.get()}').doconvert() # Input number, input unit, reslut unit and convert and round
    #a = '{:.2f}'.format(a)
    resultin.set(a)                 # Set a as result in resultin
def resetf():                       # Define the function "resetf" to rest the input and the result to zero
    resultin.set(0)                 # Set the result to zero
    userin.set(0)                   # Set the userinput to zero
# ---- Title ----
head = tk.Label(root,text="Unit Converter") # Setup a heading
head.grid(row=0,column=0,columnspan=2)      # Position the heading
# ---- User input ----
userinput = tk.Entry(root,textvariable=userin,width=10)      # Setup the input field
userinput.grid(row=1,column=0)                               # Position 
# --- 1. Drop down menu ----
unitfirst = ttk.Combobox(root,textvariable=uf,width=10)      # Create 1. drop down menu 
unitfirst['value']=('mm','cm','m','km','in','ft','yd','mi')  # content of the drop down menu 
unitfirst.grid(row=1,column=1)                               # Position
# --- 2. Drop down menu ----
unitsecond = ttk.Combobox(root,textvariable=us,width=10)     # Create 2. drop down menu 
unitsecond['value']=('mm','cm','m','km','in','ft','yd','mi') # Content of the drop down menu  
unitsecond.grid(row=2,column=1)                              # Position
# --- Reslut ---
result = tk.Label(root,textvariable=resultin)                # Setup the result field
result.grid(row=2,column=0)                                  # Position 
# --- Submit buttom ---
submit = tk.Button(root,text="SUBMIT",command=conv)          # Create a buttom
submit.grid(row=3,columnspan=2)                              # Position 
# --- Reset buttom ---
reset = tk.Button(root,text="RESET",command=resetf)          # Create a buttom
reset.grid(row=4,columnspan=2)                               # Position 
root.mainloop()                                              # Show the widget