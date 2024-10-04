import tkinter as tk
from tkinter import ttk

# Hossz átváltás
def hossz():
    ertek = float(entry_length.get())
    egyseg = combo_length.get()
    
    if egyseg == "kilométer":
        merfoldek = ertek * 0,6215040397762585
        meterek = ertek * 1000
        millimeterek = ertek * 1000000
    elif egyseg == "mérföld":
        kilometerek = ertek * 1.609
        meterek = ertek * 1609
        millimeterek = ertek * 1609
    elif egyseg == "méters":
        kilometerek = ertek / 1000
        merfoldek = ertek / 1609
        millimeterek = ertek * 1000
    elif egyseg == "milliméter":
        kilometerek = ertek / 1000000
        merfoldek = ertek / 1609
        meterek = ertek / 1000
    
    label_result_length.config(text=f"kilométer: {kilometerek:.4f}, mérföld: {merfoldek:.4f}, méter: {meterek:.4f}, milliméter: {millimeterek:.4f}")

# Tömeg átváltás
def suly():
    ertek = float(entry_weight.get())
    egyseg = combo_weight.get()
    
    if egyseg == "kilogramm":
        gram = ertek * 1000
    elif egyseg == "font":
        kg = ertek / 2.20462
        gram = kg * 1000
    elif egyseg == "gramm":
        kg = ertek / 1000
    
    label_result_weight.config(text=f"kilogramm: {kg:.4f}, gramm: {gram:.4f}")

# Idő átváltás
def ido():
    ertek = float(entry_time.get())
    egyseg = combo_time.get()
    
    if egyseg == "óra":
        percek = ertek * 60
        masodpercek = ertek * 3600
    elif egyseg == "perc":
        hours = ertek / 60
        masodpercek = ertek * 60
    elif egyseg == "másodperc":
        hours = ertek / 3600
        percek = ertek / 60
    elif egyseg == "nap":
        orak = ertek * 24
        percek = ertek * 1440
        masodpercek = ertek * 86400
    
    label_result_time.config(text=f"óra: {orak:.4f}, perc: {percek:.4f}, másodperc: {masodpercek:.4f}")

# Fő ablak
root = tk.Tk()
root.title("mértékegység átváltó")

# Cím
label_title = tk.Label(root, text="mértékegység átváltó", font=("helvetica", 16))
label_title.pack(pady=10)

# Gombok a mértékegység-típusokhoz
button_length = tk.Button(root, text="hossz átváltás", command=lambda: open_length_window())
button_length.pack(pady=5)

button_weight = tk.Button(root, text="tömeg átváltás", command=lambda: open_weight_window())
button_weight.pack(pady=5)

button_time = tk.Button(root, text="idő átváltás", command=lambda: open_time_window())
button_time.pack(pady=5)

button_exit = tk.Button(root, text="kilépés", command=root.quit)
button_exit.pack(pady=20)

# Hossz ablak
def open_length_window():
    length_window = tk.Toplevel(root)
    length_window.title("hossz átváltás")
    
    global entry_length, combo_length, label_result_length
    
    label_length = tk.Label(length_window, text="ird be az értéket:")
    label_length.pack(pady=5)
    
    entry_length = tk.Entry(length_window)
    entry_length.pack(pady=5)
    
    combo_length = ttk.Combobox(length_window, values=["kilométer", "mérföld", "méters", "milliméter"])
    combo_length.pack(pady=5)
    combo_length.current(0)  # Alapértelmezett kiválasztás

    button_convert_length = tk.Button(length_window, text="számolás", command=convert_length)
    button_convert_length.pack(pady=5)

    label_result_length = tk.Label(length_window, text="")
    label_result_length.pack(pady=5)

    button_close_length = tk.Button(length_window, text="ablak bezárása", command=length_window.destroy)
    button_close_length.pack(pady=20)

# Tömeg ablak
def open_weight_window():
    weight_window = tk.Toplevel(root)
    weight_window.title("tömeg átváltás")
    
    global entry_weight, combo_weight, label_result_weight
    
    label_weight = tk.Label(weight_window, text="írd be az értéket:")
    label_weight.pack(pady=5)
    
    entry_weight = tk.Entry(weight_window)
    entry_weight.pack(pady=5)
    
    combo_weight = ttk.Combobox(weight_window, values=["kilogramm", "font", "gramm", "uncia"])
    combo_weight.pack(pady=5)
    combo_weight.current(0)  # Alapértelmezett kiválasztás

    button_convert_weight = tk.Button(weight_window, text="számolás", command=convert_weight)
    button_convert_weight.pack(pady=5)

    label_result_weight = tk.Label(weight_window, text="")
    label_result_weight.pack(pady=5)

    button_close_weight = tk.Button(weight_window, text="ablak bezárása", command=weight_window.destroy)
    button_close_weight.pack(pady=20)

# Idő ablak
def open_time_window():
    time_window = tk.Toplevel(root)
    time_window.title("idő átváltás")
    
    global entry_time, combo_time, label_result_time
    
    label_time = tk.Label(time_window, text="írd be az értéket:")
    label_time.pack(pady=5)
    
    entry_time = tk.Entry(time_window)
    entry_time.pack(pady=5)
    
    combo_time = ttk.Combobox(time_window, values=["óra", "perc", "másodperc", "nap"])
    combo_time.pack(pady=5)
    combo_time.current(0)  # Alapértelmezett kiválasztás

    button_convert_time = tk.Button(time_window, text="számolás", command=convert_time)
    button_convert_time.pack(pady=5)

    label_result_time = tk.Label(time_window, text="")
    label_result_time.pack(pady=5)

    button_close_time = tk.Button(time_window, text="ablak bezárása", command=time_window.destroy)
    button_close_time.pack(pady=20)

hossz()
suly()
ido()
root.mainloop()