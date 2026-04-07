# backend/app/ai_client.py
import g4f


def generate_report(topic: str, style: str, word_count: int) -> str:
    """Генерация доклада через g4f"""
    
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
- Структура: введение, основная часть (3-4 раздела), заключение
- Язык: русский
- Формат: заголовки разделов, абзацы через пустую строку

Начни с заголовка доклада."""
    
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            stream=False
        )
        return response
    except Exception as e:
        raise Exception(f"Ошибка генерации: {e}")
