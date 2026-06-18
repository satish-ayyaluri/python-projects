from tkinter import *
from tkinter import messagebox
import pyperclip
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passwd_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password=[]
    for char in range(0,random.randint(6,8)):
        password.append(random.choice(letters))
    for char in range(0,random.randint(4,7)):
        password.append(random.choice(symbols))
    for char in range(0,random.randint(3,5)):
        password.append(random.choice(numbers))

    random.shuffle(password)
    strong_passwd=""
    for passwd in password:
        strong_passwd+=passwd
    password_entry.delete(0,END)
    password_entry.insert(0,strong_passwd)
    pyperclip.copy(strong_passwd)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you have't left any field are empty")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"these are the details you enterred: \n Email:{email}"
                               f"\nPassword:{password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
                website_entry.focus()






# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas=Canvas(height=200,width=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1,columnspan=3)

label=Label(text="website:")
label.grid(row=1,column=0,sticky="w")

email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0,sticky="w")

pass_label=Label(text="Password")
pass_label.grid(row=3,column=0,sticky="w")


#entrys
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,sticky="w",columnspan=2,padx=5,pady=5)

email_entry=Entry(width=35)
email_entry.insert(0,"testtemp@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2,pady=5,padx=5,sticky="w")

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1,pady=5,padx=5,sticky="w")

#button
generate_password_button=Button(text="Generate Password",command=passwd_generator)
generate_password_button.grid(row=3,column=2,columnspan=2,pady=5,padx=5)

add_button=Button(text="Add",command=save)
add_button.grid(row=4,column=1,columnspan=2,pady=5)

window.mainloop()