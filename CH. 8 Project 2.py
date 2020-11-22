from tkinter import *

class BounyGUI(Frame):
    def _compute(self):
        initialHeight=self._heightVar.get()
        bounceyIndex=self._indexVar.get()
        numberOfBonce=self._bounceVar.get()
        bounceHeight=initialHeight*bounceyIndex
        totalDistance=initialHeight
        for i in range(1,(int(numberOfBonce))):
            totalDistance+=(2*bounceHeight)
            bounceHeight=bounceHeight*bounceyIndex
        totalDistance+=bounceHeight
        self._computeVar.set(totalDistance)

    def __init__(self):
        Frame.__init__(self)
        self.master.title("Bouncy")
        self.grid()

        self._heightLabel=Label(self,text="Initial height")
        self._heightLabel.grid(row=0,column=0)
        self._heightVar = DoubleVar()
        self._heightEntry=Entry(self,textvariable = self._heightVar)
        self._heightEntry.grid(row=0,column=1)

        self._indexLabel=Label(self,text="Index")
        self._indexLabel.grid(row=1,column=0)
        self._indexVar = DoubleVar()
        self._indexEntry=Entry(self,textvariable = self._indexVar)
        self._indexEntry.grid(row=1,column=1)

        self._bounceLabel=Label(self,text="Number of Bounces: ")
        self._bounceLabel.grid(row=2,column=0)
        self._bounceVar = DoubleVar()
        self._bounceEntry=Entry(self,textvariable = self._bounceVar)
        self._bounceEntry.grid(row=2,column=1)

        self._computeButton = Button(self,text="Compute",command=self._compute)
        self._computeButton.grid(row=3,column=0)

        self._computeLabel=Label(self,text="Total Distance: ")
        self._computeLabel.grid(row=4,column=0)
        self._computeVar = DoubleVar()
        self._computeEntry=Entry(self,textvariable = self._computeVar)
        self._computeEntry.grid(row=4,column=1)

def main():
    my_gui = BounyGUI()
    my_gui.mainloop()

main()
