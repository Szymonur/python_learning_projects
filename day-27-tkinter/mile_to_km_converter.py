import tkinter

window = tkinter.Tk()
window.minsize(width=100, height=100)
window.config(pady=50, padx=50)


def calculate():
    label_result["text"] = float(miles_input.get()) * 1.609


miles_input = tkinter.Entry(width=10)
label_is_equal_to = tkinter.Label(text="is equal to")
label_miles = tkinter.Label(text="Miles")
label_km = tkinter.Label(text="Km")
label_result = tkinter.Label(text="0")
btn_calculate = tkinter.Button(text="Calculate", command=calculate)

miles_input.grid(column=1, row=0)
label_miles.grid(column=2, row=0)
label_is_equal_to.grid(column=0, row=1)
label_result.grid(column=1, row=1)
label_km.grid(column=2, row=1)
btn_calculate.grid(column=1, row=2)

window.mainloop()
