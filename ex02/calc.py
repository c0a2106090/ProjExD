import tkinter as tk
import tkinter.messagebox as tkm
def Bottonmake(a):
    global entry
    entry=tk.Entry(root,justify="right",width=10,font=("Times New Roman", 40))
    entry.grid(columnspan=4)
    for i in range(len(a)):
        for j in range(len(a[0])):
            button=tk.Button(root,text=str(a[i][j]),height=2,width=4,font=("Times New Roman",30))
            button.grid(row=i+1,column=j+1)
            button.bind("<1>",button_click)
    #button=tk.Button(root,text="0",height=2,width=4,font=("Times New Roman",30))
    #button.grid(row=4,column=0)
    #button.bind("<1>",button_click)

def button_click(event):
    btn=event.widget
    num=btn["text"]
    #tkm.showinfo(txt,f"{txt}のボタンがクリックされました")
    entry.insert(tk.END,num)
    if num=="=":
        Formula=entry.get()[:-1]
        entry.delete(0,tk.END)
        entry.insert(0,eval(Formula))

if __name__ == "__main__":  
    root=tk.Tk()
    root.geometry("300x600")
    Bottonname=[[9,8,7],[6,5,4],[3,2,1],[0,"+","="]]
    Bottonmake(Bottonname)

    root.mainloop()