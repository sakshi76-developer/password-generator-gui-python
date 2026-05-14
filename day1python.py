import string
import random
import tkinter as tk
def generate_password():
    length = int(length_enter.get())


    characters = string.ascii_letters

    if num_var.get() == 1:
        characters = characters + string.digits

    if sym_var.get()==1:
        characters = characters + string.punctuation

    password = ""

    for i in range(length):
        password = password + random.choice(characters)

    output_entry.delete(0,tk.END)
    output_entry.insert(0,password)

    

root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")

title_label = tk.Label(root,text="Random Password Generator",font=("Arial",18,"bold"))
title_label.pack(pady=10)

length_label = tk.Label(root,text="Enter The Length Of The Password",font=("Arial",13))
length_label.pack(pady=10)

length_enter = tk.Entry(root)
length_enter.pack()

num_var = tk.IntVar()
sym_var = tk.IntVar()

number_check = tk.Checkbutton(root,text="IF YOU WANT TO INCLUDE NUMBER",variable=num_var)
number_check.pack()


symbol_check = tk.Checkbutton(root,text="IF YOU WANT TO INCLUDE SYMBOL",variable=sym_var)
symbol_check.pack()

gen_button = tk.Button(root,text="Genarate Password",command=generate_password)
gen_button.pack(pady=10)

output_entry = tk.Entry(root,width=30)
output_entry.pack()

root.mainloop()
