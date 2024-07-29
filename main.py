import random
# Random Modulu içeri aktarılır

def sayi_tahmin_oyunu():
    # Sayı tahmini adlı bir fonksiyon tanımlanır
    tahmin_edilecek_sayi = random.randint(1, 100)
    # "random.randint" fonksiyonu, 1 ile 100 arası bir sayı seçer ve bunu "tahmin_edilecek_sayi" değişkenine verir
    deneme_sayisi = 0
    # Sıfır olarak başlayan değişken deneye deneye artar.
    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 100 arasında bir sayı seçtim. Bu sayıyı tahmin etmeye çalışın!")
    # Kullanıcıya hoşgeldin mesajı ve küçük bir eğitim verir.

    while True:
    # Sonsuz bir döngü oluşturur. Kullanıcı doğru tahmin edene kadar devam eder.
        kullanici_tahmini = input("Tahmininizi girin: ")
        # Kullanıcı tahminini "kullanici_tahmini" değişkinine atar
        
        
        if not kullanici_tahmini.isdigit():
            print("Lütfen geçerli bir sayı girin.")
            continue
        # Girilen sayının "random.randint" fonksiyonunda olup olmadığını kontrol ediyoruz

        kullanici_tahmini = int(kullanici_tahmini)
        # "kullanici_tahmini" değişkenini tam sayıya çeviriyoruz çünkü input fonksiyonu kullanıcının sayısını string olarak döndürür.
        deneme_sayisi += 1
        # Her bir denemede "deneme_sayisi" fonksiyonunu bir arttırıyoruz.
        if kullanici_tahmini < tahmin_edilecek_sayi:
            print("Daha yüksek bir sayı tahmin edin!")
        # "kullanici_tahmini" fonksiyonu "tahmin_edilecek_sayi" fonksiyonunda küçükse daha yüksek bir şey tahmin etmesini söylüyoruz
        elif kullanici_tahmini > tahmin_edilecek_sayi:
            print("Daha düşük bir sayı tahmin edin!")
        # "kullanici_tahmini" fonksiyonu "tahmin_edilecek_sayi" fonksiyonunda büyükse daha düşük bir şey tahmin etmesini söylüyoruz
        else:
            print(f"Tebrikler! {deneme_sayisi} denemede sayıyı doğru tahmin ettiniz.")
            break
        # Kullanıcının tahmini doğruysa onu tebrik edip deneme sayısı gösterip uygulamayı kapatıyoruz

if __name__ == "__main__":
    sayi_tahmin_oyunu()
