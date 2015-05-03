# defining and testing the sudokubox and skyscraper info box classes

from tkinter import *

root=Tk()

class SkyBox(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.button=Button(parent,
                        text="1",
                        relief=FLAT,
                        fg="black",
                        activeforeground="black",
                        width=2,
                        command=self.switch)
        self.button.pack()
        # plan for the future: on hover, show how many it currently sees
        # advanced version: range for max and min
        #self.bind('<Enter>',skyhover)
        
    def switch(self):
        if self.button.cget("fg")=="white":
            self.button.configure(fg="black", activeforeground="black")
        else:
            self.button.configure(fg="white", activeforeground="white")
    def disable(self):
        self.button.configure(state=DISABLED, text="")

# single Sudoku button inside a box (1-9). Parent is a SudBox.
# contains the code for updating/removing values from the box

class SudButton(Button):
    # need box identity + which number (1-9) it's going to be to initiate
    def __init__(self,parent,n):
        self.parent=parent
        Button.__init__(self,
                        parent,
                        text=n,
                        font=("Helvetica", 8),
                        foreground="white",
                        activeforeground="white",
                        disabledforeground="white",
                        background="white",
                        highlightbackground="blue",
                        width=1,
                        relief=FLAT,
                        command=self.click)
        self.value=n
        self.enabled=0
    # upon click or keystroke, we switch around
    # also changes values in parent
    def click(self):
        n=self.value
        if self.enabled==0:
            self.config(foreground="black", activeforeground="black")
            self.enabled=1
            self.parent.values.append(n)
            self.parent.values.sort()
        else:
            self.config(foreground="white", activeforeground="white")
            self.enabled=0
            self.parent.values.remove(n)
        # if there's now only one value, send it to the big label!
        if len(self.parent.values)==1:
            self.parent.thevalue=(str(self.parent.values[0]))
        else:
            self.parent.thevalue=""
        self.parent.label.config(text=self.parent.thevalue)
    # option to remove entirely if we're playing with a less than 9x9 grid
    def kill(self):
        self.config(state=DISABLED)
        

class SudBox(Frame):
    def __init__(self, parent):
        self.parent=parent
        Frame.__init__(self, parent)
        # family of 1-9 buttons
        self.buttons={}
        for i in range(3):
            for j in range(3):
                n=3*i+j+1
                self.buttons[n]=SudButton(self,n)
                self.buttons[n].grid(row=i,column=j)
        # and one big label if there's only one selected?
        self.thevalue=""
        self.label=Label(self,
                         text="",
                         font=("Helvetica", 32),
                         bg="white")
        # said label fills out the entire box
        self.label.grid(row=0,column=0, rowspan=3, columnspan=3, sticky=N+S+W+E)
        self.label.lower(self.buttons[1])
        # and a list of values
        self.values=[]
        self.bind("<Enter>", self.onEnter)
        self.bind("<Leave>", self.onLeave)
    def onLeave(self, event):
        if self.thevalue:
            self.label.lift(self.buttons[9])
        else:
            self.label.lower(self.buttons[1])
    def onEnter(self, event):
        self.label.lower(self.buttons[1])

# plan for the future: make this into a hoverbox
# showing how many skyscrapers the box currently sees
#def skyhover(event):
#    print(event.widget.icoord + event.widget.jcoord)
def printvalues():
    print(Sud.thevalue)
    
Blub=SkyBox(root)
Sud=SudBox(root)
testbutton=Button(root, text="Click me to test!", command=printvalues)

testbutton.pack(side=RIGHT)
Blub.pack(side=TOP)
Sud.pack(side=TOP)


root.mainloop()
