# 💫 Telegram Stars Payment Bot

A full-stack Telegram bot project that allows users to make payments using **Telegram Stars** through a **Mini App WebApp** interface.

---

## 🚀 Features

- ✅ Aiogram 3 Telegram bot
- ✅ FastAPI backend for WebApp integration
- ✅ Clean HTML+JS WebApp frontend
- ✅ Dockerized (backend + Nginx)
- ✅ WebApp uses Telegram `MainButton` for Stars-based virtual purchase
- ✅ Ready for production deployment

---

## 📦 Technologies

- Python 3.11
- Aiogram 3
- FastAPI
- HTML / JavaScript (WebApp)
- Docker + Docker Compose
- Nginx (to serve WebApp and reverse proxy API)

---


## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/JahongirHakimjonov/tgstars.git
cd tgstars
````

### 2. Configure your bot

Edit `app/bot.py` and set your bot token:

```python
bot = Bot(token="YOUR_BOT_TOKEN")
```

Edit `webapp/index.html` and set your deployed domain:

```js
fetch("https://yourdomain.com/api/pay", ...)
```

---

### 3. Build & Run via Docker

```bash
docker compose up --build -d
```

* Backend (FastAPI) runs at: `http://localhost:8000`
* WebApp served by Nginx at: `http://localhost/`
* WebApp POST `/api/pay` is reverse-proxied to backend

---

## 🧪 Local Testing

To test locally via Telegram:

* Use [ngrok](https://ngrok.com/) to expose the server:

  ```bash
  ngrok http 80
  ```
* Update `webapp/index.html` with your `ngrok` public URL
* Send your bot the "Open WebApp" button and try the payment flow

---

## ✅ TODO / Optional Improvements

* 🔐 Validate `initData` from Telegram WebApp
* 🧾 Save purchases to a database (e.g., SQLite/Postgres)
* 🛡️ Use HTTPS via Nginx + Let's Encrypt for production
* ⚙️ Add Stars balance deduction via Telegram's official Stars API (if available)

---

## 📸 Screenshots

| WebApp UI           | Telegram View                         |
|---------------------| ------------------------------------- |
| ![WebApp](src/web/img.png) | ![Telegram](src/web/img.png) |

---

## 📄 License

MIT License © 2025

---

## 🤝 Contributions

Pull requests and feedback welcome. For major changes, please open an issue first.