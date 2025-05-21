baslangic_bakiye = 1000
islem_gecmisi = []

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
        print(f"Güncel bakiyeniz: {baslangic_bakiye}₺")

    elif secim == 2:
        miktar = int(input("Yatırılacak tutarı girin: "))
        baslangic_bakiye += miktar
        islem_gecmisi.append(("Yatırma", miktar))
        print(f"{miktar}₺ yatırıldı. Yeni bakiyeniz: {baslangic_bakiye}₺")
        print("İşlem geçmişin:", islem_gecmisi)

    elif secim == 3:
        cekim = int(input("Lütfen çekmek istediğiniz miktarı giriniz: "))
        
        if cekim <= 0:
            print("Negatif ya da sıfır para çekemezsiniz!")
            continue
        
        if cekim <= baslangic_bakiye:
            baslangic_bakiye -= cekim
            islem_gecmisi.append(("Çekim", cekim))
            print(f"{cekim}₺ çekildi. Yeni bakiyeniz: {baslangic_bakiye}₺")
            print("İşlem geçmişin:", islem_gecmisi)
        else:
            print("Hesap bakiyenizden daha fazlasını çekemezsiniz.")

    elif secim == 4:
        print("\n--- İşlem Geçmişi ---")
        if not islem_gecmisi:
            print("Henüz işlem yapılmamış.")
        else:
            for index, (islem_tipi, miktar) in enumerate(islem_gecmisi, start=1):
                print(f"{index}. {islem_tipi} - {miktar}₺")

    elif secim == 5:
        print("Çıkışa yönlendiriliyorsunuz...")
        break
