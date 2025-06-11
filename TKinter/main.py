from tkinter import Checkbutton, Listbox, Radiobutton, Scale, Spinbox, Tk, Label, Button, Entry, Text

window = Tk()
window.title("GUI")
window.config(padx=20,pady=20)
window.minsize(500, 300)

x = "This a label"

label = Label(text=x, font=("Arial", 24, "bold"))
# label.pack()
label.grid(row=0, column=0)


def click_button():
    print("Click Button")
    label["text"] = "Button Got Clicked"


button = Button(text="Click", command=click_button)
# button.pack(padx=10, pady=10)
button.grid(row=1, column=1, padx=10, pady=10)


button = Button(text="New Button", command=click_button)
# button.pack(padx=10, pady=10)
button.grid(row=0, column=2, padx=10, pady=10)


input = Entry(width=20)
input.grid(row=2,column=3)

# text=Text(height=5,width=40)
# text.focus()

# text.pack(padx=10, pady=10)


# def value_update():
#     value = spinbox.get()
#     print("value change to:", value)


# spinbox = Spinbox(command=value_update)
# spinbox.pack(padx=10, pady=10)


# scale=Scale()
# scale.pack()

# check_button=Checkbutton()
# check_button.pack()

# radio_button=Radiobutton()
# radio_button.pack()

# list_box=Listbox(height=5,width=30)
# list_box.pack()

window.mainloop()
