from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=400, height=200)


def miles_to_km(*args):
    print("I got Clicked")
    miles = float(input.get())
    km = round(miles*1.6)
    result_label.config(text = f"{km}",font = ("Tahoma", 24, "bold"))

# Label
miles_label = Label(text = "Miles", font = ("Tahoma", 24, "bold"))
miles_label.grid(column=2, row=0)

km_label = Label(text = "Km", font = ("Tahoma", 24, "bold"))
km_label.grid(column=2, row=1)

equal_label = Label(text = "is equal to", font = ("Tahoma", 24, "bold"))
equal_label.grid(column=0, row=1)

result_label = Label(text = "0", font = ("Tahoma", 24, "bold"))
result_label.grid(column=1, row=1)


# Button
new_button = Button(text = "Calculate", command = miles_to_km)
new_button.grid(column=1, row =3)

#Entry 
input = Entry(width =5,font = ("Tahoma", 24))
print(input.get())
input.grid(column=1, row =0)


window.mainloop()