from pickle import TRUE
import tkinter as tk
import tkinter.messagebox as tkm
import math
def Buttonmake(a):
    global entry
    entry=tk.Entry(root,justify="right",width=10,font=("Times New Roman", 40))
    entry.grid(columnspan=5)
    for i in range(len(a)):
        for j in range(len(a[0])):  #二重for文で二次元リスト通りに配置
            button=tk.Button(root,text=str(a[i][j]),height=1,width=4,font=("Times New Roman",30))
            button.grid(row=i+1,column=j)   #入力欄が上に入るのでi+1で1つずらす
            button.bind("<1>",button_click)

def makeFormula(F): #eval関数入れられる形に変換
    global INT  #小数点以下切り捨てを行うかの情報を保持するグローバル変数:INT
    INT=False
    F=F[:-1]
    F=F.replace("×","*")
    F=F.replace("÷","/")
    F=F.replace("^","**")
    if "TAX" in F:
        F=F.replace("TAX","*1.08")
        INT=TRUE
    if F[-1]=="!":
        F=kaijyou(F)
    return F

def kaijyou(n): #階乗
    F=n[:-1]
    F=int(F)
    a=1
    for i in range(F,1,-1):
        a*=i
    return str(a)

def button_click(event): #ボタンクリック時に呼び出される
    btn=event.widget
    num=btn["text"]
    if num=="C": #Cのみそのまま入力欄に文字を入れないので.
        entry.delete(0,tk.END)
    else:
        entry.insert(tk.END,num)
    if num=="=":
        Formula=makeFormula(entry.get())
        entry.delete(0,tk.END)
        ans=eval(Formula)
        if INT==TRUE:    #整数化する場合はansの値を小数点以下切り捨てたものに更新
            ans=math.floor(int(ans))
        entry.insert(0,ans)

if __name__ == "__main__":  
    root=tk.Tk()
    root.geometry("400x500")
    Buttonname=[["C","TAX","!","^"],[7,8,9,"÷"],[4,5,6,"×"],[1,2,3,"-"],["00",0,"=","+"]] #Cは全消去ボタン
    Buttonmake(Buttonname)
    root.mainloop()