from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="!!ALERT!!", message="No entry found, please add pass first!")
    else:
        if website in data:
            password = data[website]["password"]
            username = data[website]["email"]
            messagebox.showinfo(title=f"Password for {website}", message=f"Username : {username}\nPassword : {password}")
        else:
            messagebox.showinfo(title="!!ALERT!!", message="Entry not exist!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    pass_base = []
    pass_string = ""
    for i in range(0, 3 + 1):
      random_letter = random.choice(letters)
      pass_base.append(random_letter)
    for j in range(0, 4 + 1):
      random_number = random.choice(numbers)
      pass_base.append(random_number)
    for k in range(0, 5 + 1):
      random_symbol = random.choice(symbols)
      pass_base.append(random_symbol)
    random.shuffle(pass_base)
    for k in pass_base:
      pass_string += k
    password_entry.insert(0, pass_string)
    pyperclip.copy(pass_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().lower()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website:
                    {
                        "email" : email,
                        "password" : password
                    }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message="Don't leave any info blank!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)

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

website_entry = Entry(width=22)
website_entry.focus()
email_entry = Entry(width=41)
email_entry.insert(0, "jack.yeh@gmail.com")
password_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", width=15, command=search)
generate_password_button = Button(text="Generate Password", width=15, command=password)
add_button = Button(text="Add", width=36, command=save)
search_button.grid(column=2, row=1)
generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)







window.mainloop()