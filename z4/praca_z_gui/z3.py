import tkinter

def oblicz_koszt():
    spalanie = float(spalanie_entry.get())
    cena = float(cena_paliwa_entry.get())
    dystans = float(dystans_entry.get())

    koszt = spalanie * dystans * cena / 100

    wynik_label.configure(text=f"Koszt: {koszt}")


root = tkinter.Tk()
root.title("Kalkulator kosztów przejazdu")

spalanie_label = tkinter.Label(master=root, text="Podaj spalanie L/100km:")
spalanie_label.pack()
# a_label.grid(row=0, column=0)
spalanie_entry = tkinter.Entry(master=root)
spalanie_entry.pack()

cena_paliwa_label = tkinter.Label(master=root, text="Podaj cenę paliwa:")
cena_paliwa_label.pack()
cena_paliwa_entry = tkinter.Entry(master=root)
cena_paliwa_entry.pack()

dystans_label = tkinter.Label(master=root, text="Podaj pokonany dystans:")
dystans_label.pack()
dystans_entry = tkinter.Entry(master=root)
dystans_entry.pack()

dodaj_button = tkinter.Button(master=root, text="Dodaj", command=oblicz_koszt)
dodaj_button.pack()

# czysc_button = tkinter.Button(master=root, text="Czysc", command=czysc_napisy)
# czysc_button.pack()

wynik_label = tkinter.Label(master=root, text="Koszt: -")
wynik_label.pack()

root.mainloop()