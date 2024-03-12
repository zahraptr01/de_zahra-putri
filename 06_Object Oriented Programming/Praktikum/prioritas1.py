# 1. desain kelas pelanggan
class Pelanggan:
    def __init__(self, nama, usia, idPelanggan):
        self.__nama = nama
        self.__usia = usia
        self.__idPelanggan = idPelanggan
    
    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama

    def get_usia(self):
        return self.__usia
    
    def set_usia(self, usia):
        self.__usia = usia

    def get_idPelanggan(self):
        return self.__idPelanggan
    
    def set_idPelanggan(self, idPelanggan):
        self.__idPelanggan

    def tampilkanInfo(self):
        print("Informasi Pelanggan")
        print("Nama : ", self.__nama)
        print("Usia : ", self.__usia)
        print("ID   : ", self.__idPelanggan)


# 2. desain kelas Pelatih
class Pelatih:
    def __init__ (self, nama, spesialisasi, tahunPengalaman):
        self.__nama = nama
        self.__spesialisai = spesialisasi
        self.__tahunPengalaman = tahunPengalaman
    
    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama

    def get_spesialisasi(self):
        return self.__spesialisai
    
    def set_spesialisasi(self, spesialisasi):
        self.__spesialisai

    def get_tahunPengalaman(self):
        return self.__tahunPengalaman
    
    def set_tahuPengalaman(self, tahunPengalaman):
        self.__tahunPengalaman

    def tampilkanInfo(self):
        print("Informasi Pelatih")
        print("Nama             : ", self.__nama)
        print("Spesialisasi     : ", self.__spesialisai)
        print("Tahun Pengalaman : ", self.__tahunPengalaman)


# 3. desain kelas KelasLatihan
class KelasLatihan(Pelatih):
    def __init__(self, nama, spesialisasi, tahunPengalaman, jenisLatihan, jadwal):
        super().__init__(nama, spesialisasi, tahunPengalaman)
        self.__jenisLatihan = jenisLatihan
        self.__jadwal = jadwal

    def get_jenisLatihan(self):
        return self.__jenisLatihan

    def set_jenisLatihan(self, jenisLatihan):
        self.__jenisLatihan 

    def get_jadwal(self):
        return self.__jadwal

    def set_jadwal(self):
        self.__jadwal

    def tampilkanInfo(self):
        super().tampilkanInfo()
        print("Jenis Latihan    : ", self.__jenisLatihan)  
        print("Jadwal           : ", self.__jadwal) 


# 4. demostrasi
pelanggan1 = Pelanggan("Zahra", 20, "001")
pelanggan1.tampilkanInfo()

pelatih1 = Pelatih("Putri", "Yoga", 3)
pelatih1.tampilkanInfo()

kelas_latihan1 = KelasLatihan("Putri", "Yoga", 3, "Yogaa", "Selasa 13.30")
kelas_latihan1.tampilkanInfo()