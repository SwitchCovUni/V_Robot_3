from Tkinter import *
import tkMessageBox

nameList = []
scoreList = []
descList = []

treasureCounter = 0


def printLists():
    print nameList
    print
    print scoreList
    print
    print descList

class GridDemo( Frame ):

    
    def saveFun(self):
        global treasureCounter
        global treasurePrint

        if treasureCounter != 10:
            if len(self.entryName.get()) != 0 and len(self.entryPoints.get()) != 0 and len(self.entryDesc.get()) != 0:
                nameList.append(self.entryName.get())
                scoreList.append(self.entryPoints.get())
                descList.append(self.entryDesc.get())

                self.entryName.delete(0,1000)
                self.entryPoints.delete(0,1000)
                self.entryDesc.delete(0,1000)

                treasureCounter = treasureCounter + 1
                treasurePrint = str(treasureCounter) + "/10"
                self.labelTreasureNum.config(text=treasurePrint)
            else:
                tkMessageBox.showwarning("Error", "Fill all 3 boxes")
        else:
            tkMessageBox.showwarning("Limit reached", "You've added all treasures, click on Finish Adding Treasures button to continue")
        
    def __init__( self ):

        

        global treasureCounter
        treasurePrint = str(treasureCounter) + "/10"
        
        Frame.__init__( self )
        self.master.title( "Treasure Creator" )

        self.master.rowconfigure( 0, weight = 1 )
        self.master.columnconfigure( 0, weight = 1 )
        self.grid( sticky = W+E+N+S )

        self.labelName = Label(self, text="Treasure Name")
        self.labelName.grid (row = 1, rowspan = 1, column = 1)

        self.labelScore = Label(self, text="Treasure Score")
        self.labelScore.grid (row = 2, rowspan = 1, column = 1)

        self.labelDesc = Label(self, text="Treasure Description")
        self.labelDesc.grid (row = 3, rowspan = 1, column = 1)

        self.labelTreasureCreated = Label(self, text="Treasures Created")
        self.labelTreasureCreated.grid (row = 0, rowspan = 1, column = 1)

        self.labelTreasureNum = Label(self, text=treasurePrint)
        self.labelTreasureNum.grid (row = 0, rowspan = 1, column = 2)
        
        self.entryName = Entry(self)
        self.entryName.grid (row = 1, rowspan = 1,  column = 2, sticky = W+E+N+S) 
 
        self.entryPoints = Entry(self)
        self.entryPoints.grid(row = 2, rowspan = 1, column = 2, sticky = W+E+N+S)

        self.entryDesc = Entry(self)
        self.entryDesc.grid(row = 3, rowspan = 1, column = 2, sticky = W+E+N+S)

        self.saveButton = Button(self, text = "Save this treasure", command=self.saveFun)
        self.saveButton.grid(row = 4, column = 1, columnspan = 2, sticky = W+E+N+S)

        self.finishButton = Button(self, text = "Finish adding treasures")
        self.finishButton.grid(row = 5, column = 1, columnspan = 2, sticky = W+E+N+S)

        self.printLists = Button(self, text = "Print Test", command=printLists)
        self.printLists.grid(row = 6, column = 1, columnspan = 2, sticky = W+E+N+S)
     
        self.rowconfigure( 1, weight = 1 )
        self.columnconfigure( 1, weight = 1 )

def main():
    GridDemo().mainloop()   

if __name__ == "__main__":
    main()
