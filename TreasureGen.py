from Tkinter import *
import Tkinter as tk
import tkFileDialog

import PageOneTest

import MapGenUI

class TreasureGen(tk.Frame):
    fr1 = []
    button_array = []
    type_list = []

    photo1 = ""
    photo2 = ""
    photo3 = ""
    photo4 = ""

    file_type = [('Switch files', '*.switch')]

    change_image = ""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.fr1 = tk.Frame(self, relief="raised", borderwidth=1)


        self.photo1 = tk.PhotoImage(file="sprites/floorSprite.gif")
        self.photo2 = tk.PhotoImage(file="sprites/smallTreasure1.gif")
        self.photo3 = tk.PhotoImage(file="sprites/smallTreasure2.gif")
        self.photo4 = tk.PhotoImage(file="sprites/smallTreasure3.gif")

        self.fr1.pack(fill="both", expand=1)

        for n in range(0,1560):
            self.type_list.append(1)

        count = 1
        row = 0
        col = 0
        for n in range(0,1560):
            self.button_array.append(tk.Button(self.fr1, text = str(n),
                image = self.photo1, height = 18, width = 18, borderwidth= -1,
                padx = 0, pady = 0, relief="flat"))
            self.button_array[n].image = self.photo1
            if not (col == 5 or col == 19 or col == 34):
                self.button_array[n].bind('<Button-1>', self.buttonAction)
            else:
                self.change_image = tk.PhotoImage(file="sprites/rlight.gif")
                self.button_array[n].configure(image = self.change_image)
                self.button_array[n].image = self.change_image

            self.button_array[n].grid(row=row , column=col)

            col += 1

            if count==40:
                row += 1
                col = 0
                count = 0

            count += 1

        self.pack(fill="both", expand=1)

        MN = MapGenUI.TreasureAdderUI


        def saveMap(self):
            treasureMap = open('num.txt', 'w')

            savetext = ""
            for n in range(0,1560):
                savetext += str(self.type_list[n])

            treasureMap.write(orderList[x][1:])

        def multifunction(*args):
            for function in args:
                return function()

        nextButton = Button(self, text="Next",
                            command=lambda: multifunction(o, controller.show_frame(MN)))
        nextButton.pack(side="right", padx=5, pady=5)

        loadButton = Button(self, text="Load Map", command = self.loadFile)
        loadButton.pack(side="right", padx=5, pady=5)

        saveButton = Button(self, text="Save Map", command = self.fileSave)
        saveButton.pack(side="right", padx=5, pady=5)

    def buttonAction(self, event):
        print "This is an event binding test"
        print event.widget['text']

        for n in range(0,1560):
            if int(event.widget['text']) == n:
                self.buttonType(n)


    def buttonType(self, n):

        if self.type_list[n] == 1:
            self.type_list[n] = 3
            self.change_image = self.photo2
        elif self.type_list[n] == 3:
            self.type_list[n] = 4
            self.change_image = self.photo3
        elif self.type_list[n] == 4:
            self.type_list[n] = 5
            self.change_image = self.photo4
        elif self.type_list[n] == 5:
            self.type_list[n] = 1
            self.change_image = self.photo1

        self.button_array[n].configure(image = self.change_image)
        self.button_array[n].image = self.change_image
        tr = ""
        for n in range(0,1560):
            tr += str(self.type_list[n])

        print tr

    def loadFile(self):
        load_dialog = tkFileDialog.Open(self, filetypes = self.file_type)
        f = load_dialog.show()

        if f != '':
            loadable = self.readFile(f)
            print loadable
            # Loop splits file characters into the list

            for n in range(0,1560):
                self.type_list[n] = int(loadable[n])

            count = 1
            col = 0
            for n in range(0,1560):
                print str(self.type_list[n])
                if not (col == 5 or col == 19 or col == 34):
                    if self.type_list[n] == 1:
                        self.change_image = self.photo1
                    elif self.type_list[n] == 3:
                        self.change_image = self.photo2
                    elif self.type_list[n] == 4:
                        self.change_image = self.photo3
                    elif self.type_list[n] == 5:
                        self.change_image = self.photo4

                    self.button_array[n].configure(image = self.change_image)
                    self.button_array[n].image = self.change_image
                col += 1

                if count==40:
                    col = 0
                    count = 0
                count += 1

    def readFile(self, filename):

        f = open(filename, "r")
        text = f.read()
        return text

    def fileSave(self):
        f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".switch",
            filetypes = self.file_type)
        if f is None:
            return

        savetext = ""
        for n in range(0,1560):
            savetext += str(self.type_list[n])

        f.write(savetext)
        f.close()

    def nextFrame(self):
        page2 = MapGenUI.TreasureAdderUI()

        page2.mainloop()


def main():

    root = Tk()
    # root.geometry("800x815")
    app = TreasureGen(root)
    root.mainloop()


if __name__ == '__main__':
    main()
