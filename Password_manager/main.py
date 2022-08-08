from password_generator import generate_random_password
from random import randint
import tkinter
from tkinter import messagebox
import pyperclip


# constant - settings
MAIN_WINDOW_TITLE = "Password Manager"
MAIN_WINDOW_PADDING_X = 30
MAIN_WINDOW_PADDING_Y = 30
# canvas settings
FILE_NAME_LOGO = "logo.png"
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200
# labels settings
LABEL_WEBSITE_TEXT = "Website:"
LABEL_EMAIL_USERNAME_TEXT = "Email/Username:"
LABEL_PASSWORD_TEXT = "Password:"
# buttons settings
BUTTON_ADD_TEXT = "ADD"
BUTTON_GENERATE_PASSWORD_TEXT = "Generate Password" 
# entry settings
ENTRY_EMAIL_START_VALUE = 'EXAMPLE@gmail.com'




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    function for generating password
    """
    # generating random password
    new_password = generate_random_password(number_of_letters=randint(8,12),\
        number_of_numbers=randint(4,8),number_of_symbols=randint(2,4))
    
    # deleting whatever is in the input password entry
    inpput_password.delete(0,tkinter.END)
    
    # writing the new generated password into the password field
    inpput_password.insert(0,new_password)
    pyperclip.copy(new_password) 


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    """
    saves data to file
    """
    website_data = inpput_field_website.get()
    user_name = inpput_username.get()
    password_new = inpput_password.get()

    data = website_data + " | " + user_name + " | " + password_new +"\n"

    # simple validation - checking if fields are not empty
    if website_data and user_name and password_new: 
        # creating a message box as a confirmation
        is_ok = messagebox.askokcancel(title=website_data, \
            message=f"These are the details entered: \nEmail: {user_name}\
                \nPassword: {password_new} \n Is it ok to save?")

        if is_ok:
            with open("data.txt",'a') as f:
                f.write(data)

            # deleting the values in the entries
            inpput_field_website.delete(0,tkinter.END)
            inpput_password.delete(0,tkinter.END)

    else:
        messagebox.showerror(title="Field is required!!",\
            message="Please don't leaave any fields empty!")

    

# ---------------------------- UI SETUP ------------------------------- #
# creating the main window
window_main = tkinter.Tk()
window_main.title(MAIN_WINDOW_TITLE)
window_main.config(padx=MAIN_WINDOW_PADDING_X, pady=MAIN_WINDOW_PADDING_Y)

# creating canvas with the logo pict in the middle
canvas = tkinter.Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, \
    highlightthickness=0)
logo_image = tkinter.PhotoImage(file=FILE_NAME_LOGO)
canvas.create_image(CANVAS_WIDTH/2,CANVAS_HEIGHT/2,image=logo_image)
canvas.grid(row=0,column=1) 

# creating labels
label_website = tkinter.Label(text=LABEL_WEBSITE_TEXT,pady=2)
label_website.grid(row=1,column=0)

label_username = tkinter.Label(text=LABEL_EMAIL_USERNAME_TEXT,pady=2)
label_username.grid(row=2,column=0)

label_password = tkinter.Label(text=LABEL_PASSWORD_TEXT,pady=2)
label_password.grid(row=3,column=0)


# creating entries
inpput_field_website = tkinter.Entry(width=51)
inpput_field_website.grid(row=1,column=1,columnspan=2)
inpput_field_website.focus() # put the cursor into the widget

inpput_username = tkinter.Entry(width=51)
inpput_username.grid(row=2,column=1,columnspan=2)
inpput_username.insert(0,ENTRY_EMAIL_START_VALUE) # starting value for email/username

inpput_password = tkinter.Entry(width=32)
inpput_password.grid(row=3,column=1)

# creating buttons
button_add = tkinter.Button(text=BUTTON_ADD_TEXT,width=43,pady=2,command=save_to_file)
button_add.grid(row=4,column=1,columnspan=2)

button_generate_password = tkinter.Button(text=BUTTON_GENERATE_PASSWORD_TEXT,\
    pady=2, command=generate_password)
button_generate_password.grid(row=3,column=2)

# waiting on the user to close the window
window_main.mainloop()