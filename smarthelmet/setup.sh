#!/bin/bash
# ====================================================
# Smart Helmet Dashboard — First Time Setup Script
# Run this once to set up the project
# ====================================================

echo "📦 Installing Django..."
pip install django

echo ""
echo "⚙️  Running database migrations..."
python manage.py makemigrations riders
python manage.py makemigrations accidents
python manage.py makemigrations api
python manage.py makemigrations dashboard
python manage.py migrate

echo ""
echo "👤 Creating admin user..."
python manage.py createsuperuser

echo ""
echo "✅ Setup complete! Now run:"
echo "   python manage.py runserver"
echo ""
echo "Then open: http://127.0.0.1:8000"
