from collection import Koleksiyon  #import collection wont work - bc we use it with file name collection.Koleksiyon()
from movie import * 


def main():
    koleksiyon = Koleksiyon("29fdb2ca") # create

    # Filmler oluşturuluyor
    film1 = Aksiyon("Mad Max: Fury Road", "George Miller", 120, 2015)
    film2 = Komedi("The Grand Budapest Hotel", "Wes Anderson", 99, 2014)
    film3 = Dram("The Pursuit of Happyness", "Gabriele Muccino", 117, 2006)
    film4 = BilimKurgu("Interstellar", "Christopher Nolan", 169, 2014)
    film5 = Korku("The Conjuring", "James Wan", 112, 2013)
    film6 = Belgesel("Our Planet", "David Attenborough", 50, 2019)

    # Koleksiyona ekleniyor
    koleksiyon.film_ekle(film1)
    koleksiyon.film_ekle(film2)
    koleksiyon.film_ekle(film3)
    koleksiyon.film_ekle(film4)
    koleksiyon.film_ekle(film5)
    koleksiyon.film_ekle(film6)

    print("🎬 Film Koleksiyonu:")
    koleksiyon.listele()

    print("\n🔍 Belirli film bulma: Interstellar")
    print(koleksiyon.film_bul("Interstellar"))

    print("\n📆 2014 yılına ait filmler:")
    print("\n".join(koleksiyon.yila_gore_filtrele(2014)))

    print("\n🎬 Yönetmene göre filtreleme: Wes Anderson")
    print("\n".join(koleksiyon.yonetmene_gore_filtrele("Wes Anderson")))

    print("\n📊 Tür istatistikleri:")
    for tur, sayi in koleksiyon.tur_istatistikleri().items():
        print(f"{tur}: {sayi} film")

    print("\n⏱️ En uzun film:")
    print(koleksiyon.en_uzun_film())

    print("\n🔢 Süreye göre sıralanmış filmler:")
    for film in koleksiyon.filmleri_sirala("sure"):
        print(f"- {film.isim}: {film.sure} dk")

    print("\n❌ The Conjuring siliniyor...\n")
    koleksiyon.film_sil("The Conjuring")

    print("🎬 Güncellenmiş Film Koleksiyonu:")
    koleksiyon.listele()

    koleksiyon.film_puanlarini_yazdir("The Grand Budapest Hotel",2014)
    belgesel=koleksiyon.filmleri_ture_gore_getir("Belgesel")
    for film in belgesel:
        print(film.ozet_ver())
    
if __name__ == "__main__":
    main() 
