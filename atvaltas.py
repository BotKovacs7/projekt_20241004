import tkinter as tk
from tkinter import ttk

# Hossz átváltás
def hossz():
    ertek = float(entry_hossz.get())
    egyseg = combo_hossz.get()
    
    if egyseg == "kilométer":
        merfoldek = ertek * 0,6215040397762585
        meterek = ertek * 1000
        millimeterek = ertek * 1000000
    elif egyseg == "mérföld":
        kilometerek = ertek * 1.609
        meterek = ertek * 1609
        millimeterek = ertek * 1609
    elif egyseg == "méter":
        kilometerek = ertek / 1000
        merfoldek = ertek / 1609
        millimeterek = ertek * 1000
    elif egyseg == "milliméter":
        kilometerek = ertek / 1000000
        merfoldek = ertek / 1609
        meterek = ertek / 1000
    
    label_result_hossz.config(text=f"kilométer: {kilometerek:.4f}, mérföld: {merfoldek:.4f}, méter: {meterek:.4f}, milliméter: {millimeterek:.4f}")

# Tömeg átváltás
def suly():
    ertek = float(entry_suly.get())
    egyseg = combo_suly.get()
    
    if egyseg == "kilogramm":
        gram = ertek * 1000
    elif egyseg == "font":
        kg = ertek / 2.20462
        gram = kg * 1000
    elif egyseg == "gramm":
        kg = ertek / 1000
    
    label_result_suly.config(text=f"kilogramm: {kg:.4f}, gramm: {gram:.4f}")

# Idő átváltás
def ido():
    ertek = float(entry_ido.get())
    egyseg = combo_ido.get()
    
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
    
    label_result_ido.config(text=f"óra: {orak:.4f}, perc: {percek:.4f}, másodperc: {masodpercek:.4f}")

# Fő ablak
root = tk.Tk()
root.title("mértékegység átváltó")

# Cím
cimkecim = tk.Label(root, text="mértékegység átváltó", font=("helvetica", 16))
cimkecim.pack(pady=10)

# Gombok a mértékegység-típusokhoz
gombhossz = tk.Button(root, text="hossz átváltás", command=lambda: open_hossz_ablak())
gombhossz.pack(pady=5)

gombsuly = tk.Button(root, text="tömeg átváltás", command=lambda: open_suly_ablak())
gombsuly.pack(pady=5)

gombido = tk.Button(root, text="idő átváltás", command=lambda: open_ido_ablak())
gombido.pack(pady=5)

gombkilep = tk.Button(root, text="kilépés", command=root.quit)
gombkilep.pack(pady=20)

# Hossz ablak
def open_hossz_ablak():
    hosszablak = tk.Toplevel(root)
    hosszablak.title("hossz átváltás")
    
    global entry_hossz, combo_hossz, label_result_hossz
    
    hosszcimke = tk.Label(hosszablak, text="írd be az értéket:")
    hosszcimke.pack(pady=5)
    
    entry_hossz = tk.Entry(hosszablak)
    entry_hossz.pack(pady=5)
    
    combo_hossz = ttk.Combobox(hosszablak, values=["kilométer", "mérföld", "méters", "milliméter"])
    combo_hossz.pack(pady=5)
    combo_hossz.current(0)  # Alapértelmezett kiválasztás

    combo_hossz1 = ttk.Combobox(hosszablak, values=["kilométer", "mérföld", "méters", "milliméter"])
    combo_hossz1.pack(pady=5)
    combo_hossz1.current(1)

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
    
    global entry_suly, combo_suly, label_result_suly
    
    sulycimke = tk.Label(open_suly_ablak, text="írd be az értéket:")
    sulycimke.pack(pady=5)
    
    entry_suly = tk.Entry(open_suly_ablak)
    entry_suly.pack(pady=5)
    
    combo_suly = ttk.Combobox(open_suly_ablak, values=["kilogramm","gramm"])
    combo_suly.pack(pady=5)
    combo_suly.current(0)  # Alapértelmezett kiválasztás

    combo_suly1 = ttk.Combobox(open_suly_ablak, values=["kilogramm","gramm"])
    combo_suly1.pack(pady=5)
    combo_suly1.current(1)

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
    
    global entry_ido, combo_ido, label_result_ido
    
    idocimke = tk.Label(idoablak, text="írd be az értéket:")
    idocimke.pack(pady=5)
    
    entry_ido = tk.Entry(idoablak)
    entry_ido.pack(pady=5)
    
    combo_ido = ttk.Combobox(idoablak, values=["óra", "perc", "másodperc", "nap"])
    combo_ido.pack(pady=5)
    combo_ido.current(0)  # Alapértelmezett kiválasztás

    combo_ido1 = ttk.Combobox(idoablak, values=["óra", "perc", "másodperc", "nap"])
    combo_ido1.pack(pady=5)
    combo_ido1.current(1)

    idokonvertalas = tk.Button(idoablak, text="számolás", command=ido)
    idokonvertalas.pack(pady=5)

    label_result_ido = tk.Label(idoablak, text="")
    label_result_ido.pack(pady=5)

    gombzar = tk.Button(idoablak, text="ablak bezárása", command=idoablak.destroy)
    gombzar.pack(pady=20)

root.mainloop()