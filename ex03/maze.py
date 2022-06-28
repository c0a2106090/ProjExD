from hashlib import blake2b
from itertools import cycle
import tkinter as tk
import tkinter.messagebox as tkm


if __name__ == "__main__":   
    root=tk.Tk()
    root.title("迷えるこうかとん")
    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.place(x=0,y=0)
    canvas.pack()
    
    tori=tk.PhotoImage(file="C:/Users/admin/Downloads/プロジェクト演習/ProjExD2022/ex03/fig/8.png")
    cx=300
    cy=400
    canvas.create_image(cx,cy,image=tori,tag="tori")
    
    key=""
    tk.mainloop()