import tkinter as tk

def toplama(event=None):
    try:
        sayi1 = float(entry_sayi1.get())
        sayi2 = float(entry_sayi2.get())
        sonuc = sayi1 + sayi2
        label_sonuc.config(text="Sonuc: " + str(sonuc))
    except ValueError:
        label_sonuc.config(text="Sonuc: Geçersiz giriş!")

def cikarma(event=None):
    try:
        sayi1 = float(entry_sayi1.get())
        sayi2 = float(entry_sayi2.get())
        sonuc = sayi1 - sayi2
        label_sonuc.config(text="Sonuc: " + str(sonuc))
    except ValueError:
        label_sonuc.config(text="Sonuc: Geçersiz giriş!")

def carpma(event=None):
    try:
        sayi1 = float(entry_sayi1.get())
        sayi2 = float(entry_sayi2.get())
        sonuc = sayi1 * sayi2
        label_sonuc.config(text="Sonuc: " + str(sonuc))
    except ValueError:
        label_sonuc.config(text="Sonuc: Geçersiz giriş!")

def bolme(event=None):
    try:
        sayi1 = float(entry_sayi1.get())
        sayi2 = float(entry_sayi2.get())
        if sayi2 == 0:
            raise ZeroDivisionError("Sıfıra bölme hatası!")
        sonuc = sayi1 / sayi2
        label_sonuc.config(text="Sonuc: " + str(sonuc))
    except ValueError:
        label_sonuc.config(text="Sonuc: Geçersiz giriş!")
    except ZeroDivisionError as e:
        label_sonuc.config(text="Sonuc: " + str(e))

def eski_renge_don(event, button):
    button.config(bg=button["bg"], activebackground=button["activebackground"])

# Ana pencere
root = tk.Tk()
root.title("Hesap Makinesi")
root.geometry("380x190")

# Arka plan rengini değiştirme
root.config(bg="#f0f0f0")

# Giriş etiketleri
label_sayi1 = tk.Label(root, text="Sayı 1:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
label_sayi1.grid(row=0, column=0, padx=5, pady=5)
entry_sayi1 = tk.Entry(root, font=("Helvetica", 12), bg="#fff", fg="#333", highlightthickness=2, highlightbackground="#ccc")
entry_sayi1.grid(row=0, column=1, padx=5, pady=5)

label_sayi2 = tk.Label(root, text="Sayı 2:", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
label_sayi2.grid(row=1, column=0, padx=5, pady=5)
entry_sayi2 = tk.Entry(root, font=("Helvetica", 12), bg="#fff", fg="#333", highlightthickness=2, highlightbackground="#ccc")
entry_sayi2.grid(row=1, column=1, padx=5, pady=5)

# Buttons
button_toplama = tk.Button(root, text="Topla", command=toplama, font=("Helvetica", 12), bg="#4CAF50", fg="white", activebackground="#388E3C", activeforeground="white", width=10, relief=tk.RAISED)
button_toplama.grid(row=2, column=0, padx=5, pady=5)
button_toplama.bind("<ButtonRelease-1>", lambda event: eski_renge_don(event, button_toplama))

button_cikarma = tk.Button(root, text="Çıkar", command=cikarma, font=("Helvetica", 12), bg="#f44336", fg="white", activebackground="#D32F2F", activeforeground="white", width=10, relief=tk.RAISED)
button_cikarma.grid(row=2, column=0, padx=5, pady=5)
button_cikarma.place(x=260, y=78)
button_cikarma.bind("<ButtonRelease-1>", lambda event: eski_renge_don(event, button_cikarma))

button_carpma = tk.Button(root, text="Çarp", command=carpma, font=("Helvetica", 12), bg="#2196F3", fg="white", activebackground="#1976D2", activeforeground="white", width=10, relief=tk.RAISED)
button_carpma.grid(row=3, column=0, padx=5, pady=5)
button_carpma.bind("<ButtonRelease-1>", lambda event: eski_renge_don(event,button_carpma))

button_bolme = tk.Button(root, text="Böl", command=bolme, font=("Helvetica", 12), bg="#FFC0CB", fg="white", activebackground="#FF6EC7", activeforeground="white", width=10, relief=tk.RAISED)
button_bolme.grid(row=3, column=0, padx=5, pady=5)
button_bolme.place(x=260, y=118)
button_bolme.bind("<ButtonRelease-1>", lambda event: eski_renge_don(event,button_carpma))

# Sonuç
label_sonuc = tk.Label(root, text="Sonuc:", font=("Helvetica", 12, "bold"), bg="#f0f0f0", fg="#333")
label_sonuc.grid(row=4, columnspan=2, padx=5, pady=5)

root.mainloop()
