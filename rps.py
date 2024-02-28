import random

def play():
    user = input("Taş seçmek için 't', kağıt seçmek için 'k', makas seçmek için 'm' = ")
    computer = random.choice(['t', 'k', 'm'])

    if user == computer:
        return f'Berabere kaldınız!'

    if is_win(user, computer):
        return f'Kazandınız!'
    
    return f'Kaybettniz!'

def is_win(player, opponent):
    # kullanıcı kazanırsa doğruya döndür
        # t > m, m > k, k > t
        if (player == 't' and opponent == 'm') or (player == 'm' and opponent == 'k') \
        or (player == 'k' and opponent == 't'):
         return True
    
print (play())

import time

# Beklenen süre (saniye cinsinden)
beklenen_sure = 3

# Başlangıç zamanını kaydet
baslangic_zamani = time.time()

# Kullanıcıdan giriş iste
giris = input("Programı kapatmak için herhangi bir tuşa basın...")

# Geçen süreyi hesapla
gecen_sure = time.time() - baslangic_zamani

# Belirlenen süreden fazla mı kontrol et
if gecen_sure >= beklenen_sure:
    print("Belirlenen süreden fazla zaman geçti. Program kapanıyor...")
else:
    print("Program kapatıldı.")