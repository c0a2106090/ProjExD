import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker



def key_down(event):
    global key 
    key=event.keysym

def key_up(event):
    global key
    key=""

def main_proc():
    global mx,my,key
    if key=="Up" :
        if mass[my-1][mx]==0:
            my-=1
        else:
            root.destroy()
    elif key=="Down" :
        if mass[my+1][mx]==0:
            my+=1
        else:
            root.destroy()
    elif key=="Left" :
        if mass[my][mx-1]==0:
            mx-=1
        else:
            root.destroy()
    elif key=="Right" :
        if mass[my][mx+1]==0:
            mx+=1
        else:
            root.destroy()
    x=mx*100+50
    y=my*100+50
    canvas.coords("tori",x,y)
    root.after(100,main_proc)

if __name__ == "__main__":   
    root=tk.Tk()
    root.title("迷えるこうかとん")
    label=tk.Label(root,font=(80))
    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.place(x=0,y=0)
    canvas.pack()
    
    mass=maze_maker.make_maze(15,9)
    maze_maker.show_maze(canvas,mass)


    tori=tk.PhotoImage(file="C:/Users/admin/Downloads/プロジェクト演習/ProjExD2022/ex03/fig/8.png")
    mx,my=1,1
    cx=100
    cy=100
    canvas.create_image(cx,cy,image=tori,tag="tori")
    
    key=""
    main_proc()
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    tk.mainloop()