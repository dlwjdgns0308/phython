from tkinter import *

root = Tk()
root.title("음식주문 프로그램")
root.geometry("480x600")
root.resizable(False,False)
def order():
    hello = 0
    hello = int(chkvar1.get() * 8100 + chkvar2.get() * 8100 + chkvar3.get() * 8100 + chkvar4.get() * 8100 
    + chkvar5.get() * 8100 + chkvar6.get() * 8100 + chkvar7.get() * 8100 + 
     chkvar8.get() * 8100 + chkvar9.get() * 8100 )
    print(hello + "원입니다. 감사합니다")
Button(root, text="주문하기", command=order).pack(side="bottom")

large = LabelFrame(root, text="라지세트")
large.pack(fill="both", expand=True)
chkvar1 = IntVar()
chkvar2 = IntVar()
chkvar3 = IntVar()
chkvar4 = IntVar()
chkvar5 = IntVar()
chkvar6 = IntVar()
chkvar7 = IntVar()
chkvar8 = IntVar()
chkvar9 = IntVar()
chkbox1 = Checkbutton(large, text="빅맥 라지세트", variable=chkvar1).pack()
chkbox2 = Checkbutton(large, text="상하이 라지세트", variable=chkvar2).pack()
chkbox3 = Checkbutton(large, text="베이컨 토마토 디럭스 라지세트", variable=chkvar3).pack()

set = LabelFrame(root, text="세트")
set.pack(fill="both", expand=True)
chkbox4 = Checkbutton(set, text="빅맥 세트", variable=chkvar4).pack()
chkbox5 = Checkbutton(set, text="상하이 세트", variable=chkvar5).pack()
chkbox6 = Checkbutton(set, text="베이컨 토마토 디럭스 세트", variable=chkvar6).pack()

side = LabelFrame(root, text="사이드 메뉴")
side.pack(fill="both", expand=True)
chkbox7 = Checkbutton(side, text="맥너겟", variable=chkvar7).pack()
chkbox8 = Checkbutton(side, text="아이스크림", variable=chkvar8).pack()
chkbox9 = Checkbutton(side, text="맥윙", variable=chkvar9).pack()
root.mainloop()