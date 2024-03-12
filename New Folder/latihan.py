# contoh membuat class

class Robot:
    pass #untuk menandai bahwa blok kelas kosong dan tidak memiliki implementasi

# instance 
class Cat:
    def __init__ (self, fur_color="No Name", num_of_leg=4): #method constructor
        self._fur_color = fur_color
        self.num_of_leg = num_of_leg

manis = Cat("Hitam", 4)
pussy = Cat("Putih", 3)

# contoh tipe atribut
class Mobil:
    def __init__(self, tipe, name, roda, platnum):
        self.roda = roda #public. atribut dapat diakses melalui kelas sendiri atau di luar kelas
        self._type = tipe #protected, hanya bisa diakses oleh kelas sendiri dan kelas turunannya
        self.__name = name #private, hanya bisa diakses oleh kelasnya sendiri
        self.__platnum = platnum #private, hanya bisa diakses oleh kelasnya sendiri

class Bebek:
    def speak(self, bunyi_suara):
        return bunyi_suara

# membut objek dari kelas Bebek
donald = Bebek()

# memanggil method Speak
suara_donald = donald.speak("Kwek Kwek")
print (suara_donald)