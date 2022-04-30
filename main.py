# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from email import message
import random
import json
from re import search
from textwrap import indent

def search():
    website = website_entry.get()
    
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password = data[website]["password"]

            messagebox.showinfo(title=f"{website}", message=f"username: {email}\n password: {password}")

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File could not be found")

    except KeyError:
        messagebox.showinfo(title= "Error", message= "No details for the website could be found")





def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_numbers = random.randint(2, 4)
    nr_symbols = random.randint(2, 4)

    password_symbols  = [random.choice(symbols) for char in range(nr_symbols)]
    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_numbers = [random.choice(symbols) for char in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    new_password = "".join(password_list)
    
    password_entry.insert(0, new_password)

   



# ---------------------------- SAVE PASSWORD ------------------------------- #



def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }

    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0 :
        messagebox.showinfo(title="Oops", message="Please make sure you havent left any fields empty")

    else:
        try:
            with open("data.json", 'r') as data_file:
                data = json.load(data_file)
                

        except:


            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4 )

        else:

            data.update(new_data)

            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            
            website_entry.delete(0, END)

            password_entry.delete(0, END)


    
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
from tkinter import messagebox
from turtle import title

window = Tk()
window.title ("Password Manager")
window.config(padx =50, pady = 50)


canvas = Canvas(height=200, width=200)
logo = "C:/Users/razah/OneDrive/Desktop/python/Projects/password_manager/logo.png"
logo_image = PhotoImage(file = logo)
canvas.create_image(100, 100, image = logo_image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ",font=("Times New Roman", 12, "normal"))
website_label.grid(row=1, column=0)

website_entry = Entry(bg = "white", width=35)
website_entry.focus()
website_entry.grid(row=1, column=1)


email_label = Label(text="Email/Username: ", font=("Times New Roman", 12, "normal"))
email_label.grid(row=2, column=0)
email_entry = Entry(bg = "white", width=55)
email_entry.insert(0, "razahaji@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

pasword_label = Label(text="Password:  ", font=("Times New Roman", 12, "normal"))
pasword_label.grid(row=3, column=0)
password_entry = Entry(bg="white", width=34)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", width=20, font=("Times New Roman", 8, "normal"), command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command = save_password)
add_button.grid(row=5, column=1, columnspan=2)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(row=1, column=2)







window.mainloop()