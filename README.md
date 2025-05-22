TDG structural health monitoring assignment README file


!----IMPORTANT-----!

BEFORE RUNNING, CREATE YOUR OWN API KEY ON 
https://www.omdbapi.com/

You can use 10 minute mail. 

https://10minutemail.com

When creating a new Utils object, use this api key. 
This api key is used to get movie information from the Omdb database. 


---------------------------------------------------------------------------

🔧 UtilFuncs

OMDb API üzerinden film bilgisi çeker.

    get_movie_info_by_name(title, year=None): Film ismine göre arama yapar, yıl verilmişse eşleşen yılı döner.

    get_movie_info_by_id(imdb_id): IMDb ID’sine göre film detaylarını döner.

    get_movie_scores(title, year=None): IMDb ve Rotten Tomatoes puanlarını döner.

    get_movie_genre(title, year=None): Filmin türünü döner.

🎬 Film (Ana sınıf)

Bir filmin temel bilgilerini ve davranışlarını içerir.

    Özellikler: isim, yonetmen, sure, yil, puan

    __str__(): Filmi string olarak temsil eder.

    __eq__(other): Aynı isim ve yıla sahip filmleri eşit kabul eder.

    __lt__(other): Süre karşılaştırması yapar (sıralama için).

    ozet_ver(): Film bilgilerini kısa biçimde verir.

📚 Alt Tür Sınıflar (Hepsi Film sınıfından miras alır)

    Aksiyon, Komedi, Dram, BilimKurgu, Korku, Belgesel
    Her biri ozet_ver() metodunu kendi türüne göre özelleştirir.
   
🎞️ Koleksiyon

Filmlerden oluşan bir koleksiyonu yönetir.

    film_ekle(film): Koleksiyona film ekler.

    film_sil(isim): İsme göre filmi koleksiyondan siler.

    listele(): Koleksiyondaki tüm filmleri listeler.

    film_bul(isim): İsme göre filmi bulur ve özetini verir.

    yila_gore_filtrele(yil): Belirtilen yıla göre filtreler.

    yonetmene_gore_filtrele(yonetmen): Yönetime göre filtreler.

    filmleri_ture_gore_getir(tur_ismi): Film türüne göre filtreler (örnek: "Korku").

    tur_istatistikleri(): Hangi türden kaç film olduğunu sayar.

    en_uzun_film(): Koleksiyondaki en uzun filmi döner.

    filmleri_sirala(kriter): Filmleri yil veya sureye göre sıralar.

    veri_listesi(): Film bilgilerini tuple şeklinde döner.

    film_puanlarini_yazdir(film_adi, yil=None): API'den film puanlarını yazdırır.
