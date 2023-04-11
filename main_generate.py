from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # password_list = []
    #
    # password_list1 = [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    # password_list2 = [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    # password_list3 = [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    password_list1 = [choice(letters) for _ in range(randint(8, 10))]
    password_list2 = [choice(symbols) for _ in range(randint(2, 4))]
    password_list3 = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_list1 + password_list2 + password_list3
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    password = password_entry.get()
    email = email_entry.get()
    website = website_entry.get()
    if len(password) == 0 and len(website) == 0:
        messagebox.showinfo(title="Warning", message="Enter all data")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"There are the details entered:"
                                                    f"\nEmail:{email}\nPassword:{password}"
                                                    f"\nIs it ok to save?")

        if is_ok:
            with open("password_file", "a") as f:
                f.write(f"{website} | {email} | {password} \n")
                password_entry.delete(0, END)
                website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)


canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "navruzas@email.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

generate_button = Button(text="Generate", width=5, command=generate_pass)
generate_button.grid(row=3, column=2, columnspan=2)

window.mainloop()
