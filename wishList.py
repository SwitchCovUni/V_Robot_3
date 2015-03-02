from Tkinter import *
import tkMessageBox

class wishListTesting(Frame):

    def __init__(self):   
            
        Frame.__init__( self )
        self.master.title("Wish List")

        self.master.rowconfigure( 0, weight = 1 )
        self.master.columnconfigure( 0, weight = 1 )
        self.grid( sticky = W+E+N+S )
        
        self.rowconfigure( 1, weight = 1 )
        self.columnconfigure( 1, weight = 1 )

        self.wishlistUI(self)

    def wishlistUI(self):

        streasureOne = PhotoImage(file="Sprites/smallTreasure1.gif")
        streasureTwo = PhotoImage(file='Sprites/smallTreasure2.gif')
        streasureThree = PhotoImage(file='Sprites/smallTreasure3.gif')
        streasureFour = PhotoImage(file='Sprites/smallTreasure4.gif')
        streasureFive = PhotoImage(file='Sprites/smallTreasure5.gif')
        
        btreasureOne = PhotoImage(file='Sprites/bigTreasure1.gif')
        btreasureTwo = PhotoImage(file='Sprites/bigTreasure2.gif')
        btreasureThree = PhotoImage(file='Sprites/bigTreasure3.gif')
        btreasureFour = PhotoImage(file='Sprites/bigTreasure4.gif')
        btreasureFive = PhotoImage(file='Sprites/bigTresaure5.gif')
        
        treasureNames = open('pointList.txt', 'r')
        tresaureScores = open('treasureNameList.txt', 'r')

        with open('treasureNameList.txt') as f:
            content = f.readlines()0

        with open('pointList.txt') as f:
            pointContent = f.readlines()

        self.labelSpriteOne = Label(self, image=streasureOne)
        self.labelSpriteOne.image = streasureOne
        self.labelSpriteOne.grid(row = 1, rowspawn = 1, column = 1)
        
        self.labelNameOne = Label(self, text=content[0])
        self.labelNameOne.grid (row = 1, rowspan = 1, column = 2)

        self.labelScoreOne = Label(self, text=pointContent[0])
        self.labelScoreOne.grid (row=1, rowspan = 1, column = 3)


            

def main():
    wishListTesting().mainloop()  

if __name__ == "__main__":
    main()
