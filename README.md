# Telegram Task Management Bot

Django + Aiogram 3.x asosida yaratilgan Telegram vazifalar boshqarish boti.

## Loyiha tuzilmasi

```
├── config/          # Django settings, urls, wsgi, asgi
├── users/           # TelegramUser modeli
├── tasks/           # Task modeli va services
├── bot/             # Telegram bot (Aiogram 3.x)
│   ├── handlers/    # Bot handlerlari
│   ├── keyboards/   # Keyboardlar
│   └── states/      # FSM statelar
├── manage.py
├── requirements.txt
├── .env
└── .env.example
```

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

4. TELEGRAM_BOT_TOKEN ni .env ga qo'shing.

5. Migratsiyalarni bajaring:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Admin foydalanuvchi yarating:
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

- /start - Ro'yxatdan o'tish
- Vazifa yaratish (matn)
- Vazifalarni ko'rish (barcha, kutilayotgan, bajarilgan)
- Vazifa bajarildi
- Profil
- Yordam

## Bitrix24 integratsiya

Hozircha Bitrix24 integratsiyasi yo'q. Kelajakda `tasks/services.py` faylida `BitrixService` klassiga qo'shiladi.
