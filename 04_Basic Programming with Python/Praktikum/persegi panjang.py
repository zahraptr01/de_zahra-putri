print ("Menghitung Luas Persegi Panjang")

# p = 5
# l = 4

p = int (input ("Masukkan nilai panjang : "))
l = int (input ("Masukkan nilai lebar : "))

L = p * l
print ("Luas persegi panjang adalah : ", )
if L % 2 == 0:
    print ("even rectangle")
else:
    print ("odd rectangle")
