#Homework1-b

tekrar = "Tekrar deneme hakkı"
while tekrar == "Tekrar deneme hakkı":
    n = int(input("Lütfen tek basamaklı bir tamsayı giriniz:  "))
    if 0 <= n <= 9:
      nums=list(range(0,n,1))
      for x in nums:
        if x % 2 == 0:
           print("Çift sayılar", x)
           tekrar = "işlem bitti"
    else:
       print("Girilen sayı tek basamaklı tam sayı değil.Lütfen tek basamaklı tam sayı giriniz...")



