# backend/app/ai_client.py
from openai import OpenAI
from app.config import G4F_API_KEY, G4F_BASE_URL


client = OpenAI(
    api_key=G4F_API_KEY,
    base_url=G4F_BASE_URL
)


def generate_text(prompt: str) -> str:
    """Генерация текста через G4F API"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )
    return response.choices[0].message.content


def generate_report(topic: str, style: str, word_count: int) -> str:
    """Генерация доклада"""
    style_descriptions = {
        "academic": "академический, научный стиль с терминологией",
        "casual": "разговорный, простой язык без сложных терминов",
        "business": "деловой стиль, конкретика, профессиональная лексика",
        "creative": "творческий стиль, яркие образы, эмоциональность"
    }
    
    prompt = f"""Напиши доклад на тему: "{topic}"

Требования:
- Стиль: {style_descriptions.get(style, 'академический')}
- Объём: примерно {word_count} слов
- Структура: введение (1 абзац), основная часть (3-4 раздела), заключение (1 абзац)
- Язык: русский
- Форматирование: используй заголовки разделов, абзацы отделяй пустой строкой

Начни сразу с заголовка доклада, без вступительных фраз."""
    
    return generate_text(prompt)
