from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height =300)
window.config(padx =120, pady=200)

def button_clicked(*args):
    print("I got Clicked")
    my_label.config(text = input.get())

# Label
my_label = Label(text = "I Am a Label", font = ("Tahoma", 24, "bold"))
my_label["text"] = "New Text"

my_label.grid(column=0, row=0)
my_label.config(padx=100,pady=100)

# Button
new_button = Button(text = "New Click Me", command = button_clicked)
new_button.grid(column=2, row =0)
button = Button(text = "Click Me", command = button_clicked)
button.grid(column=1, row =1)

#Entry 

input = Entry(width =10)
print(input.get())
input.grid(column=3, row =2)










window.mainloop()