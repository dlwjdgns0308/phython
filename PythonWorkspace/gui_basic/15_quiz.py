import os
from tkinter import*

root = Tk()
root.title("제목없음 - Window 메모장")
root.geometry("640x480")
frame = Frame(root)
frame.pack()
#root.geometry("640x480+100+300") #가로 세로 +x+y
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

filename = "mynote.txt"
menu = Menu(root)
def open_file():
    with
def save_file():
    pass

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

txt = Text(root, yscrollcommand = scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

txt.insert(END,"")

scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop()