#tk calculator

from tkinter import *

root = Tk()
root.geometry("350x385")
root.resizable(0,0)
root.configure(bg = "lightblue")
root.title("calculator")

#buttons
n1 = Button(root, text="1", font=("arial", 20, "bold"))
n1.place(x= 5, y= 60, width= 60, height=60)

n2 = Button(root, text="2", font=("arial", 20, "bold"))
n2.place(x= 70, y= 60, width= 60, height=60)

n3 = Button(root, text="3", font=("arial", 20, "bold"))
n3.place(x= 135, y= 60, width= 60, height=60)

n4 = Button(root, text="4", font=("arial", 20, "bold"))
n4.place(x= 5, y= 125, width= 60, height=60)

n5 = Button(root, text="5", font=("arial", 20, "bold"))
n5.place(x= 70, y= 125, width= 60, height=60)

n6 = Button(root, text="6", font=("arial", 20, "bold"))
n6.place(x= 135, y= 125, width= 60, height=60)

n7 = Button(root, text="7", font=("arial", 20, "bold"))
n7.place(x= 5, y= 190, width= 60, height=60)

n8 = Button(root, text="8", font=("arial", 20, "bold"))
n8.place(x= 70, y= 190, width= 60, height=60)

n9 = Button(root, text="9", font=("arial", 20, "bold"))
n9.place(x= 135, y= 190, width= 60, height=60)

n0 = Button(root, text="0", font=("arial", 20, "bold"))
n0.place(x= 5, y= 255, width= 190, height=60)






root.mainloop()