def arac_tipi(arac_tip):
    if arac_tip == "economic":
        return 900
    elif arac_tip == "sedan":
        return 1200
    elif arac_tip == "suv":
        return 1600
    else:
        return "Please enter a valid vehicle type :"


def sigorta_istiyor_mu(gun_sayisi, sigorta):
    if sigorta == "y":
        return gun_sayisi * 150
    elif sigorta == "n":
        return 0
    else:
        return "Please enter a valid value : "


def indirim_uygula(toplam, gun_sayisi):
    if gun_sayisi >= 5:
        return toplam - (toplam * 0.08)
    elif gun_sayisi <= 0:
        return "Enter a valid date :"
    else:
        return toplam


def toplam_ucret_hesapla(secim, gun_sayisi, sigorta):
    gunluk_fiyat = arac_tipi(secim)
    sigorta_hesap = sigorta_istiyor_mu(gun_sayisi, sigorta)
    ara_toplam = (gunluk_fiyat * gun_sayisi) + sigorta_hesap
    sonuc = indirim_uygula(ara_toplam, gun_sayisi)
    return sonuc


secim = input("Enter vehicle type (economic,sedan,suv) :")
gun_sayisi = int(input("How many days would you like to rent :"))
sigorta = input("Do you want insurance? (y/n) :")

print(toplam_ucret_hesapla(secim, gun_sayisi, sigorta))
