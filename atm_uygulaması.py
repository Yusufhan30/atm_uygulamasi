import sys
import json
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)



with open("users.json", "r") as dosya:
    users = json.load(dosya)


kullanici_adi = input("Kullanıcı adınızı girin: ")


if kullanici_adi not in users:
    print(Fore.YELLOW + "Bu kullanıcı sistemde bulunamadı.")

    sys.exit()
    
    
correct_pin = users[kullanici_adi]["pin"]
hak = 3

while hak > 0:
    kullanici_sifresi = (input("Lütfen şifrenizi giriniz: "))

    if kullanici_sifresi == correct_pin:
        print(Fore.GREEN + "Şifre doğru, sisteme yönlendiriliyorsunuz...")
        break

    else:
        hak -= 1
        print(Fore.RED + f"Şifre yanlış! Lütfen tekrar deneyiniz. Kalan hakkınız: {hak}")
else:
    print("3 defa hatalı giriş yaptınız. Sistemden çıkılıyor.")
    sys.exit()



bakiye = users[kullanici_adi]["bakiye"]
gecmis = users[kullanici_adi]["gecmis"]


while True:
    print("\n--- BANKA MENÜSÜ ---")
    print("1 - Bakiye Görüntüle")
    print("2 - Para Yatır")
    print("3 - Para Çek")
    print("4 - İşlem Geçmişi")
    print("5 - Çıkış")

    secim = int(input("Seçiminiz: "))

    if secim == 1:
        print("Bakiye görüntüleme:")
        print(f"Güncel bakiyeniz: {bakiye}₺")

    elif secim == 2:
        miktar = int(input("Yatırılacak tutarı girin: "))
        bakiye += miktar
        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        gecmis.append(("Yatırma", miktar,zaman))
        print(Fore.GREEN + f"{miktar}₺ yatırıldı. Yeni bakiyeniz: {bakiye}₺")
        print("İşlem geçmişin:", gecmis)

    elif secim == 3:
        cekim = int(input("Lütfen çekmek istediğiniz miktarı giriniz: "))
        
        if cekim <= 0:
            print("Negatif ya da sıfır para çekemezsiniz!")
            continue
        
        if cekim <= bakiye:
            bakiye -= cekim
            zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            gecmis.append(("Çekim", cekim,zaman))
            print(f"{cekim}₺ çekildi. Yeni bakiyeniz: {bakiye}₺")
            print("İşlem geçmişin:", gecmis)
        else:
            print("Hesap bakiyenizden daha fazlasını çekemezsiniz.")

    elif secim == 4:
        print("\n--- İşlem Geçmişi ---")
        if not gecmis:
            print("Henüz işlem yapılmamış.")
        else:
            for index, (islem_tipi, miktar) in enumerate(gecmis, start=1):
                print(f"{index}. {islem_tipi} - {miktar}₺")

    elif secim == 5:
        print("Çıkışa yönlendiriliyorsunuz...")

    with open("islem_gecmisi.txt", "w", encoding="utf-8") as dosya:
        dosya.write("--- İŞLEM GEÇMİŞİ ---\n")
        for index, (islem_tipi, miktar, zaman) in enumerate(gecmis, start=1):
            dosya.write(f"{index}. [{zaman}] {islem_tipi} - {miktar} TL\n")
        dosya.write("\n--- Oturum sonlandırıldı. Teşekkürler. ---\n")

    users[kullanici_adi]["bakiye"] = bakiye
    users[kullanici_adi]["gecmis"] = gecmis

    with open("users.json", "w") as dosya:
        json.dump(users, dosya, indent=4)

        
    break
