
print("T.C İNKILAP TARİHİ VE ATATÜRKÇÜLÜK BİLGİ YARIŞMASINA \n ********HOŞGELDİNİZ********")


toplam_puan = 0
soru1 = input("1.SORU Mustafa Kemal Atatürk'ün ilk askeri başarısı nedir?: \n")
soru1 = soru1.upper()
cevap1 = u"TRABLUSGARP SAVAŞI"

if (soru1 == cevap1 ):
     toplam_puan = toplam_puan + 10
     print("Doğru Cevap...\n")

else:
     toplam_puan = toplam_puan
     print("Yanlış Cevap...\n")

soru2 = input("2.SORU Mustafa Kemal'e TBMM tarafından Mareşallik rütbesi ve Gazilik ünvanı hangi savaştan sonra verilmiştir?: \n")
soru2 = soru2.upper()
cevap2 = u"SAKARYA MEYDAN MUHAREBESİ"

if (soru2 == cevap2):
     toplam_puan = toplam_puan + 10
     print("Doğru Cevap...\n")

else:
     toplam_puan = toplam_puan
     print("Yanlış Cevap...\n")

soru3 = input("3.SORU Yeni Türk Devletinin sınırlarını belirleyen ve 28 Ocak 1920 de kabul edilen belgenin adı nedir? : \n")
soru3 = soru3.upper()
cevap3 = u"MİSSAKI MİLLİ"

if (soru3 == cevap3 ):
     toplam_puan = toplam_puan + 10
     print("Doğru Cevap...\n")

else:
     toplam_puan = toplam_puan
     print("Yanlış Cevap...\n")

soru4 = input("4.SORU Kurtuluş savaşı sonunda hangi ateşkes antlaşması yapılmıştır?: \n")
soru4 = soru4.upper()
cevap4 = u"MUDANYA" 

if (soru4 == cevap4 ):
     toplam_puan = toplam_puan + 10
     print("Doğru Cevap...\n")

else:
     toplam_puan = toplam_puan
     print("Yanlış Cevap...\n")

soru5 = input("5.SORU Türk Medeni Kanunu hangi ülkeden alınmıştır?: \n")
soru5 = soru5.upper()
cevap5 = u"İSVİÇRE"

if (soru5 == cevap5 ):
     toplam_puan = toplam_puan + 10
     print("Doğru Cevap...\n")

else:
     toplam_puan = toplam_puan
     print("Yanlış Cevap...\n")

soru6 = input("6.SORU 3 Mart 1924’te Erkan-ı Harbiye Vekâleti kaldırılarak yerine hangi kurum kurulmuştur?: \n")
soru6 = soru6.upper
cevap6 = u"GENELKURMAY BAŞKANLIĞI"
if (soru6 == cevap6 ):
     toplam_puan = toplam_puan + 10
     print("Doğru Cevap...\n")
else:
     toplam_puan = toplam_puan
     print("Yanlış Cevap...\n")

soru7 = input("7.SORU Mustafa Kemal’in eğitimi çağdaşlaştırmak, laikleştirmek ve okul çeşitliliğini ortadan kaldırmak için çıkardığı kanundur?: \n")
soru7 = soru7.upper()
cevap7 = "TEVHİDİ TEDRİSAT KANUNU"

if (soru7 == cevap7 ):
     toplam_puan = toplam_puan + 10
     print("Doğru Cevap...\n")
else:
     toplam_puan = toplam_puan
     print("Yanlış Cevap...\n")

soru8 = input("8.SORU Hangi gelişme ile meclis hükümeti sisteminden kabine sistemine geçilmiştir?: \n")
soru8 = soru8.upper()
cevap8 = u"CUMHURİYETİN İLANI"

if (soru8 == cevap8 ):
     toplam_puan = toplam_puan + 10
     print("Doğru Cevap...\n")
else:
     toplam_puan = toplam_puan
     print("Yanlış Cevap...\n")

soru9 = input("9.SORU Türk denizlerinde yük ve yolcu taşıma hakkının yabancılardan alınarak Türk vatandaşlarına verilmesi için çıkarılan kanunun adı nedir?: \n")
soru9 = soru9.upper()
cevap9 = u"KABOTAJ KANUNU"

if (soru9 == cevap9 ):
     toplam_puan = toplam_puan + 10
     print("Doğru Cevap...\n")
else:
     toplam_puan = toplam_puan
     print("Yanlış Cevap...\n")

soru10 = input("10.SORU Mustafa Kemal Atatürk ilk görev yeri olan Suriye’de bulunduğu sırada yakın arkadaşları ile birlikte kurduğu cemiyetin adı nedir?: \n")
soru10 = soru10.upper()
cevap10 = u"VATAN VE HÜRRİYET CEMİYETİ"

if (soru10 == cevap10 ):
     toplam_puan = toplam_puan + 10
     print("Doğru Cevap...\n")
else:
     toplam_puan = toplam_puan
     print("Yanlış Cevap...\n")


print("\n##### SONUÇ #####")
print(toplam_puan)

if (toplam_puan > 50):
    print("Bilgi yarışmasında başarılı oldunuz.")
else:
    print("Bilgi yarışmasında başarısız oldunuz.")