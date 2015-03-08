from Tkinter import *
import tkMessageBox

class wishListTesting(Frame):

    def helpButton(self):
        tkMessageBox.showwarning("Help", "Number the treasures by inputting the numbers in the entry boxes. Make sure to use 0-9")

    def saveWishList(self):
        treasureWishlist = open('wishList.txt', 'w')

        orderList = []


        orderList.append(self.entryOne.get()+"1")
        orderList.append(self.entryTwo.get()+"2")
        orderList.append(self.entryThree.get()+"3")
        orderList.append(self.entryFour.get()+"4")
        orderList.append(self.entryFive.get()+"5")
        orderList.append(self.entrySix.get()+"6")
        orderList.append(self.entrySeven.get()+"7")
        orderList.append(self.entryEight.get()+"8")
        orderList.append(self.entryNine.get()+"9")
        orderList.append(self.entryTen.get()+"10")

        orderList.sort()
        print orderList

        for x in range(0, 10):
            treasureWishlist.write(orderList[x][1:])


    def __init__(self, parent, controller):

        Frame.__init__(self, parent)
        # self.master.title("Wish List")
        #
        # self.master.rowconfigure( 0, weight = 1 )
        # self.master.columnconfigure( 0, weight = 1 )
        # self.grid( sticky = W+E+N+S )
        #
        # self.rowconfigure( 1, weight = 1 )
        # self.columnconfigure( 1, weight = 1 )

        self.fr1 = Frame(self, relief="raised", borderwidth=1)

        self.fr1.pack(fill="both", expand=False)

        self.wishlistUI()

        self.saveButton = Button(self.fr1, text="Save Wishlist", command=self.saveWishList)
        self.saveButton.grid (row=11, rowspan = 1, column = 1, columnspan = 3)

        self.helpButton = Button(self.fr1, text="Help", command = self.helpButton)
        self.helpButton.grid (row=11, rowspan = 1, column = 3, columnspan = 1)


    def wishlistUI(self):

        treasureNames = open('pointList.txt', 'r')
        tresaureScores = open('namelist.txt', 'r')


        with open('namelist.txt') as f:
            content = f.readlines()

        with open('pointList.txt') as f:
            pointContent = f.readlines()

        self.labelName = Label(self.fr1, text="Treasure Name")
        self.labelName.grid(row = 0, columnspan = 1, column = 1)

        self.labelScore = Label(self.fr1, text="Point Values")
        self.labelScore.grid(row = 0, columnspan = 1, column = 2)

        self.labelEntry = Label(self.fr1, text="Set the order")
        self.labelEntry.grid(row = 0, columnspan = 1, column = 3)

        self.labelNameOne = Label(self.fr1, text=content[0])
        self.labelNameOne.grid (row = 1, rowspan = 1, column = 1)

        self.labelScoreOne = Label(self.fr1, text=pointContent[0])
        self.labelScoreOne.grid (row = 1, rowspan = 1, column = 2)

        self.entryOne = Entry(self.fr1)
        self.entryOne.grid (row = 1, rowspan = 1, column = 3)

        self.labelNameTwo = Label(self.fr1, text=content[1])
        self.labelNameTwo.grid (row = 2, rowspan = 1, column = 1)

        self.labelScoreTwo = Label(self.fr1, text=pointContent[1])
        self.labelScoreTwo.grid (row = 2, rowspan = 1, column = 2)

        self.entryTwo = Entry(self.fr1)
        self.entryTwo.grid (row = 2, rowspan = 1, column = 3)

        self.labelNameThree = Label(self.fr1, text=content[2])
        self.labelNameThree.grid (row = 3, rowspan = 1, column = 1)

        self.labelScoreThree = Label(self.fr1, text=pointContent[2])
        self.labelScoreThree.grid (row = 3, rowspan = 1, column = 2)

        self.entryThree = Entry(self.fr1)
        self.entryThree.grid (row = 3, rowspan = 1, column = 3)

        self.labelNameFour = Label(self.fr1, text=content[3])
        self.labelNameFour.grid (row = 4, rowspan = 1, column = 1)

        self.labelScoreFour = Label(self.fr1, text=pointContent[3])
        self.labelScoreFour.grid (row = 4, rowspan = 1, column = 2)

        self.entryFour = Entry(self.fr1)
        self.entryFour.grid (row = 4, rowspan = 1, column = 3)

        self.labelNameFive = Label(self.fr1, text=content[4])
        self.labelNameFive.grid (row = 5, rowspan = 1, column = 1)

        self.labelScoreFive = Label(self.fr1, text=pointContent[4])
        self.labelScoreFive.grid (row = 5, rowspan = 1, column = 2)

        self.entryFive = Entry(self.fr1)
        self.entryFive.grid (row = 5, rowspan = 1, column = 3)

        self.labelNameSix = Label(self.fr1, text=content[5])
        self.labelNameSix.grid (row = 6, rowspan = 1, column = 1)

        self.labelScoreSix = Label(self.fr1, text=pointContent[5])
        self.labelScoreSix.grid (row = 6, rowspan = 1, column = 2)

        self.entrySix = Entry(self.fr1)
        self.entrySix.grid (row = 6, rowspan = 1, column = 3)

        self.labelNameSeven = Label(self.fr1, text=content[6])
        self.labelNameSeven.grid (row = 7, rowspan = 1, column = 1)

        self.labelScoreSeven = Label(self.fr1, text=pointContent[6])
        self.labelScoreSeven.grid (row = 7, rowspan = 1, column = 2)

        self.entrySeven = Entry(self.fr1)
        self.entrySeven.grid (row = 7, rowspan = 1, column = 3)

        self.labelNameEight = Label(self.fr1, text=content[7])
        self.labelNameEight.grid (row = 8, rowspan = 1, column = 1)

        self.labelScoreEight = Label(self.fr1, text=pointContent[7])
        self.labelScoreEight.grid (row = 8, rowspan = 1, column = 2)

        self.entryEight = Entry(self.fr1)
        self.entryEight.grid (row = 8, rowspan = 1, column = 3)

        self.labelNameNine = Label(self.fr1, text=content[8])
        self.labelNameNine.grid (row = 9, rowspan = 1, column = 1)

        self.labelScoreNine = Label(self.fr1, text=pointContent[8])
        self.labelScoreNine.grid (row = 9, rowspan = 1, column = 2)

        self.entryNine = Entry(self.fr1)
        self.entryNine.grid (row = 9, rowspan = 1, column = 3)

        self.labelNameTen = Label(self.fr1, text=content[9])
        self.labelNameTen.grid (row = 10, rowspan = 1, column = 1)

        self.labelScoreTen = Label(self.fr1, text=pointContent[9])
        self.labelScoreTen.grid (row = 10, rowspan = 1, column = 2)

        self.entryTen = Entry(self.fr1)
        self.entryTen.grid (row = 10, rowspan = 1, column = 3)
