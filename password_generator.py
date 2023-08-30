from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ------------------------------RESET MECHANISM-----------------------------#
def reset():
    username_input.delete(0, END)
    password_length_input.delete(0, END)
    generate_password_input.delete(0, END)

# -----------------------------ACCEPT MECHANISM-----------------------------#
def accept():
    
    is_ok = messagebox.askyesno(title='Confirmation', message='Are you satisfied by this password?')
    if is_ok:
        messagebox.showinfo(title='Generated password', message= f"Here's your password : {generate_password_input.get()}")

# -----------------------------PASSWORD GENERATOR--------------------------#
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U','V','W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', ')', '(', '+', '*']

character = [letters + numbers + symbols]

def generate_password():
    username = username_input.get()
    password_length = password_length_input.get()

    if len(username) == 0 or len(password_length) == 0:
        messagebox.showerror(title='Opps!!!', message="Please don't leave any field empty")

    else:
        n = int(password_length)
        password = []
        for _ in range(0,n):
            password_list = random.choice(character)
            password_element = random.choice(password_list)
            password.append(password_element)
            random.shuffle(password)
            new_password = "".join(password)

            if len(new_password) == n:
                generate_password_input.insert(0, new_password)
                # allowing user to copy password to clipboard
                pyperclip.copy(new_password)


# ------------------------------UI SET-UP-----------------------------------#
window = Tk()
window.title('Password Generator')
window.config(padx=50, pady=50)

# heading 
heading = Label(text='Password Generator', fg= '#b063ad', font="Arial 30 bold underline", anchor=CENTER)
heading.grid(row=0, column=1)

# adding logo 
canvas = Canvas(width=200, height=160)
logo_img = PhotoImage(file = 'logo.png')
canvas.create_image(100, 80, image = logo_img )
canvas.grid(row=1, column=1, padx=10, pady=10)

# labels
username_label = Label(text='Enter user name:')
username_label.grid(row=2, column=0, padx=10, pady=10)

password_length_label = Label(text='Enter password length:')
password_length_label.grid(row=3, column=0, padx=10, pady=10)

generate_password_label = Label(text='Generated password:')
generate_password_label.grid(row=4, column=0, padx=10, pady=10)

# Entries
username_input = Entry(width=35)
username_input.grid(row=2, column=1)
username_input.focus()

password_length_input = Entry(width=35)
password_length_input.grid(row=3, column=1)

generate_password_input = Entry(width=35)
generate_password_input.grid(row=4, column=1)

# buttons
password_button = Button(text='GENERATE PASSWORD', fg='white', bg='#b063ad', command=generate_password)
password_button.grid(row=4, column=2)

accept_button = Button(text='ACCEPT', fg='#b063ad',command=accept)
accept_button.grid(row=5, column=1, padx=10, pady=10)

reset_button = Button(text='RESET', fg='#b063ad', command=reset)
reset_button.grid(row=6, column=1, padx=10, pady=10)

window.mainloop()