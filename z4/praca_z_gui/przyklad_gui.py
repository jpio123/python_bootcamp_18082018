import tkinter

def zlacz_napisy():
    a = a_entry.get()
    b = b_entry.get()
    wynik_label.configure(text=f"Wynik: {a+b}")

def czysc_napisy():
    wynik_label.configure(text="Wynik: -")

root = tkinter.Tk()
root.title("Prosty kalkulator")

a_label = tkinter.Label(master=root, text="a")
a_label.pack()
# a_label.grid(row=0, column=0)
a_entry = tkinter.Entry(master=root)
a_entry.pack()

b_label = tkinter.Label(master=root, text="b")
b_label.pack()
b_entry = tkinter.Entry(master=root)
b_entry.pack()

dodaj_button = tkinter.Button(master=root, text="Dodaj", command=zlacz_napisy)
dodaj_button.pack()

czysc_button = tkinter.Button(master=root, text="Czysc", command=czysc_napisy)
czysc_button.pack()

wynik_label = tkinter.Label(master=root, text="Wynik: -")
wynik_label.pack()

root.mainloop()