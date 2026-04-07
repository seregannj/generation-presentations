# backend/app/ai_client.py
import g4f
import asyncio
from concurrent.futures import ThreadPoolExecutor

# Пул потоков для синхронных вызовов g4f
executor = ThreadPoolExecutor(max_workers=2)


def _generate_sync(prompt: str) -> str:
    """Синхронная функция для вызова g4f"""
    return g4f.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    )


async def generate_report(topic: str, style: str, word_count: int) -> str:
    """Асинхронная генерация доклада через g4f в отдельном потоке"""
    
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
    
    # Запускаем в отдельном потоке, чтобы не конфликтовать с event loop FastAPI
    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(executor, _generate_sync, prompt)
    
    if not response or len(response) < 50:
        raise Exception("Пустой ответ от модели")
    
    return response
