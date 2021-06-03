from tkinter import *
from random import *
A = []
def rotto():
    e.delete(0,END)
    for i in range(1,7):
        a = randint(1,45)
        A.append(a) 
    for j in A:
        e.insert(0, j)
        e.insert(0, " ") 
    A.clear()
    
root = Tk()
root.title("My Tkinter")
root.geometry("640x480")
root.resizable(True, False)
btn = Button(root, padx=10, pady=10, text="로또번호 출력", command=rotto)
btn.pack()
e = Entry(root, width = 40)
e.pack()
e.insert(0, "로또번호를 출력합니다")

root.mainloop()