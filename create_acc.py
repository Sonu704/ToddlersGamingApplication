import os
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import re
import smtplib
from email.message import EmailMessage
import game_conf

username = ""
email = ""
password = ""


def create_acount():
    global REGEX
    REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # --------------------------- SETTING FOR SMTP MAIL -------------------------------#

    MY_EMAIL = "sonuhchoudhary@gmail.com"
    MY_PASSWORD = "%sonu%ch@udhary0112:)"

    connection = smtplib.SMTP("smtp.gmail.com", timeout=60, port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
               'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # ---------------------------- SAVE PASSWORD ------------------------------- #

filesize = os.path.getsize("data.txt")


def enter_data_in_file():
    with open("data.txt", "a") as data_file:
        data_file.write(f"{username} | {email} | {password}\n")
        username_entry.delete(0, END)
        password_entry.delete(0, END)


def find_string(file_name, word):
    with open(file_name, 'r') as a:
        for line in a:
            line = line.rstrip()
            if re.search(r"\b{}\b".format(word), line):
                return True
    return False


def send_enterd_data():
    msg = EmailMessage()
    #msg.set_content(f"Hello {username} ! Your password for Toddlers Gaming Application is : {password}")
    #msg['From'] = MY_EMAIL
    #msg['To'] = email
    #connection.send_message(msg)
    #connection.quit()


def save_and_validate():
    global username, email, password
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    elif filesize == 0:
        ok=messagebox.askokcancel(title=username,message=f"These are the details entered: \nNo of Hours: {email} "f"\nPassword: {password} \nIs it ok to save?")
        if ok:
            enter_data_in_file()
            game_conf.chlog = 0
            game_conf.counter = int(email) * 60 * 60
            window.after(1000, lambda: window.destroy())
            send_enterd_data()
    elif not find_string("data.txt", username):
        ok= messagebox.askokcancel(title=username,message=f"These are the details entered: \nNo of hours: {email} "f"\nPassword: {password} \nIs it ok to save?")
        if ok:
            enter_data_in_file()
            game_conf.chlog=0
            game_conf.counter=int(email) * 60 * 60
            window.after(1000, lambda: window.destroy())
            send_enterd_data()
    else:
        messagebox.showinfo(title="Oops",message=f"The entered {username} is already exists !! please "f"try with other name.")
# ---------------------------- UI SETUP ------------------------------- #

def ca():
    global username_entry,email_entry,password_entry,window
    window = Tk()
    window.title("CREATE ACCOUNT")
    window.config(padx=50, pady=50)
    font_size = 20

    canvas = Canvas(height=200, width=200)
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

    # Labels
    username_lable = Label(text="Username:")
    username_lable.grid(row=1, column=0)
    email_label = Label(text="No of Hours:")
    email_label.grid(row=2, column=0)
    password_label = Label(text="Password:")
    password_label.grid(row=3, column=0)

    # Entries
    username_entry = Entry(width=35, font=("bold", 12))
    username_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    username_entry.focus()
    email_entry = Entry(width=35, font=("bold", 12))
    email_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
    email_entry.insert(0, "2")
    password_entry = Entry(width=25, font=("bold", 12))
    password_entry.grid(row=3, column=1)

    # Buttons
    generate_password_button = Button(text="Generate", command=generate_password)
    generate_password_button.grid(row=3, column=2)
    add_button = Button(text="Add", width=36, command=save_and_validate, font=("bold", 10))
    add_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

    window.mainloop()
