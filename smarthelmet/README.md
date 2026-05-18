# Smart Helmet Dashboard 🪖
**Purbanchal University — Acme Engineering College**
**Project by: Aryav Khadka, Deepakraj Jaishi, Jagerna Shrestha**

---

## 📁 Project Folder Structure

```
smarthelmet/                  ← Your main project folder
│
├── manage.py                 ← Django's run command file (don't touch)
├── setup.sh                  ← First-time setup script
├── test_send_data.py         ← Simulate ESP32 data (Phase 1 testing)
│
├── smarthelmet/              ← Project settings folder
│   ├── settings.py           ← All settings (database, apps, etc.)
│   ├── urls.py               ← Main URL router
│   └── wsgi.py               ← Web server file (don't touch)
│
├── dashboard/                ← Home dashboard app
│   ├── views.py              ← Home page logic
│   └── urls.py               ← Dashboard URLs
│
├── riders/                   ← Rider management app
│   ├── models.py             ← Rider database table
│   ├── views.py              ← Add/Edit/Delete rider logic
│   ├── forms.py              ← Rider input form
│   └── urls.py               ← Rider URLs
│
├── accidents/                ← Accident + Helmet app
│   ├── models.py             ← Helmet, SensorData, Accident tables
│   ├── views.py              ← Accident list/detail/resolve logic
│   └── urls.py               ← Accident URLs
│
├── api/                      ← ESP32 communication app
│   ├── views.py              ← Receives data from ESP32
│   └── urls.py               ← API URLs
│
├── templates/                ← All HTML pages
│   ├── base.html             ← Main layout (sidebar + navbar)
│   ├── registration/
│   │   └── login.html        ← Login page
│   ├── dashboard/
│   │   └── home.html         ← Home dashboard page
│   ├── riders/
│   │   ├── rider_list.html   ← Show all riders
│   │   ├── rider_form.html   ← Add/Edit rider form
│   │   └── rider_confirm_delete.html
│   └── accidents/
│       ├── helmet_status.html ← Live helmet status page
│       ├── accident_list.html ← All accidents page
│       └── accident_detail.html ← Single accident + map
│
└── static/                   ← CSS/JS files (if needed)
```

---

## 🚀 How to Run (Step by Step)

### Step 1 — Install Django
```bash
pip install django
```

### Step 2 — Go into the project folder
```bash
cd smarthelmet
```

### Step 3 — Create the database
```bash
python manage.py makemigrations riders
python manage.py makemigrations accidents
python manage.py makemigrations
python manage.py migrate
```

### Step 4 — Create your admin login
```bash
python manage.py createsuperuser
# Enter username, email, password when asked
```

### Step 5 — Start the server
```bash
python manage.py runserver
```

### Step 6 — Open in browser
```
http://127.0.0.1:8000
```
Login with the username and password you created.

---

## 🔌 API Endpoints (for ESP32)

### Send sensor data from ESP32:
```
POST http://your-ip:8000/api/data/
```
**JSON body:**
```json
{
    "helmet_id": "H001",
    "acceleration": 12.5,
    "tilt": 45.0,
    "latitude": 27.7172,
    "longitude": 85.3240,
    "helmet_worn": true,
    "accident": false,
    "battery": 85
}
```

### Get live status (used by dashboard):
```
GET http://your-ip:8000/api/status/
```

---

## 🧪 Testing WITHOUT ESP32 (Phase 1)

Run the simulator script:
```bash
python test_send_data.py
```
Choose:
- `1` → Send normal riding data
- `2` → Trigger a fake accident alert
- `3` → Continuous data stream

---

## 📱 Pages in the Dashboard

| URL | Page |
|-----|------|
| `/` | Home Dashboard (stats + map) |
| `/riders/` | Rider Management |
| `/riders/add/` | Add New Rider |
| `/accidents/helmets/` | Live Helmet Status |
| `/accidents/` | Accident Alerts |
| `/admin/` | Django Admin Panel |

---

## ⚡ Key Features

- ✅ Login system
- ✅ Home dashboard with live stat cards
- ✅ Helmet status monitoring (battery, GPS, safe/accident)
- ✅ 🚨 Auto accident alert popup (AJAX polling every 5 seconds)
- ✅ Leaflet.js map showing accident locations
- ✅ Google Maps link for each accident
- ✅ Rider registration with emergency contacts
- ✅ Accident history with resolve button
- ✅ REST API for ESP32 to POST sensor data
