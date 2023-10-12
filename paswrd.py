from tkinter import *
import pyperclip
import random

root = Tk()
root.geometry('350x350')
root.title('Password Generator')

passstr = StringVar()
passlen_smallalpha = IntVar()
passlen_bigalpha = IntVar()
passlen_digits = IntVar()
passlen_specialcharac = IntVar()

passlen_smallalpha.set(0)
passlen_bigalpha.set(0)
passlen_digits.set(0)
passlen_specialcharac.set(0)

 
def generate_password():
    small = passlen_smallalpha.get()
    big = passlen_bigalpha.get()
    digits = passlen_digits.get()
    special = passlen_specialcharac.get()

    pass1 = 'abcdefghijklmnopqrstuvwxyz'
    pass2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    pass3 = '0123456789'
    pass4 = '!@#$%^&*()?~_-|/'

    all_characters = ''

    if small:
        all_characters += pass1
    if big:
        all_characters += pass2
    if digits:
        all_characters += pass3
    if special:
        all_characters += pass4

    if all_characters:
        password_length = small + big + digits + special
        password = ''.join(random.choice(all_characters) for _ in range(password_length))
        passstr.set(password)
    else:
        passstr.set("Select at least one character type")

# Function to copy password to clipboard
def copy_to_clipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# Create the GUI elements
Label(root, text="Password Generator", font="calibre 20 bold").pack()

Label(root, text="Enter no. of Small alphabets").pack(pady=3)
Entry(root, textvariable=passlen_smallalpha).pack(pady=3)

Label(root, text="Enter no. of Big alphabets").pack(pady=3)
Entry(root, textvariable=passlen_bigalpha).pack(pady=3)

Label(root, text="Enter no. of Digits").pack(pady=3)
Entry(root, textvariable=passlen_digits).pack(pady=3)

Label(root, text="Enter no. of Special Characters").pack(pady=3)
Entry(root, textvariable=passlen_specialcharac).pack(pady=3)

Button(root, text="Generate Password", command=generate_password).pack(pady=7)
Entry(root, textvariable=passstr).pack(pady=3)

Button(root, text="Copy to clipboard", command=copy_to_clipboard).pack()

root.mainloop()
