def to_celsius(nilai, dari):
    if dari == 'C':
        return nilai
    elif dari == 'F':
        return (nilai - 32) * 5/9
    elif dari == 'K':
        return nilai - 273.15
    else:
        raise ValueError("Skala asal tidak valid! Gunakan C, F, atau K.")

def from_celsius(nilai, ke):
    if ke == 'C':
        return nilai
    elif ke == 'F':
        return (nilai * 9/5) + 32
    elif ke == 'K':
        return nilai + 273.15
    else:
        raise ValueError("Skala tujuan tidak valid! Gunakan C, F, atau K.")

def konversi_suhu(nilai, dari, ke):
    try:
        # Step 1: konversi ke Celsius
        celsius = to_celsius(nilai, dari)

        # Step 2: konversi dari Celsius ke skala tujuan
        hasil = from_celsius(celsius, ke)

        print(f"Hasil: {nilai}°{dari} = {hasil:.2f}°{ke}")

    except ValueError as e:
        print(e)


