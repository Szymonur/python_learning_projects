from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        label_timer["text"] = "Long break"
        label_timer["fg"] = RED
        count_down(60 * LONG_BREAK_MIN)
        return
    if reps % 2 != 0:
        label_timer["text"] = "Work"
        label_timer["fg"] = GREEN
        count_down(60 * WORK_MIN)
    if reps % 2 == 0:
        label_timer["text"] = "Short break"
        label_timer["fg"] = PINK
        count_down(60 * SHORT_BREAK_MIN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = count // 60
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count == 0:
        start_timer()
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(width=400, height=350)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "normal"))
btn_start = Button(text="Start", command=start_timer, highlightbackground=YELLOW, background="#ffffff", fg="#000000")
btn_reset = Button(text="Reset", highlightbackground=YELLOW, background="#ffffff", fg="#000000")
label_checkmarks = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"))

#  GRID
canvas.grid(column=1, row=1)
label_timer.grid(column=1, row=0)
btn_start.grid(column=0, row=2)
btn_reset.grid(column=2, row=2)
label_checkmarks.grid(column=1, row=3)

window.mainloop()
