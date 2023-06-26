from tkinter import *
count=0
def MultiPlayerGame():
    global count
    root=Tk()
    root.geometry("300x430+210+160")
    root.title("Tic Tac Toe")
    f1=Frame(root)
    f1.pack()
    Label(f1,text="TIC TAC TOE",font="comics 20",pady=10).grid(row=0,column=1,columnspan=3)
    f2=Frame(root)
    f2.pack()
    x,o="X","O"
    board=["","","","","","","","",""]
    lx=[]
    lo=[]
    w,h=10,5
    count=0
    t=[[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    def restart():
        root.destroy()
        MultiPlayerGame()
    Button(f2,text="Restart",font="aerial 20",command=restart).grid(row=0,column=0,sticky="nsew")
    Button(f2,text="Quit",font="aerial 20",command=root.destroy).grid(row=0,column=1,sticky="nsew")
    ButtonStates=["active" for i in range(9)]
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
        board[n-1]=mylabel()
        ButtonStates[n-1]="disabled"
        # displaylabel.destroy()
        if (count%2==1):
            lx.append(n-1)
            displaylabel=Label(f2,text="2nd Player's Turn",pady=5,font="aerial 20")
            displaylabel.grid(row=1,column=0,columnspan=2)
        elif(count%2==0):
            lo.append(n-1)
            displaylabel=Label(f2,text="1st Player's Turn",pady=5,font="aerial 20")
            displaylabel.grid(row=1,column=0,columnspan=2)
        lx.sort()
        lo.sort()
        for elem in t:
            counter0=0
            for integer in lx:
                if(integer in elem):
                    counter0+=1
            if(counter0==3):
                Label(f2,text="           X win         ",pady=5,font="aerial 20").grid(row=1,column=0,columnspan=2)
                for i in range(9):
                    ButtonStates[i]="disable" 
        for elem in t:
            counter0=0
            for integer in lo:
                if(integer in elem):
                    counter0+=1
            if(counter0==3):
                Label(f2,text="           O win          ",pady=5,font="aerial 20").grid(row=1,column=0,columnspan=2)
                for i in range(9):
                    ButtonStates[i]="disable" 
        body()
        
    def body():
        b11=Button(f1,text=board[0],width=w,height=h,command=lambda : press(1),state=ButtonStates[0],disabledforeground="red")
        b11.grid(row=1,column=1)
        b12=Button(f1,text=board[1],width=w,height=h,command=lambda : press(2),state=ButtonStates[1],disabledforeground="red")
        b12.grid(row=1,column=2)
        b13=Button(f1,text=board[2],width=w,height=h,command=lambda : press(3),state=ButtonStates[2],disabledforeground="red")
        b13.grid(row=1,column=3)
        b21=Button(f1,text=board[3],width=w,height=h,command=lambda : press(4),state=ButtonStates[3],disabledforeground="red")
        b21.grid(row=2,column=1)
        b22=Button(f1,text=board[4],width=w,height=h,command=lambda : press(5),state=ButtonStates[4],disabledforeground="red")
        b22.grid(row=2,column=2)
        b23=Button(f1,text=board[5],width=w,height=h,command=lambda : press(6),state=ButtonStates[5],disabledforeground="red")
        b23.grid(row=2,column=3)
        b31=Button(f1,text=board[6],width=w,height=h,command=lambda : press(7),state=ButtonStates[6],disabledforeground="red")
        b31.grid(row=3,column=1)
        b32=Button(f1,text=board[7],width=w,height=h,command=lambda : press(8),state=ButtonStates[7],disabledforeground="red")
        b32.grid(row=3,column=2)
        b33=Button(f1,text=board[8],width=w,height=h,command=lambda : press(9),state=ButtonStates[8],disabledforeground="red")
        b33.grid(row=3,column=3)
    
    displaylabel=Label(f2,text="1st Player's Turn",pady=5,font="aerial 20")
    displaylabel.grid(row=1,column=0,columnspan=2)
    body()
    root.mainloop()

MultiPlayerGame()
