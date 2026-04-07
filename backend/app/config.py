# backend/app/config.py
import os

# G4F API конфигурация
G4F_API_KEY = os.getenv("G4F_API_KEY", "g4f_u_mnlj3n_97afcf132daff7aafe278ee6e26c58b39cc4920465080170_794b53f6")
G4F_BASE_URL = os.getenv("G4F_BASE_URL", "https://g4f.space/v1")

# CORS (для разных доменов)
ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://localhost:8080",
    "https://*.github.io",  # GitHub Pages
    "*"  # Для разработки, в проде лучше убрать
]
