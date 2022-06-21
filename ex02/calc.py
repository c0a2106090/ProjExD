import tkinter as tk
import tkinter.messagebox as tkm
def Bottonmake(a):
    for i in range(3):
        for j in range(3):
            button=tk.Button(root,text=str(a[i][j]),height=2,width=4,font=("Times New Roman",30))
            button.grid(row=i,column=j)
            button.bind("<1>",button_click)
    button=tk.Button(root,text="0",height=2,width=4,font=("Times New Roman",30))
    button.grid(row=4,column=0)
    button.bind("<1>",button_click)

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    tkm.showinfo(txt,f"{txt}のボタンがクリックされました")

if __name__ == "__main__":  
    root=tk.Tk()
    root.geometry("300x500")
    Bottonname=[[9,8,7],[6,5,4],[3,2,1],[0,"",""]]
    Bottonmake(Bottonname)

    root.mainloop()