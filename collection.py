from collections import defaultdict

from utils import UtilFuncs

class Koleksiyon:
    def __init__(self,api_key):
        self.filmler = []
        self.utils = UtilFuncs(api_key)

    def film_ekle(self, film):
        self.filmler.append(film)

    def film_sil(self, isim):
        self.filmler = [film for film in self.filmler if film.isim.lower() != isim.lower()]

    def listele(self):
        if not self.filmler:
            print("Koleksiyonda hiç film yok.")
        else:
            for film in self.filmler:
                print(film.ozet_ver())

    def film_sayisi(self):
        return len(self._filmler)

    def film_bul(self, isim):
        for film in self.filmler:
            if film.isim.lower() == isim.lower():
                return film.ozet_ver()
        return "Film bulunamadı."

    def yila_gore_filtrele(self, yil):
        return [film.ozet_ver() for film in self.filmler if film.yil == yil]

    def yonetmene_gore_filtrele(self, yonetmen):
        return [film.ozet_ver() for film in self.filmler if film.yonetmen.lower() == yonetmen.lower()]

    def filmleri_ture_gore_getir(self, tur_ismi):
        # tur_ismi is a string like "Korku", "Dram", etc.
        return [film for film in self.filmler if type(film).__name__ == tur_ismi]
    
    def tur_istatistikleri(self):
        sayac = defaultdict(int)
        for film in self.filmler:
            sayac[film.__class__.__name__] += 1
        return dict(sayac)

    def en_uzun_film(self):
        if not self.filmler:
            return "Koleksiyon boş."
        en_uzun = max(self.filmler, key=lambda f: f.sure)
        return f"En uzun film: {en_uzun.isim} ({en_uzun.sure} dk)"

    def filmleri_sirala(self, kriter="yil"):
        if kriter == "yil":
            return sorted(self.filmler, key=lambda f: f.yil)
        elif kriter == "sure":
            return sorted(self.filmler, key=lambda f: f.sure)
        else:
            return self.filmler

    def veri_listesi(self):
        return [(f.isim, f.yonetmen, f.sure, f.yil, f.__class__.__name__) for f in self.filmler]

    def film_puanlarini_yazdir(self, film_adi, yil=None):
        # First check if film is in collection:
        film = self.film_bul(film_adi)
        if not film:
            print(f"Film '{film_adi}' koleksiyonda bulunamadı.")
            return
        
        # Fetch scores from OMDB or your external source:
        scores = self.utils.get_movie_scores(film_adi, yil)
        
        if not scores:
            print(f"'{film_adi}' için puanlar bulunamadı.")
            return
        
        
        print(f"🎬 {film_adi} ({yil if yil else film.yil}) puanları:")
        print(f" - IMDb Puanı: {scores.get('imdb_rating', 'Bilinmiyor')}")
        print(f" - Rotten Tomatoes: {scores.get('rotten_tomatoes', 'Bilinmiyor')}")


