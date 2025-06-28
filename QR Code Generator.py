import tkinter as tk
from tkinter import filedialog, messagebox
import os
import qrcode

def funckija():
    podaci = entry.get()
    if not podaci:
        messagebox.showwarning("Unesi neki podatak!")
        return
    
    folder = filedialog.askdirectory(title = "Izaberi folder za cuvanje")
    if not folder:
        return
    

    try:
        img = qrcode.make(podaci)
        putanja = os.path.join(folder, "moj_qr_kod.png")
        img.save(putanja)
        messagebox.showinfo("Uspeh", f"QR kod sacuvan u: /n{putanja}")
    except Exception as e:
        messagebox.showerror("Greska", str(e))
    

window = tk.Tk()
window.title("QR Code Maker")
window.geometry("600x480")

tk.Label(window, text="Unesi podatak za QR kod: ").pack(pady=10)
entry = tk.Entry(window, width=40)
entry.pack()
tk.Button(window, text="Generiši QR kod", command=funckija, bg="green", fg="white").pack(pady=20)

window.mainloop()