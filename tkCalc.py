#tk calculator

from tkinter import *

root = Tk()
root.geometry("350x385")
root.resizable(0,0)
root.configure(bg = "lightblue")
root.title("calculator")


screen_entry = Entry(root, bg = 'grey', font=("arial", 18), state=DISABLED)
screen_entry.place(x=5, y=5, width=340, height= 50)
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

multiply = Button(root, text="*", font=("arial", 20, "bold"))
multiply.place(x= 200, y= 60, width= 70, height= 60)

divide = Button (root, text="/", font=("arial", 20, "bold"))
divide.place(x= 275, y= 60, width= 70, height= 60)

plus = Button (root, text="+", font=("arial", 20, "bold"))
plus.place(x= 200, y= 125, width= 70, height= 60)

minus = Button (root, text="-", font=("arial", 20, "bold"))
minus.place(x= 275, y= 125, width= 70, height= 60)

calculate = Button (root, text="calculate", font=("arial", 20, "bold"))
calculate.place(x= 5, y= 320, width= 340, height= 60)

back = Button(root, text = "back", font=("arial", 18, "bold"))
back.place(x= 200, y = 190, width=145, height=60)

clear = Button(root, text = "clear", font=("arial", 18, "bold"))
clear.place(x= 200, y= 255, width= 145, height=60)




root.mainloop()