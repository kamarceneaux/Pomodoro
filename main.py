from tkinter import *
from windows import set_dpi_awareness
import math

set_dpi_awareness()

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
timer = None


# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    # Reset the text to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # Reset the Title Label to equal timer
    timeLbl.config(text="Timer", fg=RED)
    # Reset the checkmarks
    checkLbl.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """Responsible for calling the countdown function"""
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 2 == 1:
        count_down(work_sec)
        timeLbl.config(text="Work", fg=GREEN)
        # After a users completed a work session they a get a checkmark
    else:
        if reps == 8:
            count_down(long_break_sec)
            timeLbl.config(text="Break", fg=RED)
        else:
            count_down(short_break_sec)
            timeLbl.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Based on the input this function recieves, it'll countdown in seconds from that number and update the timer input

    Args:
        count (int): In seconds
    """
    global timer
    # Returns the largest whole number < x
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)

        for _ in range(work_sessions):
            marks += "✔"
        checkLbl.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Timer Label
timeLbl = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timeLbl.grid(row=0, column=1)

# Tomato with Timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
## Half of the width and height
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

# Start Button
startBtn = Button(text="Start", command=start_timer)
startBtn.grid(row=2, column=0)

# Reset Button
resetBtn = Button(text="Reset", command=reset_timer)
resetBtn.grid(row=2, column=2)

# Checkmark
checkLbl = Label(fg=GREEN, bg=YELLOW)
checkLbl.grid(row=3, column=1)


window.mainloop()
