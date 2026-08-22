# Telegram Task Management Bot

Django + Aiogram 3.x asosida yaratilgan Telegram vazifalar boshqarish boti.
Bitrix24 bilan integratsiyalangan — vazifalar to'g'ridan-to'g'ri Bitrix24 ga yuboriladi.

## Loyiha tuzilmasi

```
├── config/          # Django settings, urls
├── users/           # TelegramUser modeli
├── tasks/           # Task modeli va BitrixService
├── bot/             # Telegram bot (Aiogram 3.x)
│   ├── handlers/    # Bot handlerlari
│   ├── keyboards/   # Keyboardlar
│   └── states/      # FSM statelar
├── manage.py
├── requirements.txt
├── .env
└── .env.example
```

## Talablar

- Python 3.10+
- PostgreSQL yoki SQLite (ishlab chiqish uchun)
- Redis (ixtiyoriy — doimiy FSM state uchun)
- Bitrix24 webhook URL

## O'rnatish

1. Virtual muhitni yarating:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Kutubxonalarni o'rnating:
```bash
pip install -r requirements.txt
```

3. .env faylini yarating:
```bash
cp .env.example .env
```

4. .env faylini to'ldiring:
```
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
DJANGO_SECRET_KEY=your-secret-key
BITRIX_WEBHOOK_URL=https://your-portal.bitrix24.uz/rest/1/your-token/
```

5. Migratsiyalarni bajaring:
```bash
python manage.py migrate
```

6. Admin foydalanuvchi yarating (ixtiyoriy):
```bash
python manage.py createsuperuser
```

## Ishga tushirish

1. Django serverni ishga tushiring:
```bash
python manage.py runserver
```

2. Telegram botni alohida terminalda ishga tushiring:
```bash
python -m bot
```

## Xususiyatlar

- `/start` — Ro'yxatdan o'tish (Bitrix ID + telefon raqam orqali)
- `/cancel` — Joriy amalni bekor qilish
- `/help` — Yordam
- Vazifa yaratish — matn, ovozli xabar, rasm, video
- Mas'ul tanlash — Bitrix24 foydalanuvchilari orqali
- Bitrix24 ga yuborish — avtomatik ravishda vazifa yaratiladi

## Bitrix24 integratsiya

`tasks/services.py` faylida `BitrixService` klassi orqali:

- `get_user()` — Bitrix24 foydalanuvchisini olish
- `create_task()` — Bitrix24 da vazifa yaratish
- `get_all_users()` — Barcha foydalanuvchilarni olish (kesh bilan)
- `search_users()` — Foydalanuvchilarni qidirish
- `attach_file_to_task()` — Faylni vazifaga biriktirish

## Testlar

```bash
python manage.py test
```

## Health check

```bash
curl http://localhost:8000/health/
```
