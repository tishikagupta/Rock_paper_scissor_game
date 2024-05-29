from tkinter import *
import random
 
root = Tk()
 
root.geometry("300x300")
 
root.title("Rock Paper Scissor Game")    #title
 
value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}
 
 
 
def reset():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")
 
 
 
def disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
 
 
 
def rock():
    v = value[str(random.randint(0, 2))]
    if v == "Rock":
        match_result = "Match Draw"
    elif v == "Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    l4.config(text=match_result)
    l1.config(text="Rock            ")
    l3.config(text=v)
    disable()

 
 
def paper():
    v = value[str(random.randint(0, 2))]
    if v == "Paper":
        match_result = "Match Draw"
    elif v == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    l4.config(text=match_result)
    l1.config(text="Paper           ")
    l3.config(text=v)
    disable()
 
 
 
def scissor():
    v = value[str(random.randint(0, 2))]
    if v == "Rock":
        match_result = "Computer Win"
    elif v == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    l4.config(text=match_result)
    l1.config(text="Scissor         ")
    l3.config(text=v)
    disable()
 

Label(root,
      text="Rock, Paper & Scissors",
      font="normal 20 bold",
      fg="blue").pack(pady=20)
 
frame = Frame(root)
frame.pack()
 
l1 = Label(frame,
           text="Player              ",
           font=10 , fg="green")
 
l2 = Label(frame,
           text="VS             ",
           font="normal 10 bold",fg="green")
 
l3 = Label(frame, text="Computer", font=10, fg="green")
 
l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()
 
l4 = Label(root,
           text="",
           font="normal 20 bold",
           bg="violet",
           width=15,
           borderwidth=2,
           relief="solid")
l4.pack(pady=20)
 
frame1 = Frame(root)
frame1.pack()
 
b1 = Button(frame1, text="Rock",
            font=10, width=7,fg="red", bg="black",
            command=rock)
 
b2 = Button(frame1, text="Paper ",
            font=10, width=7,fg="red", bg="black",
            command=paper)
 
b3 = Button(frame1, text="Scissor",
            font=10, width=7,fg="red", bg="black",
            command=scissor)
 
b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)
 
Button(root, text="Reset Game",
       font=10, fg="blue",
       bg="yellow", command=reset).pack(pady=20)

root.mainloop()