from tkinter import *
from tkinter import messagebox
import random

EMAIL = "szymonur88828@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(4, 8)
    nr_numbers = random.randint(4, 8)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    entry_pass.delete(0, END)
    entry_pass.insert(0, ''.join(password_list))
    entry_pass.insert(0, ''.join(password_list))


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = entry_website.get()
    email_username = entry_email_username.get()
    password_e = entry_pass.get()

    if min(len(website), len(email_username), len(password_e)) == 0:
        messagebox.showerror(message="Don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail/Username: {email_username}\n"
                                               f"Password: {password_e}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email_username} | {password_e}\n")
                entry_pass.delete(0, 'end')
                entry_website.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")

window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)

label_website = Label(text="Website:")
label_email_username = Label(text="Email/Username:")
label_pass = Label(text="Password:")

entry_website = Entry(width=37)
entry_website.focus()
entry_email_username = Entry(width=37)
entry_email_username.insert(0, EMAIL)
entry_pass = Entry(width=21)

btn_generate_password = Button(text="Generate password", width=11, command=generate_password)
btn_add = Button(text="Add", width=36, command=save_data)

canvas.grid(column=1, row=0)
label_website.grid(column=0, row=1)
entry_website.grid(column=1, row=1, columnspan=2)

label_email_username.grid(column=0, row=2)
entry_email_username.grid(column=1, row=2, columnspan=2)

label_pass.grid(column=0, row=3)
entry_pass.grid(column=1, row=3)
btn_generate_password.grid(column=2, row=3)
btn_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
