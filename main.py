from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=250, height=250)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(200, 200, image=lock_img)
canvas.grid(column=1, row=1)

window.mainloop()