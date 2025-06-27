import tkinter as tk
import tkinter.font as tkFont
from tkinter import *

import math

####################################################################################################################################
#Declarations for constants/tkinter stuff
####################################################################################################################################

#Item array
hireItems = ["Balloon Arch", "Popcorn Machine", "Cotton Candy Machine", "Photo Booth", "Disco Ball", "Fog Machine", "LED Dance Floor", "Bubble Machine", "Karaoke Machine", "Folding Chairs", "Banquet Tables", "Cocktail Tables", "Table Linens", "Chair Covers", "Sashes", "Centerpieces", "String Lights", "Fairy Lights", "Party Tents", "Marquees", "Helium Tanks", "Inflatables", "Bounce House", "Water Slide", "Slip And Slide", "Piñata", "Themed Backdrops", "Stanchions", "Red Carpet", "Cake Stand", "Cupcake Tower", "Serving Trays", "Drink Dispensers", "Chafing Dishes", "Cooler Bins", "Bar Setup", "Glassware", "Plasticware", "Plates", "Napkins", "Cutlery", "Table Runners", "Serving Utensils", "Candy Buffet Jars", "Popcorn Bags", "Cotton Candy Cones", "Signage Boards", "Easels", "Party Banners", "Streamers", "Confetti Cannons", "Party Hats", "Tiaras", "Masks", "Wigs", "Costumes", "Fog Juice", "Bubble Solution", "Inflatable Arches", "Inflatable Games", "Dunk Tank", "Yard Games", "Lawn Signs", "Chalkboard Signs", "Sound System", "DJ Booth", "Microphone", "Speakers", "Projector", "Screen", "LED Uplighting", "String Curtain Backdrop", "Sequin Backdrop", "Balloon Pump", "Number Balloons", "Foil Balloons", "Latex Balloons", "Balloon Weights", "Table Numbers", "Guest Book Stand", "Photo Props", "Glow Sticks", "LED Wristbands", "Fog Chiller", "Snow Machine", "Snow Fluid", "Throne Chair", "Peacock Chair", "Cake Cutting Set", "Dessert Stands", "Neon Signs", "Drink Stirrers", "Straw Decorations", "Party Favors", "Party Bags", "Piñata Fillers", "Treasure Chest Prop", "Tiki Torches", "Tropical Decor", "Fake Palm Trees", "Flameless Candles", "Harnish Shah", "Harshul Rai"]

#Background root window, minimizing
root = Tk()
root.geometry("1x1")
root.iconify()

#Global fonts
standardFont = tkFont.Font(family="Arial", size=15)

#Hired Items quanity Counter and indexer
newHiredItems = []

####################################################################################################################################
#Global functions
####################################################################################################################################

def createTopBar(currentWindow, targetBackWindow):
    #Creating top bar
    topBarFrame = Frame(currentWindow)
    topBarFrame.configure(borderwidth=10, relief=tk.FLAT)
    topBarFrame.pack(fill=BOTH, anchor='n')

    titleFrame = Frame(topBarFrame, borderwidth=5, relief=tk.RAISED)
    titleFrame.pack(side=LEFT, fill=BOTH, expand=True, pady=10)
    Label(titleFrame, text="Julies Party Hire Store", font=tkFont.Font(family='Arial', size=30, weight="bold"), width=30, height=2).grid(row=0, column=0, padx=10, pady=10)

    buttonFrame = Frame(topBarFrame)
    buttonFrame.pack(side=RIGHT, fill=BOTH, expand=True, pady=10)

    exitButton = Button(buttonFrame, text="X", font=tkFont.Font(family='Arial', size=30, weight="bold"), borderwidth=5, relief=tk.RAISED, height=2, command=lambda: quit())
    backbutton = Button(buttonFrame, text="<-", font=tkFont.Font(family='Arial', size=30, weight="bold"), borderwidth=5, relief=tk.RAISED, height=2, command=lambda: goToWindow(currentWindow, targetBackWindow))
    
    backbutton.grid(row=0, column=1, padx=10, pady=10)
    exitButton.grid(row=0, column=2, padx=10, pady=10)



####################################################################################################################################
#Item Screen Functions
####################################################################################################################################

def changeQuantity(index, entry, delta):
    
    #Changing visual quantity
    try:
        current = int(entry.get())
    except:
        current = 0
        
    new = current + delta
    
    if new < 0:
        new = 0
    
    entry.delete(0, END)
    entry.insert(0, new)
    
    #Adding index and amount to 2d list if not 0
    if new != 0:
        #Checking if list isnt empty
        if len(newHiredItems) != 0:
            #Checking if index already exits
            for i in range(0, len(newHiredItems)):
                #If index found, set corresponding quantity to new
                if index == newHiredItems[i][0]:
                    newHiredItems[i][1] = new
                    return
            
            #If index not found, make it
            newHiredItems.append([index, new])
        #if nothing in list, append new item to list
        else:
            newHiredItems.append([index, new])
    # Removing index from list if new quantity is zero
    else:
        #if list is not empty
        if len(newHiredItems) != 0:
            #Checking if index exits
            for i in range(0, len(newHiredItems)):
                #If index exists, delete it
                if index == newHiredItems[i][0]:
                    newHiredItems.pop(i)
                    return

def createItemWindow(itemsFrame, searchBarText):
    indexList = []
    #Emptying valid index list
    indexList.clear()
    
    #Getting indexes valid for item list from searchbar
    for i in range(0, len(hireItems)):
        string = hireItems[i].lower()
        if (searchBarText).lower() in string:
            indexList.append(i)
    
    #Destroying all current items in frame
    for widget in itemsFrame.winfo_children():
        widget.destroy()
    
    #Creating canvas in main frame
    canvas = Canvas(itemsFrame, bg="lightgreen")
    canvas.pack(side=LEFT, fill=BOTH, expand=True)# Going on left hand side, and filling to the whole screen, then expanding to fit
    
    #Adding a scrollbar
    #Scrollbar with vertical orientation(going up and down), and using canvas.yview because its vertical
    scrollbar = Scrollbar(itemsFrame, orient=VERTICAL, command=canvas.yview)
    
    #Scrollbar on right side of screen, and filled from top to bottom
    scrollbar.pack(side=RIGHT, fill=Y)
    
    #Configure the canvas for scrolling
    canvas.configure(yscrollcommand=scrollbar.set)
    
    #Setting scroll region based on amount of items
    height = max(145 * math.ceil(len(indexList) / 3), 550)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=(0, 0, 2000, height)))

    #Using mouse wheel to scroll
    canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -120), "units"))

    #Frame inside canvas to put things in
    canvasFrame = Frame(canvas, bg="lightgreen")
    
    #binding frame to scrollwheel so you can still scrll whil over the frame
    canvasFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -120), "units"))

    #Add frame to window inside canvas
    canvas.create_window((0, 0), window=canvasFrame, anchor="nw")

    
    #Try catch in case of bad search or bad item
    try:
        rowCounter = 0
        colCounter = 0
        
        for i in range(0, len(indexList)):
            
            #Frames for each button
            itemFrame = Frame(canvasFrame, borderwidth=3, relief=tk.SUNKEN)
            
            itemFrame.grid(row = rowCounter, column=colCounter, pady=10, padx=10)
            
            #Titles for each item
            itemLabel = Label(itemFrame, text="{0:^40}".format(hireItems[indexList[i]]), width=20, font=standardFont)
            itemLabel.pack()
            
            #Hire frame
            itemHireFrame = Frame(itemFrame)
            itemHireFrame.pack()
            
            #Quantity label
            quantityLabel = Label(itemHireFrame, text="Quantity:", font=standardFont)
            
            #Quantity entry
            quantityEntry = Entry(itemHireFrame, font=standardFont, width=5)

            #Bingding enter key to updating value information
            quantityEntry.bind("<Return>", lambda index=indexList[i], quantityEntry=quantityEntry, delta=-1: changeQuantity(index=index, entry=quantityEntry, delta=0))
            
            #Subtract/Add quanity button
            subButton = Button(itemHireFrame, text="-", font=standardFont, command= lambda index=indexList[i], quantityEntry=quantityEntry, delta=-1: changeQuantity(index=index, entry=quantityEntry, delta=-1))
            plusButton = Button(itemHireFrame, text="+", font=standardFont, command= lambda index=indexList[i], quantityEntry=quantityEntry, delta=1: changeQuantity(index=index, entry=quantityEntry, delta=1))
            
            quantityLabel.grid(row=0, column=1)
            subButton.grid(row=1, column=0)
            quantityEntry.grid(row=1, column=1)
            plusButton.grid(row=1, column=2)
            
            #Setting default value of 0
            changeQuantity(index=indexList[i], entry=quantityEntry, delta=-1)
            
            

            #Binding everything so you can scroll while over the items
            itemFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -120), "units"))
            itemLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -120), "units"))
            itemHireFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -120), "units"))
            quantityLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -120), "units"))
            quantityEntry.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -120), "units"))
            subButton.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -120), "units"))
            plusButton.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -120), "units"))
            
            
            #Counter to shift to next item
            colCounter += 1
            if colCounter == 3:
                rowCounter += 1
                colCounter = 0
    except:
        pass






####################################################################################################################################
#WINDOW FUNCTIONS
####################################################################################################################################


def goToWindow(currentWindow, targetWindwow):
    root.iconify()
    currentWindow.destroy()
    targetWindwow()

def createMainWindow():
    global mainWindow
    mainWindow = tk.Toplevel()
    mainWindow.geometry("800x400")
    
    #Binding root being opened to reopening this window
    root.bind("<FocusIn>", lambda e: goToWindow(mainWindow, createMainWindow))
    
    windowWidth = 1000
    windowHeight = 800
    
    #Spawning window in center of the screen
    mainWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, int((root.winfo_screenwidth() / 2) - (windowWidth / 2)), int((root.winfo_screenheight() / 2) - (windowHeight / 2))))
    mainWindow.resizable(False, False)
    mainWindow.overrideredirect(True)
    mainWindow.config(borderwidth=20, relief=tk.SUNKEN)
    
    #Top Bar
    createTopBar(mainWindow, createMainWindow)
    
    #Buttons to other windows
    Button(mainWindow, text="Hire Items", borderwidth=5, font=standardFont, command=lambda: goToWindow(mainWindow, createItemSelection)).pack(pady=30, padx=30)



def createItemSelection():
    
    
    global itemSelectionWindow
    
    itemSelectionWindow = tk.Toplevel()
    
    windowWidth = 1000
    windowHeight = 800
    
    #Binding root being opened to reopening this window
    root.bind("<FocusIn>", lambda e: goToWindow(mainWindow, createItemSelection))
    
    
    itemSelectionWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, int((root.winfo_screenwidth() / 2) - (windowWidth / 2)), int((root.winfo_screenheight() / 2) - (windowHeight / 2))))
    itemSelectionWindow.resizable(False, False)
    itemSelectionWindow.overrideredirect(True)
    itemSelectionWindow.config(borderwidth=20, relief=tk.SUNKEN)
    
    #Focusing the window
    itemSelectionWindow.focus_force()
    
    #Top Bar
    createTopBar(itemSelectionWindow, createMainWindow)
    
    # create a main frame to put everything into
    mainFrame = Frame(itemSelectionWindow)
    mainFrame.config(borderwidth=5, relief=tk.RIDGE)
    mainFrame.pack(fill=BOTH, expand=True) # Fills the whole screen, and expands to fit it

    #Creating sidebar for search
    sideBar = Frame(mainFrame, bg="lightblue",  borderwidth=3, relief=tk.RIDGE)
    sideBar.pack(side=LEFT, fill=BOTH)
    
    searchLabel = Label(sideBar, text="Search", anchor="w", borderwidth=5, relief=tk.SUNKEN, font=standardFont)
    searchLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    
    searchBarTextVariable = tk.StringVar()
    searchBar = Entry(sideBar, textvariable=searchBarTextVariable, borderwidth=2)
    searchBar.grid(row=1, column=0, padx=10, sticky="w")

    #Creating frame for canvas to sit in
    itemFrame = Frame(mainFrame)
    itemFrame.pack(side=RIGHT, fill=BOTH, expand=True)
    
    #Creating item window
    createItemWindow(itemFrame, searchBar.get())
    
    #Binding entry change to refreshing the item frame
    searchBarTextVariable.trace_add("write", lambda a, b, c: createItemWindow(itemFrame, searchBarTextVariable.get()))
    
def createConfirmItemSelection():
    pass
def createHiresView():
    pass
def createReturnView():
    pass
def createReturnConfirm():
    pass





createMainWindow()

root.mainloop()