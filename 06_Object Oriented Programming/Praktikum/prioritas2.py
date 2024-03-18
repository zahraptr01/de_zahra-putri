class KelasLatihan:
    def __init__(self, namaPelatih, jenisLatihan, jadwal):
        self.nama_pelatih = namaPelatih
        self.jenis_latihan = jenisLatihan
        self.jadwal = jadwal

    def tampilkan_info(self):
        print("Informasi Kelas Latihan")
        print("Nama Pelatih  : ", self.nama_pelatih)
        print("Jenis Latihan : ", self.jenis_latihan)
        print("Jadwal        : ", self.jadwal)

class Yoga(KelasLatihan):
    def __init__(self, namaPelatih, tingkatKesulitan, jadwal):
        super().__init__(namaPelatih, "Yoga", jadwal)
        self.tingkat_kesulitan = tingkatKesulitan

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Tingkat Kesulitan : ", self.tingkat_kesulitan)
    
    def aturPosisiYoga(self, posisi):
        print("Posisi Yoga diatur menjadi : ", posisi)

class AngkatBeban(KelasLatihan):
    def __init__(self, namaPelatih, beratMaksimum, jadwal):
        super().__init__(namaPelatih, "Angkat Beban", jadwal)
        self.berat_maksimum = beratMaksimum

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Berat Maksimum : ", self.berat_maksimum)

    def aturBeratBadan(self, bb):
        print("Berat badan diatur menjadi : ", bb)

def polymorphism(kelas_latihan):
    if isinstance(kelas_latihan, Yoga):
        kelas_latihan.aturPosisiYoga("Lotus")
    elif isinstance(kelas_latihan, AngkatBeban):
        kelas_latihan.aturBeratBadan(40)

yoga_kelas = Yoga("Zahra", "Menengah", "selasa 14.30")
angkatBeban_kelas = AngkatBeban("Putri", 100, "Selasa 15.00")

kelas_latihan_arr = [yoga_kelas, angkatBeban_kelas]

for kelas_latihan in kelas_latihan_arr:
    kelas_latihan.tampilkan_info()
    polymorphism(kelas_latihan)