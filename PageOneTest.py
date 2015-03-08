import Tkinter as tk
from Tkinter import *

LARGE_FONT = ("Verdana", 12)

nameList = []
scoreList = []
descList = []

treasureCounter = 0
scoreCount = 0

class PageOne(tk.Frame):
    fr1 = []
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.fr1 = tk.Frame(self, relief="raised", borderwidth=1)

        self.fr1.pack(fill="both", expand=False)

        # label = tk.Label(self.fr1, text="Page 1", font=LARGE_FONT)
        # label.pack(pady=10,padx=10)
        #
        # button2 = tk.Button(self.fr1, text="back to home",
        #                     command=lambda: controller.show_frame(StartPage))
        # button2.pack()

        global treasureCounter
        treasurePrint = str(treasureCounter) + "/10"

        Frame.__init__( self, parent)
        #self.master.title( "Treasure Creator" )
        #
        #self.master.pack_propagate(0)
        #
        # self.master.rowconfigure( 0, weight = 1 )
        # self.master.columnconfigure( 0, weight = 1 )
        # self.grid( sticky = W+E+N+S )

        self.fr1 = tk.Frame(self, relief="raised", borderwidth=1)
        self.fr1.pack(fill="both", expand=1)


        labelName = Label(self.fr1, text="Treasure Name")
        labelName.grid (row = 1, rowspan = 1, column = 1)

        labelScore = Label(self.fr1, text="Treasure Score")
        labelScore.grid (row = 2, rowspan = 1, column = 1)

        labelDesc = Label(self.fr1, text="Treasure Description")
        labelDesc.grid (row = 3, rowspan = 1, column = 1)

        labelTreasureCreated = Label(self.fr1, text="Treasures Created")
        labelTreasureCreated.grid (row = 0, rowspan = 1, column = 1)

        labelTreasureNum = Label(self.fr1, text=treasurePrint)
        labelTreasureNum.grid (row = 0, rowspan = 1, column = 2)

        entryName = Entry(self.fr1)
        entryName.grid (row = 1, rowspan = 1,  column = 2, sticky = W+E+N+S)

        entryPoints = Entry(self.fr1)
        entryPoints.grid(row = 2, rowspan = 1, column = 2, sticky = W+E+N+S)

        entryDesc = Entry(self.fr1)
        entryDesc.grid(row = 3, rowspan = 1, column = 2, sticky = W+E+N+S)

        saveButton = Button(self.fr1, text = "Save this treasure", command=self.saveFun)
        saveButton.grid(row = 4, column = 1, columnspan = 2, sticky = W+E+N+S)

        finishButton = Button(self.fr1, text = "Finish adding treasures", command=self.listGenerate)
        finishButton.grid(row = 5, column = 1, columnspan = 2, sticky = W+E+N+S)

        # self.rowconfigure( 1, weight = 1 )
        # self.columnconfigure( 1, weight = 1 )
