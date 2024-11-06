import game_conf
from tkinter import *
from tkinter import messagebox
import re
from create_acc import *

kr = 1

REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# --------------------------- METHODS ------------------------------ #
username = ""
email = ""
password = ""
pwd = ""
count = 0
position = 0  # for storing the index


def check_entered_data():
    if len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return False
    elif len(email) == 0 or not re.fullmatch(REGEX, email):
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left email fields empty or entered "
                                                  "email is correct.")
        return False


def find_string(file_name, word):
    index = 0
    global position
    with open(file_name, 'r') as a:
        for line in a:
            index += 1
            line = line.rstrip()
            if re.search(r"\b{}\b".format(word), line):
                # print(index)
                # print(line)
                position = index - 1

                return True
    return False


def check_enterd_password(found_pwd, user_entered_pwd):
    # if len(user_entered_pwd) != 0:
    if found_pwd == user_entered_pwd:
        return True
    else:
        return False


def check():
    global pwd, count, username, email, password, flag, position, kr

    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(username) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left username fields empty.")
    else:
        with open("data.txt", "r") as file:
            if find_string("data.txt", username):
                # print("yes")
                content = file.readlines()
                found_line = content[position]
                found_value = found_line.split("|")
                pwd = found_value[2].strip()

                # ok = messagebox.askokcancel(title="Forgot password ", message=f"forgot password ?\n Please press OK to "
                #                                                               f"generate password automatically")
                #
                # if ok:
                #     password_entry.insert(0, pwd)
                #         ok = messagebox.askokcancel(title="User Login", message=f" SUCCESSFULLY LOGIN !! \n"
                #                                                             f"These are the details entered: "
                #                                                             f"\nNo of hours: {email} ")
                #
                #     if ok:
                #         game_conf.chlog=0
                #         game_conf.counter=int(email)*60*60
                #         window.after(1000, lambda: window.destroy())

                # else:
                if check_enterd_password(pwd, password):
                    ok = messagebox.askokcancel(title="User Login", message=f" SUCCESSFULLY LOGIN !! \n"
                                                                            f"These are the details entered: "
                                                                            f"\nNo of hours: {email} ")

                    if ok:
                        game_conf.chlog = 0
                        game_conf.counter = int(email) * 60 * 60
                        window.after(1000, lambda: window.destroy())

                if len(password) != 0:
                    if not check_enterd_password(pwd, password):
                        messagebox.showerror("check ",
                                             message="Please Check your password field ... it should not be empty \n and entered password should be correct")

            else:
                ok = messagebox.askokcancel("check ", message="User does not exixts !! Please create the account first")

                if ok:
                    window.destroy()
                    ca()


# --------------------------------- UI SETUP ------------------------------ #
def inti():
    global username_entry, email_entry, password_entry, window
    window = Tk()
    window.title("USER LOGIN")
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
    password_entry = Entry(width=35, font=("bold", 12), show="*")
    password_entry.grid(row=3, column=1, columnspan=2)

    # Buttons

    add_button = Button(text="Login", width=36, command=check, font=("bold", 10))
    add_button.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
    window.mainloop()

# -------------- ROUGH CODE ---------------------------- #
# if len(username) == 0 or len(password) == 0: messagebox.showinfo(title="Oops", message="Please make sure
# you haven't left any fields empty.") elif len(email) == 0 or not re.fullmatch(REGEX,
# email): messagebox.showinfo(title="Oops", message="Please make sure you haven't left email fields empty or
# entered " "email is correct.") else:

# count += 1
# if position == count - 1:
#     print(count)
# print(content)
# print(position)
# print(content[position])

# with open("data.txt", "r") as file:
#     for line in file:
#         count += 1
#         if find_string("data.txt", username):
#             print(line)
#             print("found")
#             print(username)
#             print(count)
#             break;
#     pfind = line
#     found_value = pfind.split("|")
#     pwd = found_value[2]
#     print(pwd)
#     if password == pwd:
#         print(f"yes {password}, {pwd} ")
#         print("hello")
#         # messagebox.showinfo(title="User Login", message=f"  LOGIN  SUCCESSFUL!! ")
#         # break
#     else:
#         print(f"no {password}, {pwd} ")
#         # messagebox.showerror("check password", message="Please Enter The Correct Password For Login !! ")
#         # break

# def check_user_exists():
#     global pwd, count, username, email, password, flag
# 
#     while count != 1:
#         password = password_entry.get()
#         pwd = password
#         count += 1
# 
#     else:
#         username = username_entry.get()
#         email = email_entry.get()
#         password = password_entry.get()
# 
#         if check_entered_data():
#             return
#         else:
#             with open("data.txt", "r") as file:
# 
#                 for line in file:
#                     if password in line:
#                         flag = 1
# 
# if flag == 1: print(f"${password}, ${pwd}") if password.__eq__(pwd): messagebox.showinfo(title="User Login", 
# message=f" SUCCESSFULLY LOGIN !! \n" f"These are the details entered: \nEmail: {email} " f"\nPassword: {password}") 
# window.after(1000, lambda: window.destroy()) else: messagebox.showerror("check password", message="Please Enter The
# Correct Password For Login !! or " "\nif you are new to application please create the " "\naccount first") elif 
# flag == 0: messagebox.showerror("check ", message="Please Enter The Correct Password For Login !! or " "\nif you 
# are new to application please create the " "\naccount first") 


# with open("data.txt", "r") as file:
#     for line in file:
#         if find_string("data.txt", username):
#             flag = 1
#             break
#
#     if flag == 0:
#         print(f"found ")
#     else:
#         print(position)
#         print(line)
