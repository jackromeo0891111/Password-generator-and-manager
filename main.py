from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("data.txt", "a") as f:
        f.write(f"{website} | {email} | {password}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry = Entry(width=40)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.insert(0, "jack.yeh@gmail.com")
password_entry = Entry(width=22)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", width=15)
add_button = Button(text="Add", width=36, command=save)
generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)







window.mainloop()