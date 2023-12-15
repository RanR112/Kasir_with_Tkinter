import tkinter as tk
import random
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk

layar = tk.Tk()
layar.title("KASIR AIUEO")
layar.geometry("1920x1200")

logo = Image.open("logoaiueoblack.png")
logo = logo.resize((60, 60))
logo = ImageTk.PhotoImage(logo)

totalBiaya = 0
totalKuantitas = 0

produk = {
    1:{"nama":"Pensil","harga":2000},
    2:{"nama":"Pulpen Standard Hitam","harga":3000},
    3:{"nama":"Pensil Warna","harga":15000},
    4:{"nama":"Crayon","harga":17000},
    5:{"nama":"Spidol","harga":2000},
    6:{"nama":"Spidol Snowman","harga":8000},
    7:{"nama":"Stabilo","harga":5000},
    8:{"nama":"Penghapus","harga":2000},
    9:{"nama":"Tipe X","harga":6000},
    10:{"nama":"Serutan","harga":2000},
    11:{"nama":"Buku Tulis","harga":3000},
    12:{"nama":"Buku Gambar","harga":6000},
    13:{"nama":"Sampul Buku","harga":2000},
    14:{"nama":"Map","harga":4000},
    15:{"nama":"Sticky Note","harga":15000},
    16:{"nama":"Paper Clip","harga":5000},
    17:{"nama":"Lem Fox","harga":12000},
    18:{"nama":"Gunting","harga":5000},
    19:{"nama":"Kertas Folio","harga":500},
    20:{"nama":"Origami","harga":12000},
    21:{"nama":"Penggaris Plastik","harga":3000},
    22:{"nama":"Penggaris Besi","harga":7000},
    23:{"nama":"Sketch Book","harga":40000},
    24:{"nama":"Kertas HVS","harga":200},
    25:{"nama":"Pulpen Standard Merah","harga":3000},
    26:{"nama":"Pulpen Standard Biru","harga":3000},
    27:{"nama":"Binder","harga":20000},
    28:{"nama":"Pensil Case","harga":7000},
    29:{"nama":"Cutter","harga":8000},
    30:{"nama":"Refill Cutter","harga":5000},
    31:{"nama":"Kalkulator","harga":15000},
    32:{"nama":"Pita","harga":3000},
    33:{"nama":"Kertas Kado","harga":3000},
    34:{"nama":"Staples","harga":7000},
    35:{"nama":"Refill Staples","harga":2000},
    36:{"nama":"Kertas Asturo Merah Muda","harga":1000},
    37:{"nama":"Kertas Asturo Biru Muda","harga":1000},
    38:{"nama":"Kertas Asturo Biru Tua","harga":1000},
    39:{"nama":"Kertas Asturo Merah Tua","harga":1000},
    40:{"nama":"Kertas Asturo Kuning Tua","harga":1000},
    41:{"nama":"Kertas Asturo Kuning Muda","harga":1000},
    42:{"nama":"Kertas Asturo Hijau Tua","harga":1000},
    43:{"nama":"Kertas Asturo Hijau Muda","harga":1000},
    44:{"nama":"Kertas Asturo Hitam","harga":1000},
    45:{"nama":"Kertas Asturo Putih","harga":1000},
    46:{"nama":"Kertas Asturo Coklat","harga":1000},
    47:{"nama":"Kertas Asturo Oranye","harga":1000},
    48:{"nama":"Kertas Asturo Ungu","harga":1000},
    49:{"nama":"Selotip","harga":2000},
    50:{"nama":"Lakban","harga":5000},
    51:{"nama":"Pulpen Joyko Q-Gel","harga":5000},
    52:{"nama":"Drawing Pen Snowman 0.1","harga":8000},
    53:{"nama":"Drawing Pen Snowman 0.2","harga":8000},
    54:{"nama":"Drawing Pen Snowman 0.3","harga":8000},
    55:{"nama":"Drawing Pen Snowman 0.4","harga":8000},
    56:{"nama":"Drawing Pen Snowman 0.5","harga":8000},
    57:{"nama":"Drawing Pen Snowman 0.6","harga":8000},
    58:{"nama":"Pensil Mekanik Joyko","harga":6000},
    59:{"nama":"Refill Pensil Mekanik Joyko","harga":2000},
    60:{"nama":"Lem Korea","harga":5000},
}

kasir = ["Aprianingtyas MP", "Giebran Abdillah", "Randy Rafael", "Ratih Burhana"]

def hargaMuncul(event):
    nama_produk = pilihProduk.get()
    for k, v in produk.items():
        if v["nama"] == nama_produk:
            harga.set(v["harga"])
            break

def barangSerupa(event):
    teksProduk = pilihProduk.get().lower()
    barangMirip = [barang for barang in daftarProduk if teksProduk in barang.lower()]
    pilihProduk['values'] = barangMirip

def tambahProduk():
    produkDipilih = pilihProduk.get()
    
    if not produkDipilih:
        messagebox.showerror("Error", "Pilih Produk Terlebih Dahulu!")
        return
    
    try:
        kuantitas = int(inputKuantitas.get())
    except:
        messagebox.showerror("Error", "Tentukan Jumlah Terlebih Dahulu!")
        return
    
    if kuantitas <= 0:
        messagebox.showerror("Error", "Jumlah Harus Lebih dari 0!")
        return
    
    global totalBiaya, totalKuantitas
    produkCocok = [(kode, infoProduk) for kode, infoProduk in produk.items() if infoProduk['nama'] == produkDipilih]
    
    if produkCocok:
        kodeProduk, infoProduk = produkCocok[0]
        namaProduk = infoProduk['nama']
        hargaProduk = infoProduk['harga']
        totalHarga = hargaProduk*kuantitas
        
        produkSama = keranjang.get_children()
        for item in produkSama:
            itemDetail = keranjang.item(item, "values")
            if itemDetail[1] == namaProduk:
                kuantitasAwal = int(itemDetail[3])
                totalHargaAwal = int(itemDetail[4])
                keranjang.delete(item)
                kuantitas += kuantitasAwal
                totalHarga += totalHargaAwal
                totalBiaya -= totalHargaAwal
        
        keranjang.insert("", "end", values=(kodeProduk, namaProduk, hargaProduk, kuantitas, totalHarga))
        
        totalBiaya += totalHarga
        totalKuantitas += kuantitas
        
        labelTotal.config(text=f"Total Biaya: Rp {totalBiaya:,.2f}")
        harga.set("")
        inputKuantitas.delete(0, tk.END)
        pilihProduk.delete(0, tk.END)
        pilihProduk['values'] = daftarProduk
    else:
        messagebox.showerror("Error", "Produk Tidak Valid!")

def randomstruk(x):
    acak = "00112233445566778899AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZ"
    return ''.join(random.choice(acak) for i in range(x))

def checkout():
    jumlahBayar = inputCheckout.get()
    
    try:
        jumlahBayar = int(jumlahBayar)
    except:
        messagebox.showerror("Error", "Input Tidak Valid!")
        return
    
    if jumlahBayar < totalBiaya:
        messagebox.showerror("Error", "Saldo Tidak Mencukupi!")
        
    elif totalBiaya == 0:
        messagebox.showerror("Error", "Tidak Ada Produk di Keranjang")
        
    else:
        kembalian = jumlahBayar - totalBiaya
        labelKembalian.config(text=f"Kembalian: Rp {kembalian:,.2f}")
        
        kasirOutput = pilihKasir.get()
        if not kasirOutput:
            messagebox.showerror("Error", "Pilih Nama Kasir!")
            return

        pembeliOutput = inputNama.get()
        if not pembeliOutput:
            messagebox.showerror("Error", "Isi Nama Pembeli!")
            return
        
        struk = f"\n\n{'A I U E O  ATK':^40}\n{'Jl.Cianjur, Karangpawitan,':^40}\n{'Kec. Karawang Bar., Karawang,':^40}\n{'Jawa Barat 41315, Indonesia':^40}\n{'Kab. Karawang':^40}\n\n{'='*38:^40}"
        struk += f" No Struk\t\t    : {randomstruk(10)}\n Waktu\t\t    : {datetime.now().strftime('%d %b %y, %H:%M')}\n Kasir\t\t    : {kasirOutput}\n Pembeli\t\t    : {pembeliOutput}\n{'-'*38:^40}"
        for produk in keranjang.get_children():
            nilai = keranjang.item(produk, "values")
            kodeProduk, namaProduk, hargaProduk, kuantitas, totalHarga = nilai
            hargaProduk = int(hargaProduk)
            totalHarga = int(totalHarga)
            kuantitas = int(kuantitas)
            struk += f"\n {kodeProduk}/{namaProduk}\n{kuantitas:>5,} x {hargaProduk:>6,}{totalHarga:>25,}"
        struk += f"\n{'-'*38:^40}\n Total Tagihan{totalBiaya:>25,}\n Total Bayar{jumlahBayar:>27,}\n Kembalian{kembalian:>29,}\n Total Barang{totalKuantitas:>26,}\n{'='*38:^40}\n\n\n{'<------- Terimakasih ------->':^40}\n\n"
        
        strukTeks.config(state=tk.NORMAL)
        strukTeks.delete(1.0, tk.END)
        strukTeks.insert(tk.END, "\n\n\t\t")
        strukTeks.image_create(tk.END, image=logo)
        strukTeks.insert(tk.END, struk)
        strukTeks.config(state=tk.DISABLED)
        messagebox.showinfo("Info", "Struk Berhasil Dicetak")

def hapusProduk():
    produkDihapus = keranjang.selection()
    if not produkDihapus:
        messagebox.showerror("Error", "Pilih Item yang Ingin Dihapus")
        return
    else:
        for item in produkDihapus:
            itemDetails = keranjang.item(item, "values")
            hargaDihapus = int(itemDetails[4])
            kuantitasDihapus = int(itemDetails[3])
            keranjang.delete(item)
            global totalBiaya, totalKuantitas
            totalBiaya -= hargaDihapus
            totalKuantitas -= kuantitasDihapus
            labelTotal.config(text=f"Total Biaya: Rp {totalBiaya:,.2f}")

def reset():
    global totalBiaya, totalKuantitas
    totalBiaya = 0
    totalKuantitas = 0
    pilihProduk.delete(0, tk.END)
    keranjang.delete(*keranjang.get_children())
    labelTotal.config(text="Total Biaya: Rp 0.00")
    labelKembalian.config(text="Kembalian: Rp 0.00")
    inputCheckout.delete(0, tk.END)
    pilihKasir.delete(0, tk.END)
    inputNama.delete(0, tk.END)
    harga.set("")
    strukTeks.config(state=tk.NORMAL)
    strukTeks.delete(1.0, tk.END)
    strukTeks.insert(tk.END, "\n\n\t\t")
    strukTeks.image_create(tk.END, image=logo)
    strukTeks.insert(tk.END, f"\n\n{'A I U E O  ATK':^40}\n{'Jl.Cianjur, Karangpawitan,':^40}\n{'Kec. Karawang Bar., Karawang,':^40}\n{'Jawa Barat 41315, Indonesia':^40}\n{'Kab. Karawang':^40}\n\n{'='*38:^40}")
    strukTeks.config(state=tk.DISABLED)
    
    messagebox.showinfo("Info", "Kasir Berhasil Di Reset")

namaToko = tk.Label(layar, text="PROGRAM KASIR TOKO AIUEO", font=("Helevetica", 18, "bold"))
namaToko.pack()

frame1 = tk.Frame(layar)
frame1.pack()

labelProduk = tk.Label(frame1, text="Produk :")
labelProduk.grid(row=0, column=0, padx=5, pady=15)

daftarProduk = sorted([v["nama"] for k, v in produk.items()])

pilihProduk = ttk.Combobox(frame1, values=daftarProduk, width=30)
pilihProduk.grid(row=0, column=1, padx= 10, pady=15)
pilihProduk.bind("<<ComboboxSelected>>", hargaMuncul)
pilihProduk.bind("<KeyRelease>", barangSerupa)

labelHarga = tk.Label(frame1, text="Harga :")
labelHarga.grid(row=0, column=2, padx=5, pady=15)

harga = tk.StringVar()
harga.set("")

daftarHarga = tk.Entry(frame1, textvariable=harga, state='readonly')
daftarHarga.grid(row=0, column=3, padx=10, pady=15)

labelKuantitas = tk.Label(frame1, text="Jumlah :")
labelKuantitas.grid(row=0, column=4, padx=5, pady=15)

inputKuantitas = tk.Entry(frame1)
inputKuantitas.grid(row=0, column=5, padx=10, pady=15)

tombolKeranjang = tk.Button(frame1, text="Tambahkan ke Keranjang", command=tambahProduk)
tombolKeranjang.grid(row=0, column=6, padx=10, pady=15)

frame2 = tk.Frame(layar)
frame2.pack()

keranjang = ttk.Treeview(frame2, columns=("KODE", "NAMA PRODUK", "HARGA", "JUMLAH", "TOTAL"), height=8)
keranjang.heading("#1", text="KODE")
keranjang.heading("#2", text="NAMA PRODUK")
keranjang.heading("#3", text="HARGA")
keranjang.heading("#4", text="JUMLAH")
keranjang.heading("#5", text="TOTAL")

keranjang.column("#1", width=100, anchor="center", stretch=False)
keranjang.column("#2", width=250, anchor="center", stretch=False)
keranjang.column("#3", width=150, anchor="center", stretch=False)
keranjang.column("#4", width=100, anchor="center", stretch=False)
keranjang.column("#5", width=150, anchor="center", stretch=False)
keranjang.column("#0", width=0, anchor="center", stretch=False)

keranjang.pack()

tombolHapus = tk.Button(frame2, text="Hapus dari Keranjang", command=hapusProduk)
tombolHapus.pack(pady=10)

frame3 = tk.Frame()
frame3.pack()

labelTotal = tk.Label(frame3, text="Total Biaya: Rp 0.00")
labelTotal.grid(row=0, column=0, padx=30)

labelKembalian = tk.Label(frame3, text="Kembalian: Rp 0.00")
labelKembalian.grid(row=1, column=0, padx=30)

labelCheckout = tk.Label(frame3, text="Masukkan Saldo: Rp")
labelCheckout.grid(row=2, column=0, padx=30)

inputCheckout = tk.Entry(frame3)
inputCheckout.grid(row=3, column=0, padx=30)

namaKasir = tk.Label(frame3, text="Nama Kasir:")
namaKasir.grid(row=0, column=1, padx=30)

pilihKasir = ttk.Combobox(frame3, values=kasir, width=17)
pilihKasir.grid(row=1, column=1, padx=30)

namaPembeli = tk.Label(frame3, text="Masukkan Nama Pembeli:")
namaPembeli.grid(row=2, column=1, padx=30)

inputNama = tk.Entry(frame3)
inputNama.grid(row=3, column=1, padx=30)

frame4 = tk.Frame()
frame4.pack()

tombolCheckout = tk.Button(frame4, text="Checkout", command=checkout)
tombolCheckout.pack(pady=10)

strukTeks = tk.Text(frame4, height=24, width=40)
strukTeks.insert(tk.END, "\n\n\t\t")
strukTeks.image_create(tk.END, image=logo)
strukTeks.insert(tk.END, f"\n\n{'A I U E O  ATK':^40}\n{'Jl.Cianjur, Karangpawitan,':^40}\n{'Kec. Karawang Bar., Karawang,':^40}\n{'Jawa Barat 41315, Indonesia':^40}\n{'Kab. Karawang':^40}\n\n{'='*38:^40}")
strukTeks.config(state=tk.DISABLED)
strukTeks.pack()

tombolReset = tk.Button(frame4, text="Reset Kasir", command=reset)
tombolReset.pack(pady=10)

layar.mainloop()