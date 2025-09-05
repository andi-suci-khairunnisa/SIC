from function import konversi_suhu

nilai = int(input("Masukkan nilai suhu: "))
dari = input("Dari satuan (C/F/K): ")
ke = input("Ke satuan (C/F/K): ")

konversi_suhu(nilai,dari.upper(),ke.upper())