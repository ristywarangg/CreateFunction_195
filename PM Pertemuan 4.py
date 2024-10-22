def konversisuhu(temperature, value):
    if value == 'C':
        temperaturesuhu = (temperature - 32) * 5/9 #Menghitung suhu dalam Celsius menggunakan rumus konversi.
        return temperature, 'C' #Mengembalikan hasil konversi dan unit 'C'
    else:
        temperaturesuhu = (temperature * 9/5) + 32 #Menghitung suhu dalam Fahrenheit
        return temperaturesuhu, 'F' #Mengembalikan hasil konversi dan unit 'F'

 #contoh penggunaan   
celsius_temperature = 30 #Variabel celsius_temperature diatur ke 30, yang berarti suhu yang ingin dikonversi adalah 30°C.
temperaturesuhu, terget_value = konversisuhu(celsius_temperature, 'F') #Memanggil fungsi konversisuhu dengan celsius_temperature dan 'F', dan menyimpan hasil konversi dalam temperaturesuhu dan target_value.
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°(target_value)")
#Output yang dihasilkan menunjukkan suhu dalam Celsius yang telah dikonversi ke Fahrenheit.


fahrenheit_temperature = 86 #Variabel ini menyimpan nilai suhu yang ingin dikonversi, di sini suhu yang diberikan adalah 86°F.
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C') #Memanggil fungsi konversisuhu dengan dua argumen 
print(f"{fahrenheit_temperature}°F dikonversi ke Celsius adalah {temperaturesuhu}°{target_value}")
#memberikan hasil konversi suhu