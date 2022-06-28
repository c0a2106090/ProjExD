from hashlib import blake2b
import tkinter as tk
import tkinter.messagebox as tkm

if __name__ == "__main__":   
    root=tk.Tk()
    root.title("迷えるこうかとん")

    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.place(x=0,y=0)
    canvas.pack()
    tk.mainloop()