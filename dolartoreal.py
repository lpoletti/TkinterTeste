def conversor():
    c = int(e1.get())
    f = (5.2) * (float(c))
    t1.config(state="normal")
    t1.delete('1.0',tk.END)
    t1.insert(tk.END,str(f))
    t1.config(state="disabled")

import tkinter as tk

window = tk.Tk()

window.geometry("300x250")
window.config(bg="green")
window.resizable(width=False,height=False)
window.title("Dolar para Real Conversor")

l1 = tk.Label(master=window, text="Dolar to Real Conversor",font=("Arial",15),fg="white",bg="black")
l2 = tk.Label(master=window,text="Dolar: ", font=("Arial",10, "bold"),fg="white",bg="black")
l3 = tk.Label(master=window, text="Reais: ", font=("Arial",10, "bold"),fg="white",bg="black")

empty_lb1 = tk.Label(window, bg = "red")
empty_lb2 = tk.Label(window, bg = "red")

e1 = tk.Entry(window, font=("Arial", 10))

bt = tk.Button(window,text="Converter",font=("Arial", 10),command=lambda:conversor())

t1 = tk.Text(window,state="disabled",width=15,height=0)

l1.pack()
l2.pack()
e1.pack()
bt.pack()
l3.pack()
t1.pack()

window.mainloop()