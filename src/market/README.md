**Strukturasi:**

1. **1-tab:** So‘nggi kiyimlar

    * Rasm, nomi (title), narx.
2. **2-tab:** Qidiruv sahifasi

    * Input + qidirish tugmasi.
3. **3-tab:** Kategoriyalar

    * Har bir kategoriya: rasm + nom.
    * Ichiga kirganda turlar ro‘yxati (kichik bo‘limlar).
    * Ularning ichida esa kiyimlar ro‘yxati (1-tab uslubida).
4. **4-tab:** Korzinka

    * Tanlangan kiyimlar ro‘yxati.

**Kiyim detali sahifasi:**

* Rasm, nom, tavsif, narx.
* Rangi tanlash (rang bo‘yicha mavjud o‘lchamlar avtomatik chiqadi).
* O‘lcham tanlanganda **"Qo‘shish"** tugmasi chiqadi.
* Tugmani bosganda tanlangan buyum korzinkaga tushadi.

**Texnologiyalar:**

* **Frontend:** HTML + CSS (Telegram WebApp theme API bilan uyg‘un) + JavaScript.
* **Telegram WebApp API:** `window.Telegram.WebApp` dan ranglar va native UI integratsiyasi uchun foydalaniladi.
* **Responsive dizayn:** Telefon va desktopda ishlaydi.
* **Data manbasi:** JSON yoki API orqali kiyimlar, kategoriyalar va narxlar olinadi.
