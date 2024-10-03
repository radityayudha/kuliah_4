import sys

def pilih_opsi(option, label):
    print(f"\nPilih {label}: ")
    for i, opt in enumerate(option, 1):
        print(f"{i}. {opt}")
    choice = int(input(f"Masukkan nomor pilihan {label}: "))
    
    # Validasi apakah pilihan sesuai dengan opsi yang diberikan
    if choice < 1 or choice > len(option):
        print(f"Pilihan {label} tidak valid. Program dihentikan.")
        sys.exit(1)  # Hentikan program jika input tidak valid
    return choice

def hitung_total(varian_crust, ukuran, topping_keju):
    harga_toping = 9.637
    
    if varian_crust == "1":
        harga_crust = {"personal" : 34.000, "sedang": 74.000, "besar": 105.000}.get(ukuran, 0)
    elif varian_crust == "2" or varian_crust == "3":
        harga_crust = {"personal" : 50.000, "sedang": 93.000, "besar": 130.000}.get(ukuran, 0)
    elif varian_crust == "4":
        harga_crust = {"personal" : 52.000, "sedang": 98.000, "besar": 139.000}.get(ukuran, 0)
    else:
        print("Pilihan varian crust tidak valid.")
        sys.exit(1)  # Hentikan program jika input tidak valid
    
    if topping_keju == "ya":
        harga_keju = 13.000
    else:
        harga_keju = 0
        
    total_harga = harga_toping + harga_crust + harga_keju
    return total_harga
    
# Daftar pilihan
toppings = ['Frankfurter bbq', 'Meat Monsta', 'Super Supreme', 'Super Supreme Chicken', 
            'Meat Lovers', 'Chicken Lovers', 'Cheese Lovers', 'American Favourite']
crusts = ['Pan Pizza', 'Stuffed Crust Sosis', 'Crowncrust', 'Cheesy Bites']
sizes = ['personal', 'sedang', 'besar']

print("=" * 60)
print("SELAMAT DATANG DI KASIR KELOMPOK 3".center(60))
print("=" * 60)

# Pilihan pengguna
toping = pilih_opsi(toppings, 'Topping')
varian_crust = pilih_opsi(crusts, 'Crust')
ukuran = pilih_opsi(sizes, 'Ukuran')
topping_keju = input("\nTambah topping keju di pesanan anda? (ya/tidak): ").lower()
    
# Hitung total
total = hitung_total(str(varian_crust), sizes[ukuran - 1], topping_keju)
print(f"\nTotal belanjaan: Rp.{total}")
