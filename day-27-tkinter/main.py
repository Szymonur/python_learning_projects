import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#  Label
my_label = tkinter.Label(text="I'm a label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


#  Button
def button_clicked():
    my_label["text"] = input_user.get()


button = tkinter.Button(text="Click me", command=button_clicked)
button2 = tkinter.Button(text="button2")
# button.pack()
button.grid(column=2, row=0)
button2.grid(column=1, row=1)

#  Entry
input_user = tkinter.Entry(width=10)
# input_user.pack()
input_user.grid(column=3, row=2)


window.mainloop()
