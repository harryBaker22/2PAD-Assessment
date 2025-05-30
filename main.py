import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("500x400")

# create a main frame to put everything into
mainFrame = Frame(root)
mainFrame.pack(fill=BOTH, expand=True) # Fills the whole screen, and expands to fit it

#Creating canvas in main frame
canvas = Canvas(mainFrame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)
# Going on left hand side, and filling to the whole screen, then expanding to fit

#Adding a scrollbar
#Scrollbar with vertical orientation(going up and down), and using canavs.yview because its vertical
scrollbar = Scrollbar(mainFrame, orient=VERTICAL, command=canvas.yview)
#Scrollbar on right side of screen, and filled from top to bottom
scrollbar.pack(side=RIGHT, fill=Y)

#Configure the canavs
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

#Frame inside canavs to pu things in
canvasFrame = Frame(canvas)

#Add frame to window inside canavs
canvas.create_window((0, 0), window=canvasFrame, anchor="nw")

for thing in range(100):
    Button(root, text=f"Button Number {thing} I hate Harshul RAi and Harnish Shah").grid(row=thing, column=0, pady=10)

root.mainloop()

