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
        orak = ertek / 60
        masodpercek = ertek * 60
    elif egyseg == "másodperc":
        orak = ertek / 3600
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
button_length = tk.Button(root, text="hossz átváltás", command=lambda: open_hossz_ablak())
button_length.pack(pady=5)

button_weight = tk.Button(root, text="tömeg átváltás", command=lambda: open_suly_ablak())
button_weight.pack(pady=5)

button_time = tk.Button(root, text="idő átváltás", command=lambda: open_ido_ablak())
button_time.pack(pady=5)

button_exit = tk.Button(root, text="kilépés", command=root.quit)
button_exit.pack(pady=20)

# Hossz ablak
def open_hossz_ablak():
    hosszablak = tk.Toplevel(root)
    hosszablak.title("hossz átváltás")
    
    global entry_length, combo_length, label_result_length
    
    label_hossz = tk.Label(hosszablak, text="ird be az értéket:")
    label_hossz.pack(pady=5)
    
    entry_hossz = tk.Entry(hosszablak)
    entry_hossz.pack(pady=5)
    
    combo_hossz = ttk.Combobox(hosszablak, values=["kilométer", "mérföld", "méters", "milliméter"])
    combo_hossz.pack(pady=5)
    combo_hossz.current(0)  # Alapértelmezett kiválasztás

    hosszkonvertalas = tk.Button(hosszablak, text="számolás", command=hossz)
    hosszkonvertalas.pack(pady=5)

    label_result_hossz = tk.Label(hosszablak, text="")
    label_result_hossz.pack(pady=5)

    gombzarhossz = tk.Button(hosszablak, text="ablak bezárása", command=hosszablak.destroy)
    gombzarhossz.pack(pady=20)

# Tömeg ablak
def open_suly_ablak():
    open_suly_ablak = tk.Toplevel(root)
    open_suly_ablak.title("tömeg átváltás")
    
    global entry_weight, combo_weight, label_result_weight
    
    label_suly = tk.Label(open_suly_ablak, text="írd be az értéket:")
    label_suly.pack(pady=5)
    
    entry_suly = tk.Entry(open_suly_ablak)
    entry_suly.pack(pady=5)
    
    combo_suly = ttk.Combobox(open_suly_ablak, values=["kilogramm","gramm"])
    combo_suly.pack(pady=5)
    combo_suly.current(0)  # Alapértelmezett kiválasztás

    sulykonvertalas = tk.Button(open_suly_ablak, text="számolás", command=suly)
    sulykonvertalas.pack(pady=5)

    label_result_suly = tk.Label(open_suly_ablak, text="")
    label_result_suly.pack(pady=5)

    gombzarsuly = tk.Button(open_suly_ablak, text="ablak bezárása", command=open_suly_ablak.destroy)
    gombzarsuly.pack(pady=20)

# Idő ablak
def open_ido_ablak():
    idoablak = tk.Toplevel(root)
    idoablak.title("idő átváltás")
    
    global entry_time, combo_time, label_result_time
    
    label_ido = tk.Label(idoablak, text="írd be az értéket:")
    label_ido.pack(pady=5)
    
    entry_ido = tk.Entry(idoablak)
    entry_ido.pack(pady=5)
    
    combo_ido = ttk.Combobox(idoablak, values=["óra", "perc", "másodperc", "nap"])
    combo_ido.pack(pady=5)
    combo_ido.current(0)  # Alapértelmezett kiválasztás

    idokonvertalas = tk.Button(idoablak, text="számolás", command=ido)
    idokonvertalas.pack(pady=5)

    label_result_ido = tk.Label(idoablak, text="")
    label_result_ido.pack(pady=5)

    gombzar = tk.Button(idoablak, text="ablak bezárása", command=idoablak.destroy)
    gombzar.pack(pady=20)

root.mainloop()