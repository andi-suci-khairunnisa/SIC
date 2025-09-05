def konversi_suhu(nilai, dari, ke):
  if (dari == 'C') and (ke == 'F'):
    hasil = (nilai*9/5) + 32
    print(f"Hasil: {nilai}°C = {hasil:.2f}°F")

  elif (dari == 'C') and (ke == 'K'):
    hasil = nilai + 273.15
    print(f"Hasil: {nilai}°C = {hasil:.2f}°K")

  elif (dari == 'F') and (ke == 'C'):
    hasil = (nilai-32)*(5/9)
    print(f"Hasil: {nilai}°F = {hasil:.2f}°C")

  elif (dari == 'F') and (ke == 'K'):
    hasil = (nilai-32)*(5/9) + 273.15
    print(f"Hasil: {nilai}°F = {hasil:.2f}°K")

  elif (dari == 'K') and (ke == 'C'):
    hasil = nilai - 273.15
    print(f"Hasil: {nilai}°K = {hasil:.2f}°C")

  elif (dari == 'K') and (ke == 'F'):
    hasil = (nilai - 273.15) * (9/5) +32
    print(f"Hasil: {nilai}°K = {hasil:.2f}°F")

  else:
    print("Input yang dimasukkan tidak valid!")
    


