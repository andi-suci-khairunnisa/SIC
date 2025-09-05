# ##soal nomor 1

# kopi = "Kopi Pagi"
# harga_kopi = 18000.5
# roti = "Roti Cokelat"
# harga_roti = 10000
# status = True

# print(f"""
# Nama produk 1: {kopi}
# Harga produk 1: {harga_kopi}
# Nama produk 2: {roti}
# Harga produk 2: {harga_roti}
# Status ketersediaan roti: {status}
#       """)

# ##soal nomor 2

# jumlah_kopi_str = input("Masukkan jumlah pesanan kopi: ")
# jumlah_roti_str = input("Masukkan jumlah pesanan roti: ")
# jumlah_kopi_int = int(jumlah_kopi_str)
# jumlah_roti_int = int(jumlah_roti_str)

# print(f"""
# Tipe data awal jumlah kopi: {type(jumlah_kopi_str)}
# Tipe data awal jumlah roti: {type(jumlah_roti_str)}
# Tipe data setelah konversi: {type(jumlah_kopi_int)}
#       """)

# ##soal nomor 3

# total_harga_kopi = harga_kopi * jumlah_kopi_int
# total_harga_roti = harga_roti * jumlah_roti_int
# total_belanja = total_harga_kopi + total_harga_roti
# uang_bayar = 50000
# kembalian = uang_bayar - total_belanja

# print(f"""
# Total harga kopi: {total_harga_kopi}
# Total harga roti: {total_harga_roti}
# Total belanja keseluruhan: {total_belanja}
# Uang yang dibayarkan: {uang_bayar}
# Kembalian: {kembalian}
#       """)

### soal nomor 4



kopi = "Kopi Pagi"
harga_kopi = 18000.5
nama_pelanggan = input("Masukkan nama pelanggan: ")
jumlah_kopi= int(input("Masukkan jumlah pesanan kopi: "))
total_harga_kopi = harga_kopi * jumlah_kopi

pesan_terima_kasih = "Terima kasih, ni" + nama_pelanggan +  " sudah berbelanja di Coffe Shop Bahagia"

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("*"*25)
print(pesan_terima_kasih)
print("*"*25)
print(f"Total {kopi} adalah Rp{total_harga_kopi}")
