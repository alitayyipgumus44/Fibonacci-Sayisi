""" Konsoldan girdi olarak terim sayısı girilen maksimum ve minimum fibonacci sayıları arasındaki 15'e bölünebilen sayıları konsola yazdırınız. """

print("*** BASAMAK SAYISI GİRİLDİĞİ ZAMAN O BASAMAĞA SAHİP FİBONACCİ SAYILARI ARASINDAKİ 15'E TAM BÖLÜNEN SAYILARI LİSTELEYEN PROGRAM ***")
print("\n")

fibonacciSayilari = [] #Fibonacci sayılarını alması için dizi tanımlanması

a = 1
b = 1
c = 0

while c<100000: #En fazla 5 basamak olacak şekilde while döngüsünün devam etmesi
    c = a+b
    a = b
    b = c
    fibonacciSayilari.append(b) #En fazla 5 basamağa kadar olan sayıların diziye aktarılması

fibonacciSayilari.pop() #Dizideki istemediğimiz son eleman olan 6 basamaklı sayının diziden çıkarılması

print("+ Fibonacci Sayıları Dizisi: ",end="")
print(fibonacciSayilari)
print("\n")

basamaksayisi= 0

while True: #Kullanıcının geçersiz basamağı (programı sonlandırmak istediği zaman) girene kadar programın devam etmesi için sonsuz döngü oluşturulması

    basamaksayisi = int(input("Basamak Sayısını Giriniz (0 Girmeniz Programı Sonlandıracaktır!): "))
    print("\n")

    if (int(basamaksayisi) == 0): #Geçersiz basamağın programı sonlandırma komutu olarak atanması

        exit()

    elif (int(basamaksayisi) == 1):

        print("- Bir basamaklı bir sayı 15'e tam bölünemez. Bu yüzden 1'den büyük bir basamak giriniz!")
        print("\n")

    elif (int(basamaksayisi) == 2):

        print("- 2 Basamaklı Fibonacci Sayıları: ", end="")
        print(fibonacciSayilari[4:9])

        minfbs = fibonacciSayilari[4]
        maksfibs = fibonacciSayilari[8]

        print("- Girdiğiniz Basamak Sayısındaki Minimum Fibonacci Sayısı: ", end="")
        print(minfbs)

        print("- Girdiğiniz Basamak Sayısındaki Maksimum Fibonacci Sayısı: ", end="")
        print(maksfibs)

        basamak2 = []

        while minfbs <= maksfibs:

            if (minfbs % 15 == 0):
                basamak2.append(minfbs)
            minfbs += 1

        print("- Bu İki Sayı Arasındaki 15'e Bölünebilen Sayılar :", end=" ")
        print(basamak2)
        print("\n")

    elif (int(basamaksayisi) == 3):

        print("- 3 Basamaklı Fibonacci Sayıları: ", end="")
        print(fibonacciSayilari[9:14])

        minfbs = fibonacciSayilari[9]
        maksfibs = fibonacciSayilari[13]

        print("- Girdiğiniz Basamak Sayısındaki Minimum Fibonacci Sayısı: ", end="")
        print(minfbs)

        print("- Girdiğiniz Basamak Sayısındaki Maksimum Fibonacci Sayısı: ", end="")
        print(maksfibs)

        basamak3 = []

        while minfbs <= maksfibs:

            if (minfbs % 15 == 0):
                basamak3.append(minfbs)
            minfbs += 1

        print("- Bu İki Sayı Arasındaki 15'e Bölünebilen Sayılar :", end=" ")
        print(basamak3)
        print("\n")


    elif (int(basamaksayisi) == 4):

        print("- 4 Basamaklı Fibonacci Sayıları: ", end="")
        print(fibonacciSayilari[14:18])

        minfbs = fibonacciSayilari[14]
        maksfibs = fibonacciSayilari[17]

        print("- Girdiğiniz Basamak Sayısındaki Minimum Fibonacci Sayısı: ", end="")
        print(minfbs)

        print("- Girdiğiniz Basamak Sayısındaki Maksimum Fibonacci Sayısı: ", end="")
        print(maksfibs)

        basamak4 = []

        while minfbs <= maksfibs:

            if (minfbs % 15 == 0):
                basamak4.append(minfbs)
            minfbs += 1

        print("- Bu İki Sayı Arasındaki 15'e Bölünebilen Sayılar :", end=" ")
        print(basamak4)
        print("\n")

    elif (int(basamaksayisi) == 5):

        print("- 5 Basamaklı Fibonacci Sayıları: ", end="")
        print(fibonacciSayilari[18:23])

        minfbs = fibonacciSayilari[18]
        maksfibs = fibonacciSayilari[22]

        print("- Girdiğiniz Basamak Sayısındaki Minimum Fibonacci Sayısı: ", end="")
        print(minfbs)

        print("- Girdiğiniz Basamak Sayısındaki Maksimum Fibonacci Sayısı: ", end="")
        print(maksfibs)

        basamak5 = []

        while minfbs <= maksfibs:

            if (minfbs % 15 == 0):
                basamak5.append(minfbs)
            minfbs += 1

        print("- Bu İki Sayı Arasındaki 15'e Bölünebilen Sayılar :", end=" ")
        print(basamak5)
        print("\n")

    else:

        print("- Girdiğiniz basamak sayısı en fazla 5 olabilir!")
        print("\n")

