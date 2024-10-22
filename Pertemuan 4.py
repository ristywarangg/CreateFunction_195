import math #library untuk operasi matematika

luas_lingkaran = lambda r: math.pi * r*r
#lambda :mendefinisikan fungsi anonim (tanpa nama) yang menerima satu parameter, yaitu r (jari-jari lingkaran).
#math.pi * r * r adalah ekspresi yang akan dievaluasi dan dikembalikan sebagai hasil dari fungsi. 


#Contoh penggunaannya
jari_jari = 7
area = luas_lingkaran(jari_jari)
#area :digunakan untuk menghitung dan menyimpan luas dari sebuah lingkaran berdasarkan jari-jari yang diberikan. 
print(f"Luas lingkaran dengan jari_jari {jari_jari} adalah {area:.2f}") 
#mencetak kalimat yang menjelaskan luas lingkaran berdasarkan nilai jari-jari yang diberikan dan hasil perhitungan luas,