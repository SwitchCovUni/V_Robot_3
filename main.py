import Tkinter as tk
from Tkinter import *

LARGE_FONT = ("Verdana", 12)

import TreasureGen
import MapGenUI
import PageOneTest
import wishList

class main(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="none", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.grid_propagate(1)
        self.frames = {}
        
        # Load all files with frames as modules
        TG = TreasureGen.TreasureGen
        MGU = MapGenUI.TreasureAdderUI
        TN = MapGenUI.trapNumber
        WL = wishList.wishListTesting
        
        # Loop to extract all the tramse in to dictionary
        for F in (TG, MGU, TN, WL):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(TG)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


def qf(quickPrint):
    print(quickPrint)

treasureCounter = 0


app = main()
app.mainloop()
