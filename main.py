meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "SUS": "Şüpheli biri ve ya bir şey",
            "SUP": "Nasılsın?",
            "CAP": "Doğru değil, yalan",
            "SIGMA": "Cool"
    



    
}
word = input("Anlamadığnız bir kelime yazınız(Hepsini büyük ile giriniz) :")

if word in meme_dict.keys():
    print(meme_dict[word])

else:
    print("Bu Kelime Sözlükte Yok!")
