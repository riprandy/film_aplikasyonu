# main.py



# api key =29fdb2ca 
# Ana Film sınıfı
class Film:
    def __init__(self, isim, yonetmen, sure, yil, puan=None): # constructor with optional puan parameter
        self.isim = isim  #class methods
        self.yonetmen = yonetmen
        self.sure = sure  # dakika cinsinden
        self.yil = yil
        self.puan = puan  # not 
        

    def __str__(self):
        return f"{self.isim} ({self.yil}) - {self.yonetmen}, {self.sure} dk , {self.puan}"   #print overload?? idk python
    
    def __eq__(self, other): #operator for comparing movie name and year, if same returns true 
            if not isinstance(other, Film):
                return False
            return self.isim == other._isim and self.yil == other.yil
    def __lt__(self, other): #compares durations of two movies 
        return self.sure < other.sure
    

    def ozet_ver(self):
        return f"{self.isim} ({self.yil}), {self.yonetmen} tarafından yönetildi."  #override method

# Alt türler
class Aksiyon(Film): # inherited class 
    def ozet_ver(self):
        return f"[Aksiyon] {self.isim} ({self.yil}) - {self.sure} dk: Heyecan dolu sahneleriyle {self.yonetmen}'in eseri."


class Komedi(Film):
    def ozet_ver(self):
        return f"[Komedi] {self.isim} ({self.yil}) - {self.yonetmen} tarafından yönetilen neşeli bir yapım."


class Dram(Film):
    def ozet_ver(self):
        return f"[Dram] {self.isim} ({self.yil}) - Derin duygular ve çarpıcı anlatımıyla {self.yonetmen} imzası taşır."


class BilimKurgu(Film):
    def ozet_ver(self):
        return f"[Bilim Kurgu] {self.isim} ({self.yil}) - {self.yonetmen}'dan geleceği sorgulatan bir film."


class Korku(Film):
    def ozet_ver(self):
        return f"[Korku] {self.isim} ({self.yil}) - {self.yonetmen}'in tüyler ürperten eseri."


class Belgesel(Film):
    def ozet_ver(self):
        return f"[Belgesel] {self.isim} ({self.yil}) - {self.yonetmen} tarafından hazırlanan bilgilendirici bir yapım."


# Koleksiyon sınıfı: Filmleri ekle, sil, listele, filtrele


# Test senaryosu
