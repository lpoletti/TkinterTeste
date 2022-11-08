import tkinter as tk
from tkinter import ttk

def Hello():
    label = tk.Label(text = "Hello World! Teste Tkinter!!!",fg = "White",bg="Green").pack()


window = tk.Tk()

window.title("Teste Tkinter")
window.geometry("600x500+290+10")

# greeting = tk.Label(text = "Hello World! Teste Tkinter!!!")
# greeting.place(x=190,y=210)

# label = tk.Label(text="Hello World! Teste Tkinter!!!", fg="white",bg="green",width=30,height=10)
# label.place(x=190, y=210)

# button = tk.Button(text="Clique-me",width=25,height=10,bg="Black",fg="White", command=Hello)
# button.pack()

# label = tk.Label(text="Nome")
# entry = tk.Entry()

# label.pack()
# entry.pack()

# nome = tk.Label(window,text="Nome").place(x=30,y=50)
# email = tk.Label(window,text="E-mail").place(x=30,y=90)
# passw = tk.Label(window, text="Passwaord").place(x=30,y=130)

# e1 = tk.Entry(window).place(x=80,y=50)
# e2 = tk.Entry(window).place(x=80,y=90)
# e3 = tk.Entry(window).place(x=100,y=130)

# frame1 = tk.Frame()
# label1 = tk.Label(master=frame1,text="Frame 1",bg="#4682b4")
# frame1.pack()
# label1.pack()

# frame2 = tk.Frame()
# label2 = tk.Label(master=frame2,text="Frame 2",bg="green")
# frame2.pack()
# label2.pack()

# border = {
#     "flat" : tk.FLAT,
#     "sunken" : tk.SUNKEN,
#     "raised" : tk.RAISED,
#     "groove" : tk.GROOVE,
#     "ridge" : tk.RIDGE
# }

# for relief_name, relief in border.items():
#     fname = tk.Frame(master = window, relief=relief,borderwidth=5)
#     fname.pack(side=tk.LEFT)
#     label = tk.Label(master=fname, text=relief_name)
#     label.pack()

frame1 = tk.Frame(master = window, width=100, height=100, bg="red")
frame1.pack(fill=tk.X)

frame2 = tk.Frame(master = window, width=100, height=100, bg="yellow")
frame2.pack(fill=tk.X)

frame3 = tk.Frame(master = window, width=100, height=100, bg="green")
frame3.pack(fill=tk.X)


window.mainloop()
