from Tkinter import *
import tkMessageBox

nameList = []
scoreList = []
descList = []

treasureCounter = 0
scoreCount = 0


class TreasureAdderUI(Frame):

    def trapSave(self):
        treasurePointMap = open("pointList.txt", "a")
        treasurePointMap.write(self.entryTrapNumber.get())
           
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

    def listGenerate(self):
        
        global scoreList
        global scoreCount
        trapCounter = 0
      
        if treasureCounter == 10:
        
            originalMap = open('num.txt', 'r')
            orgRead = originalMap.read()
            treasurePointMap = open('pointList.txt', 'w')

            for fileCount in scoreList:
                if scoreCount < len(scoreList):
                    newVal = (scoreList[scoreCount])
                    treasurePointMap.write(newVal+"\n")
                    scoreCount += 1
            
            Frame.__init__( self )
            self.master.title( "Traps" )
    
            self.master.rowconfigure( 0, weight = 1 )
            self.master.columnconfigure( 0, weight = 1 )
            self.grid( sticky = W+E+N+S )

            self.labelTrapNumber = Label(self, text="Number of traps")
            self.labelTrapNumber.grid (row = 1, rowspan = 1, column = 1)

            self.entryTrapNumber = Entry(self)
            self.entryTrapNumber.grid (row = 1, rowspan = 1,  column = 2, sticky = W+E+N+S)

            self.trapButton = Button(self, text = "Save Traps", command=self.trapSave)
            self.trapButton.grid(row = 2, column = 1, columnspan = 2, sticky = W+E+N+S)
            
        
        else:
            tkMessageBox.showwarning("Not enough Treasure", "You haven't added all the treasure yet!")
                                 
    def __init__(self):

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

        self.finishButton = Button(self, text = "Finish adding treasures", command=self.listGenerate)
        self.finishButton.grid(row = 5, column = 1, columnspan = 2, sticky = W+E+N+S)
     
        self.rowconfigure( 1, weight = 1 )
        self.columnconfigure( 1, weight = 1 )

def main():
    TreasureAdderUI().mainloop()   

if __name__ == "__main__":
    main()
