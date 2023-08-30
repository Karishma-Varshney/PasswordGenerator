from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=500, height=300)
window.config(padx=250, pady=100)

# entering a number by the user
input = Entry(width=10)
input.insert(END, string='0')
input.grid(column=1, row=0)

# calculation button
def button_clicked():
    miles = float(input.get())
    km = miles * 1.609
    label4.config(text=km)
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# labels
label1 = Label(text='Miles')
label1.config(padx=10)
label1.grid(column=2, row=0)
label2 = Label(text='is equal to')
label2.config(padx=10)
label2.grid(column=0, row=1)
label3 = Label(text='Km')
label3.grid(column=2, row=1)
label4 = Label(text='0')
label4.grid(column=1, row=1)


window.mainloop()

