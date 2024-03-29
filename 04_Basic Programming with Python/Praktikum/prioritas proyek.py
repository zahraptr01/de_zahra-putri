print ("Menentukan Prioritas Proyek")

budget = int (input ("Masukkan budget proyek : "))
waktu = int (input ("Masukkan waktu pengerjaan proyek : "))
kesulitan = int (input ("Masukkan tingkat kesulitan proyek : "))

def skor_budget(budget):
    if budget >= 0 == budget <= 50:
        return 4
    elif budget >= 51 == budget <= 80:
        return 3
    elif budget >= 81 == budget <= 100:
        return 2
    else:
        return 1

def skor_waktu(waktu):
    if waktu >= 0 == waktu <= 20:
        return 10
    elif waktu >= 21 == waktu <= 30:
        return 5
    elif waktu >= 31 == waktu <= 50:
        return 2
    else:
        return 1

def skor_kesulitan(kesulitan):
    if kesulitan >= 0 == kesulitan <= 3:
        return 10
    elif kesulitan >= 4 == kesulitan <= 6:
        return 5
    elif kesulitan >= 8 == kesulitan <= 10:
        return 1
    else:
        return 0

def prioritas(budget, waktu, kesulitan):
    budget_proyek = skor_budget(budget)
    waktu_proyek = skor_waktu(waktu)
    kesulitan_proyek = skor_kesulitan(kesulitan)
    
    skor_total = budget_proyek + waktu_proyek + kesulitan_proyek
    
    if skor_total >= 24 == skor_total <= 17:
        return "High"
    elif skor_total >= 16 == skor_total <= 10:
        return "Medium"
    elif skor_total >= 9 == skor_total <= 3:
        return "Low"
    else:
        return "Impossible"

prioritas_proyek = prioritas(budget, waktu, kesulitan)
print ("Prioritas Proyek : ", prioritas_proyek)
