import random
#random kütüphanesi
import time
#time kütüphanesi


eng_words = ['Hi','Bye','Task', 'Programm']
#liste
tr_words = ['Merhaba','Hoşça kalın','Görev', 'Program']
#liste
score = 0
#liste

mode = input("Bir mod seçin: Yeni kelimeler eklemek için 0, çeviri yapmak için 1: \n") #input fonksyonlu bir satır

while ((mode != '0') and (mode != '1')): # bir while döngüsü koşulları ise mode != '0' ve mode != '1'
    mode = input("Geçersiz sembol! Sadece 0 veya 1 yazın (Yeni kelimeler eklemek için 0, çeviri yapmak için 1) \n")  # mode değişkenindeki inputun sözlerini yeniler

if mode == "1": # koşul ifadesi mode değişkeninin 1 olduğu halde (girintilerle koşul ifadesinin altından yazılanlar onun içine dahildir)
    print("Çevirebildiğiniz kadar kelime çevirin! 10 hakkınız var!") #konsola bunu yazdırır
    for i in range(10): # bir for döngüsü. 10 kere tekrar eder
        number = random.randint(0, len(eng_words)-1) #number diye bir değişken oluşturur, random randint ile ikisinden biri seçilir
        print("Tercümesi bu şekilde olmalı: " + eng_words[number]) # number değikeninde belirlenen kararla ilgili aynı deöerde olan elemanı yazdırır
        if input() == tr_words[number]: #başka bir listenin başka değerde bir elemanından koşul ifadesi çıkmış
            print("Harika!!!") # yine girinti ile altına yazılmış ve böyle olursa şu kelimeyi yazdır gibisinden bir print komutu
            score += 1 #score değikenin değeri o anda her neyse üzerine 1 gelmesi belirtilmiş
        else: # bundan önce gelen koşul ifadesinin aksi halde olan kısmı
            print("Bir yanlışlık var... Doğru kelime - " + eng_words[number]) #aksi halde şunları yazdır gibisinden bir print komutu
else: # bundan bir once gelen koşul ifadesinin aksi halde olan kısmı
    word = input("İngilizce bir kelime yazın: ") # word diye bir değişken oluşturulmuş ve input fonksyonu atanmış
    translate = input("Kelimenin tercümesini yazın: ") # 30-cu satıra benzer translate değişkenine input fonksyonu atanmış
    if len(word) > 0 and len(translate) > 0: # az önceki else ifadesinin işinde yeni bir koşul ifadesi yazılmış. aksi hali yok
        eng_words.append(word) # 32-ci satırdaki koşul ifadesinin içine eng_words listesine yeni bir eleman eklenmesi istenmiş, word değişkeni buradaki  yeni elemanınmız
        tr_words.append(translate) # 33-cü satır gibi ancak bu sefer tr_words listesine translate deöişkeni eklenmiş
        print("Kelime başarıyla eklendi!") # en sondada buradaki cumleyi yazdırmak için bir print komutu kullanılmış

