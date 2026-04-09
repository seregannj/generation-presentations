import os

# G4F configuration
G4F_API_KEY = os.getenv("G4F_API_KEY", "key")
G4F_BASE_URL = os.getenv("G4F_BASE_URL", "url")

# CORS origins
ALLOWED_ORIGINS = [
    "https://seregannj.github.io/gendoc",
    "https://seregannj.github.io/gendoc/console",
    "https://seregannj.github.io/gendoc/console/*"
]
