from Tkinter import *
import tkMessageBox
import Tkinter

import wishList

nameList = []
scoreList = []
descList = []

treasureCounter = 0
scoreCount = 0
treasurePointMap = []

class TreasureAdderUI(Frame):
    fr1 = []

    finishButton = []

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

        if treasureCounter == 10:
            self.listGenerate()
    def listGenerate(self):

        global scoreList
        global scoreCount
        trapCounter = 0

        if treasureCounter == 10:

            originalMap = open('num.txt', 'r')
            orgRead = originalMap.read()
            self.treasurePointMap = open('pointList.txt', 'w')
            treasureNamesFile = open('namelist.txt', 'w')

            for fileCount in scoreList:
                if scoreCount < len(scoreList):
                    newVal = (scoreList[scoreCount])
                    self.treasurePointMap.write(newVal+"\n")
                    scoreCount += 1

            scoreCount = 0

            for fileCount in nameList:
                if scoreCount < len(nameList):
                    newVal = (nameList[scoreCount])
                    treasureNamesFile.write(newVal+"\n")
                    scoreCount += 1

            self.finishButton.configure(state=NORMAL)

        else:
            tkMessageBox.showwarning("Not enough Treasure", "You haven't added all the treasure yet!")

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        self.fr1 = Frame(self, relief="raised", borderwidth=1)

        self.fr1.pack(fill="both", expand=False)

        global treasureCounter
        treasurePrint = str(treasureCounter) + "/10"

        Frame.__init__( self, parent)


        self.fr1 = Frame(self, relief="raised", borderwidth=1)
        self.fr1.pack(fill="both", expand=1)


        self.labelName = Label(self.fr1, text="Treasure Name")
        self.labelName.grid (row = 1, rowspan = 1, column = 1)

        self.labelScore = Label(self.fr1, text="Treasure Score")
        self.labelScore.grid (row = 2, rowspan = 1, column = 1)

        self.labelDesc = Label(self.fr1, text="Treasure Description")
        self.labelDesc.grid (row = 3, rowspan = 1, column = 1)

        self.labelTreasureCreated = Label(self.fr1, text="Treasures Created")
        self.labelTreasureCreated.grid (row = 0, rowspan = 1, column = 1)

        self.labelTreasureNum = Label(self.fr1, text=treasurePrint)
        self.labelTreasureNum.grid (row = 0, rowspan = 1, column = 2)

        self.entryName = Entry(self.fr1)
        self.entryName.grid (row = 1, rowspan = 1,  column = 2, sticky = W+E+N+S)

        self.entryPoints = Entry(self.fr1)
        self.entryPoints.grid(row = 2, rowspan = 1, column = 2, sticky = W+E+N+S)

        self.entryDesc = Entry(self.fr1)
        self.entryDesc.grid(row = 3, rowspan = 1, column = 2, sticky = W+E+N+S)

        self.saveButton = Button(self.fr1, text = "Save this treasure", command=self.saveFun)
        self.saveButton.grid(row = 4, column = 1, columnspan = 2, sticky = W+E+N+S)

        self.finishButton = Button(self.fr1, text = "Finish adding treasures", state=DISABLED, command=lambda: controller.show_frame(trapNumber))
        self.finishButton.grid(row = 5, column = 1, columnspan = 2, sticky = W+E+N+S)


class trapNumber(Frame):
    fr1 = []
    trapButton = []

    def trapSave(self):
        self.treasurePointMap = open("pointList.txt", "a")
        self.treasurePointMap.write(self.entryTrapNumber.get())

    def __init__(self, parent, controller):

        Frame.__init__( self, parent )
        # self.master.title( "Traps" )
        #
        #
        # self.master.rowconfigure( 0, weight = 1 )
        # self.master.columnconfigure( 0, weight = 1 )
        # self.grid( sticky = W+E+N+S )
        self.fr1 = Frame(self, relief="raised", borderwidth=1)
        self.fr1.pack(fill="both", expand=1)

        self.labelTrapNumber = Label(self.fr1, text="Number of traps")
        self.labelTrapNumber.grid (row = 1, rowspan = 1, column = 1)

        #tk_name = StringVar()
        #tk_name.set("")
        #tk_name.trace("w", self.text_changed)

        #self.entryTrapNumber = Entry(self.fr1, textvariable=tk_name)
        #self.entryTrapNumber.grid (row = 1, rowspan = 1,  column = 2, sticky = W+E+N+S)

        def text_changed(*args):
            s = tk_name.get()
            try:
                int(s)
                s = int(s)
                if s > 0 and s < 26:
                    print 'Yes'
                    self.trapButton.configure(state=NORMAL)
                else:
                    print 'no'
                    self.trapButton.configure(state=DISABLED)
            except ValueError:
                print "no"
                self.trapButton.configure(state=DISABLED)



        tk_name=Tkinter.StringVar()
        tk_name.set("")
        tk_name.trace("w", text_changed)

        entry_1 = Tkinter.Entry(self.fr1, textvariable=tk_name)
        entry_1.grid(row=1, column=1, sticky="W")

        WL = wishList.wishListTesting

        def multifunction(*args):
            for function in args:
                return function()

        self.trapButton = Button(self.fr1, text = "Save Traps", state=DISABLED, command=lambda: multifunction(self.trapSave, controller.show_frame(WL)))
        self.trapButton.grid(row = 2, column = 1, columnspan = 2, sticky = W+E+N+S)


def main():
    root = Tk()
    root.geometry("500x815")
    app = TreasureAdderUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
