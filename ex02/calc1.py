import tkinter as tk
import tkinter.messagebox as tkm
root=tk.Tk()
root.geometry("300x500")

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    tkm.showinfo(txt,f"{txt}のボタンがクリックされました")

def Bottonmake(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            button=tk.Button(root,text=str(a[i][j]),height=2,width=4)
            button.grid(row=i+1,column=j+1)
            button.bind("<1>",button_click)


Bottonname=[[9,8,7],[6,5,4],[3,2,1],[0,"+","="]]
Bottonmake(Bottonname)

root.mainloop()