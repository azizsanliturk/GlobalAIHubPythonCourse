#Homework3

#Öğrenci1
vize1 = float(input("Ögrenci 1 Vize: "))
final1 = float(input("Ögrenci 1 Final: "))
proje1 = float(input("Ögrenci 1 Proje: "))
if 0 <= vize1 <= 100 and 0 <= proje1 <= 100 and 0 <= final1 <= 100: 
    gecme_notu1 = vize1* (0.3) + proje1 * (0.3) + final1 * (0.4)
    ögrenci1 = gecme_notu1
else:
   print("Birinci öğrencide not girişi hatalı..")
   exit()

# Öğrenci 2

vize2 = float(input("Ögrenci 2 Vize: "))
final2 = float(input("Ögrenci 2 Final: "))
proje2 = float(input("Ögrenci 2 Proje: "))
if 0 <= vize2 <= 100 and 0 <= proje2 <= 100 and 0 <= final2 <= 100:
    gecme_notu2 = vize2 * (0.3) + proje2* (0.3) + final2 * (0.4)
    ögrenci2 = gecme_notu2
else:
    print("İkinci öğrencide not girişi hatalı..")
    exit()    
# Öğrenci 3
vize3 = float(input("Ögrenci 3 Vize: "))
final3 = float(input("Ögrenci 3 Final: "))
proje3 = float(input("Öğrenci 3 Proje: "))
if 0 <= vize3 <= 100 and 0 <= proje3 <= 100 and 0 <= final3 <= 100:
   gecme_notu3 = vize3 * (0.3) + proje3* (0.3) + final3 * (0.4)
   ögrenci3 = gecme_notu3
else:
    print("Üçüncü öğrencide not girişi hatalı..")
    exit()   
# Öğrenci 4

vize4 = float(input("Ögrenci 4 Vize: "))
final4 = float(input("Ögrenci 4 Final: "))
proje4 = float(input("Ögrenci 4 Proje: "))
if 0 <= vize4 <= 100 and 0 <= proje4 <= 100 and 0 <= final4 <= 100: 
    gecme_notu4 = vize4 * (0.3) + proje4 * (0.3) + final4 * (0.4)
    ögrenci4 = gecme_notu4
else:
    print("Dördüncü öğrencide not girişi hatalı..")
    exit()    
# Öğrenci 5

vize5 = float(input("Ögrenci 5 Vize: "))
final5 = float(input("Ögrenci 5 Final: "))
proje5 = float(input("Ögrenci 5 Proje: "))
if 0 <= vize5 <= 100 and 0 <= proje5 <= 100 and 0 <= final5 <= 100: 
    gecme_notu5 = vize5 * (0.3) + proje5 * (0.3) + final5 * (0.4)
    ögrenci5 = gecme_notu5
else:
    print("Beşinci öğrencide not girişi hatalı..")
    exit()
sınıf ={ögrenci1:gecme_notu1, ögrenci2:gecme_notu2, ögrenci3:gecme_notu3, ögrenci4:gecme_notu4, ögrenci5:gecme_notu5}

sınıf_list = list(sınıf.values())
list.reverse(sınıf_list)
print(sınıf_list)