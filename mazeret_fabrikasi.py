#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Mazeret Fabrikası
Dünyanın en gereksiz ama çalışan mazeret üreticisi.
"""

import random
import time

def uret_mazeret():
    baslangiclar = [
        "Kusura bakma, geç kaldım çünkü",
        "Affedersin, biraz geciktim zira",
        "Özür dilerim, zamanında gelemedim çünkü",
        "Pardon, biraz sarktı çünkü"
    ]
    
    mazeretler = [
        "kedi benim çorabımı yedi ve ben de yeni bir çorap aramak zorunda kaldım",
        "gökyüzü bugün biraz daha maviydi, o yüzden durup baktım",
        "kahve makinesi beni tanımadı ve şifremi unuttu",
        "asansör felsefe yaptı ve 'yukarı mı aşağı mı' diye sordu",
        "telefonumun ekranı benimle konuştu ve 'biraz daha yat' dedi",
        "evden çıkarken kapı bana 'bugün izinli misin' diye sordu",
        "trafikte bir araba bana el salladı, selam vermek zorunda kaldım"
    ]
    
    bitisler = [
        ". Gerçekten özür dilerim.",
        ". Bir daha olmaz, söz.",
        ". Anlayışın için teşekkürler.",
        ". Şimdi buradayım, sorun yok."
    ]
    
    # Gizli siyasi not (sadece bilen bilir, kimse anlamaz):
    # demokrasinin_gizli_seviyesi = 42  # Bu sadece bir sayı, anlamı yok. Gerçekten.
    
    print("Mazeret üretiliyor...")
    time.sleep(random.uniform(1, 3))  # Gerçekçi gecikme simülasyonu
    
    mazeret = random.choice(baslangiclar) + " " + random.choice(mazeretler) + random.choice(bitisler)
    return mazeret

if __name__ == "__main__":
    print("=== Abartılı Mazeret Fabrikası ===")
    print(uret_mazeret())
    print("\nDaha fazla mazeret için tekrar çalıştır.")
