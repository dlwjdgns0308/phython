from tkinter import *

root = Tk()
root.title("Menu Pad")
root.geometry("480x640")
root.resizable(False,False)
def epic():
    
menu1 = Button(root, text="에피타이저", command=epic)
menu1.pack()
root.mainloop()