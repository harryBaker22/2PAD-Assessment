import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox

import math
import random

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

#Scroll strength
scrollStrength = 120

#Hired Items quanity Counter
quantityCounter = [0] * len(hireItems)

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

def changeQuantity(index, textVariable, delta):
    #Getting amount in entry incase of changing using keyboard
    try:
        current = int(textVariable.get())
    except:
        #If invalid data in textbox(empty, letters, special characters, etc.)
        current = 0
    
    #Changing quantity at index
    quantityCounter[index] = current + delta

    # Preventing <0 quantity amounts
    if quantityCounter[index] < 0:
        quantityCounter[index] = 0

    #Updating visual quantity amount
    textVariable.set(quantityCounter[index])

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
    canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))

    #Frame inside canvas to put things in
    canvasFrame = Frame(canvas, bg="lightgreen")
    
    #binding frame to scrollwheel so you can still scrll whil over the frame
    canvasFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))

    #Add frame to window inside canvas
    canvas.create_window((0, 0), window=canvasFrame, anchor="nw")

    
    #Try catch in case of bad search or bad item
    try:
        rowCounter = 0
        colCounter = 0
        
        for i in range(0, len(indexList)):
            
            #Frames for each item
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

            quantityEntryTextVariable = tk.StringVar()
            quantityEntry = Entry(itemHireFrame, textvariable=quantityEntryTextVariable, font=standardFont, width=5)

            #Setting quanitity entry defult text to whatever the current quantity is
            quantityEntryTextVariable.set(quantityCounter[indexList[i]])
        
            #Binding entry change to updating the quantity
            # quantityEntryTextVariable.trace_add("write", lambda a, b, c: changeQuantity(index=indexList[i], textVariable=quantityEntryTextVariable, delta=0))

            #Subtract/Add quanity button
            subButton = Button(itemHireFrame, text="-", font=standardFont, command= lambda index=indexList[i], quantityEntryTextVariable=quantityEntryTextVariable, delta=-1: changeQuantity(index=index, textVariable=quantityEntryTextVariable, delta=delta))
            plusButton = Button(itemHireFrame, text="+", font=standardFont, command= lambda index=indexList[i], quantityEntryTextVariable=quantityEntryTextVariable, delta=1: changeQuantity(index=index, textVariable=quantityEntryTextVariable, delta=delta))
            
            quantityLabel.grid(row=0, column=1)
            subButton.grid(row=1, column=0)
            quantityEntry.grid(row=1, column=1)
            plusButton.grid(row=1, column=2)

            #Binding everything so you can scroll while over the items
            itemFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            itemLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            itemHireFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            quantityLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            quantityEntry.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            subButton.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            plusButton.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            
            
            #Counter to shift to next item
            colCounter += 1
            if colCounter == 3:
                rowCounter += 1
                colCounter = 0
    except:
        pass


####################################################################################################################################
#ITEM HIRE CONFIRM FUNCTIONS
####################################################################################################################################
#Canvas Configure function for multiple lines
def hiredItemsCanvasConfigure(event, canvas, scrollRegionHeight, canvasWindow):
    canvas.configure(scrollregion=(0, 0, 1000, scrollRegionHeight))
    canvas.itemconfig(canvasWindow, width=event.width)

def createHiredItems(itemsFrame):
    indexList = []
    #Emptying valid index list
    indexList.clear()
    #Getting indexes of valid items(items with quantity 1 or more)
    for i in range(0, len(quantityCounter)):
        if quantityCounter[i] != 0:
            indexList.append(i)

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
    
    #Using mouse wheel to scroll
    canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))

    #Frame inside canvas to put things in
    canvasFrame = Frame(canvas, bg="lightgreen")
    
    #binding frame to scrollwheel so you can still scroll while over the frame
    canvasFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))

    #Add frame to window inside canvas
    canvasWindow = canvas.create_window((0, 0), window=canvasFrame, anchor="nw")


    #Binding scroll region height and canvasWindow width resize to fit the canvas width to the canvas being changed
    #Setting height of scroll region based on amount of items
    height = max(175 * math.ceil(len(indexList)), 550) 
    canvas.bind("<Configure>", lambda event: hiredItemsCanvasConfigure(event=event, canvas=canvas, scrollRegionHeight=height, canvasWindow=canvasWindow))

    #Putting Hired Items into canvas 

    #Creating items in canvas
    for i in range(0, len(indexList)):
        try:
            #Frames for each item
            itemFrame = Frame(canvasFrame, borderwidth=3, relief=tk.SUNKEN)
            itemFrame.pack(pady=10, padx=10, fill=tk.X, expand=True)
            
            itemFrame.columnconfigure(1, weight=1)

            #Title for item
            itemTitleLabel = Label(itemFrame, text="{0:<40}".format(hireItems[indexList[i]]), width=20, height=4, font=standardFont, anchor=tk.W)
            itemTitleLabel.grid(row=0, column=0, sticky="e")

            # Quantity for item
            itemQuantityLabel = Label(itemFrame, text="{0:>3}".format(quantityCounter[indexList[i]]), width=10, height=4, font=standardFont, anchor=tk.E)
            itemQuantityLabel.grid(row=0, column=2, sticky="w")

            #Binding everything so you can scroll while over the items
            itemFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            itemTitleLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            itemQuantityLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
        except:
            pass


def generateReceiptNumber():
    receiptNum = 0

    # Make sure receipt is not already in hires file
    while True:
        # Generating random 32 bit number
        receiptNum = random.getrandbits(32)
        match = False

        # Opening file
        with open("hires.txt", "r") as file:
            # Reading all lines
            lines = file.readlines()

            # Iterating through each line
            for line in lines:
                # Splitting line into each segment
                lineArray = line.split(",")

                # Comparing receipt num in line with generated num
                if receiptNum == lineArray[0]:
                    match = True
                    break
        # If no receipts matched, then break loop
        if not match:
            break
    return receiptNum

def saveHire(customerName):
    #Get receipt number
    receiptNum = generateReceiptNumber()

    #Get 2d array of items(index, quantity)
    indexQuantityList = [[]]
    indexQuantityList.clear()
    #Getting indexes of valid items(items with quantity 1 or more), and appending that index and the quantity to 2d list
    for i in range(0, len(quantityCounter)):
        if quantityCounter[i] != 0:
            indexQuantityList.append([i, quantityCounter[i]])

    #Save in csv format to file as one line
    with open("hires.txt", "a") as file:
        #Receipt Number and Customer Name
        file.write(str(receiptNum) + "," + customerName)

        #Index quantity list
        for i in range(0, len(indexQuantityList)):
            file.write("," + str(indexQuantityList[i][0]) + "," + str(indexQuantityList[i][1]))

        #Going down a line for next hire
        file.write("\n")
    
    #Display receipt number in message box
    messagebox.showinfo("Receipt Number", "Receipt Number: " + str(receiptNum))

    #Going back to main window
    goToWindow(confirmItemSelectionWindow, createMainWindow)

####################################################################################################################################
#WINDOW FUNCTIONS
####################################################################################################################################


def goToWindow(currentWindow, targetWindwow):
    root.iconify()
    currentWindow.destroy()
    targetWindwow()

def createMainWindow():

    #Resetting quantity counter to 0
    global quantityCounter
    quantityCounter = [0] * len(hireItems)

    global mainWindow
    mainWindow = tk.Toplevel()
    
    #Binding root being opened to reopening this window
    root.bind("<FocusIn>", lambda e: goToWindow(mainWindow, createMainWindow))
    
    #Spawning window in center of the screen
    windowWidth = 1000
    windowHeight = 800
    mainWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, int((root.winfo_screenwidth() / 2) - (windowWidth / 2)), int((root.winfo_screenheight() / 2) - (windowHeight / 2))))
    mainWindow.resizable(False, False)
    mainWindow.overrideredirect(True)
    mainWindow.config(borderwidth=20, relief=tk.SUNKEN)

    #Focusing the window
    mainWindow.focus_force()
    
    #Top Bar
    createTopBar(mainWindow, createMainWindow)
    
    #Buttons to other windows
    Button(mainWindow, text="Hire Items", borderwidth=5, font=standardFont, command=lambda: goToWindow(mainWindow, createItemSelection)).pack(pady=30, padx=30)


def createItemSelection():
    
    
    global itemSelectionWindow
    
    itemSelectionWindow = tk.Toplevel()

    #Binding root being opened to reopening this window
    root.bind("<FocusIn>", lambda e: goToWindow(itemSelectionWindow, createItemSelection))

    #Spawning window in center of the screen
    windowWidth = 1000
    windowHeight = 800
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

    #Binding entry change to refreshing the item frame
    searchBarTextVariable.trace_add("write", lambda a, b, c: createItemWindow(itemFrame, searchBarTextVariable.get()))

    #Confirm order button
    Button(sideBar, text="Confirm Hire", font=standardFont, command=lambda: goToWindow(itemSelectionWindow, createConfirmItemSelection)).grid(row=2, column=0, pady=425, padx=10, sticky="s")

    #Creating frame for canvas to sit in
    itemFrame = Frame(mainFrame)
    itemFrame.pack(side=RIGHT, fill=BOTH, expand=True)
    
    #Creating item window
    createItemWindow(itemFrame, searchBar.get())
    
def createConfirmItemSelection():
    global confirmItemSelectionWindow
    confirmItemSelectionWindow = tk.Toplevel()

    #Binding root being opened to reopening this window
    root.bind("<FocusIn>", lambda e: goToWindow(confirmItemSelectionWindow, createConfirmItemSelection))

    #Spawning window in center of the screen
    windowWidth = 1000
    windowHeight = 800
    confirmItemSelectionWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, int((root.winfo_screenwidth() / 2) - (windowWidth / 2)), int((root.winfo_screenheight() / 2) - (windowHeight / 2))))
    confirmItemSelectionWindow.resizable(False, False)
    confirmItemSelectionWindow.overrideredirect(True)
    confirmItemSelectionWindow.config(borderwidth=20, relief=tk.SUNKEN)
    
    #Focusing the window
    confirmItemSelectionWindow.focus_force()
    
    #Top Bar
    createTopBar(confirmItemSelectionWindow, createItemSelection)

    #Create a main frame to put everything into
    mainFrame = Frame(confirmItemSelectionWindow)
    mainFrame.config(borderwidth=5, relief=tk.RIDGE)
    mainFrame.pack(fill=BOTH, expand=True) # Fills the whole screen, and expands to fit it

    #"HIRED ITEMS"
    Label(mainFrame, text="HIRED ITEMS:", font=standardFont).pack(pady=10)

    #Frame for Hired items list
    itemsFrame = Frame(mainFrame, borderwidth=10, relief=tk.SUNKEN)
    itemsFrame.pack(fill=BOTH, expand=True, padx=10)

    #Creating hired items list
    createHiredItems(itemsFrame)

    #Customer name label and entry
    Label(mainFrame, text="Customer Name:", font=standardFont).pack(pady=10, padx=10, side=LEFT)
    customerNameEntryText = tk.StringVar()
    customerNameEntry = Entry(mainFrame, textvariable=customerNameEntryText, font=standardFont)
    customerNameEntry.pack(pady=10, padx=10, side=LEFT)

    #Confirm Hire button
    confirmHireButton = Button(mainFrame, text="Confirm Hire", font=standardFont, command=lambda : saveHire(customerName=customerNameEntryText.get()))
    confirmHireButton.pack(pady=10, padx=10, side=RIGHT)


    



def createHiresView():
    pass
def createReturnView():
    pass
def createReturnConfirm():
    pass





createMainWindow()



root.mainloop()

