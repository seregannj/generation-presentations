# backend/app/config.py
import os

# G4F API конфигурация
G4F_API_KEY = os.getenv("G4F_API_KEY", "key")
G4F_BASE_URL = os.getenv("G4F_BASE_URL", "url")

# CORS (для разных доменов)
ALLOWED_ORIGINS = [
    "https://seregannj.github.io/gendoc/console/*"
]
