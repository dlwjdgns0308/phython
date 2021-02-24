from tkinter import*

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 맨 윗줄
btn_f16 = Button(root, text="F16")
btn_f17 = Button(root, text="F17")
btn_f18 = Button(root, text="F18")
btn_f19 = Button(root, text="F19")

btn_f16.grid(row=0, column=0)
btn_f17.grid(row=0, column=1)
btn_f18.grid(row=0, column=2)
btn_f19.grid(row=0, column=3)

#클리어 줄
btn_clear = Button(root, text="clear")
btn_equal = Button(root, text="=")
btn_div = Button(root, text="/")
btn_mul = Button(root, text="*")

btn_clear.grid(row=1, column=0, sticky=N+E+W+S)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S)
btn_div.grid(row=1, column=2, sticky=N+E+W+S)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S)

btn_enter = Button(root, text="enter")
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S) #현재 위치로부터 아래쪽으로 2칸

btn_0 = Button(root, text="0")
btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S) #현재 위치로부터 오른쪽으로 2칸
root.mainloop()