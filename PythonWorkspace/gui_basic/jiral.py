from tkinter import *
from random import *
A = []
def rotto():
    for i in range(1,7):
        a = randint(1,45)
        A.append(a) 
    print(A)
    A.clear()
    
root = Tk()
root.title("My Tkinter")
root.geometry("640x480")
root.resizable(True, False)
btn = Button(root, padx=10, pady=10, text="랜덤번호 입력", command=rotto)
btn.pack()
root.mainloop()