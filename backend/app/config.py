# backend/app/config.py
import os

# G4F API конфигурация
G4F_API_KEY = os.getenv("G4F_API_KEY", "key")
G4F_BASE_URL = os.getenv("G4F_BASE_URL", "url")

# CORS (для разных доменов)
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8080",
    "https://*.github.io",  # GitHub Pages
    "*"  # Для разработки, в проде лучше убрать
]
