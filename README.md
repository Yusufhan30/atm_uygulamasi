# 🏦 ATM Uygulaması

Bu proje, Python ile geliştirilmiş terminal tabanlı çok kullanıcılı bir **ATM simülasyonudur**.  
Kullanıcı doğrulama, bakiye yönetimi, işlem geçmişi ve kalıcı veri saklama özelliklerine sahiptir.

---

## 🚀 Özellikler

- ✅ Kullanıcı adı ve PIN doğrulama
- 💰 Bakiye görüntüleme
- ➕ Para yatırma
- ➖ Para çekme (negatif/limit kontrolü ile)
- 🧾 İşlem geçmişi (zaman damgalı)
- 🟢 Renkli terminal (colorama desteği)
- 💾 Kalıcı veri kaydı (JSON formatında)
- 🔒 3 yanlış girişte güvenli çıkış

---

## 💡 Kullanılan Yapılar

- `if/elif/else` koşulları  
- `while` döngüsü  
- `list`, `dict`, `json` kullanımı  
- `with open()` dosya işlemleri  
- `colorama` ile renkli terminal çıktısı  
- `datetime` ile zaman damgası  
- Çok kullanıcılı JSON veri yapısı

---

## 🗂 Dosyalar

| Dosya Adı            | Açıklama                                  |
|----------------------|-------------------------------------------|
| `atm_uygulamasi.py`  | Uygulamanın ana Python dosyası            |
| `users.json`         | Kullanıcı adı, PIN, bakiye, geçmiş verisi |
| `islem_gecmisi.txt`  | Kullanıcının işlem geçmişi (çıkışta kaydedilir) |

---

## 🔧 Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/Yusufhan30/atm_uygulamasi.git
