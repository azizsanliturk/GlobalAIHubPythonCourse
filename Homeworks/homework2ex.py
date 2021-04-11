print("*******İyi Günler. Hoşgeldiniz.*******")

ıdpw = {'azizsanliturk':'abcdef'}


ıd=input("Lüften kullanıcı adını yazınız: ")
pw=input("Lütfen şifrenizi yazınız: ")
   
if ıd in ıdpw.keys() and pw in ıdpw.values():
    print("Giriş yapıldı...")
else:
    print ("Kullanıcı adı veya şifre yanlış...")