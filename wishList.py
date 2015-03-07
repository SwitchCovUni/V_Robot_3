from Tkinter import *
import tkMessageBox

class wishListTesting(Frame):

    def helpButton(self):
        tkMessageBox.showwarning("Help", "Number the treasures by inputting the numbers in the entry boxes. Make sure to use 0-9")

    def saveWishList(self):
        treasureWishlist = open('wishListOrder.txt', 'w')

        orderList = []


        orderList.append(self.entryOne.get()+"treasure1")
        orderList.append(self.entryTwo.get()+"treasure2")
        orderList.append(self.entryThree.get()+"treasure3")
        orderList.append(self.entryFour.get()+"treasure4")
        orderList.append(self.entryFive.get()+"treasure5")
        orderList.append(self.entrySix.get()+"treasure6")
        orderList.append(self.entrySeven.get()+"treasure7")
        orderList.append(self.entryEight.get()+"treasure8")
        orderList.append(self.entryNine.get()+"treasure9")
        orderList.append(self.entryTen.get()+"treasure10")

        orderList.sort()
        print orderList

        for x in range(0, 10):
            treasureWishlist.write(orderList[x][1:]+'\n')


    def __init__(self):

        Frame.__init__( self )
        # self.master.title("Wish List")
        #
        # self.master.rowconfigure( 0, weight = 1 )
        # self.master.columnconfigure( 0, weight = 1 )
        # self.grid( sticky = W+E+N+S )

        self.rowconfigure( 1, weight = 1 )
        self.columnconfigure( 1, weight = 1 )

        self.wishlistUI()

    def wishlistUI(self):

        treasureNames = open('pointList.txt', 'r')
        tresaureScores = open('treasureNameList.txt', 'r')


        with open('treasureNameList.txt') as f:
            content = f.readlines()

        with open('pointList.txt') as f:
            pointContent = f.readlines()

        self.labelName = Label(self, text="Treasure Name")
        self.labelName.grid(row = 0, columnspan = 1, column = 1)

        self.labelScore = Label(self, text="Point Values")
        self.labelScore.grid(row = 0, columnspan = 1, column = 2)

        self.labelEntry = Label(self, text="Set the order")
        self.labelEntry.grid(row = 0, columnspan = 1, column = 3)

        self.labelNameOne = Label(self, text=content[0])
        self.labelNameOne.grid (row = 1, rowspan = 1, column = 1)

        self.labelScoreOne = Label(self, text=pointContent[0])
        self.labelScoreOne.grid (row = 1, rowspan = 1, column = 2)

        self.entryOne = Entry(self)
        self.entryOne.grid (row = 1, rowspan = 1, column = 3)

        self.labelNameTwo = Label(self, text=content[1])
        self.labelNameTwo.grid (row = 2, rowspan = 1, column = 1)

        self.labelScoreTwo = Label(self, text=pointContent[1])
        self.labelScoreTwo.grid (row = 2, rowspan = 1, column = 2)

        self.entryTwo = Entry(self)
        self.entryTwo.grid (row = 2, rowspan = 1, column = 3)

        self.labelNameThree = Label(self, text=content[2])
        self.labelNameThree.grid (row = 3, rowspan = 1, column = 1)

        self.labelScoreThree = Label(self, text=pointContent[2])
        self.labelScoreThree.grid (row = 3, rowspan = 1, column = 2)

        self.entryThree = Entry(self)
        self.entryThree.grid (row = 3, rowspan = 1, column = 3)

        self.labelNameFour = Label(self, text=content[3])
        self.labelNameFour.grid (row = 4, rowspan = 1, column = 1)

        self.labelScoreFour = Label(self, text=pointContent[3])
        self.labelScoreFour.grid (row = 4, rowspan = 1, column = 2)

        self.entryFour = Entry(self)
        self.entryFour.grid (row = 4, rowspan = 1, column = 3)

        self.labelNameFive = Label(self, text=content[4])
        self.labelNameFive.grid (row = 5, rowspan = 1, column = 1)

        self.labelScoreFive = Label(self, text=pointContent[4])
        self.labelScoreFive.grid (row = 5, rowspan = 1, column = 2)

        self.entryFive = Entry(self)
        self.entryFive.grid (row = 5, rowspan = 1, column = 3)

        self.labelNameSix = Label(self, text=content[5])
        self.labelNameSix.grid (row = 6, rowspan = 1, column = 1)

        self.labelScoreSix = Label(self, text=pointContent[5])
        self.labelScoreSix.grid (row = 6, rowspan = 1, column = 2)

        self.entrySix = Entry(self)
        self.entrySix.grid (row = 6, rowspan = 1, column = 3)

        self.labelNameSeven = Label(self, text=content[6])
        self.labelNameSeven.grid (row = 7, rowspan = 1, column = 1)

        self.labelScoreSeven = Label(self, text=pointContent[6])
        self.labelScoreSeven.grid (row = 7, rowspan = 1, column = 2)

        self.entrySeven = Entry(self)
        self.entrySeven.grid (row = 7, rowspan = 1, column = 3)

        self.labelNameEight = Label(self, text=content[7])
        self.labelNameEight.grid (row = 8, rowspan = 1, column = 1)

        self.labelScoreEight = Label(self, text=pointContent[7])
        self.labelScoreEight.grid (row = 8, rowspan = 1, column = 2)

        self.entryEight = Entry(self)
        self.entryEight.grid (row = 8, rowspan = 1, column = 3)

        self.labelNameNine = Label(self, text=content[8])
        self.labelNameNine.grid (row = 9, rowspan = 1, column = 1)

        self.labelScoreNine = Label(self, text=pointContent[8])
        self.labelScoreNine.grid (row = 9, rowspan = 1, column = 2)

        self.entryNine = Entry(self)
        self.entryNine.grid (row = 9, rowspan = 1, column = 3)

        self.labelNameTen = Label(self, text=content[9])
        self.labelNameTen.grid (row = 10, rowspan = 1, column = 1)

        self.labelScoreTen = Label(self, text=pointContent[9])
        self.labelScoreTen.grid (row = 10, rowspan = 1, column = 2)

        self.entryTen = Entry(self)
        self.entryTen.grid (row = 10, rowspan = 1, column = 3)

        self.saveButton = Button(self, text="Save Wishlist", command=self.saveWishList)
        self.saveButton.grid (row=11, rowspan = 1, column = 1, columnspan = 3)

        self.helpButton = Button(self, text="Help", command = self.helpButton)
        self.helpButton.grid (row=11, rowspan = 1, column = 3, columnspan = 1)
def main():
    wishListTesting().mainloop()

if __name__ == "__main__":
    main()
