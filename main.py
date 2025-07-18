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
standardFont = ("Lucida Sans", 14)
buttonColour = "#7dc6f0"
windwoColour = "#7D8DF0"
canvasColour = "#C6F07D"
backgroundColour = "#4FB2EB"

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
    topBarFrame.configure(borderwidth=10, relief=tk.GROOVE, bg=backgroundColour)
    topBarFrame.pack(fill=X, anchor='nw')

    titleFrame = Frame(topBarFrame, borderwidth=5, relief=tk.RAISED, bg="#7DF0E0")
    titleFrame.pack(side=LEFT, fill=BOTH, expand=True, pady=10, padx=10)
    Label(titleFrame, text="Julies Party Hire Store", font=tkFont.Font(family="Lucida Sans", size=30, weight="bold"), height=2, bg="#7DF0E0").pack(pady=10, anchor=tk.CENTER)

    buttonFrame = Frame(topBarFrame, bg=backgroundColour)
    buttonFrame.pack(side=RIGHT, pady=10)

    exitButton = Button(buttonFrame, text="X", font=tkFont.Font(family="Lucida Sans", size=30, weight="bold"), borderwidth=5, relief=tk.RAISED, height=2, bg=buttonColour, command=lambda: quit())
    backbutton = Button(buttonFrame, text="<-", font=tkFont.Font(family="Lucida Sans", size=30, weight="bold"), borderwidth=5, relief=tk.RAISED, height=2, bg=buttonColour, command=lambda: goToWindow(currentWindow, targetBackWindow))
    
    backbutton.grid(row=0, column=1, padx=10, pady=10)
    exitButton.grid(row=0, column=2, padx=10, pady=10)



####################################################################################################################################
#Item Screen Functions
####################################################################################################################################

def changeQuantity(index, label, delta):
    #Getting amount in entry incase of changing using keyboard
    try:
        current = int(label.cget("text"))
    except:
        #If invalid data in textbox(empty, letters, special characters, etc.)
        current = 0
    
    #Changing quantity at index
    quantityCounter[index] = current + delta

    # Preventing <0 quantity amounts
    if quantityCounter[index] < 0:
        quantityCounter[index] = 0

    # Updating visual quantity amount
    label.configure(text=quantityCounter[index])

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
    canvas = Canvas(itemsFrame, bg=canvasColour)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)# Going on left hand side, and filling to the whole screen, then expanding to fit
    
    #Adding a scrollbar
    #Scrollbar with vertical orientation(going up and down), and using canvas.yview because its vertical
    scrollbar = Scrollbar(itemsFrame, orient=VERTICAL, command=canvas.yview)
    
    #Scrollbar on right side of screen, and filled from top to bottom
    scrollbar.pack(side=RIGHT, fill=Y)
    
    #Configure the canvas for scrolling
    canvas.configure(yscrollcommand=scrollbar.set)
    
    #Setting scroll region based on amount of items
    height = max(125 * math.ceil(len(indexList) / 3), 550)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=(0, 0, 2000, height)))

    #Using mouse wheel to scroll
    canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))

    #Frame inside canvas to put things in
    canvasFrame = Frame(canvas, bg=canvasColour)
    
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
            itemFrame = Frame(canvasFrame, borderwidth=3, relief=tk.SUNKEN, bg="lightblue")
            
            itemFrame.grid(row = rowCounter, column=colCounter, pady=10, padx=2)

            #Titles for each item
            itemLabel = Label(itemFrame, text="{0:^40}".format(hireItems[indexList[i]]), width=20, font=standardFont, bg="lightblue")
            itemLabel.pack()

            #Hire frame
            itemHireFrame = Frame(itemFrame, bg="lightblue")
            itemHireFrame.pack()

            #Quantity label
            quantityLabel = Label(itemHireFrame, text="Quantity:", font=standardFont, bg="lightblue")

            #Quantity amount label
            quantityAmountLabel = Label(itemHireFrame, font=standardFont, width=5, borderwidth=5, relief=tk.GROOVE, bg=buttonColour)

            quantityAmountLabel.configure(text=quantityCounter[indexList[i]])

            #Subtract/Add quanity button
            subButton = Button(itemHireFrame, text="-", font=standardFont, bg=buttonColour, command= lambda index=indexList[i], label=quantityAmountLabel, delta=-1: changeQuantity(index=index, label=label, delta=delta))
            plusButton = Button(itemHireFrame, text="+", font=standardFont, bg=buttonColour, command= lambda index=indexList[i], label=quantityAmountLabel, delta=1: changeQuantity(index=index, label=label, delta=delta))

            quantityLabel.grid(row=0, column=1)
            subButton.grid(row=1, column=0)
            quantityAmountLabel.grid(row=1, column=1)
            plusButton.grid(row=1, column=2)

            #Binding everything so you can scroll while over the items
            itemFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            itemLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            itemHireFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            quantityLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            quantityAmountLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
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
def newHiredItemsCanvasConfigure(event, canvas, scrollRegionHeight, canvasWindow):
    canvas.configure(scrollregion=(0, 0, 1000, scrollRegionHeight))
    canvas.itemconfig(canvasWindow, width=event.width)

def createNewHiredItemsViewCanvas(itemsFrame):
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
    #Setting height of scroll region based on height of window
    canvas.bind("<Configure>", lambda event: newHiredItemsCanvasConfigure(event=event, canvas=canvas, scrollRegionHeight=canvasFrame.winfo_height(), canvasWindow=canvasWindow))

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
    
    #Display receipt number in message box for feedback to user
    messagebox.showinfo("Receipt Number", "Receipt Number: " + str(receiptNum))

    #Going back to main window
    goToWindow(confirmItemSelectionWindow, createMainWindow)

####################################################################################################################################
#HIRES VIEW FUNCTIONS
####################################################################################################################################
def hiresViewsCanvasConfigure(event, canvas, scrollRegionHeight, canvasWindow):
    canvas.configure(scrollregion=(0, 0, 1000, scrollRegionHeight))
    canvas.itemconfig(canvasWindow, width=event.width)

def viewHire(index):
    goToWindow(hiresViewWindow, createReturnConfirm, index)

def createHiresViewCanvas(frame, searchedNumber):
    #Destroying all current items in frame for refresh
    for widget in frame.winfo_children():
        widget.destroy()
    
    #Valid index list
    indexList = []
    indexList.clear()
    
    #Getting current hires file in array of lines
    linesArray = []
    with open("hires.txt", "r") as file:
        linesArray = file.readlines()

    #Finding indexs of lines with matching receipt numbers to the seacrhbar
    for i in range(0, len(linesArray)):
        #Splitting each line into seperate elements
        lineArray = linesArray[i].split(",")

        #Getting receipt number
        receiptNumber = lineArray[0]

        #If matching, append index to valid index list
        if searchedNumber in receiptNumber:
            indexList.append(i)

    #Creating canvas in main frame
    canvas = Canvas(frame, bg="lightgreen")
    canvas.pack(side=LEFT, fill=BOTH, expand=True)# Going on left hand side, and filling to the whole screen, then expanding to fit
    
    #Adding a scrollbar
    #Scrollbar with vertical orientation(going up and down), and using canvas.yview because its vertical
    scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    
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
    #Setting height of scroll region based on amount of valid hires
    height = max(125 * math.ceil(len(indexList)), 550) 
    canvas.bind("<Configure>", lambda event: hiresViewsCanvasConfigure(event=event, canvas=canvas, scrollRegionHeight=height, canvasWindow=canvasWindow))

    #Putting Hired Items into canvas 

    #Creating items in canvas
    for i in range(0, len(indexList)):
        try:
            #Getting line split into elements
            lineArray = linesArray[indexList[i]].split(",")

            #Frames for each hire
            hireFrame = Frame(canvasFrame, borderwidth=3, relief=tk.SUNKEN)
            hireFrame.pack(pady=10, padx=10, fill=tk.X, expand=True)

            #Info Frame
            infoFrame = Frame(hireFrame)
            infoFrame.pack(side=LEFT, fill=X, expand=True)
            infoFrame.columnconfigure(1, weight=1)

            #Receipt Number
            hireReceiptNumLabel = Label(infoFrame, text="{0:>10}".format(lineArray[0]), height=4, font=standardFont, anchor=tk.W)
            hireReceiptNumLabel.grid(row=0, column=0, sticky="e", padx=10)

            #Customer Name
            hireCustomerNameLabel = Label(infoFrame, text="{0:>30}".format(lineArray[1]), height=4, font=standardFont, anchor=tk.E)
            hireCustomerNameLabel.grid(row=0, column=2, sticky="w", padx=10)

            #View hire button and frame
            viewFrame = Frame(hireFrame)
            viewFrame.pack(side=RIGHT)

            viewButton = Button(viewFrame, text="View", font=standardFont, command=lambda index=indexList[i]: viewHire(index))
            viewButton.pack(padx=10)

            #Binding everything so you can scroll while over the items
            hireFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            infoFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            hireReceiptNumLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            hireCustomerNameLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            viewFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            viewButton.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
        except:
            pass

####################################################################################################################################
#RETURN VIEW FUNCTIONS
####################################################################################################################################
def returnHire(index):
    #Get file as an array of lines
    with open("hires.txt", "r") as file:
        linesArray = file.readlines()

    #Remove line at index
    linesArray.pop(index)

    #Override file with the same array
    with open("hires.txt" , "w") as file:
        for line in linesArray:
            file.write(line)
    
    #Show message box for feedback to user
    messagebox.showinfo("Info", "Hire has been marked as returned")
    #Back to main page
    goToWindow(returnConfirmWindow, createMainWindow)

def returnCanvasConfigure(event, canvas, scrollRegionHeight, canvasWindow):
    canvas.configure(scrollregion=(0, 0, 1000, scrollRegionHeight))
    canvas.itemconfig(canvasWindow, width=event.width)

def createReturnItemsViewCanvas(itemsFrame, lineArray):
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


    #Binding scroll region height and canvasWindow width resize to fit the canvas, to the canvas being changed
    #Setting height of scroll region based on amount of items
    height = max(125 * math.ceil((len(lineArray) - 2) / 2), 420)
    canvas.bind("<Configure>", lambda event: returnCanvasConfigure(event=event, canvas=canvas, scrollRegionHeight=height, canvasWindow=canvasWindow))

    #Putting Hired Items into canvas 
    #Creating items in canvas
    for i in range(2, math.ceil(len(lineArray) / 2) + 1):
        try:
            # Calculating currently used item index and quantity
            itemIndex = int(lineArray[i*2 - 2])
            quantity = int(lineArray[i*2 - 1])

            #Frames for each item
            itemFrame = Frame(canvasFrame, borderwidth=3, relief=tk.SUNKEN)
            itemFrame.pack(pady=10, padx=10, fill=tk.X, expand=True)
            
            itemFrame.columnconfigure(1, weight=1)

            #Title for item
            itemTitleLabel = Label(itemFrame, text="{0:<40}".format(hireItems[itemIndex]), width=20, height=4, font=standardFont, anchor=tk.W)
            itemTitleLabel.grid(row=0, column=0, sticky="e")

            # Quantity for item
            itemQuantityLabel = Label(itemFrame, text="{0:>3}".format(quantity), width=10, height=4, font=standardFont, anchor=tk.E)
            itemQuantityLabel.grid(row=0, column=2, sticky="w")

            #Binding everything so you can scroll while over the items
            itemFrame.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            itemTitleLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
            itemQuantityLabel.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -scrollStrength), "units"))
        except:
            pass

####################################################################################################################################
#WINDOW FUNCTIONS
####################################################################################################################################


def goToWindow(currentWindow, targetWindwow, *args):
    root.iconify()
    currentWindow.destroy()
    targetWindwow(args)

def createMainWindow(*args):

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
    mainWindow.config(borderwidth=20, relief=tk.RAISED, bg=windwoColour)

    #Focusing the window
    mainWindow.focus_force()
    
    #Top Bar
    createTopBar(mainWindow, createMainWindow)
    
    #Buttons to other windows
    buttonFrame = Frame(mainWindow, bg="lightblue")
    buttonFrame.pack(fill=BOTH, expand=True, anchor="n")
    Button(buttonFrame, text="Hire Items", borderwidth=5, relief=tk.RAISED, font=("Lucida Sans", 25), width=20, height=3, bg=buttonColour, command=lambda: goToWindow(mainWindow, createItemSelection)).pack(pady=10, padx=30)
    Button(buttonFrame, text="View Current Hires", borderwidth=5, relief=tk.RAISED, font=("Lucida Sans", 25), width=20, height=3, bg=buttonColour, command=lambda: goToWindow(mainWindow, createHiresView)).pack(pady=10, padx=30)


def createItemSelection(*args):
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
    itemSelectionWindow.config(borderwidth=20, relief=tk.RAISED, bg=windwoColour)
    
    #Focusing the window
    itemSelectionWindow.focus_force()
    
    #Top Bar
    createTopBar(itemSelectionWindow, createMainWindow)
    
    # create a main frame to put everything into
    mainFrame = Frame(itemSelectionWindow, bg=backgroundColour)
    mainFrame.config(borderwidth=5, relief=tk.RIDGE)
    mainFrame.pack(fill=BOTH, expand=True) # Fills the whole screen, and expands to fit it

    #Creating sidebar for search
    sideBar = Frame(mainFrame, bg=backgroundColour,  borderwidth=3, relief=tk.RIDGE)
    sideBar.pack(side=LEFT, fill=BOTH)
    
    searchLabel = Label(sideBar, text="Search", anchor="w", borderwidth=5, relief=tk.RAISED, font=standardFont, bg=buttonColour)
    searchLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    
    searchBarTextVariable = tk.StringVar()
    searchBar = Entry(sideBar, textvariable=searchBarTextVariable, borderwidth=2, bg=buttonColour)
    searchBar.grid(row=1, column=0, padx=10, sticky="w")

    #Binding entry change to refreshing the item frame
    searchBarTextVariable.trace_add("write", lambda a, b, c: createItemWindow(itemFrame, searchBarTextVariable.get()))

    #Confirm order button
    Button(sideBar, text="Check Hire", font=standardFont, bg=buttonColour, command=lambda: goToWindow(itemSelectionWindow, createConfirmItemSelection)).grid(row=2, column=0, pady=425, padx=10, sticky="s")

    #Creating frame for canvas to sit in
    itemFrame = Frame(mainFrame)
    itemFrame.pack(side=RIGHT, fill=BOTH, expand=True)
    
    #Creating item window
    createItemWindow(itemFrame, searchBar.get())
    
def createConfirmItemSelection(*args):
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
    confirmItemSelectionWindow.config(borderwidth=20, relief=tk.RAISED, bg=windwoColour)
    
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
    itemsFrame = Frame(mainFrame, borderwidth=10, relief=tk.RAISED)
    itemsFrame.pack(fill=BOTH, expand=True, padx=10)

    #Creating hired items list
    createNewHiredItemsViewCanvas(itemsFrame)

    #Customer name label and entry
    Label(mainFrame, text="Customer Name:", font=standardFont).pack(pady=10, padx=10, side=LEFT)
    customerNameEntryText = tk.StringVar()
    customerNameEntry = Entry(mainFrame, textvariable=customerNameEntryText, font=standardFont)
    customerNameEntry.pack(pady=10, padx=10, side=LEFT)

    #Confirm Hire button
    confirmHireButton = Button(mainFrame, text="Confirm Hire", font=standardFont, command=lambda : saveHire(customerName=customerNameEntryText.get()))
    confirmHireButton.pack(pady=10, padx=10, side=RIGHT)


def createHiresView(*args):
    global hiresViewWindow
    hiresViewWindow = tk.Toplevel()

    #Binding root being opened to reopening this window
    root.bind("<FocusIn>", lambda e: goToWindow(hiresViewWindow, createHiresView))

    #Spawning window in center of the screen
    windowWidth = 1000
    windowHeight = 800
    hiresViewWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, int((root.winfo_screenwidth() / 2) - (windowWidth / 2)), int((root.winfo_screenheight() / 2) - (windowHeight / 2))))
    hiresViewWindow.resizable(False, False)
    hiresViewWindow.overrideredirect(True)
    hiresViewWindow.config(borderwidth=20, relief=tk.RAISED, bg=windwoColour)
    
    #Focusing the window
    hiresViewWindow.focus_force()
    
    #Top Bar
    createTopBar(hiresViewWindow, createMainWindow)

    #Create a main frame to put everything into
    mainFrame = Frame(hiresViewWindow)
    mainFrame.config(borderwidth=5, relief=tk.RIDGE)
    mainFrame.pack(fill=BOTH, expand=True) # Fills the whole screen, and expands to fit it

    #Frame for receipt number search
    receiptNumberFrame = Frame(mainFrame)
    receiptNumberFrame.pack(anchor=tk.NW)

    #Receipt number label and entry
    Label(receiptNumberFrame, text="Search Receipt No.:", font=standardFont).grid(row=0, column=0, pady=10, padx=10)
    customerNameEntryText = tk.StringVar()
    customerNameEntry = Entry(receiptNumberFrame, textvariable=customerNameEntryText, font=standardFont)
    customerNameEntry.grid(row=0, column=1, pady=10, padx=10)

    #Frame for hires to go in
    hireFrame = Frame(mainFrame, borderwidth=10, relief=tk.RAISED)
    hireFrame.pack(fill=BOTH, expand=True)

    #Binding search bar entry change to refreshing the hires shown
    customerNameEntryText.trace_add("write", lambda a, b, c: createHiresViewCanvas(hireFrame, customerNameEntryText.get()))

    #Creating canvas with hires in it
    createHiresViewCanvas(hireFrame, customerNameEntryText.get())


def createReturnConfirm(hireIndex, *args):
    #Getting index of hire in file from the passed tuple
    index = hireIndex[0]
    
    global returnConfirmWindow
    returnConfirmWindow = tk.Toplevel()

    #Binding root being opened to reopening this window
    root.bind("<FocusIn>", lambda e: goToWindow(returnConfirmWindow, createReturnConfirm, index))

    #Spawning window in center of the screen
    windowWidth = 1000
    windowHeight = 800
    returnConfirmWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, int((root.winfo_screenwidth() / 2) - (windowWidth / 2)), int((root.winfo_screenheight() / 2) - (windowHeight / 2))))
    returnConfirmWindow.resizable(False, False)
    returnConfirmWindow.overrideredirect(True)
    returnConfirmWindow.config(borderwidth=20, relief=tk.RAISED, bg=windwoColour)
    
    #Focusing the window
    returnConfirmWindow.focus_force()
    
    #Top Bar
    createTopBar(returnConfirmWindow, createHiresView)

    #Create a main frame to put everything into
    mainFrame = Frame(returnConfirmWindow)
    mainFrame.config(borderwidth=5, relief=tk.RIDGE)
    mainFrame.pack(fill=BOTH, expand=True) # Fills the whole screen, and expands to fit it

    #"HIRED ITEMS"
    Label(mainFrame, text="HIRED ITEMS:", font=standardFont).pack(pady=10)

    #Frame for Hired items list
    itemsFrame = Frame(mainFrame, borderwidth=10, relief=tk.RAISED)
    itemsFrame.pack(fill=BOTH, expand=True, padx=10)
    
    #Getting lines from file
    linesArray = []
    with open("hires.txt", "r") as file:
        linesArray = file.readlines()
    lineArray = linesArray[index].split(",")

    #Creating currently hired items list
    createReturnItemsViewCanvas(itemsFrame, lineArray)

    #Customer name label
    Label(mainFrame, text="Customer Name: {0:<30}".format(lineArray[1]), font=standardFont).pack(pady=10, padx=10, side=LEFT)

    #Mark as returned button
    confirmReturnButton = Button(mainFrame, text="Mark As Returned", font=standardFont, command=lambda : returnHire(index))
    confirmReturnButton.pack(pady=10, padx=10, side=RIGHT)

#Creating main window
createMainWindow()
#Starting loop
root.mainloop()