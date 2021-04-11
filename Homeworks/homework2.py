print("*******İyi Günler. Hoşgeldiniz.*******")


ıd = "azizsanliturk16"
pw ="Abcdef_123?*"



ıd1= input("Lütfen kullanıcı adını giriniz: ")
pw1= input("Lütfen şifrenizi giriniz: ")

if (ıd != ıd1 and pw == pw1):
    print("Kullanıcı adınız hatalı")
elif (ıd == ıd1 and pw != pw1):
    print("Şifreniz hatalı")
elif (ıd != ıd1 and pw!= pw1):
    print("Kullanıcı adınız ve şifreniz hatalıdır.")
else:
    print("Tebrikler, Başarıyla giriş yaptınız")