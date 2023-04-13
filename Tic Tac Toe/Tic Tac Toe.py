from tkinter import *
count=0
def game():
    global count
    root=Tk()
    root.geometry("300x430+200+150")
    root.title("Tic Tac Toe")
    f1=Frame(root)
    f1.pack()
    Label(f1,text="TIC TAC TOE",font="comics 20",pady=10).grid(row=0,column=1,columnspan=3)
    f2=Frame(root)
    f2.pack()
    x,o="X","O"
    l=["","","","","","","","",""]
    lx=[]
    lo=[]
    w,h=10,5
    count=0
    t=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    def restart():
        root.destroy()
        game()
    Button(f2,text="Restart",font="aerial 20",command=restart).grid(row=0,column=0)
    Button(f2,text="Quit",font="aerial 20",command=root.destroy).grid(row=0,column=1)
    def mylabel():
        global count
        if(count%2==0):     #even
            label=x
        if(count%2==1):      #odd
            label=o
        count=count+1
        return label
    def press(n):
        global count
        l[n-1]=mylabel()
        body()
        if (count%2==1):
            lx.append(n-1)
        elif(count%2==0):
            lo.append(n-1)
        lx.sort()
        lo.sort()
        for elem in t:
            counter0=0
            for integer in lx:
                if(integer in elem):
                    counter0+=1
            if(counter0==3):
                Label(f2,text="X win",pady=5,font="aerial 20").grid(row=1,column=0,columnspan=2)
        for elem in t:
            counter0=0
            for integer in lo:
                if(integer in elem):
                    counter0+=1
            if(counter0==3):
                Label(f2,text="O win",pady=5,font="aerial 20").grid(row=1,column=0,columnspan=2)
    def body():
        b11=Button(f1,text=l[0],width=w,height=h,fg="red",command=lambda : press(1))
        b11.grid(row=1,column=1)
        b12=Button(f1,text=l[1],width=w,height=h,fg="red",command=lambda : press(2))
        b12.grid(row=1,column=2)
        b13=Button(f1,text=l[2],width=w,height=h,fg="red",command=lambda : press(3))
        b13.grid(row=1,column=3)
        b21=Button(f1,text=l[3],width=w,height=h,fg="red",command=lambda : press(4))
        b21.grid(row=2,column=1)
        b22=Button(f1,text=l[4],width=w,height=h,fg="red",command=lambda : press(5))
        b22.grid(row=2,column=2)
        b23=Button(f1,text=l[5],width=w,height=h,fg="red",command=lambda : press(6))
        b23.grid(row=2,column=3)
        b31=Button(f1,text=l[6],width=w,height=h,fg="red",command=lambda : press(7))
        b31.grid(row=3,column=1)
        b32=Button(f1,text=l[7],width=w,height=h,fg="red",command=lambda : press(8))
        b32.grid(row=3,column=2)
        b33=Button(f1,text=l[8],width=w,height=h,fg="red",command=lambda : press(9))
        b33.grid(row=3,column=3)
    body()
    root.mainloop()

game()
