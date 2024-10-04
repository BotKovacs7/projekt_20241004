import tkinter as tk
from tkinter import ttk

# Hossz átváltás
def convert_length():
    value = float(entry_length.get())
    unit = combo_length.get()
    
    if egyseg == "Kilométer":
        miles = value * 0.621371
        meters = value * 1000
        millimeters = value * 1000000
    elif unit == "Mérföld":
        kilometers = value * 1.60934
        meters = value * 1609.34
        millimeters = value * 1609340
    elif unit == "Méters":
        kilometers = value / 1000
        miles = value / 1609.34
        millimeters = value * 1000
    elif unit == "Milliméter":
        kilometers = value / 1000000
        miles = value / 1609340
        meters = value / 1000
    
    label_result_length.config(text=f"Kilométer: {kilometers:.4f}, Mérföld: {miles:.4f}, Méter: {meters:.4f}, Milliméter: {millimeters:.4f}")

# Tömeg átváltás
def convert_weight():
    value = float(entry_weight.get())
    unit = combo_weight.get()
    
    if unit == "Kilogramm":
        pounds = value * 2.20462
        grams = value * 1000
        ounces = value * 35.274
    elif unit == "Font":
        kilograms = value / 2.20462
        grams = kilograms * 1000
        ounces = value * 16
    elif unit == "Gramm":
        kilograms = value / 1000
        pounds = kilograms * 2.20462
        ounces = kilograms * 35.274
    elif unit == "Uncia":
        kilograms = value / 35.274
        pounds = value / 16
        grams = kilograms * 1000
    
    label_result_weight.config(text=f"Kilogramm: {kilograms:.4f}, Font: {pounds:.4f}, Gramm: {grams:.4f}, Uncia: {ounces:.4f}")

# Idő átváltás
def convert_time():
    value = float(entry_time.get())
    unit = combo_time.get()
    
    if unit == "Óra":
        minutes = value * 60
        seconds = value * 3600
    elif unit == "Perc":
        hours = value / 60
        seconds = value * 60
    elif unit == "Másodperc":
        hours = value / 3600
        minutes = value / 60
    elif unit == "Nap":
        hours = value * 24
        minutes = value * 1440
        seconds = value * 86400
    
    label_result_time.config(text=f"Óra: {hours:.4f}, Perc: {minutes:.4f}, Másodperc: {seconds:.4f}")

# Fő ablak
root = tk.Tk()
root.title("Mértékegység Átváltó")

# Cím
label_title = tk.Label(root, text="Mértékegység Átváltó", font=("Helvetica", 16))
label_title.pack(pady=10)

# Gombok a mértékegység-típusokhoz
button_length = tk.Button(root, text="Hossz Átváltás", command=lambda: open_length_window())
button_length.pack(pady=5)

button_weight = tk.Button(root, text="Tömeg Átváltás", command=lambda: open_weight_window())
button_weight.pack(pady=5)

button_time = tk.Button(root, text="Idő Átváltás", command=lambda: open_time_window())
button_time.pack(pady=5)

button_exit = tk.Button(root, text="Kilépés", command=root.quit)
button_exit.pack(pady=20)

# Hossz ablak
def open_length_window():
    length_window = tk.Toplevel(root)
    length_window.title("Hossz Átváltás")
    
    global entry_length, combo_length, label_result_length
    
    label_length = tk.Label(length_window, text="Írd be az értéket:")
    label_length.pack(pady=5)
    
    entry_length = tk.Entry(length_window)
    entry_length.pack(pady=5)
    
    combo_length = ttk.Combobox(length_window, values=["Kilométer", "Mérföld", "Méters", "Milliméter"])
    combo_length.pack(pady=5)
    combo_length.current(0)  # Alapértelmezett kiválasztás

    button_convert_length = tk.Button(length_window, text="Számolás", command=convert_length)
    button_convert_length.pack(pady=5)

    label_result_length = tk.Label(length_window, text="")
    label_result_length.pack(pady=5)

    button_close_length = tk.Button(length_window, text="Ablak Bezárása", command=length_window.destroy)
    button_close_length.pack(pady=20)

# Tömeg ablak
def open_weight_window():
    weight_window = tk.Toplevel(root)
    weight_window.title("Tömeg Átváltás")
    
    global entry_weight, combo_weight, label_result_weight
    
    label_weight = tk.Label(weight_window, text="Írd be az értéket:")
    label_weight.pack(pady=5)
    
    entry_weight = tk.Entry(weight_window)
    entry_weight.pack(pady=5)
    
    combo_weight = ttk.Combobox(weight_window, values=["Kilogramm", "Font", "Gramm", "Uncia"])
    combo_weight.pack(pady=5)
    combo_weight.current(0)  # Alapértelmezett kiválasztás

    button_convert_weight = tk.Button(weight_window, text="Számolás", command=convert_weight)
    button_convert_weight.pack(pady=5)

    label_result_weight = tk.Label(weight_window, text="")
    label_result_weight.pack(pady=5)

    button_close_weight = tk.Button(weight_window, text="Ablak Bezárása", command=weight_window.destroy)
    button_close_weight.pack(pady=20)

# Idő ablak
def open_time_window():
    time_window = tk.Toplevel(root)
    time_window.title("Idő Átváltás")
    
    global entry_time, combo_time, label_result_time
    
    label_time = tk.Label(time_window, text="Írd be az értéket:")
    label_time.pack(pady=5)
    
    entry_time = tk.Entry(time_window)
    entry_time.pack(pady=5)
    
    combo_time = ttk.Combobox(time_window, values=["Óra", "Perc", "Másodperc", "Nap"])
    combo_time.pack(pady=5)
    combo_time.current(0)  # Alapértelmezett kiválasztás

    button_convert_time = tk.Button(time_window, text="Számolás", command=convert_time)
    button_convert_time.pack(pady=5)

    label_result_time = tk.Label(time_window, text="")
    label_result_time.pack(pady=5)

    button_close_time = tk.Button(time_window, text="Ablak Bezárása", command=time_window.destroy)
    button_close_time.pack(pady=20)

root.mainloop()