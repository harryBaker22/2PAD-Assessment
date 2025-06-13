import tkinter as tk
from tkinter import *

#Item array
hireItems = ["balloon arch", "popcorn machine", "cotton candy machine", "photo booth", "disco ball", "fog machine", "LED dance floor", "bubble machine", "karaoke machine", "folding chairs", "banquet tables", "cocktail tables", "table linens", "chair covers", "sashes", "centerpieces", "string lights", "fairy lights", "party tents", "marquees", "helium tanks", "inflatables", "bounce house", "water slide", "slip and slide", "piñata", "themed backdrops", "stanchions", "red carpet", "cake stand", "cupcake tower", "serving trays", "drink dispensers", "chafing dishes", "cooler bins", "bar setup", "glassware", "plasticware", "plates", "napkins", "cutlery", "table runners", "serving utensils", "candy buffet jars", "popcorn bags", "cotton candy cones", "signage boards", "easels", "party banners", "streamers", "confetti cannons", "party hats", "tiaras", "masks", "wigs", "costumes", "fog juice", "bubble solution", "inflatable arches", "inflatable games", "dunk tank", "yard games", "lawn signs", "chalkboard signs", "sound system", "DJ booth", "microphone", "speakers", "projector", "screen", "LED uplighting", "string curtain backdrop", "sequin backdrop", "balloon pump", "number balloons", "foil balloons", "latex balloons", "balloon weights", "table numbers", "guest book stand", "photo props", "glow sticks", "LED wristbands", "fog chiller", "snow machine", "snow fluid", "throne chair", "peacock chair", "cake cutting set", "dessert stands", "neon signs", "drink stirrers", "straw decorations", "party favors", "party bags", "piñata fillers", "treasure chest prop", "tiki torches", "tropical decor", "fake palm trees", "flameless candles"]

#Background root window
root = Tk()
root.geometry("1x1")
root.iconify()

def goToWindow(currentWindow, targetWindwow):
    currentWindow.destroy()
    targetWindwow()

def createMainWindow():
    global mainWindow
    mainWindow = tk.Toplevel()
    mainWindow.geometry("800x400")
    
    windowWidth = 1000
    windowHeight = 800
        
    #Spawning window in center of the screen
    mainWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, int((root.winfo_screenwidth() / 2) - (windowWidth / 2)), int((root.winfo_screenheight() / 2) - (windowHeight / 2))))
    mainWindow.resizable(False, False)
    mainWindow.overrideredirect(True)
    
    Button(mainWindow, text="Test Button", borderwidth=5, command=lambda: goToWindow(mainWindow, createItemSelection)).pack(pady=30, padx=30)




def createItemSelection():
    global itemSelectionWindow
    itemSelectionWindow = tk.Toplevel()
    
    windowWidth = 500
    windowHeight = 400
    
    itemSelectionWindow.geometry("%dx%d+%d+%d" % (windowWidth, windowHeight, int((root.winfo_screenwidth() / 2) - (windowWidth / 2)), int((root.winfo_screenheight() / 2) - (windowHeight / 2))))
    # itemSelectionWindow.resizable(False, False)
    # itemSelectionWindow.overrideredirect(True)
    
    #Focusing the window
    itemSelectionWindow.focus_force()
    
    # create a main frame to put everything into
    mainFrame = Frame(itemSelectionWindow)
    mainFrame.pack(fill=BOTH, expand=True) # Fills the whole screen, and expands to fit it

    #Creating sidebar for search
    sideBar = Frame(mainFrame)
    sideBar.pack(side=LEFT, fill=Y, expand=True)
    
    searchLabel = Label(sideBar, text="Search", anchor="w")
    searchLabel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    
    searchBar = Entry(sideBar, textvariable="Search...", borderwidth=2)
    searchBar.grid(row=1, column=0, padx=10, sticky="w")
    
    #Test catagory buttons
    Button(sideBar, text="Catagory 1").grid(row=2, column=0, pady=2, padx=10, sticky="w")
    Button(sideBar, text="Catagory 2").grid(row=3, column=0, pady=2, padx=10, sticky="w")

    #Creating frame for canvas to sit in
    itemFrame = Frame(mainFrame)
    itemFrame.pack(side=RIGHT, fill=BOTH, expand=True)
    
    #Creating canvas in main frame
    canvas = Canvas(itemFrame)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)
    # Going on left hand side, and filling to the whole screen, then expanding to fit

    #Adding a scrollbar
    #Scrollbar with vertical orientation(going up and down), and using canvas.yview because its vertical
    scrollbar = Scrollbar(itemFrame, orient=VERTICAL, command=canvas.yview)
    
    #Scrollbar on right side of screen, and filled from top to bottom
    scrollbar.pack(side=RIGHT, fill=Y)

    #Configure the canvas for scrolling
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    #Using mouse wheel to scroll
    canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(int(event.delta / -60), "units"))

    #Frame inside canvas to put things in
    canvasFrame = Frame(canvas)


    #Add frame to window inside canvas
    canvas.create_window((0, 0), window=canvasFrame, anchor="nw")

    for i in range(1, 50):
        Button(canvasFrame, text="{0:^40}".format(hireItems[i*2 - 2]), command= lambda: quit(), width=20).grid(row=i, column=0, pady=10)
        Button(canvasFrame, text="{0:^40}".format(hireItems[i*2 -1]), command= lambda: quit(), width=20).grid(row=i, column=1, pady=10)
    return

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

