from time import sleep
import os

# oyun tahtasını liste halinde hazırladık
tahta = [["___","___","___"],
         ["___","___","___"],
         ["___","___","___"]
        ]


print("\n"*15)

# tahtayı ekrana bastırdık
    # \t ile tab boşluğu verdik expandables() ile bu değeri genişlettik *i diyerek parçaladık ve ekrana daha temiz bir çıktı verdik   
for i in tahta:
    print("\t".expandtabs(30), *i, end="\n"*2)


# kazanma ölçütlerini yani kazanma durumlarını listeledik
kazanma_ölçütleri = [
[[0, 0], [1, 0], [2, 0]],
[[0, 1], [1, 1], [2, 1]],
[[0, 2], [1, 2], [2, 2]],
[[0, 0], [0, 1], [0, 2]],
[[1, 0], [1, 1], [1, 2]],
[[2, 0], [2, 1], [2, 2]],
[[0, 0], [1, 1], [2, 2]],
[[0, 2], [1, 1], [2, 0]]
]


x_durumu = []
o_durumu = []

# terminali temiszlemek için
def clear():
    input("enter a basın")
    sleep(0.5)
    os.system('cls')


sıra = 2
while True:
    
# eğer sıra çiftse x te tek se o dadır.
    if sıra % 2 == 0:
        işaret = "X".center(3)
    else:
        işaret = "O".center(3)

    print()
    print("İŞARET: {}\n".format(işaret))
    sleep(0.3)


# x y kordinatlarını aldık
    x = input("yukarıdan aşağıya [1, 2, 3]: ".ljust(30))
    if x == "q":
        print("x pes etti...")
        sleep(1)
        break
    y = input("soldan sağa [1, 2, 3]: ".ljust(30))
    if y == "q":
        print("o pes etti...")
        sleep(1)
        break
    

# index numaralarını tutturmak için 1 çıkmamız gerekti
    x = int(x)-1
    y = int(y)-1

    print("\n"*15)

# eğer x y kordinatları boşsa işareti yazdırdık ve o kordinatları işaretin durum listesine ekledik
    if tahta[x][y] == "___":
        tahta[x][y] = işaret
        if işaret == "X".center(3):
            x_durumu += [[x, y]]
        elif işaret == "O".center(3):
            o_durumu += [[x, y]]
        sıra += 1
    else:
        print("\nORASI DOLU! TEKRAR DENEYİN\n")
    
            
# tahtanın güncel halini ekrana yazdırdık
    for i in tahta:
        print("\t".expandtabs(30), *i, end="\n"*2)
   
   


# x veya o için durum değerlerinin içinde kazanma ölçütleri oluşmuşsa o oyuncu kazandı demektir ve oyun biter.
   
    for i in kazanma_ölçütleri:
        o = [z for z in i if z in o_durumu]
        x = [z for z in i if z in x_durumu]
        if len(o) == len(i):
            clear()
            print("""      
            
                               O KAZANDI :)
                 """)
            sleep(1.7)
            quit()
        if len(x) == len(i):
            clear()
            print("X KAZANDI :)")
            sleep(1.7)
            quit()
